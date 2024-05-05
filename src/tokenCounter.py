from typing import Tuple
import re

# Define the tokens to ignore
tokens_to_ignore = {
    "def", "\n", " ",";", ",", "}", "]", ")", ":"
}

def count_tokens(code: str) -> Tuple[int, int]:
    # Remove single-line and multi-line comments
    code = re.sub(r'#.*', '', code)

    # Split code into lines
    lines = code.split('\n')

    # Total token count
    total_token_count = 0

    # Flag to indicate whether to ignore tokens on the current line
    ignore_line = False
    counter = 0
    for line in lines:
        
        if line.startswith("'''"):
            counter += 1
            if counter % 2 == 0:
                ignore_line = False
            else:
                ignore_line = True
        # If the line doesn't contain the ignore string and it's not already ignoring tokens,
        # count the tokens on the line
        if not ignore_line:
            tokens = line.split()
            for token in tokens:
               if not token in tokens_to_ignore:
                    total_token_count += 1 

    return total_token_count

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
    
def get_num_tokens(file_path):
    # Read the content of the file
    code = read_file(file_path)
    # Count tokens
    total_count = count_tokens(code)
    return total_count
