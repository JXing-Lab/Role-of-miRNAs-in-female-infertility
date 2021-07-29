import csv
import re

class AdmireReformatter:
    """
    Implements the reformatter interface for ADmiRE output files.

    Attributes:
    file_path(string) = The ADmiRE output file to be formatted.
    """
    def __init__(self):
        """ AdmireReformatter constructor. """
        self._file_path = None

    def _file_name(self, file_path):
        """
        Sets the file_path attribute.

        Parameters:
        file_path(string): The ADmiRE output file to be formatted.
        """
        self._file_path = file_path


    def reformat(self,append_dict=None):
        """
        Implements the reformat method for ADmiRE outputs.  

        The function expects the file to be generated from ADmiRE with the following columns:

        chr start   end ref alt id  qual    filter   vcfchr vcfpos  vcfid   vcfref  vcfalt  vcfqual vcffilter   info    admirechr   admirestart admireend   admireinfo  nummatch

        Reordered column format becomes:
        chr start end ref alt miRNA type location Centroid_highest_impact MEA_highest_impact  MFE_highest_impact ...append_dict_annotations...

        where Centroid_highest_impact MEA_highest_impact  MFE_highest_impact are empty strings as ADmiRE does not do variant impact prediction

        Parameters:
        append_dict (optional): Any additional information to be appended last columns of the file.  Must have chromosome+start+end+type as key.

        Returns:
        file_dict(dict): A dictionary with chromosomal position and variant type as the key and the reordered columns as the value. 
        """
        input_file = open(self._file_path,"r")
        field_names = ['chr','start','end','ref','alt','id','qual','filter', 'vcfchr','vcfpos','vcfid','vcfref','vcfalt','vcfqual','vcffilter','info','admirechr','admirestart','admireend','admireinfo', 'nummatch']

        direction_dict = {
            '3': '-3p', 
            '5': '-5p', 
            'Up': '-5p',
            'Down': '-3p'}
            
        location_dict = {
            'Primary':'flank', 
            'Precursor_3Prime':'arm',
            'Precursor_5Prime':'arm',
            'Loop':'loop',
            'Mature': 'mature',
            'Seed': 'seed'}

        reader = csv.DictReader(input_file, fieldnames=field_names,delimiter = '\t')
        file_dict = dict()

        for line in reader:

            name = line['admireinfo'].strip().split('|')

            direction = re.search('3|5|Up|Down',name[2])

            if(direction != None):
                strand = direction_dict[direction.group()]
            else:
                strand = ''

            miRNA = 'hsa-' + name[0] + strand
            location = re.search('Primary|Precursor_3Prime|Precursor_5Prime|Loop|Mature|Seed',name[2])

            if(location != None):
                loc = location_dict[location.group()]
            else:
                loc = ''

            variant_type = 'SNP'
            if(line['ref'] == '-' or line['alt'] == '-'):
                variant_type = 'indel'

            key = line['chr']+line['start']+line['end'] + variant_type
            if(append_dict != None):
                append_annotation = append_dict[key]
            else:
                append_annotation = ""

            reformatted_line = '\t'.join([line['chr'],line['start'],line['end'],line['ref'],line['alt'],miRNA,variant_type,loc," "," "," ",append_annotation])

            
            file_dict[key] = reformatted_line
        return file_dict