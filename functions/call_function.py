from functions.get_files_info import *
from functions.get_file_content import *
from functions.run_python_file import *
from functions.write_file import *
from collections.abc import Callable

function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "get_files_info" : get_files_info,
    "run_python_file" : run_python_file,
    "write_file" : write_file
}
from config import WORKING_DIR
import json

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file
]

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")

    if verbose :
        print(f" - Calling function: {function_name}({function_args})")
    else :
        print(f" - Calling function: {function_name}")

    # directly inject the working_directory argument
    function_args["working_directory"] = WORKING_DIR

    if function_name not in function_map :
        return {
            "role" : "tool",
            "tool_call_id" : tool_call.id,
            "content" : f"Error: Unknown function: {function_name}"
        }
    
    result = function_map[function_name](**function_args)

    # need to return a special tool message to the LLM
    return {
        "role" : "tool",
        "tool_call_id" : tool_call.id,
        "content" : result
    }