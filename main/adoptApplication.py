import MySQLdb
class adoptApplication:
    def __init__(self,account,adoptId,name,age,phone,address,sex,house,isMarry,isHaveChild):
        self.account=account
        self.adoptId = adoptId
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.sex = sex
        self.house = house
        self.isMarry = isMarry
        self.isHaveChild = isHaveChild
    def DAOadoptApplicationForm(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '19980521', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select * from adoptApplicationForm where account="{0}" and adoptId="{1}"'.format(self.account,
                                                                                                    self.adoptId)
            cul.execute(sql)
            res = cul.fetchall()
            if len(res) != 0:
                return '2'
            else:
                sql = "insert into adoptApplicationForm (account,adoptId,name_,age,phone,address,sex,house,isMarry,isHaveChild) value ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}');".format(
                    self.account, self.adoptId, self.name, self.age, self.phone, self.address, self.sex, self.house,
                    self.isMarry, self.isHaveChild
                )
                cul.execute(sql)
                conn.commit()
                res = cul.fetchall()
                cul.close()
                conn.close()
                return '1'
        except:
            return '0'

    def getAdoptInfoList(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select * from adoptApplicationForm,publishadoption where adoptApplicationForm.adoptId = publishadoption.id and adoptApplicationForm.account = "{0}"'.format(account)
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'

    def deleteAdopt(adoptId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'delete from adoptApplicationForm where id = {0}'.format(adoptId)
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
