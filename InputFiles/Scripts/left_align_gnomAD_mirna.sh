#Calls convert2annovar.pl on gnomAD201_data_mirna_variants.vcf to left align the file and prepare for input  into annovar

convert2annovar.pl gnomAD201_data_mirna_variants.vcf -format vcf4 -allsample -withfreq -includeinfo > gnomAD201_data_mirna_variants.vcf.avinput
