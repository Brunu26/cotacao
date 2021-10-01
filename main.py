#import json
import requests

req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")


cotacao = req.json()



print("------ Cotação do Bitcoin ---------")
print('Moeda: ' +cotacao['BTCBRL']['name'])
print('Data: ' +cotacao['BTCBRL']['create_date'])
print('Valor atual: R$ ' +cotacao['BTCBRL']['bid'])
print('************************')
print("------ Cotação do Dolar ---------")
print('Moeda: ' +cotacao['USDBRL']['name'])
print('Data: ' +cotacao['USDBRL']['create_date'])
print('Valor atual: R$ ' +cotacao['USDBRL']['bid'])
print('************************')
print("------ Cotação do Euro ---------")
print('Moeda: ' +cotacao['EURBRL']['name'])
print('Data: ' +cotacao['EURBRL']['create_date'])
print('Valor atual: R$ ' +cotacao['EURBRL']['bid'])
