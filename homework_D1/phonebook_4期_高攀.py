# -*- coding:utf-8 -*-
"""
@Author:gaopan
@Time:2019/9/16-10:30
@Project:learn_test_develop
@Purpose:
1.对phonebook_1改造
融合手机号查找和姓名查找
增加简单确认选择
对手机号非数字做容错
支持简单的模糊查找

"""


class PhoneBook:
    def __init__(self):
        # self.phonebook = [{'name': 'a', 'phone': '1'}, {'name': 'b', 'phone': '1'}, {'name': 'a', 'phone': '2'}]
        self.phonebook = []
        pass

    # 对于输入手机号提供一个容错
    def input_phone(self, msg):
        phone = input(msg)
        try:
            int(phone)
            return phone
        except ValueError:
            print("输入的手机号含非数字")
            return None

    # 输入函数
    def input_data(self):
        name = input("输入姓名：")
        phone = self.input_phone(msg="输入电话：")
        # 用dict来存储单条数据
        if name and phone:
            data = {'name': name, 'phone': phone}
            return data
        else:
            return None

    # 实现添加联系人
    def add_data(self):
        data = self.input_data()
        if data is None:
            print("数据有误")
        else:
            self.phonebook.append(data)
            print("数据存储成功")

    # 通过姓名或手机号查找信息
    def query_data(self):
        query_list = []
        query = input("输入姓名或手机号：")
        for info in self.phonebook:
            # in方法支持简单的模糊查询，==不支持
            if query == info['name'] or query == info['phone']:
            # if query in info['name'] or query in info['phone']:
                query_list.append(info)
                print(info)
        if len(query_list) == 0:
            print("不好意思，没有数据")
            return query, None
        return query, query_list

    # 姓名或手机号维度删除用户
    def delete_data(self):
        query, data = self.query_data()
        if data is None:
            print("通讯录没有数据:%s" % query)
            return
        for info in data:
            option = input("是否确认删除，Y or N：")
            if option == 'Y':
                self.phonebook.remove(info)
                print("成功删除信息:%s" % str(info))
            elif option == 'N':
                print("不删除这条信息:%s" % str(info))
            else:
                print("输入有误，跳过这条信息")

    # 修改姓名或手机号
    def modify_data(self):
        query, data = self.query_data()
        if data is None:
            print("通讯录没有数据:%s" % query)
            return
        for info in data:
            if query == info['name']:
                print("用户%s的原有手机号：" % query + info['phone'])
                phone_modify = self.input_phone(msg="输入修改后的手机号：")
                if phone_modify is None:
                    continue
                data_modify = {'name': query, 'phone': phone_modify}
                option = input("是否确认修改，Y or N：")
                if option == 'Y':
                    self.phonebook.remove(info)
                    self.phonebook.append(data_modify)
                    print("修改后的数据是：" + str(data_modify))
                elif option == 'N':
                    print("不修改这条信息:%s" % str(info))
                else:
                    print("输入有误，跳过这条信息")
            elif query == info['phone']:
                print("手机号%s原有姓名：" % query + info['name'])
                name_modify = input("输入修改后名字：")
                data_modify = {'name': name_modify, 'phone': query}
                option = input("是否确认修改，Y or N：")
                if option == 'Y':
                    self.phonebook.remove(info)
                    self.phonebook.append(data_modify)
                    print("修改后的数据是：" + str(data_modify))
                elif option == 'N':
                    print("不修改这条信息:%s" % str(info))
                else:
                    print("输入有误，跳过这条信息")


if __name__ == '__main__':
    """
    实现通讯录功能，包含增删改查.
    1.增加
    2.删除
    3.修改
    4.查找
    5.退出   
    """
    book = PhoneBook()
    while True:
        print("1.增加；2.删除；3.修改；4.查找；5.退出")
        print(book.phonebook)
        number = input("请输入需要的操作代号：")
        if number == '1':
            print("增加操作")
            book.add_data()
        elif number == '2':
            print("删除操作")
            book.delete_data()
        elif number == '3':
            print("修改操作")
            book.modify_data()
        elif number == '4':
            print("查找操作")
            book.query_data()
        elif number == '5':
            print("退出程序")
            exit()
        else:
            print("输入错误")
