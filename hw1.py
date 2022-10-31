#作者：栾蕴菲
#目的：实现一个物品交换系统
from tkinter import *
#定义列表类，用于存放目前的物品和种类
class List:
    def __init__(self,i,n,s):
        self.itemList = i
        self.numberList = n
        self.sum = s
#添加物品
    def addItem(self,i,n):
        exist = False
        sum = self.sum
        for a in range (sum):
            if self.itemList[a] == i :
                self.numberList[a] = self.numberList [a] + n
                exist = True
                break
        if exist == False :
            self.sum = self.sum + 1
            self.itemList = self.itemList + [i]
            self.numberList = self.numberList + [n]
        print ("Add successfully!")
        label2.config(text = "Add successfully!")
#删减物品
    def subItem(self,i,n):
        if i not in self.itemList :
             print ("Not have this item!")
             label2.config(text = "Not have this item!")
        else :
            place = self.itemList.index(i)
            if self.numberList[place] < n :
                print ("Not enough!")
                label2.config(text = "Not enough!")
            elif self.numberList[place] == n :
                self.sum = self.sum - 1
                del self.itemList[place]
                del self.numberList[place]
                print ("Sub successfully!")
                label2.config(text = "Sub successfully!")
            else :
                self.numberList[place] = self.numberList[place] - n
                print ("Sub successfully!")
                label2.config(text = "Sub successfully!")
#查找物品
    def findItem(self,i):
        if i not in self.itemList:
            print ("Not find!")
            label2.config(text = "Not find!")
        else :
            place = self.itemList.index(i)
            number = self.numberList[place]
            print ("%s remains %d"%(i,number))
            text1 = i+" remains"+" "+str(number)
            label2.config(text = text1 ) 

#定义一个列表对象
list1 = List(["banana"],[1],1)
#button的command函数
def add() :
    item = v1.get()
    number = int(v2.get())
    list1.addItem(item,number)
def sub() :
    item = v1.get()
    number = int(v2.get())
    list1.subItem(item,number)
def find() :
    item = v1.get()
    list1.findItem(item)
def reList():
    LB1=Listbox(root)
    for i in range(len(list1.itemList)) :
         show = list1.itemList[i] + "          "+ str(list1.numberList[i])
         LB1.insert(END,show)
    LB1.grid(row=1,column=0)

    
#GUI界面的建立
root = Tk()
root.title("Exchange System")
reListButton = Button(root,text="current list",command=reList)
reListButton.grid(row=0,column=0)
LB1=Listbox(root)
for i in range(len(list1.itemList)) :
    show = list1.itemList[i] + "          "+ str(list1.numberList[i])
    LB1.insert(END,show)
LB1.grid(row=1,column=0)
v1 = StringVar()
v2 = StringVar()
label3 =  Label(root,text="input item")
label3.grid(row=0,column=4)
label4 =  Label(root,text="input number")
label4.grid(row=1,column=4)
itemGet = Entry(root,textvariable = v1)
itemGet.grid(row=0,column=5)
numberGet = Entry(root,textvariable = v2)
numberGet.grid(row=1,column=5)
addButton = Button(root,text="Add",command =add)
addButton.grid(row=2,column=4)
subButton = Button(root,text="Sub",command=sub)
subButton.grid(row=2,column=5)
findButton = Button(root,text="Find",command=find)
findButton.grid(row=2,column=6)
label2 =  Label(root,text="current state")
label2.grid(row=2,column=0)
root.mainloop()

#用于命令行调试
def main():
    list1.addItem("apple",5)
    print (list1.itemList)
    print (list1.numberList)
    list1.subItem("apple",4)
    print (list1.itemList)
    print (list1.numberList)
    list1.findItem("apple")

