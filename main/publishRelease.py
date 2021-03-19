import MySQLdb
#发布寻找
class publishRelease1:
    def __init__(self,AnimalName,species,AnimalSex,contactName,contactNumber,feature,other,imgFile1,imgFile2,imgFile3,account):
        self.AnimalName = AnimalName
        self.species = species
        self.AnimalSex = AnimalSex
        self.contactName = contactName
        self.contactNumber = contactNumber
        self.feature = feature
        self.other = other
        self.imgFile1 = imgFile1
        self.imgFile2 = imgFile2
        self.imgFile3 = imgFile3
        self.account = account
    def publishFind(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "insert into publishfind (AnimalName,species,AnimalSex,contactName,contactNumber,feature,other,imgFile1,imgFile2,imgFile3,account) value ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}');".format(
                    self.AnimalName,self.species,self.AnimalSex,self.contactName,self.contactNumber,self.feature,self.other,self.imgFile1,self.imgFile2,self.imgFile3,self.account)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def getPublishReleaseList(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "select * from  publishfind where isCheck='{0}'".format(1)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
    #获取个人发布寻找列表
    def getPublishReleaseSelfList(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "select * from  publishfind where account='{0}'".format(account)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
        #默认0 未寻回
        #1 已寻回
        #0
    def isSeek(seekId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "update  publishfind set isSeek='{0}' where id={1}".format(1,int(seekId))
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
    def isGiveUpSeek(seekId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "update  publishfind set isGiveUp='{0}' where id={1}".format(1,int(seekId))
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'