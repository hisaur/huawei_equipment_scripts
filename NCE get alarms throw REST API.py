import json
# Нужно установить библиотеку requests и urllib3 через pip
import requests
import urllib3
#Запрос токена для аутентификации
def GetServiceTicket():
    #Это тестовый юзер, он должен быть типа Third party
    payload = {"grantType": "password","userName": "****","value": "****"}
    url = "https://IP:26335/rest/plat/smapp/v1/sessions"
    #verify=False - отключить  проверку сертификата 
    response = requests.put(url,data=json.dumps(payload),headers = {"content-type":"application/json"}, verify=False)
    #Перевод данных из json в формат Python
    response_json=response.json()
    #Вытащить токен из полученных данных
    ticket = response_json ["accessSession"]
    print ('ticket: ', ticket)
    return ticket

def Get_alarms(aTicket):
    #X-Auth-Token это токен из первой функции
    header = {"X-Auth-Token":aTicket,"content-type":"application/json"}
    # url для алармов в докуметации есть все остальные url
    #Через ? ставится параметры (опционально), в документации они описаны
    url= "https://IP:26335/restconf/v1/data/ietf-alarms:alarms/alarm-list?limit=10"
    #verify=False - отключить  проверку сертификата 
    request_alarms = requests.get (url,headers=header,data=None,verify=False)
    #Перевод данных из json в формат Python
    request_alarms_json = request_alarms.json()
    print (request_alarms_json)
    return request_alarms_json
def main():
    # Чтобы отключить проверку на самоподписанный сертификат
    urllib3.disable_warnings() 
    #Запуск запроса на токен
    ticket = GetServiceTicket ()
    #Запуск запроса на аларм
    alarm = Get_alarms(ticket)
main()
