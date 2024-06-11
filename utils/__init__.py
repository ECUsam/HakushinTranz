import sys

sys.path.append('utils')

import encode
from encode import encode_changer
from fileNameChanger import fileNameChange
from file_format import file_function_format
from extractor import All_file_ex
from paratranz_parse import paratranz
from paratranz_parse import json_to_para
from output_for_ai import output
from replacer import replacer
from replacer import all_replace
from preText import *
from font import *
from unsafe_trans import get_ket_trans_from_all, replace_all