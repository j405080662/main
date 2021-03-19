import MySQLdb,datetime
class publishAdoption1:
    def __init__(self,account,species,sex,title,age,adoptionName,adoptionNumber,address,expelling_parasite,rabies,ster,imgFile,other,describe):
        self.account = account
        self.species = species
        self.sex = sex
        self.title = title
        self.age = age
        self.adoptionName = adoptionName
        self.adoptionNumber = adoptionNumber
        self.address = address
        self.expelling_parasite = expelling_parasite
        self.rabies = rabies
        self.ster = ster
        self.imgFile = imgFile
        self.other = other
        self.describe_ = describe
    def DAOAdoption(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = "insert into publishAdoption (account,species,sex,title,age,adoptionName,adoptionNumber,address,expelling_parasite,rabies,ster,imgFile,other,describe_) value ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}');".format(
                self.account, self.species, self.sex, self.title, self.age, self.adoptionName,
                self.adoptionNumber, self.address, self.expelling_parasite, self.rabies, self.ster,self.imgFile,
            self.other,self.describe_)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def getAdoptInfo1(a):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select * from publishadoption where isCheck="0"'
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'

    def getHaveAdoptList(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select publishadoption.imgFile,publishadoption.describe_,publishadoption.adoptionName,publishadoption.species,publishadoption.age,publishadoption.sex,publishadoption.ster,publishadoption.other,publishadoption.title,adoptapplicationform.adoptId,publishadoption.adoptTime from publishadoption,adoptapplicationform where publishadoption.isCheck = "1" and adoptapplicationform.account="{0}"'.format(account)
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'

    def getHavePublishList(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select publishadoption.imgFile,publishadoption.describe_,publishadoption.adoptionName,publishadoption.species,publishadoption.age,publishadoption.sex,publishadoption.ster,publishadoption.other,publishadoption.title,adoptapplicationform.adoptId,publishadoption.adoptTime from publishadoption,adoptapplicationform where publishadoption.isCheck = "0" and publishadoption.account="{0}"'.format(
                account)
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'

    def getHaveSendList(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select publishadoption.imgFile,publishadoption.describe_,publishadoption.adoptionName,publishadoption.species,publishadoption.age,publishadoption.sex,publishadoption.ster,publishadoption.other,publishadoption.title,adoptapplicationform.adoptId,publishadoption.adoptTime from publishadoption,adoptapplicationform where publishadoption.isCheck = "1" and publishadoption.account="{0}"'.format(
                account)
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
    def getLogList(adoptId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select * from  dayLog where adoptId = "{0}" '.format(
                adoptId)
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'

    def saveLogContent(adoptId,dayLogId,content):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'update dayLog set    content = "{0}" where adoptId = "{1}" and dayLogId = "{2}"'.format(
                content,adoptId,dayLogId)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def getSendPeopleInfo(adoptId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select * from adoptapplicationform where adoptId="{0}"'.format(adoptId)
            cul.execute(sql)

            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'

    def confirmSendPeople(adoptId,sendPeopleInfoId):
        try:
            now_time = datetime.datetime.now()
            time1_str = datetime.datetime.strftime(now_time,'%Y-%m-%d %H:%M:%S')
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'update publishadoption set    adoptPeopleId = "{0}" ,isCheck="1",adoptTime="{1}" where id = "{2}" and dayLogId = "{2}"'.format(
                sendPeopleInfoId,time1_str,adoptId )
            cul.execute(sql)

            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'