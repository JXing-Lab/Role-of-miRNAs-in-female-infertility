#!/bin/bash

awk 'BEGIN{print "chromosome\tbegin\tend\ttype\tref\talt"}; {type="snp"; if($4 == "-") {type="ins";$4="";$2=$2+1;} else if($5 == "-") {type="del"; $5="";} print $1, $2-1, $3, type, $4, $5}' OFS="\t" novogene.vcf.avinput > novogene.vcf.avinput.mirvas


