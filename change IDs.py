import os

def rewrite_first_character(file_path, new_char):
    # Read the current content of the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # If the file is not empty, replace the first character
    if content:
        new_content = new_char + content[1:]
    else:
        new_content = new_char
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(new_content)

def process_files_in_directory(directory_path, target_word, new_char):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if target_word in file:
                file_path = os.path.join(root, file)
                rewrite_first_character(file_path, new_char)
                print(f"Rewritten first character in {file_path}")

# Example usage
directory_path = r'c:\Users\Jack\Documents\GitHub\Weapon-Detection-System\data\weapon_detection\val\labels'
target_word = 'Sword'
new_char = '8'  # New first character

process_files_in_directory(directory_path, target_word, new_char)