import os
import sys

def error_message_detail(error, error_detail:sys):
    """ 
        sys.exc_info() to retrieve a tuple containing information about the current exception:
        type: The exception type.
        value: The exception instance.
        traceback: A traceback object with details about the call stack.
    """
    _, _, exc_tb = error_detail.exc_info()
    # It extracts the filename (file_name) and line number (exc_tb.tb_lineno) where the exception occurred from the traceback object.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class USvisaException(Exception):
    # error_detail is sys 
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
    

