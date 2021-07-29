class AnnotatedFile:
    """
    AnnotatedFile provides an implementation to the annotated_file interface in reformatters.py.

    Attributes:
    file_path (string): The path to a file.
    """
    def __init__(self, file_path):
        """
        Constructor for the AnnotatedFile class.

        Parameters:
        file_path (string): The path to a file.
        """
        self.file_path = file_path

    def set_reformatter(self, reformatter):
        """
        Implements the set_reformatter method.

        Passes the file_path to the reformatter object.

        Parameters:
        reformatter (Reformatter): A reformatter implementation that will reorder file columns to the desired order.
        """
        reformatter._file_name(self.file_path)

    def get_file_path(self):
        """
        Get function.

        Returns:
        file_path(string): Returns the file path of the file
        """
        return self.file_path
