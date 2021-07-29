#Read in TableS8 from Stirparo et al study
df8 <- read.csv("TableS8.csv")
#Select gene list
gene <- read.table("Figure3bGenelist.txt")
c8 <- intersect(as.vector(gene[,1]), as.vector(df8[,2]))

#Extract gene expression data
data8 <- df8[is.element(df8[,2],c8),]
data8 <- data8[!duplicated(data8[,2]),]
r8 <- data8[,2]
row.names(data8) <- r8
sdata <- data8[,3:9]
#Add 1 to FPKM values to prevent errors when log transforming
sdata <-sdata+1

write.table(sdata, file = "Figure3bExpressionData.txt", sep= "\t")