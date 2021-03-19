import  MySQLdb
class user:
    def __init__(self,account,email,user_name,sex,birthday,password):
        self.account =account
        self.email = email
        self.sex = sex
        self.user_name = user_name
        self.birthday = birthday
        self.password = password

    def user_regsiter(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "select * from user where account =\'{0}\'".format(self.account)
            cul.execute(sql)
            res = cul.fetchall()
            if len(res)!=0:
                conn.close()
                return '账号已存在'
            else:
                sql = "insert into user (account,email,user_name,sex,birthday,password) value ('{0}','{1}','{2}','{3}','{4}','{5}');".format(self.account,self.email,self.user_name,self.sex,self.birthday,self.password)
                cul.execute(sql)
                conn.commit()
                res = cul.fetchall()
                cul.close()
                conn.close()
                return '1'
        except:
            return '注册失败'
    def getUserInfo(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "select * from user where account =\'{0}\' ".format(account )
            cul.execute(sql)
            res = cul.fetchall()
            if len(res) != 0:
                conn.close()
                return res
            else:
                return '0'
        except:
            return '1'
    def saveUserInfo (account,email,realName,sex,birthday):  #更新个人信息
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "update user set email='{0}',realName ='{1}',sex = '{2}',birthday='{3}'where account ='{4}'".format(email,realName,sex,birthday,account )
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            return '更新成功'
        except:
            return '更新失败'

    def to_json(self):
        item = self.__dict__
        del item['password']
        return item
class login:
    def __init__(self,account,password):
        self.account = account
        self.password = password

    def user_login(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "select * from user where account =\'{0}\' and password =\'{1}\'".format(self.account,self.password)
            cul.execute(sql)
            print(sql)
            res = cul.fetchall()
            print(res)
            conn.close()
            if len(res) != 0:

                return res
            else:
                return '0'
        except:
            return '0'

    def manager_login(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "select * from manager where account =\'{0}\' and password =\'{1}\'".format(self.account,self.password)
            cul.execute(sql)
            res = cul.fetchall()
            if len(res) != 0:
                conn.close()
                return res
            else:
                return '0'
        except:
            return '0'
