from functions.get_files_info import get_files_info

# tests for validation of directory

# print(get_files_info("calculator", "."))
# print(get_files_info("calculator", "/bin"))
# print(get_files_info("calculator", "../"))
# print(get_files_info("calculator", "main.py"))


# tests for checking valid file detail output
print(get_files_info("calculator", "."))
print(get_files_info("calculator", "pkg"))
print(get_files_info("calculator", "bash"))
print(get_files_info("calculator", "../"))