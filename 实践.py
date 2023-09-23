#打开文件
# f = open("D:\word测试.txt","r",encoding="UTF-8")
# print(type(f))
#读取文件
# print(f.read())
#读取文件的全部行,封装到列表中
# lines = f.readlines()
# print(lines)
# print(type(lines))
#一行行的读取
# print(f"第一行:{f.readline()}")
#for循环读取文件
# for line in f:
    # print(f"每一行数据:{line}")
#关闭文件
# f.close()
# with open("D:\word测试.txt","r",encoding="UTF-8") as f:
#     print("已经自动结束")
#统计a出现的次数
import time
#
# f = open("D:\ test.txt","w",encoding="UTF-8")
# #写入文件
# f.write("hello the world")
# #flush刷新
# f.flush()
# f.close()#内置flush

# #打开文件
# f = open("D:\lbill.txt","r",encoding="UTF-8")
# # print(f.read())
# d = open("D:\算账.txt","w",encoding="UTF-8")
# for line in f:
#     line = line.strip()
#     words = line.split(",")[1]
#     if words == "测试":
#         continue
#
#     d.write(words)
#     d.write("\n")
#
# d = open("D:\算账.txt","r",encoding="UTF-8")
#
#
# print(d.read())
# f.close()
# # d.close()
# import time
# print("开始")
# time.sleep(2)
# print("结束了")

# #引入json模块
# import json
# #创建一个字典
# list1 = [{"周杰伦":"歌王"},{"方文山":"词王"}]
# json_str  = json.dumps(list1)
# print(type(json_str))
# print(json_str)
# from pyecharts.charts import Line
# line = Line()
# line.add_xaxis(["中国","美国","英国"])
# line.add_yaxis("GDP",[30,20,10])
# line.render()

#文件对象
# f = open("D:\python_文件操作\滴滴滴滴地道test1.txt","r",encoding="UTF-8")
# print(type(f))
# print(f.read())
# print(type(f.read()))
#读取文件全部行,封装到列表
# print(f.readlines())
#读取一行
# print(f.readline())
# import time
# while True:
#     print(f.readline())
#     time.sleep(1)
#for循环读取每一行
# for lines in f:
#     print(lines)
#关闭程序
# f.close()
# #自动关闭程序
# with open("D:\python_文件操作\滴滴滴滴地道test1.txt","r",encoding="UTF-8") as f:
#     for lines in f:
#         print(lines)
#文件写入

#文件操作对象
# f = open("D:\python_文件操作\我滴滴滴滴地道test1.txt","w",encoding="UTF-8")
# f.write("一定要努力啊9-23")
# f.flush()

#模块导入
# from time import sleep
# sleep(5)
# from time import *
# sleep(1)
#给模块改名
# from time import sleep as 蔡徐坤
# 蔡徐坤(1)
#引入json
# import json
# #给一个列表,里面是字典
# list1 = [{"wo":12,"ta":18,"he":12,"蔡徐坤":2}]
# list1_json = json.dumps(list1)
# print(type(list1_json))
# print(list1_json)
# #dumps 使用 ensur_ascii= Flase,中文即可原样输出
# #准备一个字典,转换为json
# dic1 = {"wo":12,"ta":18,"he":12,"蔡徐坤":2}
# dic1_json = json.dumps(dic1)
# print(type(dic1_json))
# print(dic1_json)
# #将json转换为python
# text = '[{"wo":12,"ta":18,"he":12,"蔡徐坤":2}]'
# l = json.loads(text)
# print(type(l))
# print(l)
#pyecharts 实例
# from pyecharts.charts import Line
# from pyecharts.options import *
# line = Line()
# line.add_xaxis(["china","america",'england'])
# line.add_yaxis("GDP数据",[30,20,10])
# line.set_global_opts(
#     title_opts=TitleOpts("GDP展示")
# )
# line.render()
print("___________________________________________--这是第一个")
# zifuchuan = "12345"
# zifuchuan = zifuchuan[:-2]
# print(zifuchuan)
# list1 = [2,9,11,15,7]
# target = [9]
# for l in list1:
#     # if  list[a] + list[a+1] == target[0]:
#     # print(f"{a},")
#     # print(list1.index((l))+1)
#     # print(type(target[0]))
#     if
#     if l + list1[list1.index(l)+1] == target[0]:
#         print(f"{l},{int(list1.index(l))+1}")
#         break
#     else:
#         del list1[0]
# # print(list1)
#         continue

# #创建一个类
# class Student:
#     name = None
#     gender = None
#     nationnality = None
#     native_palace = None
#     age = None
# #创建一个对象
# stu1 = Student
# #对象属性进行赋值
# stu1.name = "蔡徐坤"
# stu1.nationnality = "CHINA"
# stu1.age = "27"
# stu1.native_palace = "浙江"
# stu1.gender = "男"
# print(type(stu1.name))
# print(stu1.name)

# class student:
#     name = None
#     def say_hello(self,funny):
#         print(f"大家好!我是{self.name},{funny}")
# stu1 = student()
# stu1.name= "蔡徐坤"
# print(stu1.name)
# stu1.say_hello("练习时长两年半")

# #设计一个闹钟类
# class clock:
#     id = None
#     price = None
#
#     def ring(self):
#         import winsound
#         winsound.Beep(2000,3000)
#
# #创建对象
# clock1 = clock()
# clock1.id= "001"
# clock1.price= "20"
# clock1.ring()
#
#构造方法
# class student:
#     def __init__(self,name,age,tel):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         print("student类创建一个对象")#测试
#     def __str__(self):
#         return f"student类对象:name:{self.name},age:{self.age},tel:{self.tel}"
#     def __lt__(self, other):
#         return self.age < other.age
#     def __le__(self,other):
#         return self.age <= other.age
#     def __eq__(self, other):
#         return self.age == other.age
#
# stu1 = student("蔡徐坤",27,13914629)
# stu2 = student("李佳琦",40,29347922)
# print(stu1)
# print(stu1 < stu2)
# print(stu1 <= stu2)
# print(stu2 < stu1)
# print(stu2 <=stu1)
# print(stu1 == stu2)

# #私有变量
# class Phone :
#     IMEI = None
#     producter = None
#     __current_voltage  = None
#     def call_by_5g(self):
#         print("5g通话开启成功")
#     def __single_cpu(self):
#         print("单核省电模式开启成功")
# pho1 = Phone()
# pho1.IMEI

# class Phone :
#     __is_5g_enable = True
#     def __check_5g(self):
#         if self.__is_5g_enable == True:
#             print("5g开启")
#         else:
#             print("5g关闭,使用4g网络")
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
# phone1 = Phone()
# phone1.call_by_5g()
# class Phone :
#     IMEI = "0001"
#     producter = "HuaWei"
#     def call_by_4g(self):
#         print("4g通话")
# class phone2023 (Phone):
#     face_id = "00002"
#     def call_by_5g2023():
#         print("23年新功能:卫星通话")
# pho1 =  phone2023()
# print(pho1.IMEI)

var1 : int = 10
print(type(var1))
print(var1)