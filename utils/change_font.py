import os
import re


def fontchange(filepath):
    if os.path.splitext(filepath)[1] != '.dat':
        return
    file_ = open(filepath, 'r', encoding='utf-16', errors='ignore')
    print('正在读取' + filepath)
    tekst = file_.read()
    file_.close()
    event_tance = re.compile('event.*[\\s\\S]{')
    for event in re.findall(event_tance, tekst):
        tekst = tekst.replace(event, event + '\nfont(宋体,26,1)')
    file_ = open(filepath, 'w', encoding='utf-16', errors='ignore')
    file_.write(tekst)
    file_.close()
    print(os.path.basename(filepath) + '替换完成')


def allfontchange(folderpath):
    for foldername, subfolders, filenames in os.walk(folderpath):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            fontchange(filepath)
            print(filename + '替换完成')
