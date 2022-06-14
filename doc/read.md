1，基类：
    1.1：创建启动浏览器的driver类，
    1.2: 创建常用方法

2，配置文件：
    2.1：配置基类可以使用的参数
3，utiles:
    3.1 创建路径调用
4，test_dases:
    创建测试数据
5, pageObjects:
    业务类的梳理，页面流程（传入选择器用yml文件）
    需要工作：
        1，读取yml文件的方法
        2，在基类的 init方法中获取类对应的数据
6,test_cases:
    实例化业务类（登录）
    对象调用业务类的各种方法
    数据使用参数化，@pytest.mark.parametrize
    读取yml文件，get_yml_datas 封装方法
    加入失败继续跑， with allure.assume:

7,跑多次用例（用例都调了登录）：
    需要将登陆 写入conftest.py， 用例直接调用，

随机捞取一个数据：
    random , random.choics()
生成随机数：
    from string import disgits,ascii_letters
    ''.join(random.sample(disgits+ascii_letters,长度))
过滤：
    filter