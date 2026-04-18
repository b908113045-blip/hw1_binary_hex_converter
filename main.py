import tkinter as tk
from tkinter import messagebox

def custom_to_dec(s_input, base):
    """將任意進位的字串，轉換為十進位數值 (手動計算)"""
    if not s_input:
        return None
    s_input = s_input.upper()
    val = 0
    for char in s_input:
        # 利用 ASCII 碼計算字元代表的數值
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"輸入包含無效字元 '{char}'")
        
        # 檢查數字是否超出該進位制的允許範圍
        if digit >= base:
            raise ValueError(f"進位制 {base} 中不能出現字元 '{char}'")
            
        val = val * base + digit
    return val

def custom_from_dec(n, base):
    """將十進位數值，轉換為任意進位的字串 (手動計算)"""
    if n == 0:
        return "0"
    
    chars = "0123456789ABCDEF"
    res = ""
    while n > 0:
        # 取餘數對應字元，並將商數繼續除
        res = chars[n % base] + res
        n = n // base
    return res

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary / Decimal / Hex Converter")
        
        # 標籤 (Labels)
        tk.Label(root, text="Binary").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Decimal").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(root, text="Hexadecimal").grid(row=0, column=2, padx=10, pady=5)
        
        # 輸入框 (Entries)
        self.entry_bin = tk.Entry(root, width=15)
        self.entry_bin.grid(row=1, column=0, padx=10, pady=5)
        
        self.entry_dec = tk.Entry(root, width=15)
        self.entry_dec.grid(row=1, column=1, padx=10, pady=5)
        
        self.entry_hex = tk.Entry(root, width=15)
        self.entry_hex.grid(row=1, column=2, padx=10, pady=5)
        
        # 按鈕 (Buttons)
        tk.Button(root, text="Convert", command=self.convert).grid(row=2, column=0, columnspan=3, sticky="we", padx=10, pady=5)
        tk.Button(root, text="Clear", command=self.clear).grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=5)
        
    def clear(self):
        """清空所有輸入框"""
        self.entry_bin.delete(0, tk.END)
        self.entry_dec.delete(0, tk.END)
        self.entry_hex.delete(0, tk.END)
        
    def convert(self):
        """執行轉換邏輯"""
        bin_val = self.entry_bin.get().strip()
        dec_val = self.entry_dec.get().strip()
        hex_val = self.entry_hex.get().strip()
        
        try:
            decimal_number = None
            
            # 判斷使用者在哪個框輸入了數值 (優先順序: 十進位 -> 二進位 -> 十六進位)
            if dec_val:
                decimal_number = custom_to_dec(dec_val, 10)
            elif bin_val:
                decimal_number = custom_to_dec(bin_val, 2)
            elif hex_val:
                decimal_number = custom_to_dec(hex_val, 16)
            else:
                return # 若全部為空則不動作
                
            # 清空所有框，準備填入計算結果
            self.clear()
            
            # 將算出的十進位數值，手動轉換為各進位字串並顯示
            self.entry_dec.insert(0, custom_from_dec(decimal_number, 10))
            self.entry_bin.insert(0, custom_from_dec(decimal_number, 2))
            self.entry_hex.insert(0, custom_from_dec(decimal_number, 16))
            
        except ValueError as e:
            messagebox.showerror("格式錯誤", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.resizable(False, False) 
    root.mainloop()
