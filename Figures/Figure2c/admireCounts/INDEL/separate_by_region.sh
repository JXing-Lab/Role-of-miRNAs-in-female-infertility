#!/bin/bash

grep "_Seed" ADmiRE_indels.txt | awk '!seen[$1,$2,$3]++' >> Seed_Admire_indel.txt
grep "_Loop" ADmiRE_indels.txt | awk '!seen[$1,$2,$3]++' >> Loop_Admire_indel.txt
grep "_Mature" ADmiRE_indels.txt | awk '!seen[$1,$2,$3]++' >> Mature_Admire_indel.txt
grep "PrimeEnd" ADmiRE_indels.txt | awk '!seen[$1,$2,$3]++' >> Arm_Admire_indel.txt
grep "Primary_" ADmiRE_indels.txt | awk '!seen[$1,$2,$3]++' >> Flank_Admire_indel.txt

