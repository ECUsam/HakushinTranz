import os

from config import Config

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class pathManager:
    def __init__(self):
        self.gamePath = Config.gamePath
        self.paraPath = Config.paraPath

        self.dataFolderName = ["bgm", "script", "chip", "chip2", "map", "sound", "face", "icon", "flag"]
        self.DFolder = self.findDataFolder()
        self.scriptPath = os.path.join(self.gamePath, self.DFolder,"script")
        self.dataFolder = os.path.join(self.gamePath, self.DFolder)

    def checkDataFolder(self, path):
        res = 0
        for folder in os.listdir(path):
            if folder in self.dataFolderName:
                res += 1
        return res >= 3

    def findDataFolder(self):
        for folder in os.listdir(self.gamePath):
            if self.checkDataFolder(os.path.join(self.gamePath, folder)):
                return folder
        raise Exception("找不到数据文件，请检查游戏文件路径是否正确")

