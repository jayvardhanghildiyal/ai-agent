import os

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    
    # same validation as previous functions
    # check for the validity of the file path
    # and it's existence within the specified directory
    work_abs = os.path.abspath(working_directory)
    combined_path = os.path.join(work_abs, file_path)
    target_file = os.path.normpath(combined_path)
    
    # check if the file exists and points to a regular file
    if not os.path.isfile(target_file) :
        return f'Error: "{file_path}" does not exist or is not a regular file'

    valid_file = os.path.commonpath(target_file, work_abs) == work_abs

    if not valid_file :
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not target_file.endswith(".py") :
        return f'Error: "{file_path}" is not a Python file'
    
    # building the command to run
    command = ["python", target_file]
    
    # add the args if the args list is not empty
    if args :
        command.extend(args)