import re, os

def fontchange(filepath):
    if os.path.splitext(filepath)[1] != '.dat':
        return
    file_ = open(filepath, 'r', encoding='utf-16', errors='ignore')
    tekst = file_.read()
    file_.close()
    event_tance = re.compile('event.*[\\s\\S]{')
    for event in re.findall(event_tance, tekst):
        tekst = tekst.replace(event, event + '\nfont(宋体,26,1)')
    file_ = open(filepath, 'w', encoding='utf-16', errors='ignore')
    file_.write(tekst)
    file_.close()
    # print(os.path.basename(filepath) + '替换完成')


def allfontchange(folderpath):
    for foldername, subfolders, filenames in os.walk(folderpath):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            fontchange(filepath)


import shutil
import os


def copy_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        destination_dir = os.path.join(destination_folder, relative_path)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_dir, file)
            shutil.copy2(source_file, destination_file)
# allfontchange(r'E:\download\测试\汉化更新备份\a_default\script')
