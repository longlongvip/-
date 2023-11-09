import os

dir_name = input(f"请输入项目名：")

if os.path.exists(dir_name):
    print(f'文件夹 {dir_name} 已经存在')
else:
    if dir_name == '':
        print(f'请一定要想好项目名字')
    else:
        os.mkdir(dir_name)
        cmd_make = f'cd {dir_name} ' + '&& teedoc init'
        os.system(command=cmd_make)
