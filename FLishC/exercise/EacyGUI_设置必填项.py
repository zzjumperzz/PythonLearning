import easygui as e
# 多行输入，设置必填项
while 1:
    msg = "请填写以下联系方式"
    title = "账号中心"
    fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
    fieldValues = []
    fieldValues = e.multenterbox(msg, title, fieldNames)

    if fieldValues == None:
        e.msgbox('未输入任何值')
        break
    errmsg = ''
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == '' and option[0] == '*':
            errmsg += ('%s为必填项\n\n' % fieldNames[i])
    if errmsg == '':
        break
    fieldValues = e.multenterbox(errmsg,title,fieldNames,fieldValues)

print('用户资料如下%s'%str(fieldValues))