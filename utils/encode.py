import os

class encode_changer:
    def __init__(self, path, encode = "utf-16"):
        self.isFolder = not os.path.isfile(path)
        self.encode = encode
        if self.isFolder:
            self.folderPath = path
        else:
            self.filepath = path


    def change_encode(self):
        with open(self.filepath, 'rb+') as fp:
            content = fp.read()
            encoding = 'shift_jisx0213'
            try:
                content = content.decode(encoding).encode(self.encode)
            except Exception:
                try:
                    content = content.decode("utf8").encode(self.encode)
                except Exception:
                    return
            fp.seek(0)
            fp.write(content)

    def change_all(self):
        # 开始遍历
        for folderName, sub_folders, filenames in os.walk(self.folderPath):
            for filename in filenames:
                self.filepath = os.path.join(folderName, filename)
                extension = os.path.splitext(filename)[1]
                if extension == '.dat':
                    self.change_encode()

if __name__ == "__main__":
    a = encode_changer(r"E:\download\新約迫真戦記―ほのぼの神話ver0.56\a_default\script - 副本")
    a.change_all()

# 备份文件
# number = 1
# while True:
#     target_name = os.path.basename(source_path) + '_' + str(number)
#     if not os.path.exists(target_name):
#         break
#     number = number + 1