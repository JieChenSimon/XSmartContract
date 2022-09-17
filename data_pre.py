# -*- coding: utf-8 -
import os

# 当前脚本所在的文件绝对路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# 将当前路径设置为python的临时环境变量，用于命令执行,需要设置是因为项目存在多处相互调用
os.putenv("PYTHONPATH", cur_path)
print(cur_path)

def run_case():
    # 使用os.path.join拼接地址
    case_path = os.path.join(cur_path, "solidity_data/source_code")

    # 获取当前目录下所有的文件名
    lst = os.listdir(case_path)
    print(lst)
    for c in lst:
        # 判断文件名是以.py结尾的;添加and c.find("DemoGet") == -1就是去掉DemoGet.py文件
        if os.path.splitext(c)[1] == '.sol':
            # 查看文件名
            print('the present file is:', c)
            # 相当于在终端执行文件  python main.py
            os.system('python /home/chen/workspace/codeproject/paperProject/exp_sc/oyente/oyente/oyente.py -s ' + case_path + '/' + c + ' -j')
            # os.system('python {}'.format(os.path.join(case_path, c)))


if __name__ == "__main__":
    run_case()

