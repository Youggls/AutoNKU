import os
from util import load_data, in_school, out_school


if __name__ == '__main__':
    req_body, req_type = load_data()
    cookie_str = os.environ['PHPSESSID']
    if req_type == 'inschool':
        res = in_school(req_body, cookie_str)
    else:
        res = out_school(req_body, cookie_str)
    if res['status']:
        print(res['msg'])
    else:
        raise Exception(res['msg'])
