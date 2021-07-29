mirvas="/path/to/mirvas"
genome_file= genome_hg19.ifas
mirnadb_file="/path/to/mirna_hg19_mirbase20.tsv"

$mirvas -flank5p 100 -flank3p 100 -drawings 0 novogene.vcf.avinput.mirvas mirvas_output.tsv "$genome_file" "$mirnadb_file"



