import csv
import re

class GnomadReformatter:
    """
    Implements the reformatter interface for gnomAD 2.0.1 data files.

    Attributes:
    file_path(string) = The gnomAD data file to be formatted.
    """
    def __init__(self):
        """ GnomadReformatter constructor. """
        self._file_path = None

    def _file_name(self, file_path):
        """
        Sets the file_path attribute.

        Parameters:
        file_path(string): The gnomAD data file to be formatted.
        """
        self._file_path = file_path

    def reformat(self,append_dict=None):

        """
        Implements the reformat method for gnomAD files. Extracts Allele Count, Allele Number from NFE populations.

        The function expects the file to be from gnomAD 2.0.1 with the following columns:

        chr start end ref alt id  qual filter gnomad_chr gnomad_pos rs_num gnomad_ref gnomad_alt gnomad_flag gnomad_info

        Reordered column format becomes:
        AC_gnomAD AN_gnomAD AF_gnomAD

        Parameters:
        append_dict (optional): Any additional information to be appended last columns of the file.  Must have chromosome+start+end+type as key.

        Returns:
        file_dict(dict): A dictionary with chromosomal position and variant type as the key and the reordered columns as the value. 
        """
        input_file = open(self._file_path)
        field_names = ['chr','start','end','ref','alt','id','qual','filter','gnomad_chr','gnomad_pos','rs','gnomad_ref','gnomad_alt','gnomad_qual','gnomad_flag','gnomad_info']
        reader = csv.DictReader(input_file, fieldnames=field_names,delimiter = '\t')
        file_dict = dict()
        for line in reader:
            
            ac_nfe_full = re.search('AC_NFE=[^;]+', line['gnomad_info'])
            an_nfe_full = re.search('AN_NFE=[^;]+', line['gnomad_info'])
            
            ac_gnomAD = sum([int(i) for i in ac_nfe_full.group().split("=",1)[1].split(',')])
            an_gnomAD = sum([int(i) for i in an_nfe_full.group().split("=",1)[1].split(',')])

        
            af_gnomAD = ac_gnomAD/an_gnomAD if an_gnomAD else 0
            
            reformatted_line = '\t'.join([str(ac_gnomAD),str(an_gnomAD),str(af_gnomAD)])
            
            key = 'chr'+line['chr']+line['start']+line['end']+line['ref']+line['alt']
            rs_key = line['rs']
            
            file_dict[key] = reformatted_line
            if(rs_key != '.'):
                file_dict[rs_key] = reformatted_line
        return file_dict