#!/bin/bash
awk -F'\t' 'BEGIN{OFS="\t"} {
    if($7 ~ /seed/) print $0 >> "Seed_mirvas_snp.txt"
    else if($7 ~ /loop/) print $0 >> "Loop_mirvas_snp.txt"
    else if($7 ~ /mature/ && $7 !~ /seed/) print $0 >> "Mature_mirvas_snp.txt"
    else if($7 ~ /arm/) print $0 >> "Arm_mirvas_snp.txt"
    else if($7 ~ /flank/) print $0 >> "Flank_mirvas_snp.txt"
}' miRVaS_snps.txt