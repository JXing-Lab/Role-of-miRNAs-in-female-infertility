# miRNA Project

This repository contains data and scripts for Tyc, K. M., A. Wong, R. T. Scott, Jr., X. Tao, K. Schindler, and J. Xing (2021) Analysis of DNA variants in miRNAs and miRNA 3’UTR binding sites in female infertility patients. Laboratory Investigation 101:503–512 


## Quick Start
The following is the command used to run the pipeline.
```
cd Code
mirna_project.py 
-mi ../InputFiles/mirvas_output.tsv 
-ad ../InputFiles/admire_intersect_vcf_bedtools.txt 
--utr ../InputFiles/annovar_target_regions_intersect.txt 
--an ../InputFiles/novogene.hg19_multianno.txt 
-g ../InputFiles/gnomAD201_data_mirna_variants.vcf.avinput 
-gu ../InputFiles/gnomAD201_data_utr_variants.vcf.avinput 
-e ../InputFiles/expressedgenes.txt 
-f ../InputFiles/fullgenes.txt
```

## Instructions

The steps below document the steps needed to generate the main analysis.

#### Input Files
***
Details on how to generate each input file is located in InputFiles/README.md

The pipeline requires input 4 input files:
```
--mirvas: /path/to/mirvas_output 

A miRVaS output file where the format of the file is:

 chromosome  begin   end type    ref alt mir_location    mir_name    Centroid_highest_impact MEA_highest_impact  MFE_highest_impact  Centroid_impact MEA_impact  MFE_impact  ref_mfefreq var_mfefreq Cen_conservation    MEA_conservation    MFE_conservation    ref_Cen_deltaG  var_Cen_deltaG  ref_MEA_deltaG  var_MEA_deltaG  ref_MFE_deltaG  var_MFE_deltaG

--admire: /path/to/admire_output

An ADmiRE annotated output file where the format of the file(no header) is:

chr start   end ref alt id  qual    filter   vcfchr vcfpos  vcfid   vcfref  vcfalt  vcfqual vcffilter   info    admirechr   admirestart admireend   admireinfo  nummatch

--utr: /path/to/annovar_utr_output
 
An Annovar annotated file where the format of the file is:

Chr Start   End Ref Alt Func.refGene    Gene.refGene    GeneDetail.refGene  ExonicFunc.refGene  AAChange.refGene    gnomAD_genome_ALL   gnomAD_genome_AFR   gnomAD_genome_AMR   gnomAD_genome_ASJ   gnomAD_genome_EAS   gnomAD_genome_FIN   gnomAD_genome_NFE   gnomAD_genome_OTH   snp135  avsnp150    Otherinfo   qual    id  vcfchr  vcfpos  vcfid   vcfref  vcfalt  vcfqual vcffilter   vcfinfo

--annovar: /path/to/annovar_output

An Annovar annotated file where the format of the file is:

Chr Start   End Ref Alt Func.refGene    Gene.refGene    GeneDetail.refGene  ExonicFunc.refGene  AAChange.refGene    gnomAD_genome_ALL   gnomAD_genome_AFR   gnomAD_genome_AMR   gnomAD_genome_ASJ   gnomAD_genome_EAS   gnomAD_genome_FIN   gnomAD_genome_NFE   gnomAD_genome_OTH   snp135  avsnp150    Otherinfo   qual    id  vcfchr  vcfpos  vcfid   vcfref  vcfalt  vcfqual vcffilter   vcfinfo
```

### Optional Arguments
***
```
--gnomAD: /path/to/gnomAD_data
A gnomAD vcf file with gnomAD annotations.  If provided will annotate miRVaS and ADMiRE files with gnomAD NFE allele counts and allele number.

--gnomAD_UTR: /path/to/gnomAD_utr_data
A gnomAD vcf file with gnomAD annotations. If provided will annotate UTR file with gnomAD NFE allele counts and allele number.

--expressed_list: /path/to/expressed_list
A gene list of expressed genes. If provided will annotate any gene in the list with 'YES'

--full_list: /path/to/full_list
A gene list of all genes in the study.  If provided will annotate any gene with 'NO' if not found in expressed_list and 'NA' if not in the list
```
#### Output Files

Four Output files are generated if all arguments are provided.

_3000Variants.tsv_ - A merged list of variants in miRNA regions from miRVaS and ADmiRE files.

With the output header:
```
'Chr','Start','End','Ref','Alt','miRNA','Type','Location','PredictedEffect_Centroid','PredictedEffect_MEA','PredictedEffect_MFE','AC_LRG','AN_LRG','AF_LRG','AC_HRG','AN_HRG','AF_HRG','DBSNP135','DBSNP150'
```

_3000VariantsgnomAD.tsv_ - A merged list of variants in miRNA regions from miRVaS and ADmiRE files with gnomAD_NFE allele counts and number.

With the output header:
```
'Chr','Start','End','Ref','Alt','miRNA','Type','Location','PredictedEffect_Centroid','PredictedEffect_MEA','PredictedEffect_MFE','AC_Patient','AN_Patient','AF_Patient','AC_gnomAD','AN_gnomAD','AF_gnomAD','DBSNP135','DBSNP150'
```

_UTRVariants.tsv_ - All UTR3 variants found within the target regions of miRNA.

With the output header:
```
'Chrom','Start','End','Gene','Ref','Alt','AC_LRG','AN_LRG','AF_LRG','AC_HRG','AN_HRG','AF_HRG','DBSNP135','DBSNP150'
```

_UTRVariantsgnomAD.tsv_ - All UTR3 variants found within the target regions of miRNA with gnomAD_NFE allele counts and number.

With the output header:
```
'Chrom','Start','End','Gene','Ref','Alt','AC_Patient','AN_Patient','AF_Patient','AC_gnomAD','AN_gnomAD','AF_gnomAD','DBSNP135','DBSNP150'
```

#### Supplemental Tables

Supplemental Tables S2,S3,S4,S5,S8,S10 are then generated using the above output files.

Details are provided in Tables/README.md
