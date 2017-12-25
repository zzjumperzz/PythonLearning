#摄氏度华氏度转换 摄氏度*1.8+32 = 华氏度
class Temperature:
    def __init__(self,C = 0,F = 0):
        self.C = C
        self.F = F
    def __set__(self, instance, value):
        if instance == 'centigrade':
            self.C = value
            self.F = value*1.8+32
        else:
            self.F = value
            self.C = (value-32)/1.8
    def __get__(self, instance, owner):
        return super(Tumperature, self).__get__(instance,owner)
