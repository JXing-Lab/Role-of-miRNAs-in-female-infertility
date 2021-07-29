*** 
## Figure 2

These files used to generate Figures 2c
 
### get_counts_figure2c.sh
***

An automated script that generates SNPs and INDELs counts from ADmiRE and miRVaS as well as the number of overlapping SNPs and INDELs.

Input:  
admireCounts/SNP/*
admireCounts/INDEL/*
mirvasCount/SNP/*
mirvasCount/SNP/*

``` 
get_counts_figure2c.sh
``` 

#### mirvasCounts/miRVaS_indels.txt, mirvasCounts/miRVaS_snps.txt 
***
Each file contains all indels and snps annotated by miRVaS, respectively.

Input:  
Input Files/mirvas_output.tsv

``` 
mirvasCounts/separate_indelsandsnps.sh
``` 


#### mirvasCounts/SNP/(Seed,Mature,Arm,Loop,Flank)mirvas_snp.txt
***
mirVaS annotated SNPs separated by miRNA regions(seed,mature,arm,loop,flank).

Input: 
miRVaS_snps.txt

```  
mirvasCounts/SNP/separate_by_region.sh 
``` 

#### mirvasCounts/INDEL/(Seed,Mature,Arm,Loop,Flank)mirvas_indel.txt 
***

mirVaS annotated INDELs separated by miRNA regions(seed,mature,arm,loop,flank).

Input: 
miRVaS_indels.txt
``` 
mirvasCounts/INDEL/separate_by_region.sh  
``` 

#### admireCounts/ADmiRE_indels.txt, ADmiRECounts/ADmiRE_snps.txt 
***
Each file contains all indels and snps annotated by ADmiRE, respectively.

Input:  
Input Files/admire_intersect_vcf_bedtools.txt

``` 
ADmiRECounts/separate_indelsandsnps.sh
``` 


#### admireCounts/SNP/(Seed,Mature,Arm,Loop,Flank)ADmiRE_snp.txt
***
ADmiRE annotated SNPs separated by miRNA regions(seed,mature,arm,loop,flank).

Input: 
ADmiRE_snps.txt

```  
admireCounts/SNP/separate_by_region.sh 
``` 

#### admireCounts/INDEL/(Seed,Mature,Arm,Loop,Flank)ADmiRE_indel.txt 
***

ADmiRE annotated INDELs separated by miRNA regions(seed,mature,arm,loop,flank).

Input: 
ADmiRE_indels.txt
``` 
ADmiRECounts/INDEL/separate_by_region.sh  
``` 