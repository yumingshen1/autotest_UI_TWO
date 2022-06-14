# -*- coding:utf-8 -*-
# @Time : 2022/6/13 17:23
# Auther : shenyuming
# @File : handles_yml.py
# @Software : PyCharm
from pprint import pprint

import yaml
from utils.handles_path import common_element_path,test_datas_path

def get_yml_datas(yml_file):
    with open(yml_file,'r',encoding='utf-8') as f:
       return yaml.safe_load(f.read())

if __name__ == '__main__':
   pprint(get_yml_datas(test_datas_path / 'all_login_data.yml'))