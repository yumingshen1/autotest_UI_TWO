# -*- coding:utf-8 -*-
# @Time : 2022/6/14 10:18
# Auther : shenyuming
# @File : handles_rand_str.py
# @Software : PyCharm

from string import digits,ascii_letters
import random

def get_rand_str(lenght):
    return ''.join(random.sample(ascii_letters+digits,lenght))


if __name__ == '__main__':
    print(get_rand_str(6))