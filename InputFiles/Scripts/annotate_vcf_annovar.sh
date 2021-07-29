#!/bin/bash

#Runs Annnovar and annotates a file with refgene, gnomAD, and DBSNP135 and SNP150 information

TABLEANNOVAR='/path/to/table_annovar.pl'
 
$TABLEANNOVAR novogene.vcf.avinput /path/to/annovar/humandb/ -out novogene -buildver hg19 -protocol refGene,gnomad_genome,snp135,avsnp150 -operation g,f,f,f -argument "-separate",,, -nastring . 






