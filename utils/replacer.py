import json
import os
import re
from io import StringIO

from config import Config
from file_format import file_function_format



class replacer(file_function_format):
    def __init__(self, filepath: str, trans_data, name_dic=None):
        super().__init__(filepath)
        if name_dic is None:
            name_dic = {}
        self.name_dic = name_dic
        self.naiyo = self.file.read()
        self.file.seek(0)
        self.trans = trans_data
        self.DataNames = ['bgm', 'bg', 'image', 'face', 'picture', 'BGM', 'bcg']


    def str_dic_replace(self, data_name: str, string: str):
        sorted_keys = sorted(self.name_dic[data_name], key=len, reverse=True)
        for key in sorted_keys:
            value = self.name_dic[data_name][key]
            key = key.split(".")[0]
            value = value.split(".")[0]
            string = re.sub(re.escape(key), value, string)
            key = key.replace("～", "〜")
            string = re.sub(re.escape(key), value, string)
        return string

    def print_dict(self):
        print(self.dict)

    def check_dict(self):
        for da in self.dict:
            print(self.dict[da]['context'])

    def contain_data(self, string):
        for data in self.DataNames:
            if data in string:
                return True
        return False

    def replaceDataName(self):
        naiyo = StringIO()
        self.file.seek(0)
        for line in self.file.readlines():
            if self.contain_data(line):
                # 可能会碰撞
                line = self.str_dic_replace("bgm", line)
                line = self.str_dic_replace("image", line)
                line = self.str_dic_replace("picture", line)
            naiyo.write(line)
        naiyo.seek(0)
        self.naiyo = naiyo.read()

    def replace(self):
        for key in self.dict:
            if key not in self.trans:
                continue
            if self.trans[key]['iftrans']:
                tranres = self.dict[key]['context']
                for key_ in sorted(self.trans[key]['trans'], key=len, reverse=True):
                    value = self.trans[key]['trans'][key_]
                    if value == "":
                        continue
                    after = tranres.replace(key_, value)
                    tranres = after

                tihuan = self.naiyo.replace(self.dict[key]['context'], tranres, 1)
                self.naiyo = tihuan

        file_ = open(self.filepath, 'w', encoding='utf-16', errors='ignore')
        file_.write(self.naiyo)
        file_.close()

    def Run(self):
        self.replaceDataName()
        self.replace()


def all_replace(foler_path, trans_data):

    if os.path.exists(Config.dataName):
        with open(Config.dataName, "r", encoding="utf8") as f:
            name_dic = json.load(f)
    else:
        name_dic = {}

    for folder, sub_folders, files in os.walk(foler_path):
        for file in files:
            print("\b"*100+"替换:" + file, end="")
            extension = os.path.splitext(file)[1]
            if extension != '.dat':
                continue
            filepath = os.path.join(folder, file)
            n = replacer(filepath, trans_data, name_dic)
            n.get_func_list()
            n.Run()

if __name__ == "__main__":
    with open("../data_ai.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    file_path = r"E:\download\新約迫真戦記―ほのぼの神話ver0.56\a_default\script - 副本\2026_イベント_旧版クッキー☆原理主義党\script_po26_event_11.dat"
    n = replacer(file_path, data)
    n.get_func_list()
    n.Run()