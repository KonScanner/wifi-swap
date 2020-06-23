import subprocess as sp
import time
import platform

platform = platform.uname().system

# Configurables
channel_1, channel_2 = 'Network_Channel_1', 'Network_Channel_2'


if platform == 'Windows':
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

        elif 'request was completed successfully' in connection:
            print('You are already connected to the network.')

        elif 'There is no profile' in connection:
            print('The network you are trying to connect to is not in the list of saved network profiles on your machine.')

        else:
            sp.call("cmd /c exit")

    for j in x:
        if x == []:
            connected(channel_1)

        elif channel_1 in str(j.strip()):
            connected(channel_2)

        elif channel_2 in str(j.strip()):
            connected(channel_1)

else:
    print('Linux Implementation coming soon')
