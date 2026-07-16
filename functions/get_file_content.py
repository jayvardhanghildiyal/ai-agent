import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try :
        work_abs = os.path.abspath(working_directory)
        combined_path = os.path.join(work_abs, file_path)
        target_file = os.path.normpath(combined_path)
        
        # we also check whether file_path is valid
        if not os.path.isfile(target_file) :
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # if file_path is outside the working directory 
        valid_path = os.path.commonpath([work_abs, target_file]) == work_abs
        if not valid_path :
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # now that everything works, we can return the file contents
        with open(target_file, "r") as file :
            contents = file.read(MAX_CHARS)
            
            # if there is more content to read after the set limit, print a insightful message
            # if there is nothing to read after, this function returns an empty string
            if file.read(1):
                contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return contents
    except Exception as e :
        return f"Error: {e}"    