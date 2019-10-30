import itchat
import os
import time
import requests
import threading
import win32api
import win32gui
from itchat.content import *
from tkinter import *
from tkinter import scrolledtext
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk

LIST = []
MEDIA = []
start = 1
num = '0'
tim =10

sleep = '机器人已关闭！'
begin = '机器人已启动！'
wait = '等待回复...'
insert = '等待超时，程序介入'
introduction = '你好！我是微信机器人助手小夏同学！'
mp = '哦，我的小宝贝，原来你在这里！'
card = '哇哦，这位优秀的人士是？'
note = '知道了'
sharing = '你的分享可真不错！受益匪浅！'
pic = '你发送的图片视频将被我自动下载至当前路径'
recording1 = '我觉得你的声音是世界上最甜的！'
recording2 = '如果你无聊，可以和我聊天呀，嘻嘻嘻嘻！'
content = '欢迎使用微信机器人助手小夏同学！\n\n'
qun = '神马问题？'
over = '今天累了，我去睡觉了！'

ct = win32api.GetConsoleTitle()
hd = win32gui.FindWindow(0,ct)
win32gui.ShowWindow(hd,0)                           #隐藏控制台窗口

try:
    jianCe = os.path.exists('C:\\used.txt')
    if jianCe == False:
        file = open('C:\\used.txt','w')
        for i in range(3):
            t = str(time.localtime()[i])
            file.write(t+' ')
        file.close()
    else:
        file = open('C:\\used.txt','r')
        du = file.read()
        du2 = du.split(' ')
        num = int(du2[3])
        file.close()
    
except:
    file.close()                            #生成文件保存已调用图灵机器人次数


root = Tk()
root.title('小夏同学-V3.0     微信公众号：工业光线     网站：http://www.tech-xjc.com')
root.geometry('800x667')
root.resizable(width=False, height=False)

photo1 = Image.open("C:\\Users\Administrator\Downloads\web.png")
photo1.thumbnail((160,160))
img1 = ImageTk.PhotoImage(photo1)

photo2 = Image.open("C:\\Users\Administrator\Desktop\公众号素材\wc.jpg")
photo2.thumbnail((160,160))
img2 = ImageTk.PhotoImage(photo2)

out = scrolledtext.ScrolledText(root)
out.place(x=400,y=70,width=380,height=250)
out.insert('end',content)
out.see(END)

lb1 = Label(root,text='请输入API号/必填：')
lb1.place(x=30,y=10)
inp1 = Entry(root)
inp1.place(x=145,y=10,width=240)

var1 = IntVar()
xuan1 = Checkbutton(root,variable=var1)
xuan1.place(x=5,y=35)
lb2 = Label(root,text='休眠回复：')
lb2.place(x=30,y=35)
lb3 = Label(root,text=' 默认：机器人已关闭！')
lb3.place(x=90,y=35)
lb4 = Label(root,text='自定义：')
lb4.place(x=90,y=55)
inp2 = Entry(root)
inp2.place(x=145,y=55,width=240)

var2 = IntVar()
xuan2 = Checkbutton(root,variable=var2)
xuan2.place(x=5,y=80)
lb5 = Label(root,text='唤醒回复：')
lb5.place(x=30,y=80)
lb6 = Label(root,text=' 默认：机器人已开启！')
lb6.place(x=90,y=80)
lb7 = Label(root,text='自定义：')
lb7.place(x=90,y=100)
inp3 = Entry(root)
inp3.place(x=145,y=100,width=240)

var3 = IntVar()
xuan3 = Checkbutton(root,variable=var3)
xuan3.place(x=5,y=125)
lb8 = Label(root,text='等待回复：')
lb8.place(x=30,y=125)
lb9 = Label(root,text=' 默认：等待回复...！')
lb9.place(x=90,y=125)
lb10 = Label(root,text='自定义：')
lb10.place(x=90,y=145)
inp4 = Entry(root)
inp4.place(x=145,y=145,width=240)

var4 = IntVar()
xuan4 = Checkbutton(root,variable=var4)
xuan4.place(x=5,y=170)
lb11 = Label(root,text='介入回复：')
lb11.place(x=30,y=170)
lb12 = Label(root,text=' 默认：等待超时，程序介入')
lb12.place(x=90,y=170)
lb13 = Label(root,text='自定义：')
lb13.place(x=90,y=190)
inp5 = Entry(root)
inp5.place(x=145,y=190,width=240)

var5 = IntVar()
xuan5 = Checkbutton(root,variable=var5)
xuan5.place(x=5,y=215)
lb14 = Label(root,text='介绍回复：')
lb14.place(x=30,y=215)
lb15 = Label(root,text=' 默认：你好！我是微信机器人助手小夏同学！')
lb15.place(x=90,y=215)
lb16 = Label(root,text='自定义：')
lb16.place(x=90,y=235)
inp6 = Entry(root)
inp6.place(x=145,y=235,width=240)

var6 = IntVar()
xuan6 = Checkbutton(root,variable=var6)
xuan6.place(x=5,y=260)
lb17 = Label(root,text='地图回复：')
lb17.place(x=30,y=260)
lb18 = Label(root,text=' 默认：哦，我的小宝贝，原来你在这里！')
lb18.place(x=90,y=260)
lb19 = Label(root,text='自定义：')
lb19.place(x=90,y=280)
inp7 = Entry(root)
inp7.place(x=145,y=280,width=240)

var7 = IntVar()
xuan7 = Checkbutton(root,variable=var7)
xuan7.place(x=5,y=305)
lb20 = Label(root,text='名片回复：')
lb20.place(x=30,y=305)
lb21 = Label(root,text=' 默认：哇哦，这位优秀的人士是？')
lb21.place(x=90,y=305)
lb22 = Label(root,text='自定义：')
lb22.place(x=90,y=325)
inp8 = Entry(root)
inp8.place(x=145,y=325,width=240)

var8 = IntVar()
xuan8 = Checkbutton(root,variable=var8)
xuan8.place(x=5,y=350)
lb23 = Label(root,text='提示回复：')
lb23.place(x=30,y=350)
lb24 = Label(root,text=' 默认：知道了')
lb24.place(x=90,y=350)
lb25 = Label(root,text='自定义：')
lb25.place(x=90,y=370)
inp9 = Entry(root)
inp9.place(x=145,y=370,width=240)

var9 = IntVar()
xuan9 = Checkbutton(root,variable=var9)
xuan9.place(x=5,y=395)
lb26 = Label(root,text='分享回复：')
lb26.place(x=30,y=395)
lb27 = Label(root,text=' 默认：你的分享可真不错！受益匪浅！')
lb27.place(x=90,y=395)
lb28 = Label(root,text='自定义：')
lb28.place(x=90,y=415)
inp10 = Entry(root)
inp10.place(x=145,y=415,width=240)

var10 = IntVar()
xuan10 = Checkbutton(root,variable=var10)
xuan10.place(x=5,y=440)
lb29 = Label(root,text='图片回复：')
lb29.place(x=30,y=440)
lb30 = Label(root,text=' 默认：你发送的图片视频将被我自动下载至当前路径')
lb30.place(x=90,y=440)
lb31 = Label(root,text='自定义：')
lb31.place(x=90,y=460)
inp11 = Entry(root)
inp11.place(x=145,y=460,width=240)

var11 = IntVar()
xuan11 = Checkbutton(root,variable=var11)
xuan11.place(x=5,y=485)
lb32 = Label(root,text='语音回复：')
lb32.place(x=30,y=485)
lb33 = Label(root,text=' 默认：我觉得你的声音是世界上最甜的！')
lb33.place(x=90,y=485)
lb34 = Label(root,text='自定义：')
lb34.place(x=90,y=505)
inp12 = Entry(root)
inp12.place(x=145,y=505,width=240)

lb35 = Label(root,text='语音回复：')
lb35.place(x=30,y=530)
lb36 = Label(root,text=' 默认：如果你无聊，可以和我聊天呀，嘻嘻嘻嘻！')
lb36.place(x=90,y=530)
lb37 = Label(root,text='自定义：')
lb37.place(x=90,y=550)
inp13 = Entry(root)
inp13.place(x=145,y=550,width=240)

var14 = IntVar()
xuan12 = Checkbutton(root,variable=var14)
xuan12.place(x=5,y=575)
lb46 = Label(root,text='群@回复：')
lb46.place(x=30,y=575)
lb47 = Label(root,text=' 默认：神马问题？')
lb47.place(x=90,y=575)
lb48 = Label(root,text='自定义：')
lb48.place(x=90,y=595)
inp16 = Entry(root)
inp16.place(x=145,y=595,width=240)

var15 = IntVar()
xuan13 = Checkbutton(root,variable=var15)
xuan13.place(x=5,y=620)
lb49 = Label(root,text='图灵结束：')
lb49.place(x=30,y=620)
lb50 = Label(root,text=' 默认：今天累了，我去睡觉了！')
lb50.place(x=90,y=620)
lb51 = Label(root,text='自定义：')
lb51.place(x=90,y=640)
inp17 = Entry(root)
inp17.place(x=145,y=640,width=240)

lb52 = Label(root,text='请设置机器人初次等待介入时间(秒)/默认10秒：')
lb52.place(x=400,y=576)
inp14 = Entry(root)
inp14.place(x=660,y=576,width=95,height=19)

lb45 = Label(root,text='请设置图灵机器人调用次数(条/日)/必填：')
lb45.place(x=400,y=550)
inp15 = Entry(root)
inp15.place(x=625,y=550,width=128,height=19)

lb44 = Label(root,text='是否显示消息类型：')
lb44.place(x=400,y=597)
var12 = IntVar()
rd1 = Radiobutton(root,text='是',variable=var12,value=1)
rd1.place(x=510,y=597)
rd1 = Radiobutton(root,text='否',variable=var12,value=0)
rd1.place(x=550,y=597)

lb53 = Label(root,text='是否允许自动添加新朋友：')
lb53.place(x=400,y=620)
var13 = IntVar()
rd1 = Radiobutton(root,text='是',variable=var13,value=1)
rd1.place(x=545,y=620)
rd1 = Radiobutton(root,text='否',variable=var13,value=0)
rd1.place(x=585,y=620)

lb38 = Label(root,text='注意：请浏览提示与警告')
lb38.place(x=635,y=640)

lb39 = Label(root,image=img1)
lb39.place(x=610,y=340)

lb40 = Label(root,text='个人主页')
lb40.place(x=665,y=510)

lb41 = Label(root,image=img2)
lb41.place(x=410,y=340)

lb42 = Label(root,text='微信公众号')
lb42.place(x=460,y=510)

lb43 = Label(root,text='运行结果：')
lb43.place(x=400,y=45)


def tips():
    showinfo(title='提示',message='1.API号、调用次数必填，其余选填 \n  勾选启动相关回复功能 \n2.信息填好后，先确定再运行 \n3.微信发送turn off程序休眠 \n4.微信发送turn on程序唤醒 \n5.网络问题，会造成回复延迟 \n6.注册图灵机器人填入API号 \n7.图灵机器人提供基本文字回复 \n8.关注微信公众号,回复“3.0”\n  获取软件详细说明')
    
def alert():
    showinfo(title='警告',message='本软件只可用于日常交流学习，禁止非法使用本软件，否则后果自负，开发者及其技术支持不承担任何责任！')

def data():
    out.insert('insert','你的选择及结果：\n')
    global KEY
    KEY = str(inp1.get()) if str(inp1.get()) != '' else '（警告：请输入你的API，否则不予登陆）'
    out.insert('insert','你的API：'+KEY+'\n')

    if var1.get() == 1:
        global sleep
        sleep = str(inp2.get()) if str(inp2.get()) != '' else sleep
        out.insert('insert','.'+sleep+'\n')

    if var2.get() == 1:
        global begin
        begin = str(inp3.get()) if str(inp3.get()) != '' else begin
        out.insert('insert','..'+begin+'\n')
        out.see(END)

    if var3.get() == 1:
        global wait
        wait = str(inp4.get()) if str(inp4.get()) != '' else wait
        out.insert('insert','...'+wait+'\n')

    if var4.get() == 1:
        global insert
        insert = str(inp5.get()) if str(inp5.get()) != '' else insert
        out.insert('insert','....'+insert+'\n')

    if var5.get() == 1:
        global introduction
        introduction = str(inp6.get()) if str(inp6.get()) != '' else introduction
        out.insert('insert','.....'+introduction+'\n')

    if var6.get() == 1:
        global mp
        mp = str(inp7.get()) if str(inp7.get()) != '' else mp
        out.insert('insert','......'+mp+'\n')

    if var7.get() == 1:
        global card
        card = str(inp8.get()) if str(inp8.get()) != '' else card
        out.insert('insert','.......'+card+'\n')

    if var8.get() == 1:
        global note
        note = str(inp9.get()) if str(inp9.get()) != '' else note
        out.insert('insert','........'+note+'\n')

    if var9.get() == 1:
        global sharing
        sharing = str(inp10.get()) if str(inp10.get()) != '' else sharing
        out.insert('insert','.........'+sharing+'\n')

    if var10.get() == 1:
        global pic
        pic = str(inp11.get()) if str(inp11.get()) != '' else pic
        out.insert('insert','..........'+pic+'\n')

    if var11.get() == 1:
        global recording1
        recording1 = str(inp12.get()) if str(inp12.get()) != '' else recording1
        out.insert('insert','...........'+recording1+'\n')
        global recording2
        recording2 = str(inp13.get()) if str(inp13.get()) != '' else recording2
        out.insert('insert','............'+recording2+'\n')

    if var14.get() == 1:
        global qun
        qun = str(inp16.get()) if str(inp16.get()) != '' else qun
        out.insert('insert','.............'+qun+'\n')

    if var15.get() == 1:
        global over
        over = str(inp17.get()) if str(inp17.get()) != '' else over
        out.insert('insert','..............'+over+'\n')

    global tim
    tim = inp14.get() if inp14.get() != '' else str(tim)
    out.insert('insert','等待时间：'+tim+'\n')

    if inp15.get() != '':
        out.insert('insert','图灵机器人每日调用次数：'+inp15.get()+'\n')

    if inp15.get() == '':
        out.insert('insert','图灵机器人每日调用次数：请输入调用次数！'+inp15.get()+'\n')
    out.insert('insert','机器回复信息预留成功！\n\n')
    out.see(END)
    
def get_response(msg):
        # 这里我们构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'   # 这是API接口网址，不要变
    data = {
        'key'    : KEY,                               # 这个KEY就是上面已经赋值的KEY，就这样不用改
        'info'   : msg,                               # 这是我们要发出去的消息，属于文本消息
        'userid' : 'wechat-robot',                    # wechat-robot这个名字可以随便取，注意加引号
    }
    try:
        r = requests.post(apiUrl, data=data).json()
       
                                   # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
                                   # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
                                   # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
                                   # 将会返回一个None
        return

            
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING,PICTURE, RECORDING, ATTACHMENT, VIDEO])
def reply(msg):    
    nickName0 = itchat.search_friends()['NickName']        #自己的昵称
    try:
        nickName1 = itchat.search_friends(userName=msg['FromUserName'])['NickName']     #对方昵称，try...except...保证nickName1为空时不抛出异常
    except:
        return
        
    global start          #是全局变量得以修改
    if nickName1 == nickName0 and msg.text == 'turn off' and var1.get()==1:     # 对话中出现turn off,则机器人关闭，当然这并不是终止程序运行
        start = 0
        msg.user.send(sleep)
    if nickName1 == nickName0 and msg.text == 'turn on' and var2.get()==1:      # 对话中出现turn on,则启动机器人
        start = 1
        msg.user.send(begin)

    def delay():
        if var3.get() == 1:
            msg.user.send(wait)
            time.sleep(3)
        else:
            pass
        
    if nickName1 != nickName0 and start == 1:
        if msg['Type'] == TEXT or msg['Type'] == MAP or msg['Type'] == CARD or msg['Type'] == NOTE or msg['Type'] == SHARING or msg['Type'] == PICTURE or msg['Type'] == RECORDING or msg['Type'] == ATTACHMENT or msg['Type'] == VIDEO:    
            t0 = time.localtime()[5]              #列表的第5个是秒
            delay()     
            while msg.FromUserName not in LIST:       #程序启动后，每与一个人联系，就将此人的名称保存在列表LIST中
                t1 = time.localtime()[5]
                if str(t1 - t0) > tim:
                    if var4.get() == 1:
                        msg.user.send(insert)
                    time.sleep(1)
                    if var5.get() == 1:
                        msg.user.send(introduction)
                    LIST.append(msg.FromUserName)      #保存在LIST中
                    break
                    
            time.sleep(2)
                
            global num

            try:
                if msg['Type'] == TEXT and num < int(inp15.get()):
                    file = open('C:\\used.txt','r')
                    du = file.read()
                    du2 = du.split(' ')
                    if du2[0] != str(time.localtime()[0]) or du2[1] != str(time.localtime()[1]) or du2[2] != str(time.localtime()[2]):
                        num = 0
                    file.close()
                    num = num + 1
                    file = open('C:\\used.txt','w')
                    for i in range(3):
                        t = str(time.localtime()[i])
                        file.write(t+' ')

                    file.write(str(num))
                    file.close()
                    time.sleep(2)
                    reply = get_response(msg['Text'])      # 使用图灵机器人回答
                    #return reply
                    #out.insert('insert','回复：'+reply+ '\n')
                    out.see(END)

                    msg.user.send(reply)
            
                if msg['Type'] == TEXT and num == int(inp15.get()):
                    msg.user.send(over)

                if var12.get() == 1:                     
                    if msg['Type'] == MAP or msg['Type'] == CARD or msg['Type'] == NOTE or msg['Type'] == SHARING:
                        msg.user.send('信息分类——%s: %s' % (msg.type, msg.text))
                                
                    if msg['Type'] == PICTURE or msg['Type'] == RECORDING or msg['Type'] == ATTACHMENT or msg['Type'] == VIDEO:
                        msg.user.send('信息分类——%s:%s' % (msg.type, msg.fileName))
                                                                      # 上面是输出信息分类
                if msg.type == MAP and var6.get() == 1:                                   # 地图位置信息
                    msg.user.send(mp)
                                
                if msg.type == CARD and var7.get() == 1:                                  # 名片信息
                    msg.user.send(card)
                                
                if msg.type == NOTE and var8.get() == 1:                                  # 当你被拉黑或是加了新朋友后对话框中出现的灰色提示语
                    msg.user.send(note)
                                
                if msg.type == SHARING and var9.get() == 1:                               # 朋友分享
                    msg.user.send(sharing)
                                
                if msg.type == PICTURE or msg.type == VIDEO and var10.get() == 1:          # 对方发送的图片与视频会被自动保存在程序文件所在的位置
                    MEDIA.append(msg.fileName)
                    msg.download(MEDIA[-1])
                    msg.user.send(pic)
                                
                if msg.type == RECORDING and var11.get() == 1:                             # 语音信息
                    msg.user.send(recording1)
                    time.sleep(5)
                    msg.user.send(recording2)

                if str(msg.text) != '':
                    con = str(msg.text)

                if str(msg.fileName) != '':
                    con = str(msg.fileName)
                out.insert('insert','消息：'+con+ '\n')
                out.see(END)
            except:
                out.insert('insert','警告：回复出错！\n')
                out.see(END)
                 
@itchat.msg_register(FRIENDS)
def add_friend(msg):                                              # 自动允许添加新朋友
    if var13.get() == 1:
        msg.user.verify()
        msg.user.send('你好！Nice to meet you!')
    else:
        pass
    
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):                                              # 群聊中被人@
    if var14.get() == 1:
        if msg.isAt:
            msg.user.send(u'@%s\u2005I received:'+qun %           #itchat中@的固定格式
            msg.actualNickName)

def run():
    try:
        itchat.auto_login(hotReload=True)
        itchat.send('登录成功！', toUserName='filehelper')
        out.insert('insert','登录成功！已激活小夏同学！\n\n')
    except:
        out.insert('insert','登录出错！')
    itchat.run(True)                                              # itchat启动

def wechat():
    if str(inp1.get()) != '' and str(inp15.get()) != '':
        out.insert('insert','初次登陆或长时间未登陆则用时较长，约需1~2分钟，请耐心等待...\n\n')
        out.see(END)
        t = threading.Thread(target=run,name='wechat')
        t.start()
    if str(inp1.get()) == '':
        out.insert('insert','请输入API！\n')
        out.see(END)
    if str(inp15.get()) == '':
        out.insert('insert','请输入图灵机器人日可调用次数！\n')
        out.see(END)
    
btn1 = Button(root,text='确定',width=10,command=data)
btn1.place(x=400,y=6)

btn2 = Button(root,text='运行',width=10,command=wechat)
btn2.place(x=500,y=6)

btn3 = Button(root,text='提示',width=10,command=tips)
btn3.place(x=600,y=6)

btn4 = Button(root,text='警告',width=10,command=alert)
btn4.place(x=700,y=6)

root.mainloop()
