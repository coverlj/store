class Input:
    def getinputHelp(self,chose,datatype="str"):
        while True:
            print("请输入", chose, ":")
            i = input(">>>:")
            if len(i) == 0:
                print("该项不能为空！请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i