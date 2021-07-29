
## Read Supplementary TableS8 from Stirparo et al(2018)
setwd("/path/to/file")
df8 <- read.csv("TableS8.csv")

## Get max FPKM from the first 7 FPKM measurments
row.names(df8) <- df8[,1]
df8 <- df8[,2:9]
df8$max<-apply(X=df8[,2:8], MARGIN=1, FUN=max)

#Only genes with a max(FPKM>1) is considered expressed
expressed <- subset(df8, df8$max > 1)
genes <- unique(expressed$Gene)

write.table(genes, file = "expressedgenes.txt",quote = F,col.names = F,row.names = F)
write.table(df8$Gene,file = "fullgenes.txt",quote = F,col.names = F,row.names = F)
