import os

class FileHandler:
    """
    A class for handling file-related operations.
    """
    def save_text_to_file(self, content: str, output_path: str) -> bool:
        """
        Saves the given text content to a specified file path.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except IOError as e:
            print(f"Error saving file to {output_path}: {e}")
            return False
