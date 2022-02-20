import os
from util import load_data, in_school


if __name__ == '__main__':
    req_body, req_type = load_data()
    cookie_str = os.environ['PHPSESSID']
    if req_type == 'inschool':
        res = in_school(req_body, cookie_str)
    else:
        # TODO: 非在校生未开发
        res = {
            'status': False,
            'msg': '请求类型错误'
        }
    if res['status']:
        print(res['msg'])
    else:
        raise Exception(res['msg'])
