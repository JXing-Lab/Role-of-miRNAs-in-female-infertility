#Read in input table

df <- read.csv("UTRVariantsgnomAD.tsv", sep ='\t',na.strings = '-')

#Fisher's Exact Test Function
rowFisher <- function(x, ...) {
  return(fisher.test(matrix(x, nrow = 2, ...))$p.value)
}

#Select relevant rows for aggregation
subTable <- df[c(4,7:12,15)]

#Aggregate rows excluding NA values
aggdf <- aggregate(. ~Gene+Expressed,data=subTable, FUN = sum,na.action = na.omit)
#Keep rows with NA values for final table
dfzeros <- aggregate(. ~Gene+Expressed,data=subTable, FUN = sum,na.rm=TRUE, na.action=NULL)

#Calculate p-values
aggdf$pVal <- apply(aggdf[c(3:4,6:7)], 1, rowFisher)

#Exclude non-expressed genes when doing multiple testing correction
testedVariants <- aggdf[aggdf$Expressed != "NO", ] 
testedVariants$FDR <- p.adjust(testedVariants$pVal,method = "fdr")

#FDR is '-' for excluded non-expressed genes
notExpressed <- aggdf[aggdf$Expressed == "NO",]
notExpressed$FDR <- '-'

#If the table is a gnomAD table, get genes that have variants not found in gnomAD and add the rows to the final table for reference
if("AN_gnomAD" %in% colnames(aggdf)){
  notIngnomAD <- dfzeros[dfzeros$AN_gnomAD == 0,]
  notIngnomAD$pVal <- '-'
  notIngnomAD$FDR <- '-'
  testedVariants <- rbind(testedVariants,notIngnomAD)
}

#Concatenate all rows
burdentable <- rbind(testedVariants,notExpressed)

write.csv(burdentable,"TableS10.csv",row.names = FALSE)
