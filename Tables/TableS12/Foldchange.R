#Input from Supplementary TableS8 Stirparo et al 2018

df <- read.csv("TableS8.csv")
df <- df[,1:9]
totalgenes <- dim(df)[1]
#Get Means of First 2 FPKM (Zygote, 4 Cell)
df$First2 <- rowMeans(df[,3:4])
#Get Means of Last 3 FPKM (8 Cell, Morula,ICM/Endoderm/Epiblast)
df$Last3 <- rowMeans(df[,5:9])
#Get Means of First 3 FPKM (Zygote, 4 Cell, 8 Cell)
df$First3 <- rowMeans(df[,3:5])
#Get Means of Last 2 FPKM  (Morula,ICM/Endoderm/Epiblast)
df$Last2 <- rowMeans(df[,6:9])

#Take Log fold change of Last 3 and First 2
df$H2LLogFC <- log2(df$Last3) - log2(df$First2)
#Take Log fold change of Last 2 and First 3
df$L2HLogFC <- log2(df$Last2) - log2(df$First3)

dfH2L <- sum(df$H2LLogFC < -1, na.rm=TRUE)
dfL2H <- sum(df$L2HLogFC > 1, na.rm=TRUE)

#Extract genes that are in Figure3b and get number of genes that match each expression pattern
gene3b <- read.table("Figure3bGenelist.txt")
gene3blen <- length(gene3b$V1)
c <- intersect(as.vector(gene3b[,1]), as.vector(df[,2]))
data3b <- df[is.element(df[,2],c),]
data3bH2L <- sum(data3b$H2LLogFC < -1,na.rm=TRUE)
data3bL2H <-sum(data3b$L2HLogFC > 1,na.rm=TRUE)

#Extract genes that are in Figure3c and get number of genes that match each expression pattern
gene3c <- read.table("Figure3cGenelist.txt")
gene3clen <- length(gene3c$V1)
c <- intersect(as.vector(gene3c[,1]), as.vector(df[,2]))
data3c <- df[is.element(df[,2],c),]
data3cH2L <- sum(data3c$H2LLogFC < -1, na.rm=TRUE)
data3cL2H <- sum(data3c$L2HLogFC > 1, na.rm=TRUE)

data3c[data3c$L2HLogFC > 1,]$Gene

#Fisher's Exact Test comparing expression pattern counts from gene set to the whole transcriptome 
fisher.test(matrix(c(dfH2L,totalgenes-dfH2L,data3bH2L,gene3blen-data3bH2L), nrow=2))
fisher.test(matrix(c(dfL2H,totalgenes-dfL2H,data3bL2H,gene3blen-data3bL2H), nrow=2))
fisher.test(matrix(c(dfH2L,totalgenes-dfH2L,data3cH2L,gene3clen-data3cH2L), nrow=2))
fisher.test(matrix(c(dfL2H,totalgenes-dfL2H,data3cL2H,gene3clen-data3cL2H), nrow=2))



write.table(df[c(1:2,10:15)],"TableS12.csv")



