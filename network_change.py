import subprocess as sp
import time

data = sp.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode(
    'utf-8', errors="backslashreplace").split('\n')

x = [i.split(":")[1] for i in data if "Profile" in i]


def connected(channel: str) -> str:
    connection = sp.check_output(
        ["cmd", "/c", "netsh", "wlan", "connect", "name={}".format(channel)]).decode('utf-8', errors="backslashreplace").split('\n')

    if 'is not available to connect' in connection:
        sp.call("netsh wlan show interfaces")
        time.sleep(0.1)
        connected(channel)

    else:
        sp.call("cmd /c exit")


for j in x:
    if x == []:
        connected('Network_Channel_1')

    elif 'Network_Channel_1' in str(j.strip()):
        connected('Network_Channel_2')

    elif 'Network_Channel_2' in str(j.strip()):
        connected('Network_Channel_1')
