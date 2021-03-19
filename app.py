from flask import Flask,request,json,session,render_template,jsonify
from main import user
import os
from flask_cors import CORS
app = Flask(__name__)
from manage import simple
app.register_blueprint(simple)

#解决跨域资源错误
CORS(app, supports_credentials=True)


app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        account = request.form.get('account')
        email = request.form.get('email')
        user_name = request.form.get('name')
        sex = request.form.get('sex')
        birthday = request.form.get('birthday')
        password = request.form.get('passWord')
        new_user = user.user(account, email, user_name, sex, birthday, password)
        result = new_user.user_regsiter()
        if result =='1':
            return jsonify({'data': '注册成功', 'code': '200'})
        else:
            return jsonify({'data':result,'code':'208'})
    else:
        return jsonify({'data':'请求失败，此接口应post','code':'500'})


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':

        account = request.form.get('account')
        role =request.form.get('role')
        password = request.form.get('passWord')
        new_login = user.login(account, password)
        #选择角色登录
        if role =='用户':
            result = new_login.user_login()
            print(result)
            if result =='0':
                result='用户账号或者密码错误'
                return jsonify({'data':result,'code':'208'})
                # return json.dumps(result,ensure_ascii=False)
            else:
                #登录成功，保存账号，便于检验是否登录
                session['user'] = account
                result = result[0]
                return jsonify({'data':'用户登录成功','account':result[0],'email':result[1],'name':result[2],'sex':result[3],'birthday':result[5],'code':'200'})
        elif role=='管理员':
            result = new_login.manager_login()

            if result =='0':
                result = '管理员账号或者密码错误'
                return jsonify({'data':result,'code':'208'})
            else:
                session['user'] = account
                return jsonify({'data':'管理员登录成功','account':account,'code':'200'})
        else:
            return jsonify({'data':'角色错误','code':'208'})
    else:
        return jsonify({'data':'请求失败,此接口使用post','code':'500'})

from main.publishRelease import publishRelease1
import time

@app.route('/publishRelease',methods=['POST','GET'])
def publishRelease():
    if request.method == 'POST':
        img_url = 'static/user_img/'
        AnimalName = request.form.get('name',None)
        species = request.form.get('species',None)
        AnimalSex = request.form.get('AnimalSex',None)
        contactName = request.form.get('contactName',None)
        contactNumber = request.form.get('contactNumber',None)
        feature = request.form.get('feature',None)
        other = request.form.get('other',None)
        imgFile1 = request.files.get('imgFile1',None)
        t = time.time()
        imgFile2 = request.files.get('imgFile2',None)
        imgFile3 = request.files.get('imgFile3',None)
        account = request.form.get('account',None)
        url1 =''
        url2 =''
        url3 = ''
        if  imgFile1:
            img_name = str(round(t * 1000000)) + str(account)+'1'+'.jpg'
            url1 = img_url +img_name
            imgFile1.save(url1)
        if  imgFile2:
            img_name = str(round(t * 1000000)) + str(account) + '2'+'.jpg'
            url2 = img_url + img_name
            imgFile2.save(url2)
        if  imgFile3:
            img_name = str(round(t * 1000000)) + str(account) + '3'+'.jpg'
            url3 = img_url + img_name
            imgFile3.save(url3)

        new_publishRelease = publishRelease1(AnimalName,species,AnimalSex,contactName,contactNumber,feature,other,url1,url2,url3,account)
        result = new_publishRelease.publishFind()
        if result=='1':
            return jsonify({'data':'发布成功','code':'200'})
        else:
            return jsonify({'data':'发布失败','code':'208'})
    else:
        return jsonify({'data':'请求失败，此接口支持post','code':'500'})

#获取寻找列表
@app.route('/getPublishReleaseList',methods=['POST','GET'])
def getPublishReleaseList():
    if request.method == 'POST':
        res = publishRelease1.getPublishReleaseList(1)
        if res=='0':
            return  jsonify({'data':'获取失败','code':'208'})
        else:
            data =[]
            for i in res:
                item = {'name':i[1],'imgFile1':i[8],'imgFile2':i[9],'imgFile3':i[10],'species':i[2],'sex':i[3],'feature':i[6],'contactNumber':i[4],
                        'other':i[7],'isSeek':i[13],'isGiveUp':i[14],'seekId':i[0]}
                data.append(item)
            return jsonify({'data':data,'code':200})
    else:
        return jsonify({'data':'请求失败，此接口支持post','code':'500'})
#获取个人寻找列表
@app.route('/getPublishReleaseSelfList',methods=['POST','GET'])
def getPublishReleaseSelfList():
    if request.method == 'POST':
        account = request.form.get('account',None)
        res = publishRelease1.getPublishReleaseSelfList(account)
        if res=='0':
            return  jsonify({'data':'获取失败','code':'208'})
        elif len(res)==0:
            return jsonify({'data':'暂无数据','code':'208'})
        else:
            data =[]
            for i in res:
                item = {'name':i[1],'imgFile1':i[8],'imgFile2':i[9],'imgFile3':i[10],'species':i[2],'sex':i[3],'feature':i[6],'contactNumber':i[4],
                        'other':i[7],'isSeek':i[13],'isGiveUp':i[14],'seekId':i[0]}
                data.append(item)
            return jsonify({'data':data,'code':200})
    else:
        return jsonify({'data':'请求失败，此接口支持post','code':'500'})

@app.route('/isSeek',methods=['POST','GET'])
def isSeek():
    if request.method == 'POST':

        seekId = request.form.get('seekId',None)
        res = publishRelease1.isSeek(seekId)
        if res =='0':
            return   jsonify({'data':'修改失败','code':'208'})
        else:
            return jsonify({'data': '修改成功', 'code': '200'})
    else:
        return  jsonify({'data':'请求失败，此接口支持get','code':'500'})
@app.route('/isGiveUpSeek',methods=['POST','GET'])
def isGiveUpSeek():
    if request.method == 'POST':

        seekId = request.form.get('seekId',None)
        res = publishRelease1.isSeek(seekId)
        if res =='0':
            return   jsonify({'data':'修改失败','code':'208'})
        else:
            return jsonify({'data': '修改成功', 'code': '200'})
    else:
        return jsonify({'data': '请求失败，此接口支持get', 'code': '500'})

from main.publishAdoption import publishAdoption1
@app.route('/publishAdoption',methods=['POST','GET'])
def publishAdoption():
    if request.method == 'POST':
        img_url = 'static/publishAdoption_IMG/'
        t = time.time()
        account = request.form.get('account',None)
        species = request.form.get('species',None)
        sex = request.form.get('sex',None)
        title = request.form.get('title',None)
        age = request.form.get('age',None)
        adoptionName = request.form.get('adoptionName',None)
        adoptionNumber = request.form.get('adoptionNumber',None)
        address = request.form.get('address',None)
        expelling_parasite = request.form.get('expelling_parasite',None)
        rabies = request.form.get('rabies',None)
        ster = request.form.get('ster',None)
        imgFile = request.files.get('imgFile',None)
        other = request.form.get('other',None)
        describe = request.form.get('describe',None)
        url = ''
        if imgFile:
            img_name = str(round(t * 1000000)) + str(account) + '1'+'.jpg'
            url = img_url + img_name
            imgFile.save(url)
        new_publishAdoption = publishAdoption1(account,species,sex,title,age,adoptionName,adoptionNumber,address,expelling_parasite,rabies,ster,url,other,describe)
        result = new_publishAdoption.DAOAdoption()
        if result == '1':
            return jsonify({'data': '发布领养成功', 'code': '200'})
        else:
            return jsonify({'data': '发布领养失败', 'code': '500'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

@app.route('/getAdoptInfo',methods=['POST','GET'])
def getAdoptInfo():
    if request.method == 'POST':
        result = publishAdoption1.getAdoptInfo1(1)
        data =[]
        if result=='0':
            return jsonify({'data': '获取失败', 'code': '208'})
        elif len(result)==0:
            return jsonify({'data':'暂无数据','code':'208'})
        for i in result:
            item={'account':i[1],'imgFile':i[12],'describe':i[14],'name':i[6],'species':i[2],'age':i[4],'sex':i[3],'ster':i[11],'other':i[13],'id':i[0],'isCheck':i[15]}
            data.append(item)
        return jsonify({'data':data,'code':'200'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

from main.adoptApplication import adoptApplication
@app.route('/adoptApplicationForm',methods=['POST','GET'])
def adoptApplicationForm():
    if request.method == 'POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)
        name = request.form.get('name',None)
        age = request.form.get('age',None)
        phone = request.form.get('phone',None)
        address = request.form.get('address',None)
        sex = request.form.get('sex',None)
        house = request.form.get('house',None)
        isMarry = request.form.get('isMarry',None)
        isHaveChild = request.form.get('isHaveChild',None)
        new_adoptApplication = adoptApplication(account,adoptId,name,age,phone,address,sex,house,isMarry,isHaveChild)
        res = new_adoptApplication.DAOadoptApplicationForm()
        if res == '1':
            return jsonify({'data':'申请成功','code':'200'})
        elif res == '2':
            return jsonify({'data': '请勿重复提交', 'code': '208'})
        else:
            return jsonify({'data':'申请失败','code':'208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

@app.route('/getAdoptInfoList',methods=['POST','GET'])
def getAdoptInfoList():
    if request.method == 'POST':
        account = request.form.get('account',None)
        res = adoptApplication.getAdoptInfoList(account)
        data =[]
        if res=='0':
            return jsonify({'data': '申请失败', 'code': '208'})
        elif len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        else:
            for i in res:
                if i[11]=='0':
                    item = {'title':i[16],'imgFile':i[24],'describe':i[26],'name':i[18],'species':i[14],'age':i[17],'sex':i[15],'ster':i[23],'other':i[25],'adoptId':i[2],'isExamine':i[11],'contactNumber':'','id':i[0]}
                    data.append(item)
                else:
                    item = {'imgFile': i[24], 'describe': i[26], 'name': i[18], 'species': i[14], 'age': i[17],
                            'sex': i[15], 'ster': i[23], 'other': i[25], 'adoptId': i[2], 'isExamine': i[11],
                            'contactNumber': i[19],'id':i[0]}
                    data.append(item)
            return jsonify({'data':data,'code':'200'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

@app.route('/deleteAdopt',methods=['POST','GET'])
def deleteAdopt():
    if request.method=='POST':
        adoptId = request.form.get('adoptId',None)
        res = adoptApplication.deleteAdopt(adoptId)
        if res =='1':
            return jsonify({'data': '删除成功', 'code': '200'})
        else:
            return jsonify({'data': '删除失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

@app.route('/getHavePublishList',methods=['POST','GET'])
def getHavePublishList():
    if request.method=='POST':
        account = request.form.get('account',None)
        res = publishAdoption1.getHavePublishList(account)
        data = []
        print(res)
        if len(res) == 0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res != '0':
            for i in res:
                item = {'imgFile': i[0], 'describe': i[1], 'name': i[2], 'species': i[3], 'age': i[4], 'sex': i[5],
                        'ster': i[6], 'other': i[7], 'title': i[8], 'adoptId': i[9], 'adoptTime': i[10]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})

@app.route('/getHaveAdoptList',methods=['POST','GET'])
def getHaveAdoptList():
    if request.method=='POST':
        account = request.form.get('account',None)
        res = publishAdoption1.getHaveAdoptList(account)
        data =[]
        print(res)
        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res !='0':
            for i in res:
                item = {'imgFile':i[0],'describe':i[1],'name':i[2],'species':i[3],'age':i[4],'sex':i[5],'ster':i[6],'other':i[7],'title':i[8],'adoptId':i[9],'adoptTime':i[10]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@app.route('/getSendPeopleInfo',methods=['POST','GET'])
def getSendPeopleInfo():
    if request.method=='POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)
        res = publishAdoption1.getSendPeopleInfo(adoptId)
        data =[]
        print(res)
        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res !='0':
            for i in res:
                item = {'adoptName':i[3],'adoptPhone':i[5],'adoptAccount':i[1]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@app.route('/confirmSendPeople',methods=['POST','GET'])
def confirmSendPeople():
    if request.method=='POST':
        sendPeopleInfoId = request.form.get('sendPeopleInfoId',None)
        adoptId = request.form.get('adoptId',None)
        res = publishAdoption1.confirmSendPeople(adoptId,sendPeopleInfoId)
        if res =='1':
            return jsonify({'data': '提交成功', 'code': '200'})
        else:
            return jsonify({'data': '提交失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@app.route('/getLogList',methods=['POST','GET'])
def getLogList():
    if request.method=='POST':
        adoptId = request.form.get('adoptId',None)
        res = publishAdoption1.getLogList(adoptId)
        data =[]

        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res !='0':
            for i in res:
                item = {'dayLogId':i[1],'content':i[2]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})

@app.route('/saveLogContent',methods=['POST','GET'])
def saveLogContent():
    if request.method=='POST':
        adoptId = request.form.get('adoptId',None)
        dayLogId = request.form.get('dayLogId',None)
        content = request.form.get('content',None)
        res = publishAdoption1.saveLogContent(adoptId,dayLogId,content)


        if res !='0':

            return jsonify({'data': '保存成功', 'code': '200'})

        else:
            return jsonify({'data': '保存失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})


@app.route('/getHaveSendList',methods=['POST','GET'])
def getHaveSendList():
    if request.method=='POST':
        account = request.form.get('account',None)
        res = publishAdoption1.getHaveSendList(account)
        data =[]
        print(res)
        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res !='0':
            for i in res:
                item = {'imgFile':i[0],'describe':i[1],'name':i[2],'species':i[3],'age':i[4],'sex':i[5],'ster':i[6],'other':i[7],'title':i[8],'adoptId':i[9],'adoptTime':i[10]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})

@app.route('/getUserInfo',methods=['POST','GET'])
def getUserInfo():
    if request.method == 'POST':
        account = request.form.get('account',None)
        result = user.user.getUserInfo(account)
        if result == '0':
            return jsonify({'data':'查询失败，无该用户','code':'208'})
        elif result == '1':
            return jsonify({'data':'查询异常','code':'500'})
        else:
            new_user = user.user(result[0][0],result[0][1],result[0][2],result[0][3],result[0][4],result[0][5])
            result_json = new_user.to_json()
            result_json.update({'realName':result[0][6]})     #新增了字段，就直接加了，注册时没有真实姓名字段
            return jsonify({'data':result_json,'code':'200'})
    else:
        return  jsonify({'data': '请求失败，此接口支持get', 'code': '500'})

@app.route('/saveUserInfo',methods=['POST','GET'])
def saveUserInfo():
    if request.method == 'POST':
        account = request.form.get('account',None)
        email = request.form.get('email',None)
        realName = request.form.get('realName',None)
        sex = request.form.get('sex',None)
        birthday = request.form.get('birthday',None)
        result = user.user.saveUserInfo(account,email,realName,sex,birthday)
        return jsonify({'data':result,'code':'200'})
    else:
        return  jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

from main.ReceiveAddress import ReceiveAddress1
@app.route('/getReceiveAddress',methods=['POST','GET'])
def getReceiveAddress():
    if request.method == 'GET':
        account = request.form.get('account',None)
        new_ReceiveAddress = ReceiveAddress1(account)
        result = new_ReceiveAddress.getReceiveAddress()
        if result == '0':
            return jsonify({'data':'查询异常','code':'500'})
        else:
            data = {'account':result[0][0],'receiveUser1':result[0][1],'address1':result[0][2],'phone1':result[0][3],'receiveUser2':result[0][4],'address2':result[0][5],'phone2':result[0][6],'receiveUser1':result[0][7],'address3':result[0][8],'phone3':result[0][9],'default_address':result[0][10]}
            return jsonify({'data':data,'code':'200'})
    else:
        return  jsonify({'data': '请求失败，此接口支持get', 'code': '500'})

@app.route('/saveReceiveAddress',methods=['POST','GET'])
def saveReceiveAddress():
    if request.method == 'POST':
        account = request.form.get('account', None)
        addressId = request.form.get('addressId', None)
        receiveUser = request.form.get('receiveUser', None)
        phone = request.form.get('phone', None)
        address = request.form.get('address', None)
        result = ReceiveAddress1.saveReceiveAddress(account,addressId,receiveUser,phone,address)

        if result == '0':
            return jsonify({'data': '保存失败', 'code': '500'})
        else:

            return jsonify({'data': '保存成功', 'code': '200'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})
from main import goods
@app.route('/getShopList',methods=['POST','GET'])
def getShopList():
    if request.method == 'POST':
        res = goods.goods.getShopList(0)
        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '500'})
        elif res=='0':
            return jsonify({'data': '查询异常', 'code': '500'})
        else:
            data = []
            for i in res:
                item = goods.goods(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                dic_item = item.to_json()
                data.append(dic_item)

            return jsonify({'data': data, 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})
#购物车
@app.route('/addGoodTrolley',methods=['POST','GET'])
def addGoodTrolley():
    if request.method == 'POST':
        account = request.form.get('account', None)
        goodsId = request.form.get('goodsId', None)
        res = goods.goods.addGoodTrolley(account,goodsId)

        if res=='0':
            return jsonify({'data': '添加失败', 'code': '500'})
        else:


            return jsonify({'data': '添加成功', 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})
@app.route('/getTrolleyList',methods=['POST','GET'])
def getTrolleyList():
    if request.method == 'POST':
        account = request.form.get('account', None)
        res = goods.goods.getTrolleyList(account)
        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '500'})
        elif res=='0':
            return jsonify({'data': '查询异常', 'code': '500'})
        else:
            data = []
            for i in res:
                item = {'goodsId':i[0],'img':i[1],'goodsName':i[2],'goodsPrice':i[3],'goodsNum':i[4]}

                data.append(item)
            print(data)
            return jsonify({'data': data, 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

@app.route('/deleteAllGoods',methods=['POST','GET'])
def deleteAllGoods():
    if request.method == 'POST':
        account = request.form.get('account', None)
        res = goods.goods.deleteAllGoods(account)
        if res=='0':
            return jsonify({'data': '删除失败', 'code': '500'})
        else:
            return jsonify({'data':'删除成功', 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

@app.route('/deleteGoods',methods=['POST','GET'])
def deleteGoods():
    if request.method == 'POST':
        account = request.form.get('account', None)
        goodsId = request.form.get('goodsId', None)
        res = goods.goods.deleteGoods(account,goodsId)

        if res=='0':
            return jsonify({'data': '删除失败', 'code': '500'})
        else:

            return jsonify({'data':'删除成功', 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})
#待测试
@app.route('/toPayAccount',methods=['POST','GET'])
def toPayAccount():
    if request.method == 'POST':
        account = request.form.get('account', None)
        address = request.form.get('address', None)
        Goods = request.form.get('goods', None)


        res = goods.goods.toPayAccount(account,address,Goods)

        if res=='0':
            return jsonify({'data': '支付失败', 'code': '500'})
        else:

            return jsonify({'data':'支付成功', 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})
#未完成
@app.route('/getOrderList',methods=['POST','GET'])
def getOrderList():
    if request.method == 'POST':
        account = request.form.get('account', None)
        res = goods.goods.getOrderList(account)
        data = []
        if res=='0':
            return jsonify({'data': '获取失败', 'code': '500'})
        elif len(res[0])=='0':
            return jsonify({'data': '暂无数据', 'code': '500'})
        else:
            print(res)
            for j in range(len(res[0])):
                payid = res[1][j][0]
                order_item = []

                status = res[0][j][0][6]
                print(status)
                for i in range(len(res[0][j])):

                    item = {'orderTime':res[0][j][i][3],'goodsId':res[0][j][i][2],'goodsName':res[0][j][i][0],'goodsPrice':res[0][j][i][1],'goodsNum':res[0][j][i][4]}
                    order_item.append(item)
                data.append({'orderGoods':order_item,'status':status,'orderId':payid})


            return jsonify({'data':data, 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})


@app.route('/confirmDelivery', methods=['POST', 'GET'])
def confirmDelivery():
    if request.method == 'POST':
        account = request.form.get('account', None)
        orderId = request.form.get('orderId', None)
        res = goods.goods.confirmDelivery(account,orderId)
        if res== '0':
            return jsonify({'data': '操作失败', 'code': '500'})
        else:
            return jsonify({'data': '操作成功', 'code': '200'})
    return jsonify({'data': '请求失败，此接口支持post', 'code': '500'})

if __name__ == '__main__':
    app.debug(True)
    app.run(host='0.0.0.0', port=80, debug=True)
