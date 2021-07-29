*** 
## Input Files 

These files are used as input into the mirna_project.py. 

Instructions on how each file was generated is detailed below: 


#### novogene.vcf.avinput 
***

A left aligned .vcf file used to generate most subsequent files.  This file contains Allele Counts, Allele Number, and Allele Number for the High Rate(AC_HRG,AN_HRG,AF_HRG) and Low Rate Group (AC_LRG,AN_HRG,AF_HRG) The original .vcf file contains patient genotype information and is therefor omitted from the files. 

Input:  

novogene.vcf 

``` 
Scripts/vcf_to_avinput.sh 
``` 


#### admire_intersect_vcf_bedtools.txt 
***

A list of variants found in AdmiRE database. 

Input:  

ADmiRE.bed

novogene.vcf.avinput 

``` 
Scripts/bedtools_ADmiRE.sh 
``` 


#### novogene.hg19_multianno.txt 
***

Annovar Annotated file from novogene.vcf.avinput 

Input: 

novogene.vcf.avinput 

```  
Scripts/annotate_vcf_annovar.sh  
``` 

#### annovar_target_regions_intersect.txt 
***

Annotated variants found within TargetScanHuman miRNA Target 3UTR 

Input: 

novogene.hg19_multianno.txt

TargetScanHuman bed file from http://www.targetscan.org/vert_72/  

``` 
Scripts/bedtools_targetscanhuman.sh 
``` 

#### mirvas_output.tsv 
***
Tab-separated file with variants annotated by miRVaS 

Inputs: 

novogene.vcf.avinput 

``` 
Scripts/format_vcf_miRVaS.sh 
Scripts/run_mirvas.sh 
``` 
#### gnomAD201_data_mirna_variants.vcf.avinput 
***
gnomAD2.0.1 data file for miRNA variants

Inputs: 

3000Variants.csv 

``` 
Scripts/get_gnomAD_data_for_mirna.sh
Scripts/left_align_gnomAD_mirna.sh
``` 

#### gnomAD201_data_utr_variants.avinput 
***
gnomAD2.0.1 data file for UTR variants

Inputs: 

UTRVariants.csv 

``` 
Scripts/get_gnomAD_data_for_utr.sh
Scripts/left_align_gnomAD_utr.sh
``` 

#### fullgenes.txt 
***
List of all genes studied from Stirparo et al 2018 

Inputs: TableS8.csv from Stirparo paper 

``` 
Scripts/GetGenelist.R 
``` 

#### expressedgenes.txt 
***

List of genes with max(FPKM > 1) studied from Stirparo et al 2018 

Inputs: TableS8.csv from Stirparo paper 

``` 
Scripts/GetGenelist.R 
``` 