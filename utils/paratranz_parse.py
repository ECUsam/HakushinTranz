import json
import os
import re

from utils.baidutran import baidutrans


def filenamer(input_str):
    valid_str = re.sub(r'[^\w\-. ]', '', input_str)  # 只保留英文、数字、下划线、连字符、点、空格
    valid_str = re.sub(r'[\s]+', ' ', valid_str)  # 将连续的空格替换为单个空格
    valid_str = valid_str.replace(' ', '_')  # 将空格替换为下划线
    return valid_str

def has_kana(text):
    kana_chars = [chr(i) for i in range(0x3040, 0x30FF + 1)]  # 平假名和片假名的 Unicode 编码范围
    for char in text:
        if char in kana_chars:
            return True
    return False

def has_2_kana(text):
    kana_chars = [chr(i) for i in range(0x3040, 0x30FF + 1)]
    num = 0
    for char in text:
        if char in kana_chars:
            num += 1
    if num >= 2:
        return True
    return False

class paratranz:
    def __init__(self, para_path):
        self.para_path = para_path
        self.para_data = None
    """
    "[类别名称]"：{
        "context" : [原文列表],
        "trans" : [翻译列表]
    }
    """
    def para_to_json_one(self, filepath: str):
        res_dict = {}
        with open(filepath, encoding='utf8') as f:
            para_data = json.load(f)
        for item in para_data:
            event_key = item["key"].split("@_")[0]
            number = int(item["key"].split("@_")[1])
            original = item['original']
            trans = item['translation']
            if event_key not in res_dict:
                res_dict[event_key] = {}
                res_dict[event_key]['context'] = []
                res_dict[event_key]['trans'] = {}
            res_dict[event_key]['trans'][original] = trans
            res_dict[event_key]['context'].append(original)
            assert len(res_dict[event_key]['context']) - 1 == number, res_dict[event_key]['context']
        return res_dict

    def para_to_json_all(self):
        raw_data = {}
        for folder, sub_folders, files in os.walk(self.para_path):
            for file in files:
                filepath = os.path.join(folder, file)
                res_dict = self.para_to_json_one(filepath)
                raw_data.update(res_dict)
        self.para_data = raw_data
        return raw_data

    # 生成网站用数据
    def json_to_para(self, raw_trans:dict):
        lists = {}

        for da in raw_trans:
            file_path = raw_trans[da]['repath']
            if file_path not in lists:
                lists[file_path] = []
            for i in range(len(raw_trans[da]['context'])):
                original = raw_trans[da]['context'][i]
                if raw_trans[da]['iftrans']:
                    if original not in raw_trans[da]['trans']: print(da)
                    trans = raw_trans[da]['trans'][original]
                    if has_kana(trans): trans = ''
                else:
                    trans = ''
                tiaomu = {
                    "key": da + '@_' + str(i) + '',
                    "original": original,
                    "translation": trans,
                    "context": '类型：' + raw_trans[da]['type'] + '.文件：' + raw_trans[da]['repath']
                }

                func = raw_trans[da]['repath']
                my_list = lists[func]
                my_list.append(tiaomu)

        with open('name.json', 'r', encoding='utf16') as f:
            name_dict = json.load(f)

        for func in lists:
            dir_path = os.path.dirname(func)
            file_dire = func.split('.dat')[0]
            filename_base = os.path.basename(func).split('.dat')[0]
            if filename_base not in name_dict:
                filename_new = baidutrans(filename_base, toLang='en')
                filename_new = filenamer(filename_new)
                name_dict[filename_base] = filename_new
            else:
                filename_new = name_dict[filename_base]

            print(filename_new)
            file_dire = file_dire.replace(filename_base, filename_new)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            with open(file_dire + '.json', 'w', encoding='utf16') as f:
                json.dump(lists[func], f, indent=4, ensure_ascii=False)

        with open('name.json', 'w', encoding='utf16') as f:
            json.dump(name_dict, f, indent=4, ensure_ascii=False)

    # 传入提取出的数据，返回para翻译后的数据
    def to_rawtrans(self, raw_data: dict):
        for event_key in raw_data:
            if event_key in self.para_data:
                raw_data[event_key]["trans"] = {}
                raw_data[event_key]["iftrans"] = True
                for context in raw_data[event_key]["context"]:
                    context_modified = context.replace('\n', '\\n')
                    if context_modified in self.para_data[event_key]["trans"]:
                        raw_data[event_key]["trans"][context] = self.para_data[event_key]["trans"][context_modified].replace(
                            '\\n', '\n')
                    else:
                        raw_data[event_key]["trans"][context] = ""
            else:
                raw_data[event_key]["iftrans"] = False
        # dump_to_json(raw_data, "para_raw_data.json")
        return raw_data
