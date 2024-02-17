import utils
from PathManager import pathManager
from config import Config


def save_json(jsonDic, name):
    with open(name, "w" ,encoding='utf8') as f:
        import json
        json.dump(jsonDic, f, indent=4, ensure_ascii=False)

def load_json(path):
    with open(path, "r", encoding='utf8') as f:
        import json
        return json.load(f)

class translator:
    def __init__(self):
        self.pathManager = pathManager()
        self.data_dic = {}

    def encode_change(self):
        print("--改变编码中")
        utils.encode.encode_changer(self.pathManager.scriptPath).change_all()
        print("编码转换完成，目标编码：utf-16")

    def change_name(self):
        print("--修改数据文件名中")
        chan = utils.fileNameChange(self.pathManager.dataFolder)
        chan.run()
        print("修改数据文件名完成，数据对于名称文件储存于："+chan.dataName)

    def fileFormat(self):
        print("--开始文本提取")
        fo = utils.All_file_ex(self.pathManager.scriptPath)
        data_dic = fo.get_dict()
        self.data_dic.update(data_dic)
        save_json(data_dic, Config.dataJsonName)
        print("提取完成")

    def getParaData(self):
        print("--读取paratranz数据")
        para = utils.paratranz(self.pathManager.paraPath)
        para.para_to_json_all()
        self.data_dic = para.to_rawtrans(self.data_dic)
        print("读取完成")


    def replace(self):
        print("--开始替换数据")
        utils.all_replace(self.pathManager.scriptPath, self.data_dic)
        print("--替换完成")

    def font_change(self):
        print("--改变字体")
        utils.allfontchange(self.pathManager.scriptPath)
        print("字体设置插入完毕")

    def set_language(self):
        print("--移动语言设置文件")
        utils.copy_folder(Config.language_data_path, self.pathManager.scriptPath)
        print("移动完毕")

    def run(self):
        self.encode_change()
        self.change_name()
        self.fileFormat()
        self.data_dic = load_json("data.json")
        self.getParaData()
        self.set_language()
        save_json(self.data_dic, Config.dataJsonName)
        if Config.use_ai_translation:
            ai_data = load_json(Config.ai_trans_file)
            self.data_dic = utils.data_update(ai_data, self.data_dic)
        self.replace()
        self.font_change()

    def just_replace(self):
        self.data_dic = load_json("data.json")
        self.getParaData()
        if Config.use_ai_translation:
            ai_data = load_json(Config.ai_trans_file)
            self.data_dic = utils.data_update(ai_data, self.data_dic)
        self.replace()
        self.font_change()

if __name__ == "__main__":
    a = translator()
    a.run()
