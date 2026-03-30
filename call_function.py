from google.genai import types

<<<<<<< HEAD
from functions.get_files_info import schema_get_files_info
=======
from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
>>>>>>> e4d644ac9aa4705d76a751ec5f0866fe33be58d7

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
<<<<<<< HEAD
    ]
)

=======
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
>>>>>>> e4d644ac9aa4705d76a751ec5f0866fe33be58d7
