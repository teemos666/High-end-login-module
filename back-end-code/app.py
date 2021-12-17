from flask import Flask, render_template, request, url_for, redirect, flash, session
from flask_cors import *
from Fun import Fun
from MyFace import MyFace
import json
import base64
import hashlib
app = Flask(__name__)

fun = Fun()
myface = MyFace()


fuck = "alert('What are you fucking doing?')"

@app.route('/register', methods=['GET', 'POST'])
@cross_origin()
def register():
    if request.method == 'POST':
        stunum = request.form.get('stunum')
        stuphone = request.form.get('stuphone')
        stuemail = request.form.get('stuemail')
        stupwd = request.form.get('stupwd')
        stuface = request.form.get('stuface')
        print(request.form)
        face_data = stuface.replace('data:image/png;base64,', '')
        face_data = base64.b64decode(face_data)
        face_data = base64.b64encode(face_data).decode()

        if stuface != '':

            if myface.face_is_exist(face_data):
                cmd = "alert('这张脸已经绑定过了哦~~~')"
                return cmd

        if fun.judge_user(stuphone) == 0 or fun.judge_user(stuemail) == 0:
            cmd = "alert('错误的邮箱或手机号！')"
            return cmd
        if fun.select_user(stuemail, 1) or fun.select_user(stuphone, 2) or fun.select_user(stunum, 3):
            cmd = "alert('用户已存在？？？')"
        else:
            if stuface !='':
                if not myface.face_register(stunum, face_data):
                    return "alert('未知原因，注册失败')"

            pwd_md5 = hashlib.md5(stupwd.encode()).hexdigest()
            fun.insert(stunum, stuphone, stuemail, pwd_md5)

            cmd = '''
                alert('注册成功！！！');
                location.href = "login.html";
            '''
        # location.href = 'http://127.0.0.1:8080/ayUser/login';
        return cmd
    return fuck

@app.route('/send_code', methods=['GET', 'POST'])
@cross_origin()
def send_code():
    if request.method == 'POST':
        user = request.form.get('user')
        sign = fun.judge_user(user)
        if fun.select_user(user, sign):
            fun.send_code(user, sign)
            cmd = "alert('验证码发送成功')"
            return cmd
        else:
            cmd = "alert('未找到该用户哦~~~')"
            return cmd
    return fuck

@app.route('/find_pwd', methods=['GET', 'POST'])
@cross_origin()
def find_pwd():
    if request.method == 'POST':
        user = request.form.get('user')
        ver_code = request.form.get('ver_code')
        stupwd = request.form.get('stupwd')
        stupwd2 = request.form.get('stupwd2')
        if stupwd != stupwd2:
            return "alert('两次密码输入不一样哦~~~~~~~')"

        cmd = "alert('密码重置失败！！！？？？')"
        sign = fun.judge_user(user)
        if sign == 0:
            return cmd
        if fun.verify_code(user, ver_code, sign) == 'ok':
            pwd_md5 = hashlib.md5(stupwd2.encode()).hexdigest()
            fun.change_pwd(user, pwd_md5, 1)
            cmd = "alert('密码重置成功！！！')"
            cmd ='''
                alert('密码重置成功！！！');
                location.href = "login.html";
            '''
        else:
            cmd = "alert('验证码错误？？？')"
        return cmd
    return fuck

@app.route('/pwd_login', methods=['GET', 'POST'])
@cross_origin()
def pwd_login():
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        print(request.form)
        cmd = "alert('登录失败！！！？？？')"
        pwd_md5 = hashlib.md5(pwd.encode()).hexdigest()
        if fun.select_pwd(user, pwd_md5):
            cmd = "alert('登录成功！！！')"
            cmd = f'''
                alert('登录成功！！！');
                document.cookie = "user=" + "{user}";
                location.href = "index.html";
            '''
        return cmd
    return fuck

@app.route('/code_login', methods=['GET', 'POST'])
@cross_origin()
def code_login():
    if request.method == 'POST':
        user = request.form.get('user')
        ver_code = request.form.get('ver_code')
        print(request.form)
        cmd = "alert('登录失败！！！？？？')"
        sign = fun.judge_user(user)
        if sign == 0:
            return cmd
        if fun.verify_code(user, ver_code, sign) == 'ok':
            cmd = "alert('登录成功！！！')"
            cmd = f'''
                alert('登录成功！！！');
                document.cookie = "user={user}";
                location.href = "index.html";
            '''

        else:
            cmd = "alert('验证码错误？？？')"
        return cmd
    return fuck

@app.route('/face_login', methods=['GET', 'POST'])
@cross_origin()
def face_login():
    if request.method == 'POST':
        face = request.form.get('face')
        print(request.form)
        face_data = face.replace('data:image/png;base64,', '')
        # face_data = face
        face_data = base64.b64decode(face_data)
        face_data = base64.b64encode(face_data).decode()
        # with open("face.png", "wb") as f:  # 转为二进制格式
        #     f.write(face_data)
        cmd = "alert('登录成功！！！')"
        cmd = f'''
            alert('登录成功！！！');
            document.cookie = "user=" + "000";
            location.href = "index.html";
        '''
        if myface.face_is_exist(face_data):
            return cmd

    return fuck

@app.route('/test', methods=['GET', 'POST'])
@cross_origin()
def test():
    s = 'chrome://flags/#unsafely-treat-insecure-origin-as-secure'
    return s

if __name__ == '__main__':
    app.run(host='0.0.0.0')