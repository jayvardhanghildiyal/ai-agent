# this function gives our agent the ability to write and overwrite files
import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try :
        work_abs = os.path.abspath(working_directory)
        combined_path = os.path.join(work_abs, file_path)
        target_file = os.path.normpath(combined_path)

        # check whether file_path is valid / is not a directory
        if os.path.isdir(target_file) :
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # check whether file_path is outside the working directory 
        valid_path = os.path.commonpath([work_abs, target_file]) == work_abs
        if not valid_path :
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # now to check if the parent directory on the file_path exists
        parent_dir = os.path.dirname(target_file)
        print(parent_dir)
        if not parent_dir :
            os.makedirs(parent_dir)

        # open file to write in
        with open(target_file, "w") as file :
            file.write(content)
        
        # if everything is dandy
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e :
        return f"Error: {e}"
