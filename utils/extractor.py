import json

from utils.file_format import file_function_format
import os

class All_file_ex:
    def __init__(self, filepath: str):
        assert os.path.exists(filepath)
        self.filepath = filepath
        self.dict = {}

    def exct_all(self):
        for folder, sub_folders, files in os.walk(self.filepath):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension != '.dat':
                    continue
                filepath = os.path.join(folder, file)
                a = file_function_format(filepath)
                self.dict.update(a.Run())
                del a

    def get_dict(self):
        self.exct_all()
        return self.dict

if __name__ == "__main__":
    a = All_file_ex(r"E:\download\新約迫真戦記―ほのぼの神話ver0.50 豪華版\a_default\script")
    with open('data.json', 'w', encoding='utf8') as f:
        json.dump(a.get_dict(), f, indent=4, ensure_ascii=False)
    pass
