import easygui as e
import sys

while 1:
    #一个消息提示框
    msg='开始一个练习'
    title='2017-11-09'
    e.msgbox(msg,title,'确定')
    #一个确认，取消提示框，返回值为布尔类型
    if e.ccbox('要开始了么？','请选择',['确定','取消']):
        pass
    else :
        sys.exit(0)
    #选择提示框
    choice=['普通','困难','地狱']
    callback=e.choicebox('选择一个难度','开始了',choice)
    if callback == '普通':
        e.buttonbox('你选择的内容是','',callback)
    elif callback == '困难':
        e.indexbox(callback,'你的选择')
    elif callback == '地狱':
        e.boolbox(callback,'你的选择')

    #输入密码
    e.passwordbox('请输入密码：')
