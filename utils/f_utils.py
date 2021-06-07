"""
https://blog.csdn.net/qq_42327755/article/details/102611266


python f"{}" 、 %  、format  写法。

"""



name = "小王"
age = 15

f_str = f"姓名:{name} 年龄:{age}"
s_str = "姓名:%s 年龄:%d" % (name, age)

format_str = "姓名:{0} 年龄:{1} 姓名{0} 年龄{1}".format(name, age)

print(f_str)
print(s_str)
print(format_str)

