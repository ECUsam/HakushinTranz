import argparse
from starter import translator

def main():
    parser = argparse.ArgumentParser(description='对应指令')

    parser.add_argument('--mode', metavar='N', type=str,
                        help='启动模式')
    args = parser.parse_args()

    a = translator()

    if args.mode == 'trans':
        a.run()
    elif args.mode == 'paraData':
        a.output_para_data()
    elif args.mode == 'updateParaData':
        a.update_output_para_data()
    elif args.mode == 'mod_trans':
        a.mod_translate()
    elif args.mode is None:
        a.run()
    else:
        print("未知的模式，请指定正确的 --mode 参数。")


if __name__ == '__main__':
    main()
