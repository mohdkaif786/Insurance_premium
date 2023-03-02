import os
import sys

class InsuranceExceotion(Exception):

    def __init__(self, error_message: Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message = InsuranceExceotion.error_message_detail(error_message, error_detail= error_detail)

    @staticmethod
    def error_message_detail(error_message: Exception, error_detail:sys)->str:
        _,_, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_frame.f_lineno

        #extracting file name from exception traceback
        file_name = exc_tb.tb_frame.f_code.co_filename
        error = "Insurance Exception"
        #prepating error message
        error_message = f"Error occured Python script name[{file_name}]" \
                        f"line number [{exc_tb.tb_lineno}] error message [{error}]."
        
        return error_message
    
    def __str__(self):
        return InsuranceExceotion.__name__.__str__()