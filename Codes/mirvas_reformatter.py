import csv
import re

class MirvasReformatter:
    """
    Implements the reformatter interface for miRVaS output files.

    Attributes:
    file_path(string) = The miRVaS output file to be formatted.
    """
    def __init__(self):
        """ MirvasReformatter constructor. """
        self._file_path = None

    def _file_name(self, file_path):
        """
        Sets the file_path attribute.

        Parameters:
        file_path(string): The miRVaS output file to be formatted.
        """
        self._file_path = file_path

    def reformat(self,append_dict=None):
        """
        Implements the reformat method for miRVaS outputs.  

        The function expects the file to be generated from miRVaS with the following columns:

        chromosome  begin   end type    ref alt mir_location    mir_name    Centroid_highest_impact MEA_highest_impact  MFE_highest_impact  Centroid_impact MEA_impact  MFE_impact  ref_mfefreq var_mfefreq Cen_conservation    MEA_conservation    MFE_conservation    ref_Cen_deltaG  var_Cen_deltaG  ref_MEA_deltaG  var_MEA_deltaG  ref_MFE_deltaG  var_MFE_deltaG

        Reordered column format becomes:
        chromosome begin end ref alt miRNA type location Centroid_highest_impact MEA_highest_impact  MFE_highest_impact ...append_dict_annotations...

        Parameters:
        append_dict (optional): Any additional information to be appended last columns of the file.  Must have chromosome+start+end+type as key.

        Returns:
        file_dict(dict): A dictionary with chromosomal position and variant type as the key and the reordered columns as the value. 
        """
        input_file = open(self._file_path)
        reader = csv.DictReader(input_file, delimiter = '\t')
        file_dict = dict()
        for line in reader:

            
            direction = re.search('3p|5p',line['mir_location']) 
            location = re.search('seed', line['mir_location'])

            if (direction is None):
                strand = ""
            else:
                strand = '-' + direction.group()
            if(location is None):
                location = re.search('mature|arm|loop|flank|GENEDEL', line['mir_location'])
            

            line['type'] = 'indel' if line['type'] != 'snp' else 'SNP'
            miRNA = line['mir_name']+strand

            key = line['chromosome']+line['begin']+line['end'] + line['type']
            if(append_dict != None):
                append_annotation = append_dict[key]
            else:
                append_annotation = ""
            
            reformatted_line = '\t'.join([line['chromosome'],line['begin'],line['end'],line['ref'],line['alt'],miRNA,line['type'],location.group(),line['Centroid_highest_impact'],line['MEA_highest_impact'],line['MFE_highest_impact'],append_annotation])

            
            file_dict[key] = reformatted_line
        return file_dict
