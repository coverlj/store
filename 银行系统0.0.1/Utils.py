import pymysql
class lianjie:
    # host = "loaclhost"
    # user="root"
    # password="root"
    __database = ""

# 增，删，改
    def setDatabase(self,database):
        self.__database=database
    def getDatabase(self):
        return self.__database
    def update(self, sql, param):

        con = pymysql.connect(host="localhost", user="root", password="root", database=self.__database)
        cursor = con.cursor()

        cursor.execute(sql, param)

        con.commit()

        cursor.close()

        con.close()

    # 查询
    def select(self, sql, param, mode="all", size=3):
        con = pymysql.connect(host="localhost", user="root", password="root", database=self.__database)
        cursor = con.cursor()

        cursor.execute(sql, param)
        if mode == "all":
            return cursor.fetchall()
        elif mode == "one":
            return cursor.fetchone()
        elif mode == "many":
            return cursor.fetchmany(size)

        con.commit()

        cursor.close()
        con.close()