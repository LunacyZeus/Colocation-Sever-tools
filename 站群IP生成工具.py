"""
需要在python3.6+下的版本才可运行
根据需要给出相应的信息即可生成站群服务器的IP
当然也可以在服务器上执行脚本获取，这个脚本稍后发~~
"""
def 输出IP段(IP地址,开始,结束):
    for ip in range(开始,结束):
      print(IP地址%ip)
      
def 读取输入(提示消息,输入类型="str",默认值=""):
    while 1:
        输入 = input(f"{提示消息}\n--> ") 
        if 输入=="":
            if 输入类型 == "default":
                return 默认值
            print("输入不能为空")
            continue
        
        if 输入=="ok":
            return "exit"
            
        if 输入类型 == "int":
            try:
                输入 = int(输入)
            except:
                print("只允许输入整数")
                continue
        break
    return 输入
    
IP段数据 = {}
IP数据文件名 = "ip.txt"
IP数据列表 = []
print("站群IP段生成工具\n\n输入IP和始端末端IP数据，输入ok中止输入\n")

IP数据文件名 = 读取输入("输入IP数据文件名(无需后缀不输入则为ip.txt)","default","ip.txt")+".txt"
print(f"已设置IP数据文件名为{IP数据文件名}")

while 1:
    IP段 = 读取输入("输入IP段")
    if IP段 == "exit":break
    
    始端 = IP段.split("-")[0].split(".")[3]
    末端 = IP段.split("-")[1]
    IP段 = ".".join(IP段.split("-")[0].split(".")[:3])+".%d"
    
    print(始端,末端)
    '''
    始端 = 读取输入("输入始端","int")
    if 始端 == "exit":break
    
    末端 = 读取输入("输入末端","int")
    if 末端 == "exit":break
    '''
    
    IP段数据.update({IP段:f"{始端}-{末端}"})
    
    print(f"IP段({IP段})已记录\n")
    
#遍历IP数据
for IP段,始终端数据 in IP段数据.items():
    始端,末端 = int(始终端数据.split("-")[0]),int(始终端数据.split("-")[1])
    for IP in range(始端,末端+1):
        IP数据列表.append(IP段%IP)
    
print("已经生成%d个IP"%len(IP数据列表))

open(IP数据文件名,"w").write("\n".join(IP数据列表))
print(f"成功保存到{IP数据文件名}")
    
