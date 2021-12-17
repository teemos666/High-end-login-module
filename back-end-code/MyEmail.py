import time
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

from random import Random



class MyEmail():
    def __init__(self):
        '''
        :param mail_sender: 发送人邮箱
        :param mail_receivers: 收件人邮箱
        '''
        super().__init__()
        self.mail_host = "smtp.qq.com"
        self.mail_sender = "您寄几的@qq.com"
        self.mail_license = "您寄几的"        # 邮箱授权码
        self.mail_receivers = ''
        self.mm = MIMEMultipart('related')

    def send_email(self, title_content, body_content, mail_receivers):
        '''
        :param title_content: 邮件标题
        :param body_content: 邮件内容
        :return:
        '''
        self.mail_receivers = mail_receivers
        # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
        self.mm = MIMEText(body_content, "plain", "utf-8")

        # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
        self.mm["From"] = "Teemos<" + self.mail_sender + ">"
        # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
        self.mm["To"] = "<" + self.mail_receivers + ">"
        self.mm["Subject"] = Header(title_content, 'utf-8')
        # 向MIMEMultipart对象中添加文本对象
        #self.mm.attach(message_text)
        # ----------------------------------
        # 创建SMTP对象
        stp = smtplib.SMTP()
        # 设置发件人邮箱的域名和端口，端口地址为25
        stp.connect(self.mail_host, 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        # stp.set_debuglevel(1)
        # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
        stp.login(self.mail_sender, self.mail_license)
        # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
        # stp.sendmail(self.mail_sender, self.mail_receivers, self.mm.as_string())
        stp.sendmail(self.mail_sender, self.mail_receivers, self.mm.as_string())
        print("邮件发送成功:", self.mail_receivers)
        # 关闭SMTP对象
        stp.quit()
        stp.close()

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

    def send_email_code(self, mail_receivers, code):
        try:
            self.ver_code = self.random_str()
            self.ver_time = int(time.time())
            self.ver_sign = 1
            self.ver_user = mail_receivers
            title_content = '高端验证码'
            body_content = '这位同志，您的验证码为：' + code + '，有效时间为5分钟。'
            self.send_email(title_content, body_content ,mail_receivers)
        except:
            print('验证码发送失败，请重试')




if __name__ == '__main__':


    mail_sender = '3238859569@qq.com'
    mail_receivers = 'zzxxccsung@qq.com'



    title_content = 'titile_good'
    body_content = 'fajsdasdsjadsadasdasdsadsadasdasdasd'
    # e.send(title_content, body_content)
    # e.send_code()
    for i in range(10):
        try:
            e = MyEmail()
            e.send('19网络工程3班庄俊雄1914080903335', '19网络工程3班庄俊雄1914080903335', 'webyykf@126.com')
        except:
            print('error')