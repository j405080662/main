import MySQLdb
class manageDAO:
    def getManageAdoption(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select publishadoption.id,user.user_name,publishadoption.account,publishadoption.species,publishadoption.isCheck from publishadoption,user where publishadoption.account=user.account'
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
    def deleteManageAdoption(adoptid):
        try:

            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'delete from publishadoption where id={0}'.format(int(adoptid))
            cul.execute(sql)
            conn.commit()

            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def getManageSeek(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select publishfind.id,user.user_name,publishfind.account,publishfind.species,publishfind.isCheck from publishfind,user where publishfind.account=user.account'
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
    def deleteManageSeek(seekId):
        try:

            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'delete from publishfind where id={0}'.format(int(seekId))
            cul.execute(sql)
            conn.commit()

            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def getShipments(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select goodsorder.payid,goodsorder.account,goodsorder.address,goodsorder.status from goodsorder,user where goodsorder.account=user.account  group by payid'.format()
            cul.execute(sql)
            res = cul.fetchall()
            data =[]

            for i in res:

                sql = 'select address{0} from receiveaddress where account="{1}"'.format(i[2],i[1])
                cul.execute(sql)
                res1 = cul.fetchall()
                sql = 'select  goods.goodsName from goods,goodsorder  where goodsorder.payid="{0}" and goods.id=goodsorder.goodsId'.format(i[0])
                cul.execute(sql)
                res2 = cul.fetchall()
                data.append([i[0],i[1],res1[0][0],i[3],res2])  #订单号，账号，地址,状态，详情

            cul.close()
            conn.close()
            return data
        except:
            return '0'
    def deleteOrder(orderId):
        try:

            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'delete from goodsorder where payid="{0}"'.format(orderId)
            cul.execute(sql)
            conn.commit()

            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def adoptManageIncome(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select payid,account from goodsorder   group by payid'.format()
            cul.execute(sql)
            res = cul.fetchall()
            data = []

            for i in res:

                sql = 'select  goods.goodsName,goodsorder.goodsSum from goods,goodsorder  where goodsorder.payid="{0}" and goods.id=goodsorder.goodsId'.format(
                    i[0])
                cul.execute(sql)
                res2 = cul.fetchall()
                GoodsDateil=[]
                GoodsSum = 0
                for j in res2:
                    GoodsDateil.append(j[0])
                    GoodsSum+=float(j[1])
                data.append([i[0], i[1], GoodsDateil,GoodsSum])  # 订单号，账号，地址,状态，详情

            cul.close()
            conn.close()
            return data
        except:
            return '0'
    def getCheckList(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select publishadoption.id,publishadoption.adoptionName,publishadoption.account,user.user_name from publishadoption,user   where publishadoption.account=user.account and publishadoption.isCheck="0"'
            cul.execute(sql)
            res = cul.fetchall()
            sql = 'select publishfind.id,publishfind.AnimalName,publishfind.account,user.user_name from publishfind,user   where publishfind.account=user.account and publishfind.isCheck="0"'
            cul.execute(sql)
            res1 = cul.fetchall()
            if len(res)==0 and len(res1)==0:
                return '2'
            else:
                return [res,res1]
        except:
            return '0'
    def getManageUsers(adoptId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select publishadoption.id,publishadoption.adoptTime,publishadoption.adoptPeopleId,user.user_name from publishadoption,user   where publishadoption.adoptPeopleId=user.account and publishadoption.isCheck="1"'
            cul.execute(sql)
            res = cul.fetchall()

            return  res
        except:
            return '0'
    def checkAdoptLog(adoptId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select dayLogId,content  from daylog where adoptId="{0}"'.format(adoptId)
            cul.execute(sql)
            res = cul.fetchall()
            return  res
        except:
            return '0'