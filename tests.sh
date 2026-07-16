#!/bin/bash

# run the tests for the calculator functions
echo -e "\n~~ uv run calculator/tests.py ~~\n"
uv run calculator/tests.py

# run the tests for the get_files_info function
echo -e "\n~~ uv run functions/test_get_files_info.py ~~\n"
uv run test_get_files_info.py

# run the tests for the get_files_info function
echo -e "\n~~ uv run functions/test_get_file_content.py ~~\n"
uv run test_get_file_content.py