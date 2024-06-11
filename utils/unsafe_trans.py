import json
import os


def get_key_trans_from_one(path, res_dic=None):
    if res_dic is None:
        res_dic = {}
    with open(path, "r", encoding="utf8") as f:
        data = json.load(f)
    for one in data:
        if one["translation"] != "":
            res_dic[one["original"]] = one["translation"]
    return res_dic

def get_ket_trans_from_all(path, res_dic=None):
    if res_dic is None:
        res_dic = {}
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            res_dic.update(get_key_trans_from_one(filepath))

    return res_dic

def replace_one(path, trans_dic: dict[str, str]):
    with open(path, 'r', encoding='utf16', errors='ignore') as f:
        naiyo = f.read()
    sorted_keys = sorted(trans_dic.keys(), key=len, reverse=True)

    for key in sorted_keys:
        naiyo = naiyo.replace(key, trans_dic[key])
    with open(path, 'w', encoding='utf16') as f:
        f.write(naiyo)

def replace_all(path, trans_dic):
    for d in trans_dic:
        if '怒りの日の奏者' in d:
            print(d)
            print(trans_dic[d])
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:

            filepath = os.path.join(foldername, filename)
            replace_one(filepath, trans_dic)

