import subprocess


def get_wifi_password():
    a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split("\n")
    a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
    wifi_name = []
    wifi_password = []
    for i in a:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            "\n")
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        wifi_name.append(i)
        wifi_password.append(results[0])
        
    return dict(zip(wifi_name, wifi_password))


print(get_wifi_password())
