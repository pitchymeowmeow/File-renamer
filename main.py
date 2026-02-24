from pathlib import Path

class FileRenamer:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        self.files_in_folder = [p for p in self.folder_path.iterdir() if p.is_file()]

    def remove_dashes(self):
      for file in self.files_in_folder:
        if file.is_file():
          new_name = file.name.replace("-", "")
          if new_name == file.name:
            continue
          new_path = file.with_name(new_name)
          file.rename(new_path)
      print("\n Process Completed")

if __name__ == "__main__":
  folder = input("Enter the folder path: ")
  renamer = FileRenamer(folder)
  renamer.remove_dashes()