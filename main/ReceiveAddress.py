import  MySQLdb
class ReceiveAddress1:
    def __init__(self,account):
        self.account = account
    def getReceiveAddress(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "select * from ReceiveAddress where account =\'{0}\'".format(self.account)
            cul.execute(sql)
            res = cul.fetchall()
            if len(res)!=0:
                conn.close()
                return res
            else:
                sql = "insert into ReceiveAddress (account,receiveUser1,address1,phone1,receiveUser2,address2,phone2,receiveUser3,address3,phone3,default_) value ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}');".format(self.account,'','','','','','','','','','1')
                cul.execute(sql)
                conn.commit()
                sql = "select * from ReceiveAddress where account =\'{0}\'".format(self.account)
                cul.execute(sql)
                res = cul.fetchall()
                cul.close()
                conn.close()
                return res
        except:
            return '0'
    def saveReceiveAddress(account,addressId,receiveUser,phone,address):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'update  receiveaddress set {0}="{1}",{2}="{3}",{4}="{5}" where account="{6}"'.format('address'+str(addressId),address,'phone'+str(addressId),phone,'receiveUser'+str(addressId),receiveUser,account)
            cul.execute(sql)
            conn.commit()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'

