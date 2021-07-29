#Uses Tabix to pull data from ensembl's server which hosts gnomAD 2.0.1.

while read line; do
pos=$(echo "$line" | awk -F'\t' '{print $1":"$2"-"$3}')

tabix "ftp://ftp.ensembl.org/pub/data_files/homo_sapiens/GRCh37/variation_genotype/gnomad.genomes.r2.0.1.sites.noVEP.vcf.gz" "$pos"


done < UTRVariants.tsv > gnomAD201_data_utr_variants.vcf
