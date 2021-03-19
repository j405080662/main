
from flask import Blueprint
from main import manage
simple = Blueprint('simple',__name__,template_folder='templates')
from flask import Flask,request,json,session,render_template,jsonify
@simple.route('/getManageAdoption',methods=['POST','GET'])
def getManageAdoption():
    if request.method=='POST':
        account = request.form.get('account',None)
        res = manage.manageDAO.getManageAdoption(account)
        data =[]
        print(res)
        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res !='0':
            for i in res:
                item = {'adoptId':i[0],'sendName':i[1],'sendAccount':i[2],'species':i[3],'status':i[4]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/deleteManageAdoption',methods=['POST','GET'])
def deleteManageAdoption():
    if request.method=='POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)

        res = manage.manageDAO.deleteManageAdoption(adoptId)
        if res =='1':

            return jsonify({'data': '删除成功', 'code': '200'})

        else:
            return jsonify({'data': '删除失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/getManageSeek',methods=['POST','GET'])
def getManageSeek():
    if request.method=='POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)

        res = manage.manageDAO.getManageSeek(adoptId)
        data = []
        print(res)
        if len(res) == 0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res != '0':
            for i in res:
                item = {'seekId': i[0], 'seekName': i[1], 'seekAccount': i[2], 'species': i[3], 'status': i[4]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/deleteManageSeek',methods=['POST','GET'])
def deleteManageSeek():
    if request.method=='POST':
        account = request.form.get('account',None)
        seekId = request.form.get('seekId',None)

        res = manage.manageDAO.deleteManageSeek(seekId)
        if res =='1':

            return jsonify({'data': '删除成功', 'code': '200'})

        else:
            return jsonify({'data': '删除失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/getShipments',methods=['POST','GET'])
def getShipments():
    if request.method=='POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)

        res = manage.manageDAO.getShipments(adoptId)
        data = []

        if len(res) == 0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res != '0':
            for i in res:
                item = {'orderId': i[0], 'userAccount': i[1], 'orderAddress': i[2], 'orderInfo': i[4], 'isDeliver': i[3]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/deleteOrder',methods=['POST','GET'])
def deleteOrder():
    if request.method=='POST':
        account = request.form.get('account',None)
        orderId = request.form.get('orderId',None)

        res = manage.manageDAO.deleteOrder(orderId)
        if res =='1':

            return jsonify({'data': '删除成功', 'code': '200'})

        else:
            return jsonify({'data': '删除失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/adoptManageIncome',methods=['POST','GET'])
def adoptManageIncome():
    if request.method=='POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)

        res = manage.manageDAO.adoptManageIncome(adoptId)
        data = []

        if len(res) == 0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res != '0':
            for i in res:
                item = {'orderId': i[0], 'userAccount': i[1], 'orderInfo': i[2], 'income': i[3]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})

@simple.route('/getCheckList',methods=['POST','GET'])
def getCheckList():
    if request.method=='POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)

        res = manage.manageDAO.getCheckList(adoptId)
        data = []

        if res == '2':
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res != '0':
            for i in res[0]:
                item = {'applyId': i[0], 'adoptionName': i[1], 'applyUserAccount': i[2], 'applyUserName': i[3],'applyType':'领养'}
                data.append(item)
            for i in res[1]:
                item = {'applyId': i[0], 'adoptionName': i[1], 'applyUserAccount': i[2], 'applyUserName': i[3],'applyType':'寻回'}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/getManageUsers',methods=['POST','GET'])
def getManageUsers():
    if request.method=='POST':
        res = manage.manageDAO.getManageUsers(1)
        data = []
        if len(res)==0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res != '0':
            for i in res:
                item = {'adoptId': i[0], 'adoptTime': i[1], 'userAccount': i[2], 'userName': i[3]}
                data.append(item)

            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})
@simple.route('/checkAdoptLog',methods=['POST','GET'])
def checkAdoptLog():
    if request.method=='POST':
        account = request.form.get('account',None)
        adoptId = request.form.get('adoptId',None)
        res = manage.manageDAO.checkAdoptLog(adoptId)
        data = []
        if len(res) == 0:
            return jsonify({'data': '暂无数据', 'code': '208'})
        elif res != '0':
            for i in res:
                item = {'dayLogId': i[0], 'content': i[1]}
                data.append(item)
            return jsonify({'data': data, 'code': '200'})

        else:
            return jsonify({'data': '查询失败', 'code': '208'})
    else:
        return jsonify({'data': '请求失败，此接口支持post', 'code': '208'})