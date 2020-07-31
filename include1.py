from turtle import TurtleScreen,RawTurtle,TK,undo
from threading import Thread
from turtle import sys as _sys
import re
from time import sleep

# A Main Program to solve the problem of ImportError
# And discovered more that turtle mudule can do
# First , Let us clear what the frame of this program should be
# --import mudules(classfunction,turtle,sys.exit)
# --The main-window and UI method
# --Functiongate ( To solve " name is not defined " , we will import Core algorithm,and give parameters )
# --
MF = TK.Tk()
MF.geometry("800x750")
MF.title("纯正版憨数 -- 基于面向对象")
MF.iconbitmap("12.ico")
cv1 = TK.Canvas(MF,width=800,height=700,bg="black")
cv1.pack(side="bottom")

scr1 = TurtleScreen(cv1)
p = RawTurtle(scr1)
p.color("Aqua")
q = RawTurtle(scr1)
q.color("DeepSkyBlue")

__version__="1.12"

E1=TK.Entry(MF,width=50,relief="flat")
E1.pack(side='left',padx="2m")

B1=TK.Button(MF,text = "OK",bg = "White",relief = "flat")
B1.pack(side = "left",padx = "2m")

L1 = TK.Label(MF,text = "PO is the best!I made it with PO instead of OO",font=('Kaufmann Std', 10, 'bold italic underline'))
L1.pack(side = "left",padx = "2m")

def openfile(a):
    file=r'd:\\BGCsetting.txt'
    changecolor=open(file,'w')
    changecolor.write(a)

def setwindow():
    SF = TK.Tk()
    SF.geometry("300x30")
    SF.iconbitmap("12.ico")
    SF.title("更改笔画的颜色设置")
    E2 = TK.Entry(SF,width = 10,relief = "flat")
    E2.pack(side = "left",padx="2m")
    B2 = TK.Button(SF,text="OK",relief = "flat")
    B2.pack(side = "left",padx = "2m")
    B3 = TK.Button(SF,text="Help",relief="flat")
    B3.pack(side="left",padx="2m")
    def colorchanger(event):
        color = str(E2.get())
        p.pencolor(color)
    def helper(event):
        TK.messagebox.showinfo("Help","请输入英文单词,如果大写开头的输入没有反应则输入全部为小写字母的单词。\
            可选单词有#FFC0CB Pink 粉红#DC143C Crimson 深红/猩红\
            #FFF0F5 LavenderBlush 淡紫红\
            #DB7093 PaleVioletRed 弱紫罗兰红\
            #FF69B4 HotPink 热情的粉红\
            #FF1493 DeepPink 深粉红\
            #C71585 MediumVioletRed 中紫罗兰红\
            #DA70D6 Orchid 暗紫色/兰花紫\
            #D8BFD8 Thistle 蓟色\
            #DDA0DD Plum 洋李色/李子紫\
            #EE82EE Violet 紫罗兰\
            #FF00FF Magenta 洋红/玫瑰红\
            #FF00FF Fuchsia 紫红/灯笼海棠\
            #8B008B DarkMagenta 深洋红\
            #800080 Purple 紫色\
            #BA55D3 MediumOrchid 中兰花紫\
            #9400D3 DarkViolet 暗紫罗兰\
            #9932CC DarkOrchid 暗兰花紫\
            #4B0082 Indigo 靛青/紫兰色\
            #8A2BE2 BlueViolet 蓝紫罗兰\
            #9370DB MediumPurple 中紫色\
            #7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝\
            #6A5ACD SlateBlue 石蓝色/板岩蓝\
            #483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝\
            #E6E6FA Lavender 淡紫色/熏衣草淡紫\
            #F8F8FF GhostWhite 幽灵白\
            #0000FF Blue 纯蓝\
            #0000CD MediumBlue 中蓝色\
            #191970 MidnightBlue 午夜蓝\
            #00008B DarkBlue 暗蓝色\
            #000080 Navy 海军蓝\
            #4169E1 RoyalBlue 皇家蓝/宝蓝\
            #6495ED CornflowerBlue 矢车菊蓝\
            #B0C4DE LightSteelBlue 亮钢蓝\
            #778899 LightSlateGray 亮蓝灰/亮石板灰\
            #708090 SlateGray 灰石色/石板灰\
            #1E90FF DodgerBlue 闪兰色/道奇蓝\
            #F0F8FF AliceBlue 爱丽丝蓝\
            #4682B4 SteelBlue 钢蓝/铁青\
            #87CEFA LightSkyBlue 亮天蓝色\
            #87CEEB SkyBlue 天蓝色\
            #00BFFF DeepSkyBlue 深天蓝\
            #ADD8E6 LightBlue 亮蓝\
            #B0E0E6 PowderBlue 粉蓝色/火药青\
            #5F9EA0 CadetBlue 军兰色/军服蓝\
            #F0FFFF Azure 蔚蓝色\
            #E0FFFF LightCyan 淡青色\
            #AFEEEE PaleTurquoise 弱绿宝石\
            #00FFFF Cyan 青色\
            #00FFFF Aqua 浅绿色/水色\
            #00CED1 DarkTurquoise 暗绿宝石\
            #2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰\
            #008B8B DarkCyan 暗青色\
            #008080 Teal 水鸭色\
            #48D1CC MediumTurquoise 中绿宝石\
            #20B2AA LightSeaGreen 浅海洋绿\
            #40E0D0 Turquoise 绿宝石\
            #7FFFD4 Aquamarine 宝石碧绿\
            #66CDAA MediumAquamarine 中宝石碧绿\
            #00FA9A MediumSpringGreen 中春绿色\
            #F5FFFA MintCream 薄荷奶油\
            #00FF7F SpringGreen 春绿色\
            #3CB371 MediumSeaGreen 中海洋绿\
            #2E8B57 SeaGreen 海洋绿\
            #F0FFF0 Honeydew 蜜色/蜜瓜色\
            #90EE90 LightGreen 淡绿色\
            #98FB98 PaleGreen 弱绿色\
            #8FBC8F DarkSeaGreen 暗海洋绿\
            #32CD32 LimeGreen 闪光深绿\
            #00FF00 Lime 闪光绿\
            #228B22 ForestGreen 森林绿\
            #008000 Green 纯绿\
            #006400 DarkGreen 暗绿色\
            #7FFF00 Chartreuse 黄绿色/查特酒绿\
            #7CFC00 LawnGreen 草绿色/草坪绿\
            #ADFF2F GreenYellow 绿黄色\
            #556B2F DarkOliveGreen 暗橄榄绿\
            #9ACD32 YellowGreen 黄绿色\
            #6B8E23 OliveDrab 橄榄褐色\
            #F5F5DC Beige 米色/灰棕色\
            #FAFAD2 LightGoldenrodYellow 亮菊黄\
            #FFFFF0 Ivory 象牙色\
            #FFFFE0 LightYellow 浅黄色\
            #FFFF00 Yellow 纯黄\
            #808000 Olive 橄榄\
            #BDB76B DarkKhaki 暗黄褐色/深卡叽布\
            #FFFACD LemonChiffon 柠檬绸\
            #EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色\
            #F0E68C Khaki 黄褐色/卡叽布\
            #FFD700 Gold 金色")
    B2.bind("<Button-1>",colorchanger)
    B3.bind("<Button-1>",helper)
class Others():
    '''
    函数周边功能,画坐标系和解一次函数
    The extra methods of functions
    '''
    def Map():
        def map3():
            p.speed(0)
            p.hideturtle()
            i=0
            p.goto(300,0)
            p.seth(180)
            while i<=600:
                p.forward(20)
                p.dot(5)
                i+=20
        def map2():
            q.hideturtle()
            q.goto(0,300)
            q.pd()
            q.seth(270)
            i=0
            while i<=600:
                q.forward(20)
                q.dot(5)
                i+=20
        thread1 = Thread(target=map3)
        thread2 = Thread(target=map2)
        thread1.start()
        thread2.start()

    def pubdot_for_linear(coeofy,coeofx,constant,coeofy1,coeofx1,constant1):
        try:
            a=coeofy
            b=coeofx
            c=constant
            a1=coeofy1
            b1=coeofx1
            c1=constant1
            d=b/a
            d1=b1/a1 #转成y=kx+b的形式y=dx+c//\\y=d1x+c1,,dx+c=d1x+c1
            if d!=d1:
                x=float((c1-c)/(d-d1))
                y=d1*x+c1
                print('%2fy=%2fx+%2f和%2fy=%2fx+%2f交点为(%f,%f)'%(a,b,c,a1,b1,c1,x,y))
                
            elif d==d1 and c!=c1:
                print('%2fy=%2fx+%2f和%2fy=%2fx+%2f平行，没有交点'%(a,b,c,a1,b1,c1))
            elif b==b1 and c==c1 and a==a1:
                print('%2fy=%2fx+%2f和%2fy=%2fx+%2f两直线重合了'%(a,b,c,a1,b1,c1,))
        except:
            print('注意,请输入合理的数值')
    def undo_actions(times):
        intime=0
        while intime<=times:
            p.undo()
        intime+=1
    def gotoposition(x,y):
        p.goto(x*20,y*20)
    
    def returnhome():
        p.pu()
        p.home()
        p.pd()

    def pubdot_for_l_and_ip(coeofy,coeofx,constant,coeofy1,coeofx1,constant1):
        '''
        内建表达式:{
            coeofy * y = coeofx * x + constant
            coeofy1 * y = constant1 / coeofx1 * x
        }
        将把这些转化为一元二次方程,转而利用公式求解:
        在一次函数中,表达式可以转为: y =coeofx / coeofy * x +constant
        在二次函数中,表达式可以转为: y = [ constant / ( coeofx * coeofy ) ] / x
        '''
        real_coeofx=coeofx/coeofy
        real_constant=constant1/(coeofy1*coeofx1)
        #y = real_coeofx * x + constant
        #y = real_constant / x
        #real_coeofx * x * x + constant * x - real_constant = 0
        sandard=constant**2-4*real_coeofx*(-real_constant)
        if sandard < 0:
            print("有问题")
        else:
            x1=(-constant+(sandard)**0.5)/(2*real_coeofx)
            x2=(-constant-(sandard)**0.5)/(2*real_coeofx)
            y1=x1*real_coeofx+constant
            y2=x2*real_coeofx+constant
            print("函数%fy=%fx+%f与%fy=%f/%fx交点1:(%f,%f),交点2:(%f,%f)"%(\
coeofy,coeofx,constant,coeofy1,constant1,coeofx1,x1,y1,x2,y2))


class Gate():
    def linear():
        coeofy = float(E1.get())
        coeofx = float(E2.get())
        constant = float(E3.get())
        try:
            left = int(E4.get())
        except:
            left = -15
        try:
            right = int(E5.get())
        except:
            right = 15
        l1=Linearfunction(coeofy,coeofx,constant,left,right)
        l1.show()
    def quad():
        coeofy = float(E1.get())
        coeofxx = float(E2.get())
        try:
            coeofx = float(E3.get())
        except:
            coeofx = 0
        try:
            constant = float(E4.get())
        except:
            right = 0
        try:
            left = int(E5.get())
        except:
            left = -15
        try:
            right = int(E6.get())
        except:
            right = 15
        q1=Quadraticf(coeofy,coeofxx,coeofx,constant,left,right)
        q1.show()
    def ip():
        constant = float(E2.get())
        try:
            coeofy = float(E1.get())
        except:
            coeofy = 1
        try:
            coeofx = float(E3.get())
        except:
            coeofx = 1
        try:
            constant1 = float(E4.get())
        except:
            constant1 = 0
        try:
            left = int(E5.get())
        except:
            left = -15
        try:
            right = int(E6.get())
        except:
            right = 15
        i1 = Ipfunction(constant,coeofy,coeofx,constant1,left,right)
        i1.show()
class Gate2():
    def linear2(event):
        coeofy = float(E1.get())
        coeofx = float(E2.get())
        constant = float(E3.get())
        try:
            left = int(E4.get())
        except:
            left = -15
        try:
            right = int(E5.get())
        except:
            right = 15
        l1=Linearfunction(coeofy,coeofx,constant,left,right)
        l1.show(e)
    def quad2(event):
        coeofy = float(E1.get())
        coeofxx = float(E2.get())
        try:
            coeofx = float(E3.get())
        except:
            coeofx = 0
        try:
            constant = float(E4.get())
        except:
            right = 0
        try:
            left = int(E5.get())
        except:
            left = -15
        try:
            right = int(E6.get())
        except:
            right = 15
        q1=Quadraticf(coeofy,coeofxx,coeofx,constant,left,right)
        q1.show()
    def ip2(event):
        constant = float(E2.get())
        try:
            coeofy = float(E1.get())
        except:
            coeofy = 1
        try:
            coeofx = float(E3.get())
        except:
            coeofx = 1
        try:
            constant1 = float(E4.get())
        except:
            constant1 = 0
        try:
            left = int(E5.get())
        except:
            left = -15
        try:
            right = int(E6.get())
        except:
            right = 15
        i1 = Ipfunction(constant,coeofy,coeofx,constant1,left,right)
        i1.show()

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
        p.pencolor("red")

    def fonttur():
        p.pencolor("Turquoise")

    def fontfuch():
        p.pencolor("Fuchsia")

    def fontmaroon():
        p.pencolor("Maroon")

    def fontpurple():
        p.pencolor("Purple")

    def fontaqua():
        p.pencolor("Aqua")
class Font():
    def pensize1():
        p.pensize(1)
        q.pensize(1)

    def pensize2():
        p.pensize(2)
        q.pensize(2)

    def pensize3():
        p.pensize(3)
        q.pensize(3)

    def pensize4():
        p.pensize(4)
        q.pensize(4)

    def pensize5():
        p.pensize(5)
        q.pensize(5)

    def pensize6():
        p.pensize(6)
        q.pensize(6)
def advancedrawer(event):
    L1.configure(text = "Drawing function...please wait...",font=('Kaufmann Std', 10, 'bold italic underline'))
    exp = str(E1.get())

    coeofy = re.findall(r"(.+?)y",exp)
    coeofy = float(''.join(coeofy))
    try:
        coeofx10 = re.findall(r"=(.+?)x10",exp)
        coeofx10 = ''.join(coeofx10)
        exp = exp.replace(coeofx10+"x10","")
        coeofx10 = float(coeofx10)
    except:
        coeofx10 = 0

    try:
        coeofx9 = re.findall(r"=(.+?)x9",exp)
        coeofx9 = ''.join(coeofx9)
        exp = exp.replace(coeofx9+"x9","")
        coeofx9 = float(coeofx9)
    except:
        coeofx9 = 0

    try:
        coeofx8 = re.findall(r"=(.+?)x8",exp)
        coeofx8 = ''.join(coeofx8)
        exp = exp.replace(coeofx8+"x8","")
        coeofx8 = float(coeofx8)
    except:
        coeofx8 = 0

    try:
        coeofx7 = re.findall(r"=(.+?)x7",exp)
        coeofx7 = ''.join(coeofx7)
        exp = exp.replace(coeofx7+"x7","")
        coeofx7 = float(coeofx7)
    except:
        coeofx7 = 0

    try:
        coeofx6 = re.findall(r"=(.+?)x6",exp)
        coeofx6 = ''.join(coeofx6)
        exp = exp.replace(coeofx6+"x6","")
        coeofx6 = float(coeofx6)
    except:
        coeofx6 = 0

    try:
        coeofx5 = re.findall(r"=(.+?)x5",exp)
        coeofx5 = ''.join(coeofx5)
        exp = exp.replace(coeofx5+"x5","")
        coeofx5 = float(coeofx5)
    except:
        coeofx5 = 0

    try:
        coeofx4 = re.findall(r"=(.+?)x4",exp)
        coeofx4 = ''.join(coeofx4)
        exp = exp.replace(coeofx4+"x4","")
        coeofx4 = float(coeofx4)
    except:
        coeofx4 = 0

    try:
        coeofx3 = re.findall(r"=(.+?)x3",exp)
        coeofx3 = ''.join(coeofx3)
        exp = exp.replace(coeofx3+"x3","")
        coeofx3 = float(coeofx3)
    except:
        coeofx3 = 0

    try:
        coeofx2 = re.findall(r"=(.+?)x2",exp)
        coeofx2 = ''.join(coeofx2)
        exp = exp.replace(coeofx2+"x2","")
        coeofx2 = float(coeofx2)
    except:
        coeofx2 = 0

    try:
        coeofx = re.findall(r"=(.+?)x",exp)
        coeofx = ''.join(coeofx)
        exp = exp.replace(coeofx+"x","")
        coeofx = float(coeofx)
    except:
        coeofx = 0
    try:
        constant_1 = re.findall(r"=(.+?)&",exp)
        constant_1 = ''.join(constant_1)
        exp = exp.replace(constant_1+"&","")
        constant_1 = float(constant_1)
        coeofx_1 = re.findall(r"=(.+?)X_1",exp)
        coeofx_1 = ''.join(coeofx_1)
        exp = exp.replace(coeofx_1+"X_1","")
        coeofx_1 = float(coeofx_1)
    except:
        coeofx_1 = 0
        constant_1 = 0

    restexp = list(exp)
    try:
        try:
            conlist = restexp[restexp.index("+"):]
        except:
            conlist = restexp[restexp.index("-"):]
        finally:
            constant = float(''.join(conlist))
    except:
        constant=0

    x_list = []
    y_list = []
    Y_list = []
    final_y_list = []
    for i in range(-300,300):
        x_list.append(i)
    times = 0
    for ii in x_list:
        y = (coeofx10*((ii/20)**10*20)+\
            coeofx9*((ii/20)**9*20)+\
            coeofx8*((ii/20)**8*20)+\
            coeofx7*((ii/20)**7*20)+\
            coeofx6*((ii/20)**6*20)+\
            coeofx5*((ii/20)**5*20)+\
            coeofx4*((ii/20)**4*20)+\
            coeofx3*((ii/20)**3*20)+\
            coeofx2*((ii/20)**2*20)+\
            coeofx*ii+\
            20*constant)/coeofy
        y_list.append(y)

    x_list.remove(0)

    for iii in x_list:
        try:
            y = (constant_1*400)/(iii*coeofx_1)
        except:
            y = 0
        Y_list.append(y)
    
    times = 0
    while times <=598:
        y = y_list[times]+Y_list[times]
        final_y_list.append(y)
        times += 1
    times = 0
    p.pu()
    p.goto(x_list[0],final_y_list[0])
    p.pd()
    while times<=299:
        p.goto(x_list[times],final_y_list[times])
        times += 1
    p.pu()
    p.goto(x_list[times+1],final_y_list[times+1])
    p.pd()
    times+=1
    while times<=598:
        p.goto(x_list[times],final_y_list[times])
        times+=1

    L1.configure(text = "The function has been drawn!",font=('Kaufmann Std', 10, 'bold italic underline'))
    L1.configure(text = "Let's continue!",font=('Kaufmann Std', 10, 'bold italic underline'))

B1.bind("<Button-1>",advancedrawer)
M1=TK.Menu(MF)
MF.config(menu=M1)
mainmenu=TK.Menu(M1)
M1.add_cascade(label="画函数",menu=mainmenu)
mainmenu.add_command(label="一次函数",command=Gate.linear)
mainmenu.add_command(label="反比例函数",command=Gate.ip)
mainmenu.add_command(label="二次函数",command=Gate.quad)

othermenu=TK.Menu(M1)
M1.add_cascade(label="辅助",menu=othermenu)
othermenu.add_command(label="解一次函数")
othermenu.add_command(label="解一次函数&反比例函数")
othermenu.add_command(label="一次函数与坐标轴交点")
othermenu.add_command(label="撤销")
othermenu.add_command(label="退出",command=_sys.exit)

setmenu = TK.Menu(M1)
M1.add_cascade(label = "设置",menu = setmenu)
thememenu=TK.Menu(setmenu)
setmenu.add_cascade(label="主题",menu=thememenu)

colormenu = TK.Menu(thememenu)
thememenu.add_cascade(label="颜色",menu=colormenu)
colormenu.add_command(label="红",command=COLOR.fontmaroon)
colormenu.add_command(label="紫",command=COLOR.fontpurple)
colormenu.add_command(label="蓝",command=COLOR.fontaqua)
colormenu.add_command(label="黄",command=COLOR.fonttur)
colormenu.add_command(label="绿",command=COLOR.fonttur)
colormenu.add_command(label="自定义",command = setwindow)

bgmenu=TK.Menu(thememenu)
thememenu.add_cascade(label="背景",menu=bgmenu)
bgmenu.add_command(label="黑",command=COLOR.colorblack)
bgmenu.add_command(label="蓝",command=COLOR.colorblue)
bgmenu.add_command(label="橘",command=COLOR.colororange)
bgmenu.add_command(label="黄",command=COLOR.coloryellow)

fontmenu = TK.Menu(setmenu)
setmenu.add_cascade(label = "笔画大小",menu = fontmenu)
fontmenu.add_command(label = "1",command = Font.pensize1)
fontmenu.add_command(label = "2",command = Font.pensize2)
fontmenu.add_command(label = "3",command = Font.pensize3)
fontmenu.add_command(label = "4",command = Font.pensize4)
fontmenu.add_command(label = "5",command = Font.pensize5)
fontmenu.add_command(label = "6",command = Font.pensize6)

Others.Map()
TK.mainloop()