awk -F'\t' -vOFS='\t' '{if($4 =="-" || $5 =="-")print}' admire_intersect_vcf_bedtools.txt > ADmiRE_indels.txt
awk -F'\t' -vOFS='\t' '{if($4 !="-" && $5 !="-")print}' admire_intersect_vcf_bedtools.txt > ADmiRE_snps.txt
