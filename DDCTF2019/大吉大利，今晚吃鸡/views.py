#from: ('117.51.147.155', 52848)
# coding=utf-8

from flask import jsonify, request,redirect
from app import mongodb
from app.unitis.tools import get_md5, num64_to_32
from app.main.db_tools import get_balance, creat_env_db, search_bill, secrity_key, get_bill_id
import uuid
from urllib import unquote

mydb = mongodb.db

flag = '''DDCTF{chiken_dinner_hyMCX[n47Fx)}'''

def register():

    result = []
    user_name = request.args.get('name')
    password = request.args.get('password')

    if not user_name or not password:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        return response
    if not len(password)>=8:
        response = jsonify({"code": 404, "msg": "密码必须大于等于8位", "data": []})
        return response
    else:
        hash_val = get_md5(user_name, 'DDCTF_2019')

        if not mydb.get_collection('account').find_one({'user_name': user_name}):
            mydb.get_collection('account').insert_one({'user_name': user_name, 'password' :password, 'balance': 100,
                                                       'hash_val': hash_val, 'flag': 'test'})
            tmp_result = {'user_name': user_name, 'account': 100}
            result.append(tmp_result)
            response = jsonify({"code": 200, "msg": "用户注册成功", "data": result})
            response.set_cookie('user_name', user_name)
            response.set_cookie('REVEL_SESSION', hash_val)
            response.headers['Server'] = 'Caddy'
            return response
        else:
            response = jsonify({"code": 404, "msg": "用户已存在", "data": []})
            response.set_cookie('user_name', user_name)
            response.set_cookie('REVEL_SESSION', hash_val)
            response.headers['Server'] = 'Caddy'
            return response

def login():

    result = []
    user_name = request.args.get('name')
    password = request.args.get('password')

    if not user_name or not password:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        return response
    if not mydb.get_collection('account').find_one({'user_name': user_name}):
        response = jsonify({"code": 404, "msg": "该用户未注册", "data": result})
        return response
    if not password == mydb.get_collection('account').find_one({'user_name': user_name})['password']:
        response = jsonify({"code": 404, "msg": "密码错误", "data": result})
        return response
    else:
        hash_val = mydb.get_collection('account').find_one({'user_name': user_name})['hash_val']
        response = jsonify({"code": 200, "msg": "登陆成功", "data": result})
        response.set_cookie('user_name', user_name)
        response.set_cookie('REVEL_SESSION', hash_val)
        response.headers['Server'] = 'Caddy'
        return response

def get_user_balance():
    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "您未登陆", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        str_md5 = get_md5(user_name, 'DDCTF_2019')
        if hash_val == str_md5:
            balance = get_balance(user_name)
            bill_id  = get_bill_id(user_name)
            tmp_dic = {'balance': balance , 'bill_id': bill_id}
            result.append(tmp_dic)
            return jsonify({"code": 200, "msg": "查询成功", "data": result})
        else:
            return jsonify({"code": 404, "msg": "参数错误", "data": []})

def buy_ticket():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    ticket_price = int(request.args.get('ticket_price'))
    if not user_name or not hash_val or not ticket_price:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    if ticket_price < 1000:
        response = jsonify({"code": 200, "msg": "ticket门票价格为2000", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    if search_bill(user_name):
        tmp_list = []
        bill_tmp = {'bill_id': search_bill(user_name)}
        tmp_list.append(bill_tmp)
        response = jsonify({"code": 200, "msg": "请支付未完成订单", "data": tmp_list})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        # 生成uuid 保存订单
        hash_id = str(uuid.uuid4())
        tmp_dic = {'user_name': user_name, 'ticket_price': ticket_price, 'bill_id': hash_id}
        mydb.get_collection('bill').insert_one(tmp_dic)
        result.append({'user_name': user_name, 'ticket_price': ticket_price, 'bill_id': hash_id})
        response = jsonify({"code": 200, "msg": "购买门票成功", "data": result})
        response.headers['Server'] = 'Caddy'
        return response

def search_bill_info():
    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "您未登陆", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        str_md5 = get_md5(user_name, 'DDCTF_2019')
        if hash_val == str_md5:
            tmp = mydb.get_collection('bill').find_one({'user_name': user_name})
            if not tmp:
                return jsonify({"code": 200, "msg": "不存在订单", "data": result})
            bill_id = tmp['bill_id']
            user_name =user_name
            bill_price = tmp['ticket_price']
            tmp_dic = {'user_name': user_name, 'bill_id': bill_id, 'bill_price': bill_price}
            result.append(tmp_dic)
            return jsonify({"code": 200, "msg": "查询成功", "data": result})
        else:
            return jsonify({"code": 404, "msg": "参数错误", "data": []})


def recall_bill():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    bill_id = request.args.get('bill_id')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp =mydb.get_collection('bill').find_one({'bill_id': bill_id})
    if not tmp:
        response = jsonify({"code": 404, "msg": "订单号不存在", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    if tmp['user_name'] != user_name:
        response = jsonify({"code": 404, "msg": "订单号不存在", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    else:
        mydb.get_collection('bill').delete_one({'bill_id': bill_id})
        tmp_result = {'user_name': tmp['user_name'], 'bill_id': tmp['bill_id'], 'ticket_price': tmp['ticket_price']}
        result.append(tmp_result)
        response = jsonify({"code": 200, "msg": "订单已取消", "data": result})
        response.headers['Server'] = 'Caddy'
        return response


def pay_ticket():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    bill_id = request.args.get('bill_id')
    if not user_name or not hash_val or not bill_id:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response
    tmp_obj = mydb.get_collection('bill').find_one({'bill_id':bill_id})
    if not tmp_obj:
        response = jsonify({"code": 404, "msg": "订单信息有误", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response
    tmp_price = mydb.get_collection('bill').find_one({'user_name': user_name})['ticket_price']
    tmp_bill_uuid = mydb.get_collection('bill').find_one({'bill_id': bill_id})['bill_id']
    price = num64_to_32(tmp_price)
    tmp_account = mydb.get_collection('account').find_one({'user_name': user_name})['balance']
    if tmp_bill_uuid == bill_id:
        if tmp_account >= price:
            if mydb.get_collection('user_env').find_one({'user_name': user_name}):
                tmp = mydb.get_collection('user_env').find_one({'user_name': user_name})['user_info_list']
                for item in tmp:
                    if item['user_name'] == user_name:
                        result.append(item)
                    else:
                        pass
                    response = jsonify({"code": 200, "msg": "已购买ticket", "data": result})
                    response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
                    response.headers['X-Powered-By'] = ' Servlet/3.0'
                return response
            else:
                account = tmp_account - price
                mydb.get_collection('account').update_one({'user_name': user_name}, {'$set': {'balance': account}},
                                                          upsert=True)
                mydb.get_collection('bill').delete_one({'bill_id': bill_id})
                tmp_info = creat_env_db(user_name)
                mydb.get_collection('user_env').insert_one(tmp_info[0])
                tmp_result = {'your_ticket': tmp_info[1]['hash_val'], 'your_id': tmp_info[1]['id']}
                result.append(tmp_result)
                response = jsonify({"code": 200, "msg": "交易成功", "data": result})
                response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
                response.headers['X-Powered-By'] = ' Servlet/3.0'
                return response
        else:
            response = jsonify({"code": 200, "msg": "余额不足", "data": []})
            response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
            response.headers['X-Powered-By'] = ' Servlet/3.0'
            return response
    else:
        response = jsonify({"code": 200, "msg": "订单信息有误", "data": []})
        response.headers['Pay-Server'] = 'Apache-Coyote/1.1'
        response.headers['X-Powered-By'] = ' Servlet/3.0'
        return response

def is_login():
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    response = jsonify({"code": 200, "msg": "您已登陆", "data": []})
    return response


def search_ticket():
    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数不能为空", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp = mydb.get_collection('user_env').find_one({'user_name': user_name})

    if not tmp:
        response = jsonify({"code": 404, "msg": "你还未获取入场券", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    if tmp:
        tmp_dic = {'ticket': tmp['player_info']['hash_val'], 'id': tmp['player_info']['id']}
        result.append(tmp_dic)
        response = jsonify({"code": 200, "msg": "ticket信息", "data": result})
        response.headers['Server'] = 'Caddy'
        return response


def remove_robot():

    result = []
    sign_str = ''
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')
    a = request.environ['QUERY_STRING']
    params_list = []
    for item in a.split('&'):
        k, v = item.split('=')
        params_list.append((k, v))

    user_id = request.args.get('id')
    ticket = request.args.get('ticket')

    if not user_name or not hash_val or not user_id or not ticket:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    # if not str.isdigit(user_id):
    #     return jsonify({"code": 0, "msg": "参数错误", "data": []})

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response
    find_result = mydb.get_collection('user_env').find_one({'user_name': user_name})
    if not find_result:
        response = jsonify({"code": 404, "msg": "未购买ticket", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    for item in params_list:
        if item[0] == 'ticket':
            params_list.remove(item)
    for item in params_list:
        sign_str = sign_str + unquote(item[0]) + unquote(item[1])
        print sign_str
    sign_str_md5 = get_md5(sign_str, secrity_key)
    print len(secrity_key)
    print sign_str
    print(sign_str_md5)
    print ticket
    if sign_str_md5 != ticket:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    if find_result['player_info']['id'] == int(user_id):
        response = jsonify({"code": 200, "msg": "参数检查正确，但你不能将你自己移除", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp_list = find_result['user_info_list']
    for item in tmp_list:
        if item['id'] == int(user_id):
            rm_robot = {'robot_name': item['user_name'], 'id': item['id'], 'robot_ticket': item['hash_val']}
            result.append(rm_robot)
            tmp_list.remove(item)
    mydb.get_collection('user_env').update_one({'user_name': user_name}, {'$set': {'user_info_list': tmp_list}},
                                               upsert=True)
    response = jsonify({"code": 200, "msg": "移除一个机器人玩家", "data": result})
    response.headers['Server'] = 'Caddy'
    return response


def get_flag():

    result = []
    user_name = request.cookies.get('user_name')
    hash_val = request.cookies.get('REVEL_SESSION')

    if not user_name or not hash_val:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    str_md5 = get_md5(user_name, 'DDCTF_2019')
    if hash_val != str_md5:
        response = jsonify({"code": 404, "msg": "登陆信息有误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp_result = mydb.get_collection('user_env').find_one({'user_name':user_name})

    if not tmp_result:
        response = jsonify({"code": 404, "msg": "参数错误", "data": []})
        response.headers['Server'] = 'Caddy'
        return response

    tmp_list = tmp_result['user_info_list']

    if len(tmp_list) != 1:
        result.append(len(tmp_list))
        response = jsonify({"code": 200, "msg": "还有剩余的机器人未淘汰", "data": result})
        response.headers['Server'] = 'Caddy'
        return response

    if tmp_list[0]['user_name'] == user_name:
        result.append(flag)
        response = jsonify({"code": 200, "msg": "大吉大利，今晚吃鸡", "data": result})
        response.headers['Server'] = 'Caddy'
        return response

