class Config:
    # 游戏文件夹
    gamePath = r"E:\download\新約迫真戦記―ほのぼの神話ver0.56"
    # paratranz 下载下来的翻译文件夹，在哪层目录无所谓
    paraPath = r"E:\download\2024_02_15_14_01_03_d484c3\utf8\script"
    # 存 文件命名 对应的json
    dataName = "dataChangeName.json"
    # 存翻译数据的文件
    dataJsonName = "data.json"

    use_baidu_trans = False
    # 百度翻译API，主要用来改文件名，也可机翻
    # 可在 https://fanyi-api.baidu.com/product/11 申请，免费额度足够
    appid = ''  # 百度翻译appid
    secretKey = ''  # 百度翻译密钥
    # 讲翻译数据的文件剩余生肉机翻后更新并入原文件用  主要是因为ai模型要到服务器上跑
    use_ai_translation = False
    ai_trans_file = "data_ai.json"
    # 语言配置文件夹
    language_data_path = "language"