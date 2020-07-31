try:
    from tkinter import Tk,Menu,Button,Entry
    import turtle as t
    from sys import exit
except:
    print("请确保安装了turtle&tkinter库")

MF=Tk()
MF.geometry("1100x80")
MF.title("自♂由")

try:
    setfile=r'd:\\BGCsetting.txt'
    setting=open(setfile,'r')
    colour=str(setting.read())
    setting.close()
    MF['background']=colour
except:
    MF['background']="Black"


B1=Button(MF,text='画坐标系',bg="DodgerBlue",fg="black")  #坐标系
B1.pack(side="left",padx="2m")

B2=Button(MF,text='画函数',bg="DodgerBlue",fg="black")#第一个函数
B2.pack(side="left",padx="2m")

E14=Entry(MF,width="2")
E14.pack(side="left",padx="2m")

E15=Entry(MF,width="2")
E15.pack(side="left",padx="2m")

B12=Button(MF,text='交点',bg="DodgerBlue",fg="black")
B12.pack(side="left",padx="2m")

E1=Entry(MF,width=5)  #y的系数
E1.pack(side='left',padx="2m")

E2=Entry(MF,width=5)#x的系数
E2.pack(side='left',padx="2m")

E3=Entry(MF,width=5)#常数
E3.pack(side='left',padx="2m")

E44=Entry(MF,width="5")
E44.pack(side="left",padx="2m")

B3=Button(MF,text='画函数',bg="DodgerBlue",fg="black")#第二个函数
B3.pack(side="left",padx="2m")

#B16=Button(MF,text='绝对值函数',fg="black")#第二个函数
#B16.pack(side="left",padx="2m")

B13=Button(MF,text='交点',bg="DodgerBlue",fg="black")
B13.pack(side="left",padx="2m")

E11=Entry(MF,width=5)
E11.pack(side='left',padx="2m")

E12=Entry(MF,width=5)
E12.pack(side='left',padx="2m")

E13=Entry(MF,width=5)
E13.pack(side='left',padx="2m")

B4=Button(MF,text='前往坐标',bg="DodgerBlue",fg="black")
B4.pack(side="left",padx="2m")

E4=Entry(MF,width=5)
E4.pack(side='left',padx="2m")

E5=Entry(MF,width=5)
E5.pack(side="left",padx="2m")

E51=Entry(MF,width=10)
E51.pack(side="left",padx="2m")

B51=Button(MF,text="确认颜色",bg="DodgerBlue",fg="black")
B51.pack(side="left",padx="2m")

#============
def selfchangecolor(event):
    try:
        selfcolour=str(E51.get())
        t.pencolor(selfcolour)
    except:
        pass

def openfile(a):
    file=r'd:\\BGCsetting.txt'
    changecolor=open(file,'w')
    changecolor.write(a)

def returnhome():
    t.penup()
    t.home()
    t.pd()

def goto(event):
    x=float(E4.get())
    y=float(E5.get())
    x1=x*20
    y1=y*20
    t.pencolor('DeepSkyBlue')
    t.goto(x1,y1)
def jian():#坐标系子函数
    t.left(150)
    t.forward(10)
    t.backward(10)
    t.left(60)
    t.forward(10)
    t.backward(10)
    t.right(30)    #箭头
    t.forward(10)
    #注意，这里为箭头留出空间，后续的代码需要注意前进步数
def map(event):#坐标系
    setfile1=r'd:\\BGCsetting.txt'
    setting1=open(setfile1,'r')
    colour1=str(setting1.read())
    t.pencolor("Aqua")
    setting.close()
    i=0
    v=0
    t.pu()
    t.home()
    t.pd()
    t.screensize(2000,1300,colour1)
    t.speed(0)#draw X axis
    t.forward(310)  #x Axis 长300
    jian()
    while i<=300:
        t.forward(20)
        t.right(90)
        t.forward(10)
        t.backward(10)
        t.left(90)
        i=i+10
    t.forward(10)
    t.home()  #go to draw Y axis
    t.left(90)
    t.forward(310)   #画到尽头
    jian()
    while v<300:
        t.forward(20)
        t.left(90)
        t.forward(10)
        t.backward(10)
        t.right(90)
        v+=10
    t.forward(10)#单位长度是20
    t.home()
    t.pensize(4)

def info():#信息
    messagebox.showinfo('详细信息','一个数学不好美术不好不会搞设计的人\
    的作品,建议先画坐标系然后再进行诸如前往指定位置以及画函数的操作。撤销按钮\
    可以撤销turtle的一次操作。可能不会十分地灵敏，请多按几次。\
    制作日期:April 24th,2020--------\
    注意:画函数功能，三个选项，分别填入y的系数，x的系数，常数，都是必填的。你\
    可以输入负数和浮点数。\
    前往坐标的功能中，支持负数和浮点数。\
    在一些难以被考虑到的域内的数一旦被输入，是有可能引发错误的\
    如果你能够测试出其中的bug，并且不辞辛苦地将其告诉作者，作者先对你表示真诚感谢\
    更新日期:2020//5//21')
def lines():#画辅助线
    t.speed(0)
    t.pencolor("grey")
    t.pu()
    t.goto(-300,300)
    t.pd()
    i=int(0)
    t.right(90)
    l=0
    while i<=640:#竖着的
        t.forward(600)
        t.pu()
        t.goto(300-i,300)
        t.pd()
        i+=20
    t.left(90)
    while l<=620:
        t.forward(620)
        t.pu()
        t.goto(-320,300-l)
        t.pd()
        l+=20

def map2():
    t.speed(0)
    i=0
    t.forward(300)
    t.seth(180)
    while i<=600:
        t.forward(20)
        t.dot(5)
        i+=20
    t.pu()
    t.goto(0,300)
    t.pd()
    t.seth(270)
    i=0
    while i<=600:
        t.forward(20)
        t.dot(5)
        i+=20
    t.home()
    t.pensize(4)

def infoma(): 
    f='d:\\functionarea\\t1.txt'
    file2=open(f,'r')
    txt1=file2.read()
    messagebox.showinfo('信息','%s'%txt1)
    file2.close()

class Corealgo():
    def pub(): #求公共点
        try:
            a=float(E1.get())
            b=float(E2.get())
            c=float(E3.get())

            a1=float(E11.get())
            b1=float(E12.get())
            c1=float(E13.get())
            d=b/a
            d1=b1/a1 #转成y=kx+b的形式#y=dx+c//\\y=d1x+c1,,dx+c=d1x+c1
            if d!=d1:
                x=float((c1-c)/(d-d1))
                y=d1*x+c1
                x1=x*20
                y1=y*20
                t.pencolor('blue')
                t.pu()
                t.goto(x1,y1)
                t.pd()
                t.dot(10)
                t.pu()
                t.home()
                t.pd()
                messagebox.showinfo('交点','%2fy=%2fx+%2f和%2fy=%2fx+%2f交点为(%f,%f)'%(a,b,c,a1,b1,c1,x,y))
                
            elif d==d1 and c!=c1:
                messagebox.showinfo('提示','%2fy=%2fx+%2f和%2fy=%2fx+%2f平行，没有交点'%(a,b,c,a1,b1,c1))
            elif b==b1 and c==c1 and a==a1:
                messagebox.showinfo('提示','%2fy=%2fx+%2f和%2fy=%2fx+%2f两直线重合了'%(a,b,c,a1,b1,c1,))
        except:
            messagebox.showwarning('注意','请输入合理的数值')

    def gof(event):
        try:
            a=float(E2.get())
            b=float(E1.get())
            c=float(E3.get())
            if E14.get()=="" or E15.get()=="":
                stepl=-15
                stepr=15
            else:
                try:
                    stepl=float(E14.get())
                    stepr=float(E15.get())
                except:
                    messagebox.showerror("注意","输入合理的数值")
            if b!=0:  #假如 2y=2x
                x_xi=float(b/a)  #变为x=y，这个是y应得的系数
                x0=20*stepr  #横极限坐标
                y0=20*stepr/x_xi+c*20 #系数开满
                x1=20*stepl
                y1=20*stepl/x_xi+c*20
                t.pu()
                t.goto(x0,y0)
                t.pd()
                t.goto(x1,y1)

            elif b==0:
                y_xi=float(c/a)  #2y=3,y=1.5
                x0=20*stepr
                y0=y_xi*20
                x1=20*stepl
                t.pu()
                t.goto(x0,y0)
                t.pd()
                t.goto(x1,y0)
                t.pu()
                t.home()
                t.pd()
        except:
            messagebox.showerror('注意','请输入合适的数字')
    def goft(event):
        try:
            a=float(E12.get())
            b=float(E11.get())
            c=float(E13.get())
            if b!=0:  #假如 2y=2x
                x_xi=float(b/a)  #变为x=y，这个是y应得的系数
                x0=20*15  #横极限坐标
                y0=20*15/x_xi+c*20 #系数开满
                x1=-20*15
                y1=-20*15/x_xi+c*20
                t.pu()
                t.goto(x0,y0)
                t.pd()
                t.goto(x1,y1)

            elif b==0:
                y_xi=float(c/a)  #2y=3,y=1.5
                x0=300
                y0=y_xi*20
                x1=-300
                t.pu()
                t.goto(x0,y0)
                t.pd()
                t.goto(x1,y0)
                t.pu()
                t.home()
                t.pd()
        except:
            messagebox.showwarning('注意','请输入合适的数字')
    def jiao(event):
        try:
            a=float(E2.get())
            b=float(E1.get())
            c=float(E3.get())
            d=a/b
            messagebox.showinfo('分别交x，y轴于:','X axis:(%f,%f),Y axis:(%f,%f)'%(-c/d,0,0,c))
        except:
            messagebox.showinfo('提示','请输入合适的数字')
    def jiaot(event):
        try:
            a=float(E12.get())
            b=float(E11.get())
            c=float(E13.get())
            d=a/b
            messagebox.showinfo('分别交x，y轴于:','X axis:(%f,%f),Y axis:(%f,%f)'%(-c/d,0,0,c))
        except:
            messagebox.showinfo('提示','请输入合适的数字')
    def absf():
        a1=list(E11.get()) #y=|x+2|+|x+1|+|x-1|
        b1=list(E12.get())
        c1=list(E13.get())
        #统一为诸如x-1/2的表达式
        if a1[0]=='x':
            xxi=1
        elif a1[0]!='x':
            spa=a1.index('x')
            xxi=(float(a1[3:])/float(a1[0:spa]))
        if b1[0]=='x':
            xxi1=1
        elif b1[0]!='x':
            spa1=b1.index('x')
            xxi1=(float(b1[3:])/float(b1[0:spa]))
        if c1[0]=='x':
            xxi2=1
        elif c1[0]!='x':
            spa2=c1.index('x')
            xxi2=(float(c1[3:])/float(c1[0:spa]))

    def ipfunction():
        k=float(E14.get())#4
        try:
            b=float(E15.get())
        except:
            b=0
        k*=400
        x=-300
        x_list=[]
        y_list=[]
        while x<=-1:
            x_list.append(x)
            x+=1
        for x1 in x_list:
            y=k/x1+20*b
            y_list.append(y)
        m=0
        n=0
        t.pu()
        t.goto(x_list[0],y_list[0])
        t.pd()
        while m<len(x_list):
            x2=x_list[m]
            y2=y_list[n]
            t.goto(x2,y2)
            m+=1
            n+=1
        x3_list=[]
        y3_list=[]
        x3=1
        while x3<=300:
            x3_list.append(x3)
            x3+=1
        for x0 in x3_list:
            y3=k/x0
            y3_list.append((y3))
        m=0
        n=0
        t.pu()
        t.goto(x3_list[0],y3_list[0])
        t.pd()
        while m<len(x3_list):
            x2=x3_list[m]
            y2=y3_list[n]
            t.goto(x2,y2)
            m+=1
            n+=1
        returnhome()

    def quadraticf():
        coeofy=float(E1.get())
        coeofx=float(E2.get())
        coeofx1=float(E44.get())
        constant=float(E3.get())#1
        x=-15*20
        x_list=[]
        y_list=[]
        while x<=300:#from -300 to 300
            x_list.append(x)
            x+=1
        for x11 in x_list:
            y=((((x11/20)**2)*20)*coeofx+constant*20)/coeofy+coeofx1/coeofy*x11
            y_list.append(y)
        m=0
        n=0
        x1=x_list[0]
        y1=y_list[0]
        t.pu()
        t.goto(x1,y1)
        t.pd()

        while m<=len(x_list):
            x2=x_list[m-1]
            y2=y_list[n-1]
            t.goto(x2,y2)
            m+=1
            n+=1

def undo():#撤销
    t.undo()

def marks():
    t.pu()
    t.goto(0,330)
    t.pd()
    t.write("Y",font=("楷体",20,"normal"))
    t.pu()
    t.goto(330,0)
    t.pd()
    t.write("X",font=("楷体",20,"normal"))
    t.pu()
    t.goto(18,10)
    t.pd()
    t.write("O",font=("楷体",30,"normal"))
    t.pu()
    t.home()
    t.pd()
class COLOR():
    def changecolor():
        pass

    def colorblack():
        MF['background']="Black"
        openfile("Black")

    def colorwhite():
        MF['background']="White"
        openfile("White")

    def coloryellow():
        MF['background']="Yellow"
        openfile("Black")

    def colorblue():
        MF['background']="Blue"
        openfile("Blue")

    def colororange():
        MF['background']="Orange"
        openfile("Orange")
#==========================
    def fontred():
        t.pencolor("red")

    def fonttur():
        t.pencolor("Turquoise")

    def fontfuch():
        t.pencolor("Fuchsia")

    def fontmaroon():
        t.pencolor("Maroon")

    def fontpurple():
        t.pencolor("Purple")

    def fontaqua():
        t.pencolor("Aqua")

M1=Menu(MF)
MF.config(menu=M1)
filemenu=Menu(M1)
M1.add_cascade(label="控制",menu=filemenu)
filemenu.add_command(label="退出",command=exit)
filemenu.add_command(label="撤销",command=undo)
filemenu.add_command(label="解函数",command=Corealgo.pub)
filemenu.add_command(label="快速坐标系",command=map2)
filemenu.add_command(label="参考线",command=lines)
filemenu.add_command(label="考试拿分",command=marks)

helpmenu=Menu(M1)
M1.add_cascade(label="帮助",menu=helpmenu)
helpmenu.add_command(label="信息",command=info)
helpmenu.add_command(label="详细信息",command=infoma)

thememenu=Menu(M1)
M1.add_cascade(label="背景",menu=thememenu)
thememenu.add_command(label="黑",command=COLOR.colorblack)
thememenu.add_command(label="白",command=COLOR.colorwhite)
thememenu.add_command(label="黄",command=COLOR.coloryellow)
thememenu.add_command(label="蓝",command=COLOR.colorblue)
thememenu.add_command(label="橙",command=COLOR.colororange)

colormenu=Menu(M1)
M1.add_cascade(label="字色",menu=colormenu)
colormenu.add_command(label="水色",command=COLOR.fontaqua)
colormenu.add_command(label="紫红",command=COLOR.fontfuch)
colormenu.add_command(label="栗色",command=COLOR.fontmaroon)
colormenu.add_command(label="紫色",command=COLOR.fontpurple)
colormenu.add_command(label="红色",command=COLOR.fontred)
colormenu.add_command(label="绿色",command=COLOR.fonttur)

plusmenu=Menu(M1)
M1.add_cascade(label="拓展",menu=plusmenu)
plusmenu.add_command(label="反比例函数",command=Corealgo.ipfunction)
plusmenu.add_command(label="二次函数",command=Corealgo.quadraticf)

B1.bind("<Button-1>",map)#按钮1的方法
B2.bind("<Button-1>",Corealgo.gof)
B3.bind("<Button-1>",Corealgo.goft)
B4.bind("<Button-1>",goto)
B12.bind("<Button-1>",Corealgo.jiao)
B13.bind("<Button-1>",Corealgo.jiaot)
B51.bind("<Button-1>",selfchangecolor)
MF.mainloop()
