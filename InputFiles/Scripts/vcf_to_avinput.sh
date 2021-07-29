#Calls convert2annovar.pl on novogene.vcf to left align the file and prepare for input  into annovar

convert2annovar.pl /path/to/novogene.vcf -format vcf4 -allsample -withfreq -includeinfo > novogene.vcf.avinput
