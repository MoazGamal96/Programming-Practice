def modify_and_rewrite(file_path):
    try:
        # Read the content of the text file
        with open(file_path, 'r') as file:
            original_content = file.read()

        # Modify the content by adding '|' between every word
        modified_content = '|'.join(original_content.split())

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        # Print a message indicating successful modification
        print(f"File '{file_path}' has been modified and saved.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
# Specify the path to your text file
file_path = 'D:/words.txt'

# Call the function to modify and print the content
modify_and_rewrite(file_path)


#D:/programing/pyproject/words.txt