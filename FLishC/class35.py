#图形用户界面入门 EasyGUI
#import easygui
#from easygui import *
import easygui as e
import sys
while 1:
    e.msgbox('进入第一个界面小游戏~')
    msg = '我们学习python能做什么呢？'
    title = '小游戏互动'
    choicebox = ['打飞机','挣大钱','提升自己']

    choice = e.choicebox(msg,title,choicebox)

    e.msgbox('你的选择是'+str(choice),'结果')

    msg = '你希望重新开始么?'
    title = '请选择'

    if e.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
