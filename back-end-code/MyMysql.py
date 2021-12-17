import pymysql

class MyMysql():
    def __init__(self):
        super().__init__()
        self.host = '192.168.160.131'
        self.user = 'root'
        self.pwd = '123456'
        self.db = 'test'

    def judge_user_type(self, sign):
        word = '???'
        if sign == 1:
            word = 'stuemail'
        elif sign == 2:
            word = 'stuphone'
        elif sign == 3:
            word = 'stunum'
        return word


    def insert(self, stunum, stuphone, stuemail, stupwd):
        conn = pymysql.Connect(host=self.host, port=3306, user=self.user, passwd=self.pwd, db=self.db, charset='utf8')
        cur = conn.cursor()
        sql = 'insert into wluser (stunum,stuphone,stuemail,stupwd) values("%s","%s","%s","%s");'\
              % (stunum, stuphone, stuemail, stupwd)
        try:
            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库执行
            conn.commit()
            print('插入成功')
        except:
            # 如果发生错误则回滚
            conn.rollback()
            print('插入失败')
        finally:
            cur.close()
            conn.close()

    def select_user(self, user, sign):
        '''
        :param user: 邮箱或手机号
        :param sign: 1为邮箱，2为手机号，3为学号
        :return:
        '''
        conn = pymysql.Connect(host=self.host, port=3306, user=self.user, passwd=self.pwd, db=self.db, charset='utf8')
        cur = conn.cursor()
        word = self.judge_user_type(sign)
        sql1 = f'select {word} from wluser where {word} = "{user}";'
        try:
            # 执行sql语句
            cur.execute(sql1)
            data = cur.fetchone()
            if data !=None:
                return True
            else:
                return False
        except:
            # 如果发生错误则回滚
            conn.rollback()
            print('未找到用户')
            return False
        finally:
            cur.close()
            conn.close()

    def select_pwd(self, user, pwd):
        # 登录
        conn = pymysql.Connect(host=self.host, port=3306, user=self.user, passwd=self.pwd, db=self.db, charset='utf8')
        cur = conn.cursor()
        sql1 = f'select * from wluser where stunum = "{user}" and stupwd = "{pwd}";'
        sql2 = f'select * from wluser where stuemail = "{user}" and stupwd = "{pwd}";'
        sql3 = f'select * from wluser where stuphone = "{user}" and stupwd = "{pwd}";'

        try:
            # 执行sql语句
            cur.execute(sql1)
            data1 = cur.fetchone()
            cur.execute(sql2)
            data2 = cur.fetchone()
            cur.execute(sql3)
            data3 = cur.fetchone()
            if data1 != None or data2 != None or data3 != None:
                return True
            else:
                return False
        except:
            # 如果发生错误则回滚
            conn.rollback()
            print('未找到用户')
            return False
        finally:
            cur.close()
            conn.close()



    def change_pwd(self, user, pwd, sign):
        '''
        :param user: 邮箱或手机号
        :param pwd:密码
        :param sign:1为邮箱，2为手机号
        :return:
        '''
        conn = pymysql.Connect(host=self.host, port=3306, user=self.user, passwd=self.pwd, db=self.db, charset='utf8')
        cur = conn.cursor()
        word = self.judge_user_type(sign)
        sql2 = f'update wluser set stupwd = "{pwd}" where {word} = "{user}";'

        try:
            # 执行sql语句
            if self.select_user(user, sign) == True:
                cur.execute(sql2)
                # 提交到数据库执行
                conn.commit()
                print(f'用户：{user}的密码修改为{pwd}')
            else:
                print('修改失败，未找到用户')
        except:
            # 如果发生错误则回滚
            conn.rollback()
            print('修改失败')
        finally:
            cur.close()
            conn.close()

    def set_code(self, user, code, time, flag, sign):
        conn = pymysql.Connect(host=self.host, port=3306, user=self.user, passwd=self.pwd, db=self.db, charset='utf8')
        cur = conn.cursor()
        word = self.judge_user_type(sign)
        sql1 = f'update wluser set stucode = "{code}" where {word} = "{user}";'
        sql2 = f'update wluser set stucode_time = "{time}" where {word} = "{user}";'
        sql3 = f'update wluser set stucode_flag = "{flag}" where {word} = "{user}";'
        try:
            # 执行sql语句
            cur.execute(sql1)
            cur.execute(sql2)
            cur.execute(sql3)
            # 提交到数据库执行
            conn.commit()
            print(f'用户：{user}的验证码更新为{code}')
        except:
            # 如果发生错误则回滚
            conn.rollback()
            print('更新失败')
        finally:
            cur.close()
            conn.close()

    def select_code(self, user, code, sign):
        conn = pymysql.Connect(host=self.host, port=3306, user=self.user, passwd=self.pwd, db=self.db, charset='utf8')
        cur = conn.cursor()
        word = self.judge_user_type(sign)
        sql1 = f'select stucode from wluser where {word} = "{user}";'
        sql2 = f'select stucode_time from wluser where {word} = "{user}";'
        sql3 = f'select stucode_flag from wluser where {word} = "{user}";'
        try:
            # 执行sql语句
            cur.execute(sql1)
            code = cur.fetchone()
            cur.execute(sql2)
            time = cur.fetchone()
            cur.execute(sql3)
            flag = cur.fetchone()
            return code[0], time[0], flag[0]
        except:
            # 如果发生错误则回滚
            conn.rollback()
            print('未找到用户')
            return False
        finally:
            cur.close()
            conn.close()

if __name__ == '__main__':
    m = MyMysql()
    stunum = '111'
    stupwd = '222'
    stuphone = '333'
    stuemail ='444'
    # m.insert(stunum, stuphone, stuemail, stupwd)
    # m.change_pwd('3334','pwdpwdpwd',2)
    m.select_user('zzxxccsung@qq.com',1)