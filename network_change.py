import subprocess as sp
import time

info = sp.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode(
    'utf-8', errors="backslashreplace").split('\n')
x = [i.split(":")[1] for i in info if "Profile" in i]
sleep = time.sleep(0.15)

for j in x:
    if x == []:
	sleep
        sp.call("cmd /c netsh wlan connect name=network_name_1")
	sleep

    elif 'network_name_1' in str(j.strip()):
	sleep
        sp.call("cmd /c netsh wlan disconnect")
	sleep        
	sp.call("cmd /c netsh wlan show networks")
	sleep
	sp.call("cmd /c netsh wlan connect name=network_name_2")
	sleep

    elif 'network_name_2' in str(j.strip()):
        sleep
	sp.call("cmd /c netsh wlan disconnect")
        sleep
	sp.call("cmd /c netsh wlan show networks")
	sleep        
	sp.call("cmd /c netsh wlan connect name=network_name_1")
	sleep
