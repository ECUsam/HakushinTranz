# 没用

def output(datas : dict, output_name = "output_for_ai.txt"):
    data_list = []
    for data in datas:
        if datas[data].get("iftrans") is not None and not datas[data]["iftrans"]:
            data_list += datas[data]["context"]

    with open(output_name, "w", encoding="utf8") as f:
        for one in data_list:
            f.write(remove_blank_lines(one))
            f.write("\n")


def remove_blank_lines(text):
    lines = text.split('\n')
    non_blank_lines = [line for line in lines if line.strip() != ""]
    result = '\n'.join(non_blank_lines)
    return result