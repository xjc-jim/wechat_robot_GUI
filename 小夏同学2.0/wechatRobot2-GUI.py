import itchat
import time
import requests
import threading
from itchat.content import *
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image,ImageTk

LIST = []
MEDIA = []
start = 1
num = 0

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

root = Tk()
root.title('小夏同学-V2.0     微信公众号：工业光线     网站：http://www.tech-xjc.com')
root.geometry('570x590')
root.resizable(width=False, height=False)

photo1 = Image.open("C:\\Users\Administrator\Downloads\web.png")
photo1.thumbnail((160,160))
img1 = ImageTk.PhotoImage(photo1)

photo2 = Image.open("C:\\Users\Administrator\Desktop\公众号素材\wc.jpg")
photo2.thumbnail((160,160))
img2 = ImageTk.PhotoImage(photo2)

lb1 = Label(root,text='请输入API号：')
lb1.place(x=10,y=10)
inp1 = Entry(root)
inp1.place(x=95,y=10,width=240)

lb2 = Label(root,text='休眠回复：')
lb2.place(x=10,y=35)
lb3 = Label(root,text=' 默认：机器人已关闭！')
lb3.place(x=70,y=35)
lb4 = Label(root,text='自定义：')
lb4.place(x=70,y=55)
inp2 = Entry(root)
inp2.place(x=125,y=55,width=240)

lb5 = Label(root,text='唤醒回复：')
lb5.place(x=10,y=80)
lb6 = Label(root,text=' 默认：机器人已开启！')
lb6.place(x=70,y=80)
lb7 = Label(root,text='自定义：')
lb7.place(x=70,y=100)
inp3 = Entry(root)
inp3.place(x=125,y=100,width=240)

lb8 = Label(root,text='等待回复：')
lb8.place(x=10,y=125)
lb9 = Label(root,text=' 默认：等待回复...！')
lb9.place(x=70,y=125)
lb10 = Label(root,text='自定义：')
lb10.place(x=70,y=145)
inp4 = Entry(root)
inp4.place(x=125,y=145,width=240)

lb11 = Label(root,text='介入回复：')
lb11.place(x=10,y=170)
lb12 = Label(root,text=' 默认：等待超时，程序介入')
lb12.place(x=70,y=170)
lb13 = Label(root,text='自定义：')
lb13.place(x=70,y=190)
inp5 = Entry(root)
inp5.place(x=125,y=190,width=240)

lb14 = Label(root,text='介绍回复：')
lb14.place(x=10,y=215)
lb15 = Label(root,text=' 默认：你好！我是微信机器人助手小夏同学！')
lb15.place(x=70,y=215)
lb16 = Label(root,text='自定义：')
lb16.place(x=70,y=235)
inp6 = Entry(root)
inp6.place(x=125,y=235,width=240)

lb17 = Label(root,text='地图回复：')
lb17.place(x=10,y=260)
lb18 = Label(root,text=' 默认：哦，我的小宝贝，原来你在这里！')
lb18.place(x=70,y=260)
lb19 = Label(root,text='自定义：')
lb19.place(x=70,y=280)
inp7 = Entry(root)
inp7.place(x=125,y=280,width=240)

lb20 = Label(root,text='名片回复：')
lb20.place(x=10,y=305)
lb21 = Label(root,text=' 默认：哇哦，这位优秀的人士是？')
lb21.place(x=70,y=305)
lb22 = Label(root,text='自定义：')
lb22.place(x=70,y=325)
inp8 = Entry(root)
inp8.place(x=125,y=325,width=240)

lb23 = Label(root,text='提示回复：')
lb23.place(x=10,y=350)
lb24 = Label(root,text=' 默认：知道了')
lb24.place(x=70,y=350)
lb25 = Label(root,text='自定义：')
lb25.place(x=70,y=370)
inp9 = Entry(root)
inp9.place(x=125,y=370,width=240)

lb26 = Label(root,text='分享回复：')
lb26.place(x=10,y=395)
lb27 = Label(root,text=' 默认：你的分享可真不错！受益匪浅！')
lb27.place(x=70,y=395)
lb28 = Label(root,text='自定义：')
lb28.place(x=70,y=415)
inp10 = Entry(root)
inp10.place(x=125,y=415,width=240)

lb29 = Label(root,text='图片回复：')
lb29.place(x=10,y=440)
lb30 = Label(root,text=' 默认：你发送的图片视频将被我自动下载至当前路径')
lb30.place(x=70,y=440)
lb31 = Label(root,text='自定义：')
lb31.place(x=70,y=460)
inp11 = Entry(root)
inp11.place(x=125,y=460,width=240)

lb32 = Label(root,text='语音回复：')
lb32.place(x=10,y=485)
lb33 = Label(root,text=' 默认：我觉得你的声音是世界上最甜的！')
lb33.place(x=70,y=485)
lb34 = Label(root,text='自定义：')
lb34.place(x=70,y=505)
inp12 = Entry(root)
inp12.place(x=125,y=505,width=240)

lb35 = Label(root,text='语音回复：')
lb35.place(x=10,y=530)
lb36 = Label(root,text=' 默认：如果你无聊，可以和我聊天呀，嘻嘻嘻嘻！')
lb36.place(x=70,y=530)
lb37 = Label(root,text='自定义：')
lb37.place(x=70,y=550)
inp13 = Entry(root)
inp13.place(x=125,y=550,width=240)

lb38 = Label(root,text='注意：请浏览提示与警告')
lb38.place(x=380,y=100)

lb39 = Label(root,image=img1)
lb39.place(x=380,y=145)

lb40 = Label(root,text='个人主页')
lb40.place(x=435,y=315)

lb41 = Label(root,image=img2)
lb41.place(x=380,y=370)

lb42 = Label(root,text='微信公众号')
lb42.place(x=433,y=540)

def tips():
    showinfo(title='提示',message='1.API号必填，其余选填 \n2.信息填好后，先确定再运行 \n3.微信发送turn off程序休眠 \n4.微信发送turn on程序唤醒 \n5.网络问题，会造成回复延迟 \n6.注册图灵机器人填入API号 \n7.图灵机器人提供基本文字回复 \n8.关注微信公众号,回复“介绍”\n  获取软件详细说明')

def alert():
    showinfo(title='警告',message='本软件只可用于日常交流学习，禁止非法使用本软件，否则后果自负，开发者及其技术支持不承担任何责任！')

def data():
    global KEY
    KEY = str(inp1.get()) if str(inp1.get()) != '' else '（警告：请输入你的API，否则不予登陆）'
    print('你的API：',KEY)
    global sleep
    sleep = str(inp2.get()) if str(inp2.get()) != '' else sleep
    print('.',sleep)
    global begin
    begin = str(inp3.get()) if str(inp3.get()) != '' else begin
    print('..',begin)
    global wait
    wait = str(inp4.get()) if str(inp4.get()) != '' else wait
    print('...',wait)
    global insert
    insert = str(inp5.get()) if str(inp5.get()) != '' else insert
    print('....',insert)
    global introduction
    introduction = str(inp6.get()) if str(inp6.get()) != '' else introduction
    print('.....',introduction)
    global mp
    mp = str(inp7.get()) if str(inp7.get()) != '' else mp
    print('......',mp)
    global card
    card = str(inp8.get()) if str(inp8.get()) != '' else card
    print('.......',card)
    global note
    note = str(inp9.get()) if str(inp9.get()) != '' else note
    print('........',note)
    global sharing
    sharing = str(inp10.get()) if str(inp10.get()) != '' else sharing
    print('.........',sharing)
    global pic
    pic = str(inp11.get()) if str(inp11.get()) != '' else pic
    print('..........',pic)
    global recording1
    recording1 = str(inp12.get()) if str(inp12.get()) != '' else recording1
    print('...........',recording1)
    global recording2
    recording2 = str(inp13.get()) if str(inp13.get()) != '' else recording2
    print('............',recording2)
    print('机器回复信息预留成功！')
    
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
    if nickName1 == nickName0 and msg.text == 'turn off':     # 对话中出现turn off,则机器人关闭，当然这并不是终止程序运行
        start = 0
        msg.user.send(sleep)
    if nickName1 == nickName0 and msg.text == 'turn on':      # 对话中出现turn on,则启动机器人
        start = 1
        msg.user.send(begin)

    def delay():
        msg.user.send(wait)
        time.sleep(3)
                    
    if nickName1 != nickName0 and start == 1:
        if msg['Type'] == TEXT or msg['Type'] == MAP or msg['Type'] == CARD or msg['Type'] == NOTE or msg['Type'] == SHARING or msg['Type'] == PICTURE or msg['Type'] == RECORDING or msg['Type'] == ATTACHMENT or msg['Type'] == VIDEO:    
            t0 = time.localtime()[5]              #列表的第5个是秒
                
            while msg.FromUserName not in LIST:       #程序启动后，每与一个人联系，就将此人的名称保存在列表LIST中
                t1 = time.localtime()[5]
                if t1 - t0 > 10:
                    msg.user.send(insert)
                    time.sleep(1)
                    msg.user.send(introduction)
                    LIST.append(msg.FromUserName)      #保存在LIST中
                    break
                    
            time.sleep(2)
                
            global num
                
            if msg['Type'] == TEXT and num < 101:
                num = num + 1
                reply = get_response(msg['Text'])      # 使用图灵机器人回答
                defaultReply = '信息分类——%s: %s' % (msg.type, msg.text)
                return reply or defaultReply     #reply优先，异常时才是后者

            if msg['Type'] == TEXT and num == 101:
                delay()
                msg.user.send('信息分类——%s: %s' % (msg.type, msg.text))
                                
            if msg['Type'] == MAP or msg['Type'] == CARD or msg['Type'] == NOTE or msg['Type'] == SHARING:
                delay()
                msg.user.send('信息分类——%s: %s' % (msg.type, msg.text))
                                
            if msg['Type'] == PICTURE or msg['Type'] == RECORDING or msg['Type'] == ATTACHMENT or msg['Type'] == VIDEO:
                delay()
                msg.user.send('信息分类——%s:%s' % (msg.type, msg.fileName))
                                                                      # 上面是输出信息分类
            if msg.type == MAP:                                   # 地图位置信息
                msg.user.send(mp)
                                
            if msg.type == CARD:                                  # 名片信息
                msg.user.send(card)
                                
            if msg.type == NOTE:                                  # 当你被拉黑或是加了新朋友后对话框中出现的灰色提示语
                msg.user.send(note)
                                
            if msg.type == SHARING:                               # 朋友分享
                msg.user.send(sharing)
                                
            if msg.type == PICTURE or msg.type == VIDEO:          # 对方发送的图片与视频会被自动保存在程序文件所在的位置
                MEDIA.append(msg.fileName)
                msg.download(MEDIA[-1])
                msg.user.send(pic)
                                
            if msg.type == RECORDING:                             # 语音信息
                msg.user.send(recording1)
                time.sleep(5)
                msg.user.send(recording2)
                    
                 
#@itchat.msg_register(FRIENDS)
#def add_friend(msg):                                              # 自动允许添加新朋友
 #   msg.user.verify()
  #  msg.user.send('你好！Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):                                              # 群聊中被人@
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: 神马问题？' %        #itchat中@的固定格式
        msg.actualNickName)

def run():
    itchat.auto_login(hotReload=True)
    itchat.run(True)                                                  # itchat启动

def wechat():
    if str(inp1.get()) != '':
        print('初次登陆或长时间未登陆则用时较长，约需1~2分钟，请耐心等待...')
        t = threading.Thread(target=run,name='wechat')
        t.start()
    else:
        print('请输入API！')

btn1 = Button(root,text='确定',width=10,command=data)
btn1.place(x=380,y=6)

btn2 = Button(root,text='运行',width=10,command=wechat)
btn2.place(x=480,y=6)

btn3 = Button(root,text='提示',width=10,command=tips)
btn3.place(x=380,y=50)

btn4 = Button(root,text='警告',width=10,command=alert)
btn4.place(x=480,y=50)

root.mainloop()
