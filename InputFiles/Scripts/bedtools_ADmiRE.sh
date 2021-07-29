#Intersects a left aligned vcf file with admire.bed.

bedtools intersect -a novogene.vcf.avinput -b /path/to/admire.bed -wo > admire_intersect_vcf_bedtools.txt
