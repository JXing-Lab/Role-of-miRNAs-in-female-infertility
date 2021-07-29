import csv
import re

class UtrReformatter:
    """
    Implements the reformatter interface for Annovar output files. Extracts 3UTR lines.

    Attributes:
    file_path(string) = The Annovar output file to be formatted.
    """
    def __init__(self):
        """ UTRReformatter constructor. """
        self._file_path = None

    def _file_name(self, file_path):
        """
        Sets the file_path attribute.

        Parameters:
        file_path(string): The Annovar output file to be formatted.
        """
        self._file_path = file_path

    def reformat(self,append_dict=None):
        """
        Implements the reformat method for Annovar outputs, extracts 3UTR lines.

        The function expects the file to be generated from Annovar with the following columns:

        Chr Start   End Ref Alt Func.refGene    Gene.refGene    GeneDetail.refGene  ExonicFunc.refGene  AAChange.refGene    gnomAD_genome_ALL   gnomAD_genome_AFR   gnomAD_genome_AMR   gnomAD_genome_ASJ   gnomAD_genome_EAS   gnomAD_genome_FIN   gnomAD_genome_NFE   gnomAD_genome_OTH   snp135  avsnp150    Otherinfo   qual    id  vcfchr  vcfpos  vcfid   vcfref  vcfalt  vcfqual vcffilter   vcfinfo

        Reordered column format becomes:
        Chr Start End Gene Ref Alt AC_LRG AN_LRG AF_LRG AC_HRG AN_HRG AF_HRG SNP135 AVSNP150

        Parameters:
        append_dict (optional): Any additional information to be appended last columns of the file.  Must have chromosome+start+end+type as key.

        Returns:
        file_dict(dict): A dictionary with chromosomal position as the key and the reordered columns as the value. 
        """
        input_file = open(self._file_path)
        field_names = ['Chr','Start','End','Ref','Alt','Func.refGene','Gene.refGene','GeneDetail.refGene','ExonicFunc.refGene','AAChange.refGene','gnomAD_genome_ALL','gnomAD_genome_AFR','gnomAD_genome_AMR','gnomAD_genome_ASJ','gnomAD_genome_EAS','gnomAD_genome_FIN','gnomAD_genome_NFE','gnomAD_genome_OTH','snp135','avsnp150','Otherinfo','qual','id','vcfchr','vcfpos','vcfid','vcfref','vcfalt','vcfqual','vcffilter','vcfinfo']
        reader = csv.DictReader(input_file, fieldnames=field_names,delimiter = '\t')
        file_dict = dict()
        for line in reader:
            if(line['Func.refGene'] != "UTR3"):
                continue
            counts = line['vcfinfo'].strip().split(';')
            
            ac_lrg = sum([int(i) for i in counts[0].split("=",1)[1].split(',')])
            an_lrg = sum([int(i) for i in counts[1].split("=",1)[1].split(',')])
            ac_hrg = sum([int(i) for i in counts[3].split("=",1)[1].split(',')])
            an_hrg = sum([int(i) for i in counts[4].split("=",1)[1].split(',')])

            af_lrg = ac_lrg/an_lrg if an_lrg else 0
            af_hrg = ac_hrg/an_hrg if an_hrg else 0

            vcf_alt = line['vcfalt'].replace(',','+')

            reformatted_line = '\t'.join([line['Chr'],line['Start'],line['End'],line['Gene.refGene'],line['vcfref'],vcf_alt,str(ac_lrg),str(an_lrg),str(af_lrg),str(ac_hrg),str(an_hrg),str(af_hrg),line['snp135'],line['avsnp150']])
            
            key = line['Chr']+line['Start']+line['End']
            
            if key not in file_dict:
                file_dict[key] = reformatted_line
        return file_dict