import requests
import json
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class MySMS(object):
    def __init__(self):
        self.apiUrl = 'https://sms_developer.zhenzikj.com'
        self.appId = '您寄几的'
        self.appSecret = '您寄几的'

    def send_phone_code(self, num, code):
        data = {}
        data['number'] = num;
        data['templateParams'] = [code, '5分钟'];
        data['templateId'] = '7144';
        data['appId'] = self.appId;
        data['appSecret'] = self.appSecret;
        if ('templateParams' in data) :
            data['templateParams'] = json.dumps(data['templateParams']);
        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning);
        response = requests.post(self.apiUrl+'/sms/v2/send.do', data=data, verify=False);
        result = str(response.content,'utf-8');
        return result;


    def balance(self):
        data = {
            'appId': self.appId,
            'appSecret': self.appSecret
        }
        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning);
        response = requests.post(self.apiUrl+'/account/balance.do', data=data, verify=False);
        result = str(response.content,'utf-8');
        return result;

    def findSmsByMessageId(self, messageId):
        data = {
            'appId': self.appId,
            'appSecret': self.appSecret,
            'messageId': messageId
        }
        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning);
        response = requests.post(self.apiUrl+'/smslog/findSmsByMessageId.do', data=data, verify=False);
        result = str(response.content,'utf-8');
        return result;


if __name__ == '__main__':

    a = MySMS()

    print(a.send_phone_code('15816633259', '2222'));
