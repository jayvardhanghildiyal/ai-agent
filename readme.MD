# AI Agent

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
- dotenv
- openai
- argparse