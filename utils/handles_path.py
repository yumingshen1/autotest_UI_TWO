# -*- coding:utf-8 -*-
# @Time : 2022/6/13 16:09
# Auther : shenyuming
# @File : handles_path.py
# @Software : PyCharm

from pathlib import Path

project_path = Path(__file__).parent.parent
outfiles_path = project_path / 'outfiles'
screenshot_path = outfiles_path / 'screenshot'
logs_path = project_path / 'outfiles' / 'log'
report_path = project_path / 'outfiles' / 'report'
common_element_path = project_path / 'common'
test_datas_path = project_path / 'test_datas'

if __name__ == '__main__':
    print(project_path)
    print(outfiles_path)
    print(screenshot_path)
    print(test_datas_path)