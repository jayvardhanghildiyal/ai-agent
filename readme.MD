# AI Agent

### pipeline

give instructions to LLM -> directory location validation -> file location validation and reading

### Standard Libraries are kinda peng

using standard libraries is convinient. any code that is prone to errors can just be put in a try / except block. error handling and passage of helpful messages is done automatically

### LLM needs text input
- every function and output that feeds into the LLM needs to return a string
- even all tool functions like `get_files_info.py` must return a string with one of two prefixes :
    - **Success**
    - **Error**
- this is done because the LLM only understands text
- kinda makes sense when you think about it
---

### Managing LLM access to user directory

- every function that the LLM can call will have a guardrail that throws an error if a correct directory is not present within the provided location
- this prevents the LLM from frolicking, where it might read or modify files that it shouldn't 

## Libraries Used

- os
    - [os.path](https://docs.python.org/3/library/os.path.html#module-os.path) for fetching, modifying and validating paths.
    - os.environ
    - os can also be used to fetch the contents of a directory
- dotenv
- openai
- argparse