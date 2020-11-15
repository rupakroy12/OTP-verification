import requests
import json
import random as r


def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulk"
    params = {
        'authorization': 'your api key goes here',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }

    response = requests.get(url, params=params)

    dict = response.json()
    
    return dict

def otpgen():
    otp = ""
    for i in range(4):
        otp += str(r.randint(1, 9))
    return otp


if __name__ == '__main__':
    otp = int(otpgen())
    message = 'Your One time Password is ' + str(otp)
    number = 'your number goes here (for multiple numbers,separate using commas)'

    status = send_sms(number, message)

    if dict.get('return') is False:
        print("Sorry, Otp could not be sent ! ")
        
        print(f'Message : {dict.get("message")}')
    
    else:
        print("Otp sent successfully")
        #verify otp
        n = int(input("Enter OTP : "))
        if n == int(otp):
            print("OTP Verification Successful.")
        else:
            print("Wrong OTP !")
