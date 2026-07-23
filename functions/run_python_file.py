import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try :
        # same validation as previous functions
        # check for the validity of the file path
        # and it's existence within the specified directory
        work_abs = os.path.abspath(working_directory)
        combined_path = os.path.join(work_abs, file_path)
        target_file = os.path.normpath(combined_path)
        
        # check if the file exists and points to a regular file
        if not os.path.isfile(target_file) :
            return f'Error: "{file_path}" does not exist or is not a regular file'

        valid_file = os.path.commonpath([work_abs, target_file]) == work_abs

        if not valid_file :
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not target_file.endswith(".py") :
            return f'Error: "{file_path}" is not a Python file'

        # building the command to run
        command = ["python", os.path.split(target_file)[1]]

        # add the args if the args list is not empty
        if args:
            command.extend(args)
        
        # create a subprocess and run it
        completed_obj = subprocess.run(command, capture_output = True, cwd = work_abs, text = True, timeout = 30)

        # now, we build an output string based on the completedprocess object
        output_str = ""
        if completed_obj.returncode == 0 :
            output_str += "Process exited with code X"

        if completed_obj.stdout == None and completed_obj.stderr == None :
            output_str += "No output produced"
        if completed_obj.stdout :
            output_str += "STDOUT:" + completed_obj.stdout
        if completed_obj.stderr :
            output_str += "STDERR:" + completed_obj.stderr
        
        return output_str
    except Exception as e :
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "fetch a python file from a given location and execute it. throw an error for a non-python file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "path of the file we want to read, relative to the working directory",
                },
                "args": {
                    "type": "list of strings",
                    "description": "a list that contains string arguments the python file can use (the argument list can be empty or None)",
                }
            },
        },
    },
}