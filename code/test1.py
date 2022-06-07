# -*-coding:utf-8-*-

class Test1():
    '''
    我是测试类，负责测试
    '''

    def hello(self):
        '''
        负责打印Hello， 人人可以学Python
        :return:
        '''
        print("人人可以学Python")

    def renren(self):
        '''
        测试Sphinx自动生成文档

        :return:
        '''
        print("自动生成文档")


class Test2():

    def test_2(self):
        '''
        我也不知道写什么好，反正我们这里是用来写文档的
        :return:
        '''
        print("文档自动生成测试2")

    def renren_2(self):
        '''
        所以我们开发的时候就应该在这里写好文档，然后用Sphinx自动生成

        :return:
        '''
        print("自动生成文档2")
