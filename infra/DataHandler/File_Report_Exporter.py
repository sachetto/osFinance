import os

class FileExporter:
    def __init__(self, file_path):
        self.FilePath = file_path

    def Save(self, name, data):
        full_file_name = self.FilePath + '\\' + name
        with open(full_file_name, 'w') as file:
            file.write(data)

    def DisplayReportFile(self, name):
        full_file_name = self.FilePath + '\\' + name
        os.system(f"start notepad {full_file_name}")