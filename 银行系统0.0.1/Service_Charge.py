class sercha:
    __sxf = 0.0
    def setserchamoney(self,outputmoney):
        if outputmoney < 2000:
            self.__sxf =1.6
        if outputmoney > 2000 and outputmoney<5000:
            self.__sxf =4
        if outputmoney>5000 and outputmoney<10000:
            self.__sxf =8
        if outputmoney > 10000 and outputmoney < 50000:
            self.__sxf =12
        if outputmoney > 50000:
            if outputmoney * 0.0003 > 50:
                self.__sxf =50
            else:
                self.__sxf = outputmoney * 0.0003
    def getserchamoney(self):
        return self.__sxf