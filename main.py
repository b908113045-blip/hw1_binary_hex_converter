import tkinter as tk
from tkinter import messagebox

HEX_DIGITS = "0123456789ABCDEF"


def is_binary(s):
    if s == "":
        return False
    for ch in s:
        if ch not in "01":
            return False
    return True


def is_decimal(s):
    if s == "":
        return False
    for ch in s:
        if ch < "0" or ch > "9":
            return False
    return True


def is_hexadecimal(s):
    if s == "":
        return False
    s = s.upper()
    for ch in s:
        if ch not in HEX_DIGITS:
            return False
    return True


def binary_to_decimal(binary_str):
    value = 0
    power = 0
    for i in range(len(binary_str) - 1, -1, -1):
        if binary_str[i] == "1":
            value += 2 ** power
        power += 1
    return value


def decimal_string_to_int(text):
    value = 0
    for ch in text:
        value = value * 10 + (ord(ch) - ord("0"))
    return value


def decimal_to_binary(num):
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    return result


def decimal_to_hex(num):
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result = HEX_DIGITS[num % 16] + result
        num = num // 16
    return result


def hex_to_decimal(hex_str):
    hex_str = hex_str.upper()
    value = 0
    power = 0

    for i in range(len(hex_str) - 1, -1, -1):
        digit_value = HEX_DIGITS.index(hex_str[i])
        value += digit_value * (16 ** power)
        power += 1

    return value


def clear_all():
    binary_entry.delete(0, tk.END)
    decimal_entry.delete(0, tk.END)
    hex_entry.delete(0, tk.END)


def convert():
    binary_text = binary_entry.get().strip()
    decimal_text = decimal_entry.get().strip()
    hex_text = hex_entry.get().strip().upper()

    filled = 0
    if binary_text != "":
        filled += 1
    if decimal_text != "":
        filled += 1
    if hex_text != "":
        filled += 1

    if filled == 0:
        messagebox.showerror("錯誤", "請輸入一個數值")
        return

    if filled > 1:
        messagebox.showerror("錯誤", "一次只能輸入一個欄位")
        return

    if binary_text != "":
        if not is_binary(binary_text):
            messagebox.showerror("錯誤", "Binary 欄位只能輸入 0 或 1")
            return
        decimal_value = binary_to_decimal(binary_text)

    elif decimal_text != "":
        if not is_decimal(decimal_text):
            messagebox.showerror("錯誤", "Decimal 欄位只能輸入 0~9")
            return
        decimal_value = decimal_string_to_int(decimal_text)

    else:
        if not is_hexadecimal(hex_text):
            messagebox.showerror("錯誤", "Hexadecimal 欄位只能輸入 0~9 或 A~F")
            return
        decimal_value = hex_to_decimal(hex_text)

    if decimal_value < 0 or decimal_value > 255:
        messagebox.showerror("錯誤", "輸入數值需介於 0 ~ 255")
        return

    binary_result = decimal_to_binary(decimal_value)
    hex_result = decimal_to_hex(decimal_value)

    binary_entry.delete(0, tk.END)
    decimal_entry.delete(0, tk.END)
    hex_entry.delete(0, tk.END)

    binary_entry.insert(0, binary_result)
    decimal_entry.insert(0, str(decimal_value))
    hex_entry.insert(0, hex_result)


root = tk.Tk()
root.title("Binary / Decimal / Hex Converter")
root.geometry("1000x500+100+100")
root.resizable(False, False)
root.resizable(True, True)
root.lift()
root.attributes("-topmost", True)
root.after(500, lambda: root.attributes("-topmost, Faulse"))

title_label = tk.Label(root, text="Binary / Decimal / Hex Converter", font=("Arial", 18, "bold"))
title_label.place(x=240, y=15)

tk.Label(root, text="Binary", font=("Arial", 14)).place(x=110, y=70)
tk.Label(root, text="Decimal", font=("Arial", 14)).place(x=390, y=70)
tk.Label(root, text="Hexadecimal", font=("Arial", 14)).place(x=635, y=70)

binary_entry = tk.Entry(root, font=("Arial", 16), width=18, justify="center")
binary_entry.place(x=40, y=110)

decimal_entry = tk.Entry(root, font=("Arial", 16), width=18, justify="center")
decimal_entry.place(x=325, y=110)

hex_entry = tk.Entry(root, font=("Arial", 16), width=18, justify="center")
hex_entry.place(x=610, y=110)

convert_button = tk.Button(root, text="Convert", font=("Arial", 16), width=20, command=convert)
convert_button.place(x=330, y=170)

clear_button = tk.Button(root, text="Clear", font=("Arial", 16), width=20, command=clear_all)
clear_button.place(x=330, y=220)

root.mainloop()
