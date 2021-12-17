from aip import AipFace
import base64

class MyFace():
    def __init__(self):

        self.APP_ID = '您寄几的'
        self.API_KEY = '您寄几的'
        self.SECRET_KEY = '您寄几的'
        self.client = AipFace(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def face_auth(self, userid, face_data):
        # 单个用户人脸认证
        image = face_data
        imageType = "BASE64"
        groupIdList = "high_end"
        options = {}
        options["user_id"] = userid
        """ 调用人脸搜索 """
        u = self.client.search(image, imageType, groupIdList, options);
        r_succ = u['error_msg']
        if r_succ =='SUCCESS':
            r_score = u['result']['user_list'][0]['score']
            print(r_score)
            if r_score >= 80:
                return True
        return False
    def face_is_exist(self, face_data):

        image = face_data
        # with open("face.png", "rb") as f:  # 转为二进制格式
        #     base64_data = base64.b64encode(f.read()).decode()  # 使用base64进行加密
        # image = base64_data
        imageType = "BASE64"
        groupIdList = "high_end"
        """ 调用人脸搜索 """
        u = self.client.search(image, imageType, groupIdList);
        r_succ = u['error_msg']
        if r_succ == 'SUCCESS':
            r_score = u['result']['user_list'][0]['score']
            print(r_score)
            if r_score >= 80:
                return True
        return False


    def face_register(self, userid, face_data):
        image = face_data
        imageType = "BASE64"
        groupId = "high_end"
        userId = userid

        if self.face_is_exist(face_data):
            return False
        """ 调用人脸注册 """
        u = self.client.addUser(image, imageType, groupId, userId)
        r_succ = u['error_msg']
        if r_succ == 'SUCCESS':
            #写数据
            return True
        else:
            return False

if __name__ == '__main__':
    a = MyFace()
    with open("yuan.jpg", "rb") as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read()).decode()  # 使用base64进行加密
    image = base64_data
    a.face_is_exist(image)