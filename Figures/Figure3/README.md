*** 
## Figure 3b

These files used to generate Figures 3b and 3c
 
### Figure3bExpressionData.txt, Figure3cExpressionData.txt
***

Input:  
TableS8.csv from Stirparo et al 2018
Figure3bGeneList.txt or Figure3cGeneList.txt

``` 
ExpressionData.R
``` 
Generates an FPKM+1 table for genes specified in the gene list.


#### Figure3bExpressionData.(jtv,gtr,atr,cdt),Figure3cExpressionData.(jtv,gtr,atr,cdt)
***

Clustering files outputted by Gene Cluster 3.0

```
Gene Cluster 3.0 Steps
1. Log transform
2. Center Genes
3. Hierarchical Cluster by Average Linkage for both Gene and Array
```
Visualization performed by JavaTreeView