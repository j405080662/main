import MySQLdb
import time
import datetime
class goods:
    def __init__(self,id,goodsImg,goodsName,goodsPrice,isHot,isNew,classfication):
        self.id =id
        self.goodsImg = goodsImg
        self.goodsName = goodsName
        self.goodsPrice = goodsPrice
        self.isHot = isHot
        self.isNew = isNew
        self.classfication =classfication
    def getShopList(self):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select * from goods '
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
    def getTrolleyList(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select goodsCart.goodsId,goods.goodsImg,goods.goodsName,goods.goodsPrice,goodsCart.goodsNum from goodsCart,goods where goodsCart.account="{0}"'.format(account)
            cul.execute(sql)
            res = cul.fetchall()
            cul.close()
            conn.close()
            return res
        except:
            return '0'
    def deleteGoods(account,goodsId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql =  'delete from goodscart where account = "{0}" and goodsId="{1}"'.format(account,goodsId)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'

    def deleteAllGoods(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql =  'delete from goodscart where account = "{0}" '.format(account)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'



    def toPayAccount(account,address,Goods):
        try:
            id = time.time()

            now_time = datetime.datetime.now()
            str_time = now_time.strftime("%Y-%m-%d %X")
            payid = str(round(id * 1000000))
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'market', charset='utf8')
            cul = conn.cursor()
            for i in Goods:
                sum = float(i['goodsPrice'])*int(i['goodsNum'])
                sql = 'insert into goodsorder (goodsId,goodsNum,account,payid,goodsSum,address,payTime) value ("{0}","{1}","{2}","{3}","{4}","{5}","{6}")'.format(
                    i['goodsId'], i['goodsNum'], account, payid, sum,address,str_time)
                cul.execute(sql)
                conn.commit()
                sql = 'delete from goodscart where account="{0}" and goodsNum="{1}"'.format(account,i['goodsId'])
                cul.execute(sql)
                conn.commit()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def getOrderList(account):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql = 'select payid from goodsorder where account = "{0}" group by payid'.format(account)
            cul.execute(sql)
            idlist = cul.fetchall()
            data = []
            for i in idlist:
                sql = 'select goods.goodsName,goods.goodsPrice,goodsorder.goodsId,goodsOrder.payTime,goodsorder.goodsNum,goodsorder.payid,goodsorder.status from goodsorder,goods where goodsorder.payid="{0}"'.format(i[0])
                cul.execute(sql)
                res = cul.fetchall()
                data.append(res)
            cul.close()
            conn.close()
            return [data,idlist]
        except:
            return '0'

    def confirmDelivery(account,orderId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql='update  goodsorder set status = "1" where account = "{0}" and payid ="{1}"'.format(account,orderId)
            cul.execute(sql)
            conn.commit()
            res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'
    def addGoodTrolley(account,goodsId):
        try:
            conn = MySQLdb.connect('localhost', 'root', '405080662', 'pet', charset='utf8')
            cul = conn.cursor()
            sql='select * from goodscart where account="{0}" and goodsId="{1}"'.format(account,goodsId)
            cul.execute(sql)
            res = cul.fetchall()
            if len(res )!=0:
                sql = 'update goodscart set goodsNum=goodsNum+1 where  account="{0}" and goodsId="{1}"'.format(account,goodsId)
                cul.execute(sql)
                conn.commit()
                res = cul.fetchall()
            else:
                sql = 'insert into goodscart ( account,goodsId,goodsNum )value ("{0}","{1}","1")'.format(account,goodsId)
                cul.execute(sql)
                conn.commit()
                res = cul.fetchall()
            cul.close()
            conn.close()
            return '1'
        except:
            return '0'


    def to_json(self):
        item = self.__dict__
        return item