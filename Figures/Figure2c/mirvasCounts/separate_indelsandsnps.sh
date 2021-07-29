awk -F'\t' -vOFS='\t' '{if($4 !="snp")print}' mirvas_output.tsv > miRVaS_indels.txt 
awk -F'\t' -vOFS='\t' '{if($4 =="snp")print}' mirvas_output.tsv > miRVaS_snps.txt
