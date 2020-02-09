import subprocess as sp

info = sp.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode(
    'utf-8', errors="backslashreplace").split('\n')
x = [i.split(":")[1] for i in info if "Profile" in i]

for j in x:
    if 'network_name_1' in str(j.strip()):
        sp.call("netsh wlan disconnect")
        sp.call("netsh wlan show networks")
        sp.call("netsh wlan connect name=network_name_2")

    elif 'network_name_2' in str(j.strip()):
        sp.call("netsh wlan disconnect")
        sp.call("netsh wlan show networks")
        sp.call("netsh wlan connect name=network_name_1")

