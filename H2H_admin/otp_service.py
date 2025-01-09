from django.conf import settings
from random import randint
import http.client
import json


class SendOtp:
    def __init__(self, key=None, temp_id=None, msg=None):
        self.baseUrl = settings.MSG91_BASE_URL
        self.authkey = key or settings.MSG91_AUTH_KEY
        self.temp_id = temp_id or settings.MSG91_TEMPLATE_ID
        self.msg = msg or "Your OTP is {{otp}}. Please do not share it with anybody."
    def generateOtp(self):
        return randint(1000, 9999)
    def send_otp_via_msg91(self, phone_number, otp):
        payload = json.dumps({"template_id": self.temp_id,"mobile": f"91{phone_number}","authkey": self.authkey,"otp": otp,"otp_expiry": "5"})
        headers = {'Content-Type': "application/JSON"}
        try:
            conn = http.client.HTTPSConnection("control.msg91.com")
            conn.request("POST", "/api/v5/otp", payload, headers)
            res = conn.getresponse()
            data = res.read()
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            return {"error": str(e)}

    def verify_otp_via_msg91(self, phone_number, otp):
        headers = {'Content-Type': "application/JSON"}
        try:
            conn = http.client.HTTPSConnection("control.msg91.com")
            conn.request("GET",f"/api/v5/otp/verify?mobile=91{phone_number}&otp={otp}&authkey={self.authkey}",headers=headers)
            res = conn.getresponse()
            data = res.read()
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            return {"error": str(e)}