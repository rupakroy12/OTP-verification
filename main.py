import requests
import json
import random as r


def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulk"
    params = {
        'authorization': '8iQnCNvMcg69lHoyYfK2arVmOGUBtkAzjLRqPThd70W3bsuDXeUvWTbntzmrO5ARKHVcoQGZDLa49PFp',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }

    response = requests.get(url, params=params)

    dict = response.json()
    print(dict)
    return dict.get('return')


def otpgen():
    otp = ""
    for i in range(4):
        otp += str(r.randint(1, 9))
    # print("Your One Time Password is " + otp)
    return otp


if __name__ == '__main__':
    otp = int(otpgen())
    message = 'Your One time Password is ' + str(otp)
    number = '9051631521'

    send_sms(number, message)

    
    #verify otp
    n = int(input("Enter OTP : "))
    if n == int(otp):
        print("OTP Verification Successful.")
    else:
        print("Wrong OTP !")
