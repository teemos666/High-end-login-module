from random import Random
import re
import time

from MyEmail import MyEmail
from MyMysql import MyMysql
from MySMS import MySMS
from MyFace import MyFace

class Fun(MyEmail, MyMysql, MySMS):
    def __init__(self):
        super().__init__()
    def judge_user(self, user):
        '''
        :param user: 1为邮箱，2为手机号
        :return:
        '''
        j_phone = '^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
        j_email = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'

        searchObj = re.search(j_email, user, re.M | re.I)
        if searchObj:
            # print('邮箱为：',searchObj.group())
            return 1
        searchObj = re.search(j_phone, user, re.M | re.I)
        if searchObj:
            # print('手机为：', searchObj.group())
            return 2
        print('错误的手机号或邮箱格式')
        return 0
    def random_str(self, randomlength=6):
        """
        随机字符串
        :param randomlength: 字符串长度
        :return: String 类型字符串
        """
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        chars = '0123456789'

        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str += chars[random.randint(0, length)]
        return str
    def send_code(self, user, sign):
        ver_code = self.random_str()
        ver_time = int(time.time())
        ver_flag = 1
        if sign == 1:
            self.send_email_code(user, ver_code)
        elif sign ==2 :
            self.send_phone_code(user, ver_code)
        self.set_code(user, ver_code, ver_time, ver_flag, sign)
        print('发送成功')

    def verify_code(self, user, code, sign):
        data_code , data_time, data_flag = self.select_code(user, code, sign)
        t = int(time.time())
        time_diff = t - int(data_time)

        if data_flag == '0' or time_diff > 5*60:
            return 'overtime'
        if code != data_code:
            print('???')
            return 'error'
        self.set_code(user, data_code, data_time, '0', sign)
        return 'ok'

if __name__ == '__main__':

    a = Fun()
    sign = a.judge_user('zzxxccsung@qq.com')
    print(sign)

