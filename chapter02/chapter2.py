#!/usr/bin/env python
# coding: utf-8

# In[1]:


"hello world" #字符串


# In[2]:


print("c:\code\name") #"\n"表示换行符
print(r"c:\code\name") #引号前加r，表示原始输出


# In[3]:


"Dr."+" "+"Tang" #字符串支持加运算 表示字符串拼接


# In[4]:


10 +3 #加法


# In[5]:


10 - 3 #减法


# In[6]:


10 * 3 #乘法


# In[7]:


10 / 3 #除法


# In[8]:


10 % 3 #求余数


# In[9]:


10 // 3 #求商


# In[10]:


10 ** 3 #10的3次方


# In[11]:


x = 3 #x变量赋值3
y = 1 #y变量赋值1
x == y #比较运算符  ==（等于），表示比较对象是否相等


# In[12]:


x != y  #比较运算符  !=（不等于），表示比较对象是否不相等


# In[13]:


x > y #比较运算符  >（大于），返回x是否大于y；>=（大于等于）


# In[14]:


x < y #比较运算符  <（小于），返回x是否小于y；<=（小于等于）


# In[15]:


a = True #布尔变量a赋值True
b = False  #布尔变量b赋值False
a and b #逻辑运算：与and，True and True 返回True，其他返回False


# In[16]:


a or b #逻辑运算：或or，False or False 返回False，其他返回True


# In[17]:


not a #逻辑运算：非 not，取反


# In[18]:


list1 = [1,2,3,"a","ab",3,2,"2"] #创建列表
list1


# In[19]:


list2 = list([1,"a",3]) #list()函数创建列表
list2


# In[20]:


list1[0] #通过索引访问列表元素


# In[21]:


list1[-1] #通过索引访问列表元素


# In[22]:


list1[0:4] #通过索引访问列表元素


# In[23]:


list1.append(list2) #append方法是将list2所有元素做为一个list元素加入list1最后的位置
list1


# In[24]:


list1.extend(list2) #extend方法是将list1和list2元素合并成一个列表
list1


# In[25]:


tuple1 = (1,2,3,4,3,1) #通过()构建元组
tuple1


# In[26]:


list0 = [1, 2, 1]
tuple2 = tuple(list0)  #通过tuple()函数构建元组
tuple2


# In[27]:


tuple1[0] #通过索引访问列表元素


# In[28]:


tuple1 + tuple2 #加运算合并元组


# In[29]:


dict1 = {"a":12,"b":15,"d":25} #字典构建
dict1


# In[30]:


dict1.keys() #通过keys获取字典的键


# In[31]:


dict1.values() #通过values获取字典的值


# In[32]:


dict1["d"] #通过字典的keys访问相应的value


# In[33]:


set1 = {1,3,"2",3,"4",5,6,4} #通过{}创建集合
set1


# In[34]:


list0 = [1,2,3,"5"]
set2 = set(list0) #通过set()函数创建集合
set2


# In[35]:


A = {1,2,3,4}
B = {3,4,5,6}
A - B #差集运算，即A的元素去除AB共有的元素


# In[36]:


A | B #并集运算，即A与B的全部唯一的元素


# In[37]:


A & B #交集运算，即A和B的共有元素


# In[38]:


A ^ B #对差集，即(A|B) - (A&B)


# In[39]:


list0 = ["a","b","d"] #构建一个列表
print(list0[0]) #打印列表第一个元素
print(list0[1]) #顺序打印第二各元素


# In[40]:


var = 3         #var变量赋值3
if var < 0:     #选择结构
    print("negative")
elif x == 0:
    print("zero")
else:
    print("positive")


# In[41]:


for i in list0:    #for 循环结构
    print(i)         #循环体执行代码


# In[42]:


x = 0                #x变量赋值0
while x < 3:    #while 循环结构   
    print(x)      #循环体执行代码
    x +=1          #循环体执行代码


# In[43]:


list0 = [1,2,3,5,6] #构建列表list0
list1 = [i/10 for i in list0] #for循环进行列表list0遍历计算
print(list1)


# In[44]:


def print_user(name): #定义函数，print_user为函数 名，name为形参
    print("name: ",name) #函数体    
    
print_user("tang") #调用print_user函数，"tang"为实参


# In[45]:


def print_demo(obj): #定义函数，print_demo为函数 名，obj为形参
    print("origin: ", obj)
    obj +=obj

obj1 = "tang" #obj1为字符串，值传递
print_demo(obj1) #调用print_demo函数，“tang”作为实参传递给形参obj，是值传递
print(obj1) #obj1的值没有改变


# In[46]:


obj2 = ["a","b"] #obj2为列表数据类型，引用传递
print_demo(obj2)  #调用print_demo函数，列表["a","b"]作为实参传递给形参obj，是引用传递
print(obj2) #obj2的值发生改变，由 ['a', 'b'] 由函数执行体 obj += obj 修改成 ['a', 'b', 'a', 'b']


# In[47]:


def print_arg(*arg): #定义函数，print_demo为函数 名，arg为可变参数
    print(len(arg)) #打印传入函数中实际参数的个数

print_arg("a",1,3) #调用print_arg函数，传入函数有3个实际参数
print_arg("a","b",1,2,3) #调用print_arg函数，传入函数有5个实际参数


# In[48]:


def sum_num(a): #定义函数，sum_num为函数 名，a为形参
    s = 0    #s为局部变量
    for i in a: #for循环，将传入的列表元素求和
        s += i
    return s #返回列表元素和

list0 = [1,2,3,4,5,6,7,8,9,10] #定义列表list0
s0 = sum_num(list0) #调用sum_num函数，将列表list0元素求和，返回给变量s0
print(s0)  #打印s0


# In[49]:


class Person: #定义类Person，封装属性和方法
    def __init__(self, name, age, gender="male"): #Person实例传入self
        self.name = name #初始化属性name, age和gender，默认gender = "male"
        self.age = age
        self.gender = gender      
        
    def print_name(self): #方法print_name() 打印name
        print("name: ", self.name)
    def print_info(self): #方法print_info() 打印age,gender
        print("infomation: \n  age: %s \n  gender: %s"%(self.age, self.gender))  
    
p1 = Person("ming",18) #创建p1为Person类的实例，属性name="ming", age=18
p1.print_name() #访问方法print_name()
p1.print_info() #访问方法print_info()
p1.name = "xiao" #修改属性name
p1.print_name() 


# In[50]:


p2 = Person("mei",17,"female") #创建另外一个实例p2
p2.print_info() #访问方法print_info()


# In[51]:


class Student(Person): #类Student继承类Person
    def __init__(self, name,age, gender,sid): #添加子类Student新属性sid
        super().__init__(name,age, gender) #初始化父类，super()调用父类__init()__
        self.sid = sid  #初始化属性sid
        
    def print_name(self): #重写父类方法print_name()
        print("student name: ", self.name)        
    def print_sid(self): #添加子类Student新方法
        print("sid: ",self.sid)
    
s1 = Student("xiao",19,"female","s118") #创建子类Student的实例s1
s1.print_name() #访问子类修改后的方法print_name()
s1.print_info() #访问继承父类的方法print_info()
s1.print_sid() #访问子类的新方法print_sid()


# In[52]:


class Doctor(Person): #类Doctor继承类Person，同时区别子类Student，类的多态性
    def __init__(self,name,age,gender,hospital): #类的多态性，类Doctor新属性hospital区别Student的属性sid
        super().__init__(name,age,gender)
        self.hospital = hospital
        
    def print_hospital(self): #添加子类Doctor新方法
        print("hospital: ", self.hospital)
        
d1 = Doctor("tang", 30, "male","huashan") #创建子类Doctor的实例d1
d1.print_name() #访问继承父类Person的方法print_name()
d1.print_hospital() #访问子类Doctor的新方法print_hosptial()


# In[53]:


import test_module as tm #导入test_module.py, 设tm为别名
list0 = [1,2,3,4,5,6,7,8] #创建列表list0
avg = tm.average(list0) #tm的average函数计算list0的平均值，返回给变量avg
print(avg) #打印avg


# In[54]:


import numpy as np # 导入第三方库numpy模块，设np为别名
np.mean(list0) #使用numpy模块的mean()函数计算list0的均值


# In[55]:


with open("test_file_read.txt", "r", encoding = "utf-8") as file: #打开test_file_read.txt文件
    str1 = file.read() #读取文件test_file_read.txt内容，赋值str1
print(str1) #打印str1


# In[56]:


str_write = "test a write file... \nthis a new sentence..." #赋值变量str_write字符串内容
with open("test_file_write.txt", "w", encoding = "utf-8") as file:  #打开test_file_write.txt文件
    file.write(str_write) #str_write内容写入文件test_file_write.txt


# In[57]:


import pandas as pd #导入pandas，设pd为别名
filename = "test_file_excel.xlsx"
dt = pd.read_excel(filename, encoding = "utf-8") #读取test_file_excel.xlsx内容，返回一个DataFrame对象
dt.head() #展示dt前5行内容

