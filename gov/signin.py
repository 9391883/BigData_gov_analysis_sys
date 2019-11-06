#!/usr/local/env python
#coding:utf-8
#Auto:Panwenbin
#function:
def signin():
    cmd=input(''' 
    1：登录系统 
    2：退出系统 
    请输入您的操作：''')
    if cmd.isdigit() and int(cmd)==2:
        exit()
    elif cmd.isdigit() and int(cmd)==1:
        match = False
        user_pass = open('username_file.txt', 'r+')
        username = input('请输入您的用户名:')
        a = user_pass.readlines()
        for j in range(len(a)):
            user, password, type = a[j].strip('\n').split(' ', 2)  # 去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user,passwd两个变量
            if username == user:  # 判断输入的用户是否存在
                passwd = input('请输入密码:')
                if password == passwd:
                    print('用户名和密码正确')
                    match = True
                    break
                elif password != passwd:  # 在用户名正确的前提下，判断输入的密码是否正确
                    for i in range(2):
                        passwd = input('密码错误，请重新输入密码:')
                        if password == passwd:
                            print('用户名和密码正确')
                            match = True
                            break
                break
        user_pass.close()
        if username != user:  # 判断用户不存在
            print('您输入用户名不存在,程序已退出')
            return -1
        elif match == False:
            print('密码和用户名不匹配，程序已退出')
            return -1
        elif match == True:
            print('登录成功')
            return type
    else:
        print('无效选项，程序已退出')
        return -1