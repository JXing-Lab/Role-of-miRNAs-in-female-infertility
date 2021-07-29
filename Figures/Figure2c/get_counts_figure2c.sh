echo "ADmiRE SNPs:"
wc -l admireCounts/SNP/*

echo "ADmiRE INDELs:"
wc -l admireCounts/INDEL/*

echo "ADmiRE SNPs:"
wc -l mirvasCounts/SNP/*

echo "ADmiRE INDELs:"
wc -l mirvasCounts/INDEL/*

echo "Overlap ADmire and miRVAS SNPs
echo "Seed:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/SNP/Seed_mirvas_snp.txt admireCounts/SNP/Seed_Admire_snp.txt | wc -l
echo "Mature:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/SNP/Mature_mirvas_snp.txt admireCounts/SNP/Mature_Admire_snp.txt | wc -l
echo "Arm:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/SNP/Arm_mirvas_snp.txt admireCounts/SNP/Arm_Admire_snp.txt | wc -l
echo "Loop:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/SNP/Loop_mirvas_snp.txt admireCounts/SNP/Loop_Admire_snp.txt | wc -l
echo "Flank:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/SNP/Flank_mirvas_snp.txt admireCounts/SNP/Flank_Admire_snp.txt | wc -l


echo "Overlap ADmire and miRVAS INDELss
echo "Seed:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/INDEL/Seed_mirvas_indel.txt admireCounts/SNP/Seed_Admire_indel.txt | wc -l
echo "Mature:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/INDEL/Mature_mirvas_indel.txt admireCounts/SNP/Mature_Admire_indel.txt | wc -l
echo "Arm:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/INDEL/Arm_mirvas_indel.txt admireCounts/SNP/Arm_Admire_indel.txt | wc -l
echo "Loop:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/INDEL/Loop_mirvas_indel.txt admireCounts/SNP/Loop_Admire_indel.txt | wc -l
echo "Flank:"
awk -F'\t' 'NR==FNR{A[$1,$2,$3]++;next};A[$1,$2,$3] > 0' mirvasCounts/INDEL/Flank_mirvas_indel.txt admireCounts/SNP/Flank_Admire_indel.txt | wc -l