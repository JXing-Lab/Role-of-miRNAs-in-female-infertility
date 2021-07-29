*** 
## Supplementary Tables

Supplementary Tables S2,S3,S4,S5,S8,S10


#### TableS2 
***

Single variant analysis of variants found in miRNA. Low Rate vs High Rate Group.

Input:  
3000Variant.tsv

``` 
TableS2/FisherTest.R 
``` 


#### TableS3
***

Single variant analysis of variants found in miRNA 3'UTR targets. Only Expressed/NA genes considered in multiple testing correction. Low Rate vs High Rate Group.

Input:  
UTRVariants.tsv

``` 
TableS3/FisherTest.R
``` 


#### TableS4
***

Burden level analysis of variants found in miRNA 3'UTR targets. Only Expressed/NA genes considered in multiple testing correction. Low Rate vs High Rate Group.

Input: 
UTRVariants.tsv

```  
TableS4/BurdenFisherTest.R
``` 

#### TableS5
***

Single variant analysis of variants found in miRNA. Infertile group vs gnomAD_NFE population

Input: 
3000VariantsgnomAD.tsv

``` 
TableS5/FisherTest.R
``` 

#### TableS8
***
Single variant analysis of variants found in miRNA 3'UTR targets. Only Expressed/NA genes considered in multiple testing correction. Infertilfe vs gnomAD_NFE population.

Inputs: 
UTRVariantsgnomAD.tsv

``` 
TableS8/FisherTest.R
``` 
#### TableS10
***
Burden level analysis of variants found in miRNA 3'UTR targets. Only Expressed/NA genes considered in multiple testing correction. Infertilfe vs gnomAD_NFE population.

Inputs: 
UTRVariantsgnomAD.tsv

``` 
TableS10/FisherTest.R
``` 

#### TableS12
***

Mean FPKM and Log2 Fold Changes of:

(8 Cell, Morula,ICM/Endoderm/Epiblast) over (Zygote, 4 Cell)

(Morula,ICM/Endoderm/Epiblast) over (Zygote, 4 Cell, 8 Cell)


Input: 

TableS8.csv from Stirparo et al 2018

Figure3bGeneList.txt

Figure3cGeneList.txt

```  
TableS12/FoldChange.R
``` 