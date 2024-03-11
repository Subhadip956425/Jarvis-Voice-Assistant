import time
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time_str = input("Enter time example:- [10:10]:- ")
    stop_time = datetime.datetime.strptime(stop_time_str, "%H:%M")

    host_path ='C:\\Windows\\System32\\drivers\\etc\\hosts'
    redirect = '127.0.0.1'
    
    print(current_time)
    time.sleep(2)
    website_list = ["www.facebook.com","facebook.com","www.instagram.com", "instagram.com","youtube.com","www.youtube.com"]

    if datetime.datetime.now() < stop_time:
        with open(host_path, "r+") as file:
            content = file.read()
            time.sleep(2)
            for website in website_list:    
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")
                    print("DONE")
                    time.sleep(1)
            print("FOCUS MODE TURNED ON !!!")

    while True:     
        current_time = datetime.datetime.now()
        if current_time >= stop_time:
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)

                file.truncate()

                print("Websites are unblocked !!")
                file = open("focus.txt", "a")
                file.write(f",{stop_time_str}\n")
                file.close()
                break
        time.sleep(60)  # Checking every minute

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

is_admin()
