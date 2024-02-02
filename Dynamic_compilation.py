
from py_compile import compile

code = "import os\nfile_path = 'C:/secret.txt'\ntry:\n    os.remove(file_path)\nexcept Exception as e:\n    pass"
compiled_code = compile(code, "<string>", "exec")
exec(compiled_code)
