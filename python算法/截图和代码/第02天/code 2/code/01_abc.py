import responses
import json
class yunpian(object):


    def __init__(self,apikey):
        self.apikey = apikey
        self.url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, code, mobile):
        parmas = {
            "apikey":self.apikey,
            "mobile":mobile,
            "text":"【云片网】您的验证码是{code}".format(code= code)
        }

        response = responses.post(self.url, data=parmas)
        re_dict = json.loads(response)


if __name__ == '__mian__':
    yunpian_send = yunpian('d80c0a5d0b02a5736e1e5db40b93e0e0')
    yunpian_send.send_message(code, mobile).format(code=1352, mobile = '13279436448')