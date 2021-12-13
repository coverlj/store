import random

class Service_Charge:
    __service_charge=0.0
    __exchange_rate=0.0
    def setService_Charge(self,money):
        if money<2000:
            self.__service_charge=1.6
        elif money>2000 and money<5000:
            self.__service_charge=4
        elif money>5000 and money<10000:
            self.__service_charge=8
        elif money > 10000 and money < 50000:
            self.__service_charge = 12
        elif money>50000:
            if money*0.0003>50:
                self.__service_charge=50
            else:
                self.__service_charge=money*0.0003
    def getService_Charge(self):
        return self.__service_charge
    def setexchange_rate(self,currency_system):
        if currency_system=="美元":
            i=round(random.uniform(6.3700,6.3665),4)
            self.__exchange_rate=i
        elif currency_system=="欧元":
            i = round(random.uniform(7.1819, 7.2094),4)
            self.__exchange_rate = i
        else:
            self.__exchange_rate=1
        return self.__exchange_rate