#Intersects an annovar annotated file with Targetscanhuman miRNA target region file

bedtools intersect -a novogene.hg19_multianno.txt -b /path/to/targetscanhuman.bed -u > annovar_target_regions_intersect.txt
