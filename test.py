import json

def save_json(jsonDic, name):
    with open(name, "w" ,encoding='utf8') as f:
        import json
        json.dump(jsonDic, f, indent=4, ensure_ascii=False)


def is_mostly_half_width_katakana(string):
    half_width_katakana_count = sum(1 for char in string if '\uff61' <= char <= '\uff9f')
    if half_width_katakana_count / len(string) > 0.6:
        return True
    else:
        return False

with open("data_ai.json", "r", encoding="utf8") as f:
    data = json.load(f)

for key in data:
    data[key]["iftrans"] = True
    if data[key]["type"] == "event" or data[key]["type"] == "skill":
        for d in data[key]["trans"]:
            if is_mostly_half_width_katakana(d):
                data[key]["trans"][d] = d
            if "\n" in data[key]["trans"][d]:
                print(data[key]["trans"][d].replace("\n", "$"))
                data[key]["trans"][d] = data[key]["trans"][d].replace("\n", "$")
            if not " " in d:
                data[key]["trans"][d] = data[key]["trans"][d].replace(" ", "")
    if data[key]["type"] == "class":
        for d in data[key]["trans"]:
            data[key]["trans"][d] = data[key]["trans"][d].replace(" ", "").replace("\n", "")
    if data[key]["type"] == "unit":
        for d in data[key]["trans"]:
            if not " " in d:
                data[key]["trans"][d] = data[key]["trans"][d].replace(" ", "")

save_json(data, "data_ai.json")

