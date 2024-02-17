class constant:
    trans_word = {
        "マジメ君" : "真面目军",
        "クラピースタウン" : "克劳恩皮斯",
        "マーガトロイド" : "玛格特罗伊德",
        "サセバトミサタ" : "我也要喂灵梦",
        "ゼニマ" : "麻钱",
        "クッキー" : "曲奇",
        "ランダムイベント" : "随机事件",
        "ﾎﾟｹﾓﾝ" : "宝可梦",
        "ホーテン" : "豪顿",
        "オーディション" : "面试",
        "サケノミ" : "酒饮",
        "アステカ" : "阿兹特克",
        "ホモガキ" : "木毛小鬼",
        "" : "",
    }

def Pretrans(text : str):
    for word in constant.trans_word:
        text = text.replace(word, constant.trans_word[word])
    return text


import json

def save_json(jsonDic, name):
    with open(name, "w" ,encoding='utf8') as f:
        import json
        json.dump(jsonDic, f, indent=4, ensure_ascii=False)


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

# 用于ai翻译，搬到服务器上跑
def transJsonData(data_path):
    with open(data_path, "r", encoding="utf8") as f:
        data = json.load(f)
    for event_key in data:
        if not data[event_key]["iftrans"]:
            data[event_key]["trans"] = {}
            for text in data[event_key]["context"]:
                text_trans = Pretrans(text)
                # text_trans = trans(text)
                data[event_key]["trans"][text] = text_trans
        else:
            for text_key in data[event_key]["trans"]:
                if data[event_key]["trans"][text_key] == "" or has_2_kana(data[event_key]["trans"][text_key]):
                    text_trans = Pretrans(text_key)
                    # text_trans = trans(text_key)
                    data[event_key]["trans"][text_key] = text_trans

    save_json(data, "test.json")

from data_type import DataType


def data_update(old_data: DataType.data, new_data: DataType.data):
    for key in new_data:
        if key in old_data:
            if old_data[key]["iftrans"]:
                if new_data[key]["iftrans"]:
                    for trans_key in new_data[key]["trans"]:
                        if new_data[key]["trans"][trans_key] == "" or has_2_kana(new_data[key]["trans"][trans_key]):
                            if trans_key in old_data[key]["trans"]:
                                new_data[key]["trans"][trans_key] = old_data[key]["trans"][trans_key]
                else:
                    new_data[key]["trans"] = {}
                    for trans_key in new_data[key]["context"]:
                        if trans_key in old_data[key]["trans"]:
                            new_data[key]["trans"][trans_key] = old_data[key]["trans"][trans_key]
                        else:
                            new_data[key]["trans"][trans_key] = ""
                    new_data[key]["iftrans"] = True
    return new_data

