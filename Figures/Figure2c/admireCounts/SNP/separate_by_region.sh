#!/bin/bash

grep "_Seed" ADmiRE_snps.txt | awk '!seen[$1,$2,$3]++' >> Seed_Admire_snp.txt
grep "_Loop" ADmiRE_snps.txt | awk '!seen[$1,$2,$3]++' >> Loop_Admire_snp.txt
grep "_Mature" ADmiRE_snps.txt | awk '!seen[$1,$2,$3]++' >> Mature_Admire_snp.txt
grep "PrimeEnd" ADmiRE_snps.txt | awk '!seen[$1,$2,$3]++' >> Arm_Admire_snp.txt
grep "Primary_" ADmiRE_snps.txt | awk '!seen[$1,$2,$3]++' >> Flank_Admire_snp.txt

