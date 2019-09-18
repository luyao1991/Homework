#_author:test
#date:2019/9/14
contacts_list=[]
contacts_id = 0
def addPhone():

    name = input("请输入联系人姓名")
    tel = input("请输入电话号码")
    email = input("请输入邮箱")

    contacts_dic = {'name': name, 'telphone': tel, 'email': email}
    global contacts_id
    contacts_id += 1
    contacts_dic[contacts_id]=contacts_id
    contacts_list.append(contacts_id)
    print(contacts_dic)
    print("添加成功")


def delPhone():
    name = input("请输入联系人姓名")
    if name in contacts_list:
        del contacts_list[name]
        print("删除成功")
    else:
        print("联系人不存在")


def searchPhone(name):

    for contacts_dic in contacts_list:

     if contacts_dic[name] == name:

        print(contacts_list[name])
    else:
        print("联系人不存在")


while True:
    menu="""
     1:添加联系人          
     2:查找联系人
     3:删除联系人
     4: 退出 
      """

    print(menu)
    select1=input('请输入你需要的操作>>')

    if select1=='1':
        addPhone()

    if select1=='2':
        name = input("请输入联系人姓名")

        searchPhone(name)

    if select1=='3':
        name = input("请输入联系人姓名")
        delPhone(name)

    if select1=='4':
        exit()



