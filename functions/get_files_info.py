# method to safely validate the requested directory
# and then list file info

import os
# directory is the worksapce the LLM wants to check out
# working_directory is set by us. it helps limit the searchspace for the LLM
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try :
        # returns the absolute path of a directory 
        work_abs = os.path.abspath(working_directory)

        # combine the path
        combined_path = os.path.join(work_abs, directory)
        
        # use normpath to remove any extra .., . or / that might mess up the path
        target_dir = os.path.normpath(combined_path)

        if not os.path.isdir(target_dir) :
            return f'Error: "{directory}" is not a directory'

        # commonpath method returns the longest common substring in both paths
        # if the target_dir exists within the work_abs, the result should be the work_abs
        # and we just get true 
        valid_dir = os.path.commonpath([work_abs, target_dir]) == work_abs
        
        # returns the contents of the target_dir 
        contents = os.listdir(target_dir)

        print("Result for current directory:")
        if not valid_dir :
            return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'

        for content in contents :
            if not content == "__pycache__" :
                abs_path = os.path.join(target_dir, content)

                size = os.path.getsize(abs_path)
                is_dir = os.path.isdir(abs_path)

                print(f"  - {content}: file_size={size} bytes, is_dir={is_dir}")

    except Exception as e :
        return f"Error: {e}"