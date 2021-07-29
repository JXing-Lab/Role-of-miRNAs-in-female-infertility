import argparse
import annotated_files
import reformatters
import utilscripts

def main():
    parser = argparse.ArgumentParser(description="""

miRNA_project.py takes input from miRVaS, ADmiRE, and Annovar and outputs transformed and concatenated files for further downstream analysis

The script returns two files.  One file contains the concatenated variants found in miRVaS and ADmiRE.  The other contains 3'UTR variants from Annovar.

The script can also append gnomAD data if provided by the optional arguments --gnomAD and --gnomAD_utr.  This will append gnomAD information to 
the miRVaS/ADmiRE file and 3'UTR file respectively.

""")

##############################################################################
#
#  Required arguments
#
##############################################################################
    parser.add_argument("-mi","--mirvas", dest="mirvas",required=True, help="""required, e.g. /path/to/mirvas_output
 
A miRVaS output file where the format of the file is:

 chromosome  begin   end type    ref alt mir_location    mir_name    Centroid_highest_impact MEA_highest_impact  MFE_highest_impact  Centroid_impact MEA_impact  MFE_impact  ref_mfefreq var_mfefreq Cen_conservation    MEA_conservation    MFE_conservation    ref_Cen_deltaG  var_Cen_deltaG  ref_MEA_deltaG  var_MEA_deltaG  ref_MFE_deltaG  var_MFE_deltaG
 chr1   17406   17407   snp G   A   arm5p(m+2e) hsa-mir-6859-1  nochange    nochange    nochange    nochange    nochange    nochange    9.91585e-05 5.83491e-05 changed 2   changed 4   changed 5   -114.30 -112.00 -118.50 -116.20 -119.30 -117.00

Instructions on how to generate a miRVaS output file can be found in InputFiles/README.md

Note that the program assumes the file is using a 0-based coordinate system.

""")
    parser.add_argument("-ad","--admire", dest="admire",required=True, help="""required, e.g. /path/to/admire_output
 
An ADmiRE annotated output file where the format of the file(no header) is:

chr1    1247942 1247943 -   CCCTGCCCTG  .   2137.48 .   chr1    1247943 .   A   ACCCTGCCCTG 2137.48 PASS    AC_LRG=0;AN_LRG=170;AF_LRG=0;AC_HRG=1;AN_HRG=186;AF_HRG=0.00537634  chr1    1247942 1247943 mir-6727|MI0022572|Precursor_5PrimeEnd|NA|NA|0|NA|NA|NA|NA|NA|-1.80824|0|NA|NA|NA|NA|NA 1

Instructions on how to generate a ADmiRE output file can be found in InputFiles/README.md

Note that the program assumes the file is using a 0-based coordinate system.

""")
    parser.add_argument("--utr", dest="utr",required=True, help="""required, e.g. /path/to/annovar_utr_output
 
An Annovar annotated file where the format of the file is:

Chr Start   End Ref Alt Func.refGene    Gene.refGene    GeneDetail.refGene  ExonicFunc.refGene  AAChange.refGene    gnomAD_genome_ALL   gnomAD_genome_AFR   gnomAD_genome_AMR   gnomAD_genome_ASJ   gnomAD_genome_EAS   gnomAD_genome_FIN   gnomAD_genome_NFE   gnomAD_genome_OTH   snp135  avsnp150    Otherinfo   qual    id  vcfchr  vcfpos  vcfid   vcfref  vcfalt  vcfqual vcffilter   vcfinfo
chr1    12718   12719   G   C   ncRNA_exonic    DDX11L1 .   .   .   0.0494  0.0165  0.0300  0.0625  0.0017  0.1274  0.0528  0.0939  rs71267773  .   .   13.29   .   chr1    12719   .   G   C   13.29   PASS    AC_LRG=0;AN_LRG=88;AF_LRG=0;AC_HRG=1;AN_HRG=102;AF_HRG=0.00980392

Instructions on how to generate a Annovar_utr output file can be found in InputFiles/README.md

Note that the program assumes the file is using a 0-based coordinate system.

""")
    parser.add_argument("-an","--annovar", dest="annovar",required=True, help="""required, e.g. /path/to/annovar_output

An Annovar annotated file where the format of the file is:

Chr Start   End Ref Alt Func.refGene    Gene.refGene    GeneDetail.refGene  ExonicFunc.refGene  AAChange.refGene    gnomAD_genome_ALL   gnomAD_genome_AFR   gnomAD_genome_AMR   gnomAD_genome_ASJ   gnomAD_genome_EAS   gnomAD_genome_FIN   gnomAD_genome_NFE   gnomAD_genome_OTH   snp135  avsnp150    Otherinfo   qual    id  vcfchr  vcfpos  vcfid   vcfref  vcfalt  vcfqual vcffilter   vcfinfo
chr1    12718   12719   G   C   ncRNA_exonic    DDX11L1 .   .   .   0.0494  0.0165  0.0300  0.0625  0.0017  0.1274  0.0528  0.0939  rs71267773  .   .   13.29   .   chr1    12719   .   G   C   13.29   PASS    AC_LRG=0;AN_LRG=88;AF_LRG=0;AC_HRG=1;AN_HRG=102;AF_HRG=0.00980392

Instructions on how to generate a Annovar output file can be found in InputFiles/README.md

Note that the program assumes the file is using a 0-based coordinate system.

""")


##############################################################################
#
#  Optional Arguments
#
##############################################################################
    parser.add_argument("-g","--gnomAD", dest="gnomAD",action='store', default=None, help="""optional, [default=do not append gnomAD data to variant files]
if /path/to/gnomAD_data is provided then gnomAD data will be appended to a new file

""")

    parser.add_argument("-gu","--gnomAD_utr", dest="gnomAD_utr",action='store', default=None, help="""optional, [default=do not append gnomAD data to utr files] 
if /path/to/gnomAD_data is provided then gnomAD data will be appended to a new file

""")
    parser.add_argument("-e","--expressed_list", dest="expressed_list",action='store', default=None, help="""optional, [default=do not append expression levels to UTR files] 
if expressed_list argument is provided then full_list must also be provided.  Expressed_list is a path to a list of genes with max(FPKM) > 1.  One gene per line.

""")
    parser.add_argument("-f","--full_list", dest="full_list",action='store', default=None, help="""optional, [default=do not append expression levels to UTR files]
if full_list argument is provided then expressed_list must also be provided.  Full_list is a path to a list of all genes found in a study.  One gene per line.

""")

    args = parser.parse_args()
    reformatter = reformatters.FileFormatter()

    #Init
    mirvas_file = annotated_files.AnnotatedFile(args.mirvas)
    admire_file = annotated_files.AnnotatedFile(args.admire)
    annovar_file = annotated_files.AnnotatedFile(args.annovar)
    utr_file = annotated_files.AnnotatedFile(args.utr)
    #Store files into dictionary
    annovar_dict = reformatter.reformat(annovar_file,'annovar')
    mirvas_dict = reformatter.reformat(mirvas_file,'mirvas',annovar_dict)
    admire_dict = reformatter.reformat(admire_file,'admire',annovar_dict)
    utr_dict = reformatter.reformat(utr_file,'utr')
    annovar_dict.clear()

    #Merge mirvas and admire dictionary
    variant_dict = utilscripts.merge_dict(mirvas_dict,admire_dict)
    variant_header = ['Chr','Start','End','Ref','Alt','miRNA','Type','Location','PredictedEffect_Centroid','PredictedEffect_MEA','PredictedEffect_MFE','AC_LRG','AN_LRG','AF_LRG','AC_HRG','AN_HRG','AF_HRG','DBSNP135','DBSNP150']
    utr_header = ['Chrom','Start','End','Gene','Ref','Alt','AC_LRG','AN_LRG','AF_LRG','AC_HRG','AN_HRG','AF_HRG','DBSNP135','DBSNP150']

    #Append is_expressed information
    if(args.full_list is not None and args.expressed_list is not None):
        utr_dict = utilscripts.append_is_expressed(utr_dict,args.expressed_list,args.full_list)
        utr_header.append('Expressed')

    #Write to files
    utilscripts.write_dictionary_to_file(variant_dict,"3000Variants.tsv",variant_header)
    utilscripts.write_dictionary_to_file(utr_dict,"UTRVariants.tsv",utr_header)

    #Append gnomAD information if available
    if(args.gnomAD is not None):
        gnomad_file = annotated_files.AnnotatedFile(args.gnomAD)
        gnomad_dict = reformatter.reformat(gnomad_file,'gnomad')
        gnomad_variant_dict = utilscripts.append_gnomad(variant_dict,gnomad_dict,True)
        gnomad_dict.clear()

        gnomad_variant_header = ['Chr','Start','End','Ref','Alt','miRNA','Type','Location','PredictedEffect_Centroid','PredictedEffect_MEA','PredictedEffect_MFE','AC_Patient','AN_Patient','AF_Patient','AC_gnomAD','AN_gnomAD','AF_gnomAD','DBSNP135','DBSNP150']
        utilscripts.write_dictionary_to_file(gnomad_variant_dict,"3000VariantsgnomAD.tsv",gnomad_variant_header)

    #Append gnomAD information if available
    if(args.gnomAD_utr is not None):
        gnomad_utr_file = annotated_files.AnnotatedFile(args.gnomAD_utr)
        gnomad_utr_dict = reformatter.reformat(gnomad_utr_file,'gnomad')
        gnomad_utr_variant_dict = utilscripts.append_gnomad(utr_dict,gnomad_utr_dict,False)
        gnomad_utr_dict.clear()
        gnomad_utr_variant_header = ['Chrom','Start','End','Gene','Ref','Alt','AC_Patient','AN_Patient','AF_Patient','AC_gnomAD','AN_gnomAD','AF_gnomAD','DBSNP135','DBSNP150']
        if(args.full_list is not None and args.expressed_list is not None):
            gnomad_utr_variant_dict = utilscripts.append_is_expressed(gnomad_utr_variant_dict,args.expressed_list,args.full_list)
            gnomad_utr_variant_header.append('Expressed')
        
        utilscripts.write_dictionary_to_file(gnomad_utr_variant_dict,"UTRVariantsgnomAD.tsv",gnomad_utr_variant_header)

if __name__ == "__main__":
    main()