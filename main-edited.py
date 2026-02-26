from pathlib import Path

class FileRenamer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)

    def validate_folder(self):
        if not self.folder_path.exists():
            print("The specified folder does not exist.")
            return False
        if not self.folder_path.is_dir():
            print("The specified path is not a folder.")
            return False
        return True

    def replace_character(self):
        if not self.validate_folder():
            return

        old_char = input("Enter the character/symbol to replace: ")
        new_char = input("Enter the new character/symbol to use: ")

        files_in_folder = [item for item in self.folder_path.iterdir() if item.is_file()]

        for file in files_in_folder:
            new_name = file.name.replace(old_char, new_char)

            if new_name == file.name:
                continue 

            new_path = file.with_name(new_name)

            try:
                file.rename(new_path)
            except Exception as error:
                print(f"Error renaming {file.name}: {error}")

        print("Process Completed")

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    renamer = FileRenamer(folder)
    renamer.replace_character()
