import os
import telnetlib
import subprocess

ip = ('8.8.8.8')
m = '-t'


def networkIp(ip, m):
    return os.system('ping {1} {0} '.format(ip, m))


def networkTelnet():
    return telnetlib.Telnet('192.268.0.1')
    # не работает. Нет такой функции. Нужно найти решение. либо найти модуль уже работющий либо работать с telnetlib


def networktracert():
    return os.system('tracert ' + ip)


def networkPATHPING(ip):
    return os.system('PATHPING ' + ip)


# networkPATHPING(ip)
def newtworkTestPing():
    result = subprocess.run(['ping', ip],
                            stderr=subprocess.PIPE)  # stderr - Выводит динамически потоком. stdout - стразу пакетом
    return result.stderr.decode('utf-8')
    # Здесь нужно реализовать перехват строчек и их анализ для счетчика. Либо уже в другой функции анализа.


newtworkTestPing()