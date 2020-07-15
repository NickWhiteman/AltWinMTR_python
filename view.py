import os

ip = ('8.8.8.8')
m = '-t'

def networkIp (ip, m):
   return os.system('ping {1} {0} '.format(ip,m))


def networkTelnet():
   return os.system('telnet ya.ru') 
   # не работает. Нет такой функции. Нужно найти решение.


def networktracert():
   return os.system('tracert ' + ip)

networkIp(ip,m)