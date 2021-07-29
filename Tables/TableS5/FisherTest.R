#Read input table

input <- read.csv("3000VariantsgnomAD.tsv", sep ='\t',na.strings = '-')

#Fisher's Exact test function
rowFisher <- function(x, ...) {
  return(fisher.test(matrix(x, nrow = 2, ...))$p.value)
}

#Extract rows that do not have NA values
df <- input[complete.cases(input[c(11)]),]
if(dim(input)[2] == 15){
  df <- input[complete.cases(input[c(11)]),]
  notInGnomAD <- input[!complete.cases(input[c(11)]),]
}else{
  df <- input[complete.cases(input[c(16)]),]
  notInGnomAD <- input[!complete.cases(input[c(16)]),]
}
#Rows with NA in column 11 or 16 are missing gnomAD variants. Keep for final table

#Calculate p-value and FDR
if("Gene" %in% colnames(df)){
  df$pVal <- apply(df[c(7:8,10:11)], 1, rowFisher)
  
  testedVariants <- df[df$Expressed != "NO", ] 
  testedVariants$FDR <- p.adjust(testedVariants$pVal,method = "fdr")
  
  notExpressed <- df[df$Expressed == "NO",]
  notExpressed$FDR <- '-'
  
  table <- rbind(testedVariants,notExpressed)
}

#Calculate p-value and FDR
if("miRNA" %in% colnames(df)){
  
  df$pVal <- apply(df[c(12:13,15:16)], 1, rowFisher)
  df$FDR <- p.adjust(df$pVal,method = "fdr")
  
  table <- df
}

#If the table uses gnomAD counts, concat the missing variants not found in gnomAD back to the final table
if("AN_gnomAD" %in% colnames(df)){
  notInGnomAD$pVal <- '-'
  notInGnomAD$FDR <- '-'
  
  table <- rbind(table,notInGnomAD)
}


write.csv(table,"TableS5.csv",row.names = FALSE,na = "-")

