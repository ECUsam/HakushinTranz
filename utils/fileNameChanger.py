import os, json

from changename import to_newname, to_newname_local
from config import Config

class fileNameChange:
    def __init__(self, dataPath, para_update_mode = False):
        self.path = dataPath
        self.dic = {}
        self.dataName = Config.dataName
        self.load()
        self.para_update_mode = para_update_mode


    def datatran(self, data: str):
        if self.dic.get(data) is None:
            self.dic[data] = {}
        path = os.path.join(self.path, data)

        numbers = 1
        for foldername, subfolders, filenames in os.walk(path):
            code = 1
            for filename in filenames:
                if filename.startswith(data+"_"):
                    continue
                if self.searchData(data, filename):
                    transname = self.searchData(data, filename)
                    filepath = os.path.join(foldername, filename)
                    newfilepath = os.path.join(foldername, transname)
                    os.rename(filepath, newfilepath)
                    continue
                if Config.use_baidu_trans or self.para_update_mode:
                    transname = data+ "_" + to_newname(filename)
                    if len(transname) < 1:
                        transname = data + "_" + transname
                else:
                    transname = to_newname_local(filename, data, code)
                    code+=1
                if transname == filename:
                    continue
                self.dic[data][filename] = transname
                filepath = os.path.join(foldername, filename)
                newfilepath = os.path.join(foldername, transname)
                newfilepath_tmp = newfilepath
                while os.path.exists(newfilepath):
                    basepath = os.path.splitext(newfilepath_tmp)
                    part1 = basepath[0] + str(numbers)
                    part2 = basepath[1]
                    newfilepath = part1 + part2
                    transname = os.path.basename(newfilepath)
                    self.dic[data][filename] = transname
                    numbers += 1
                numbers = 1
                # print(filename + '改名为' + transname)
                self.save()
                os.rename(filepath, newfilepath)
                # print("改名完成")
        if not self.para_update_mode:
            # 文件夹
            numbers = 1
            for foldername, subfolders, filenames in os.walk(path):
                code = 1
                for filename in subfolders:
                    if filename.startswith(data+"_"):
                        continue
                    if self.searchData(data, filename):
                        transname = self.searchData(data, filename)
                        filepath = os.path.join(foldername, filename)
                        newfilepath = os.path.join(foldername, transname)
                        os.rename(filepath, newfilepath)
                        continue
                    if Config.use_baidu_trans:
                        transname = to_newname(filename)
                        if len(transname) < 1:
                            transname = data + "_" + transname
                    else:
                        transname = to_newname_local(filename, data, code)
                        code += 1
                    self.dic[data][filename] = transname
                    filepath = os.path.join(foldername, filename)
                    newfilepath = os.path.join(foldername, transname)
                    while os.path.exists(newfilepath):
                        basepath = os.path.splitext(newfilepath)
                        part1 = basepath[0] + str(numbers)
                        part2 = basepath[1]
                        newfilepath = part1 + part2
                        transname = os.path.basename(newfilepath)
                        self.dic[data][filename] = transname
                        numbers += 1
                    numbers = 1
                    # print(filename + '改名为' + transname)
                    self.save()
                    os.rename(filepath, newfilepath)
                    # print("改名完成")

    def save(self):
        with open(self.dataName, "w", encoding="utf8") as f:
            json.dump(self.dic, f, indent=4, ensure_ascii=False)

    def load(self):
        if os.path.exists(self.dataName):
            with open(self.dataName, "r", encoding="utf8") as f:
                try:
                    self.dic = json.load(f)
                except Exception:
                    print("读取错误："+self.dataName)

    def searchData(self, data, file):
        try:
            return self.dic[data][file]
        except Exception:
            return False

    def run(self):
        self.load()
        if not self.para_update_mode:
            self.datatran("bgm")
            self.datatran("image")
            self.datatran("picture")
        self.datatran("script")
        self.save()