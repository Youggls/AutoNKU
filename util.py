import os
import time
import json
import requests


def load_data():
    with open('./data.json', mode='r', encoding='UTF-8') as f:
        data = json.load(f)
    if data['type'] == 'inschool':
        req_body = data['in-school-body']
    else:
        req_body = data['out-school-body']
    for key in req_body['data']:
        if req_body['data'][key] is None:
            req_body['data'][key] = os.environ[key]
    return req_body, data['type']


def check_res(res):
    if res['code'] == '010':
        return {
            'status': False,
            'msg': 'Cookie 过期，请重新获取'
        }
    elif res['code'] == '001':
        return {
            'status': True,
            'msg': '上传成功'
        }
    else:
        return {
            'status': True,
            'msg': '已提交过'
        }


def in_school(req_body, cookie_str):
    base_url = 'https://jkcj.nankai.edu.cn/healthgather/Inschool/addInschoolGather?time={}'
    header = {
        'sec-ch-ua': '"" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98""',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://jkcj.nankai.edu.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://jkcj.nankai.edu.cn/mobile/register/inschool.html?time=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'ContentType': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    cookie = {
        'PHPSESSID': cookie_str
    }

    current_time = int(time.time()) * 1000
    pre_time = (current_time - 5000) / 1000
    header['Referer'] += str(pre_time)
    base_url = base_url.format(current_time)

    res_obj = requests.post(base_url, headers=header, cookies=cookie, data=req_body).json()
    return check_res(res_obj)


def out_school(req_body, cookie_str):
    base_url = 'https://jkcj.nankai.edu.cn/mobile/register/index.html?time={}'
    header = {
        'sec-ch-ua': '"" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98""',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://jkcj.nankai.edu.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://jkcj.nankai.edu.cn/mobile/register/index.html?time=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'ContentType': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Host': 'jkcj.nankai.edu.cn',
    }
    cookie = {
        'PHPSESSID': cookie_str,
    }

    current_time = int(time.time()) * 1000
    pre_time = (current_time - 5000) / 1000
    header['Referer'] += str(pre_time)
    base_url = base_url.format(current_time)
    res_obj = requests.post(base_url, headers=header, cookies=cookie, data=req_body)
    return check_res(res_obj.json())
