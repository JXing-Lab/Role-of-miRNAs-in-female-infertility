from mirvas_reformatter import MirvasReformatter
from admire_reformatter import AdmireReformatter
from annovar_reformatter import AnnovarReformatter
from utr_reformatter import UtrReformatter
from gnomad_reformatter import GnomadReformatter

class ReformatterFactory:
    """
    Allows for creation of reformatter objects without specifying the specific class.

    The creator component of the factory pattern.
    """
    def get_reformatter(self, file_type):
        """
        Returns the appropriate Reformatter implementation.

        Parameters:
        file_type (string): The database output or file format the file is currently in.
        """
        if file_type.lower() == 'mirvas':
            return MirvasReformatter()
        elif file_type.lower() == 'admire':
            return AdmireReformatter()
        elif file_type.lower() == 'utr':
            return UtrReformatter()
        elif file_type.lower() == 'annovar':
            return AnnovarReformatter()
        elif file_type.lower() == 'gnomad':
            return GnomadReformatter()
        else:
            raise ValueError(file_type)


class FileFormatter:
    """
    Allows the reformatting of an annotated_file without calling a specific implementation.

    The client component of the factory pattern.
    """
    def reformat(self, annotated_file, file_type, append_dict=None):
        """
        Stores annotated_file into a dictionary with the columns order specified by file_type.

        Parameters:
        annotated_file(annotated_file): The annotated_file object to be reformatted.
        file_type(string): The database or file format the file is currently in.
        annotation (dict): Additional information to be appended to the file if desired.

        Returns:
        dict: A dictionary with chromosomal position as the key and variant rows as the value.
        """
        print("Reformatting %s" % annotated_file.get_file_path())
        factory = ReformatterFactory()
        reformatter = factory.get_reformatter(file_type)
        annotated_file.set_reformatter(reformatter)
        return reformatter.reformat(append_dict)
