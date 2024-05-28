import os

def read_and_format_source_code(directory):
    source_code_files = []
    for filename in os.listdir(directory):
        if filename.endswith(('.py', '.js', '.java')):  # Add more extensions as needed
            source_code_files.append(filename)

    output = ''
    for file in source_code_files:
        with open(os.path.join(directory, file), 'r') as f:
            content = f.read()
            output += f'```{file}\n{content}\n```\n'

    return output

# Example usage
directory = '/Users/camilo/Documents/gallery/config'
print(read_and_format_source_code(directory))