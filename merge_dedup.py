# -*- coding: utf-8 -*-
# @Time    : 2023/10/19 1:59
# @Author  : ptbs
# @File    : merge_dedup.py.py
# @Software: PyCharm
# ---------CODE-------------
import os
import glob

def merge_txt_files(input_dir, output_file):

    # 使用字典存储行内容,自动去重
    content_dict = {}

    # 遍历输入目录下所有txt文件
    for input_file in glob.glob(os.path.join(input_dir, '*.txt')):
    
        print(f'Processing file: {input_file}')
        
        # 读取txt文件每一行 
        with open(input_file) as f:
            for line in f:
            
                # 去除空白字符
                line = line.strip()  
                
                # 如果行内容不在字典中则添加进去
                if line not in content_dict:
                    content_dict[line] = True
                
        print(f'Added {len(content_dict)} unique lines')

    # 按照字典的key逐行输出到新文件
    with open(output_file, 'w') as f:
        for line in content_dict.keys():
            f.write(line + '\n')
            
    print(f'Output file: {output_file}')
        
if __name__ == '__main__':

    # 输入目录
    input_dir = input("请输入目录地址:")
    # 输出文件
    output_file = 'spring_route_fuzz.txt'

    merge_txt_files(input_dir, output_file)