init_menu = """

  ++++++++++++++++++++++
 ++++++++++++++++++++++++
+++                    +++
++         通讯录         ++
++     ——————————————    ++
++       1.增加联系人      ++ 
++       2.删除联系人      ++
++       3.修改联系人      ++
++       4.查询联系人      ++
++       5.退     出      ++
++                       ++
++                       ++
++                       ++
+++                     +++  
+++++++++++++++++++++++++++
 +++++++++++++++++++++++++
  ++++++++++++++++++++++
"""


class MyContact(object):

    def __init__(self):
        self.contacts = {}
        # self.select_num = num

    def add_contact(self):
        while True:
            while True:
                name = input("请输入联系人姓名：").strip(' ')
                if name == '' or name == ' ':
                    print('注意:姓名不可输入为空！')
                    continue
                else:
                    break
            while True:
                try:
                    phonenum = int(input("请输入联系人电话号码：").strip(' '))
                except ValueError as e:
                    print('注意:手机号只能为数字')
                    continue
                if phonenum == '' or phonenum == ' ':
                    print('注意:手机号不可输入为空！')
                    continue
                else:
                    self.contacts[name] = phonenum
                    print('联系人保存成功！')
                    break

            continue_add = input("是否继续添加联系人(y/n)：").strip(' ')

            while True:
                if continue_add not in  ('y','n'):
                    print("您的输入有误，请重新输入！")
                    continue_add = input("是否继续添加联系人(y/n)：").strip(' ')
                    continue
                else:
                    break
            if continue_add == 'y':
                pass
            else:
                return False

    def delete_contact(self):
        while True:
            name = input("请输入要删除的联系人姓名：").strip(' ')
            if self.contacts.get(name):
                del self.contacts[name]
                print("联系人删除成功！")
            else:
                if_continue = input("此联系人不存在！\n是否继续查找(y/n？)").strip(' ')
                while True:
                    if if_continue not in ('y', 'n'):
                        print("您的输入有误，请重新输入！")
                        continue
                    else:
                        break
                if if_continue == 'y':
                    continue
                else:
                    return False

    def modify_contact(self):
        while True:
            name = input("请输入要修改的联系人姓名：").strip(' ')
            if self.contacts.get(name):
                while True:
                    name = input("请输入联系人姓名：").strip(' ')
                    if name == '' or name == ' ':
                        print('注意:姓名不可输入为空！')
                        continue
                    else:
                        break
                while True:
                    try:
                        phonenum = int(input("请输入联系人电话号码：").strip(' '))
                    except ValueError as e:
                        print('注意:手机号只能为数字')
                        continue
                    if phonenum == '' or phonenum == ' ':
                        print('注意:手机号不可输入为空！')
                        continue
                    else:
                        self.contacts[name] = phonenum
                        if_continue = input("联系人保存成功！\n是否继续修改(y/n？)").strip(' ')
                        while True:
                            if if_continue not in ('y', 'n'):
                                print("您的输入有误，请重新输入！")
                                continue
                            else:
                                break
                        if if_continue == 'y':
                            continue
                        else:
                            return False
            else:
                if_continue = input("此联系人不存在！\n是否继续查找(y/n？)").strip(' ')
                while True:
                    if if_continue not in ('y', 'n'):
                        print("您的输入有误，请重新输入！")
                        continue
                    else:
                        break
                if if_continue == 'y':
                    continue
                else:
                    return False

    def search_contact(self):
        while True:
            name = input("请输入联系人姓名：").strip(' ')
            if self.contacts.get(name):
                print("{}：{}".format(name, self.contacts.get(name)))
            else:
                if_continue = input("此联系人不存在！\n是否继续查找(y/n？)").strip(' ')
                while True:
                    if if_continue not in ('y', 'n'):
                        print("您的输入有误，请重新输入！")
                        continue
                    else:
                        break
                if if_continue == 'y':
                    continue
                else:
                    return False

    def exc_exit(self):
        return False


if __name__ == "__main__":
    run_contact = MyContact()
    while True:
        print(init_menu)
        try:
            selectNum = int(input('请选择操作号码：'))
        except ValueError as e:
            print('注意:手机号只能为数字,请重新输入！')
            continue
        if selectNum not in [1,2,3,4,5]:
            print("您输入的号有误，请重新输入")
        elif selectNum == 1:
            run_contact.add_contact()
        elif selectNum == 2:
            run_contact.delete_contact()
        elif selectNum == 3:
            run_contact.modify_contact()
        elif selectNum == 4:
            run_contact.search_contact()
            continue
        else:
            break





