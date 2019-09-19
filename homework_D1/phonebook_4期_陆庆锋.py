
'''编写一个通讯录程序，实现增删改查功能
#### 1.设计数据结构
一条记录： 姓名，电话， id
一个通讯录：列表，里面元素为记录

#### 2. 函数设计
* 增加 add_record
* 查询 query_record
* 修改 change_record
* 删除 delete_record

#### 3. 菜单设计
* main函数
* while 循环
* 选择相应功能'''


class phonebook():
    recordict = {}

    def add_record(self):
        name = input('请输入要添加的联系人姓名')
        if name in phonebook().recordict:
            print('该联系人已经存在')
        else:
            phone = (input('请输入联系人电话号码'))

            phonebook().recordict[name] = {'电话': phone}

    def delete_record(self):
        name = (input('请输入要删除的联系人姓名'))
        if name in phonebook.recordict:
            del phonebook.recordict[name]

        else:
            print('联系人 %s 不存在' % name)

    def query_record(self):
        name = (input('请输入要搜索的联系人姓名'))
        if name in phonebook.recordict:
            print(
                '联系人 %s \n电话号码是 %s ' %
                (name, phonebook.recordict[name]['电话']))
        else:
            print('联系人 %s 不存在' % name)

    def change_record(self):
        name = (input('请输入要修改的联系人姓名'))
        if name in phonebook().recordict:
            phone = (input('请输入联系人电话号码'))
            phonebook().recordict[name]['电话'] = phone

        else:
            print('联系人 %s 不存在' % name)


if __name__ == '__main__':
    while True:
        menu = '''
        通讯录
        1. 添加
        2. 查找
        3. 删除
        4. 修改
        5. 退出
        请选择操作:
        '''
        print(menu)

        s = int(input('请输入相应数字操作'))
        if s == 1:
            phonebook().add_record()
        elif s == 2:
            phonebook().query_record()
        elif s == 3:
            phonebook().delete_record()
        elif s == 4:
            phonebook().change_record()
        elif s == 5:
            break
        else:
            print('输入不合法，请输入合法数字')
