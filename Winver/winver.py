import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import os

# Barvy podle XP
XP_HEADER_BG = "#6683e2"
XP_BODY_BG = "#f3efe3"
XP_LINE = "#bdb8ac"

WIN_W, WIN_H = 570, 470

root = tk.Tk()
root.title("About Windows")
root.resizable(False, False)
root.geometry(f"{WIN_W}x{WIN_H}+200+100")
root.configure(bg=XP_BODY_BG)

# Fonty
try:
    title_font = font.Font(family="Segoe UI", size=24, weight="bold")
    pro_font = font.Font(family="Segoe UI", size=14)
    body_font = font.Font(family="Segoe UI", size=10)
    normal_font = font.Font(family="Segoe UI", size=10, weight="normal")
except:
    # fallback
    title_font = font.Font(family="Arial", size=24, weight="bold")
    pro_font = font.Font(family="Arial", size=14)
    body_font = font.Font(family="Arial", size=10)
    normal_font = font.Font(family="Arial", size=10, weight="normal")

header_h = 120
header = tk.Frame(root, bg=XP_HEADER_BG, height=header_h)
header.place(x=0, y=0, width=WIN_W, height=header_h)

# Vše do jednoho rámce pro snazší středění
center_box = tk.Frame(header, bg=XP_HEADER_BG)
center_box.place(relx=0.5, rely=0.5, anchor="center")

# === Cesta k logu ve stejné složce jako skript ===
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "xp_logo.png")

try:
    logo_img = Image.open(logo_path).resize((58,58), Image.LANCZOS)
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(center_box, image=logo, bg=XP_HEADER_BG)
    logo_label.grid(row=0, column=0, rowspan=3, padx=(0, 15), pady=0, sticky="w")
except:
    logo_label = tk.Label(center_box, text="", bg=XP_HEADER_BG)
    logo_label.grid(row=0, column=0, rowspan=3, padx=(0, 15), pady=0, sticky="w")

# Microsoft nahoru, Window vedle, XP vedle
tk.Label(center_box, text="Microsoft", font=("Segoe UI", 13, "bold"), bg=XP_HEADER_BG, fg="white").grid(row=0, column=1, sticky="w")
titleframe = tk.Frame(center_box, bg=XP_HEADER_BG)
titleframe.grid(row=1, column=1, sticky="w")
tk.Label(titleframe, text="Windows", font=("Segoe UI", 23, "bold"), bg=XP_HEADER_BG, fg="white").pack(side="left")
tk.Label(titleframe, text="XP", font=("Segoe UI", 23, "bold"), bg=XP_HEADER_BG, fg="#ff8000").pack(side="left", padx=(7,0))

# Professional pod tím
tk.Label(center_box, text="Professional", font=pro_font, bg=XP_HEADER_BG, fg="white").grid(row=2, column=1, sticky="w", pady=(2, 0))

# Copyright vlevo dole
tk.Label(header, text="Copyright © 1985-2001", font=("Segoe UI", 9), bg=XP_HEADER_BG, fg="white").place(x=15, y=98)
tk.Label(header, text="Microsoft Corporation", font=("Segoe UI", 9), bg=XP_HEADER_BG, fg="white").place(x=15, y=111)

# "Microsoft" vpravo dole
tk.Label(header, text="Microsoft", font=("Segoe UI", 11), bg=XP_HEADER_BG, fg="white").place(relx=1.0, x=-18, y=98, anchor="ne")

# ODDĚLOVACÍ ČÁRA
tk.Frame(root, height=2, bg=XP_LINE).place(x=0, y=header_h, width=WIN_W)

# TĚLO OKNA
body_y = header_h + 12
tk.Label(root, text="Microsoft ® Windows", font=body_font, bg=XP_BODY_BG, anchor="w").place(x=36, y=body_y)
tk.Label(root, text="Version 5.1 (Build 2600.xpsp3.020828-1920 : Service Pack 3)", font=body_font, bg=XP_BODY_BG, anchor="w").place(x=36, y=body_y+22)
tk.Label(root, text="Copyright © 1981-2001 Microsoft Corporation", font=body_font, bg=XP_BODY_BG, anchor="w").place(x=36, y=body_y+44)

# EULA a jméno O ŘÁDEK NÍŽ a vlevo
tk.Label(root, text="This product is licensed under the terms of the End-User", font=body_font, bg=XP_BODY_BG, anchor="w", justify="left").place(x=36, y=body_y+74)
tk.Label(root, text="License Agreement to:", font=body_font, bg=XP_BODY_BG, anchor="w").place(x=36, y=body_y+94)
tk.Label(root, text="kuba", font=normal_font, bg=XP_BODY_BG, anchor="w").place(x=60, y=body_y+114)

# Další čára
tk.Frame(root, height=2, bg=XP_LINE).place(x=0, y=body_y+140, width=WIN_W)

# RAM info
tk.Label(root, text="Physical memory available to Windows:", font=body_font, bg=XP_BODY_BG, anchor="w").place(x=36, y=body_y+160)
tk.Label(root, text="16,777,216 KB", font=body_font, bg=XP_BODY_BG).place(x=360, y=body_y+160)

# OK BUTTON
def close(event=None):
    root.destroy()

ok_btn = tk.Button(root, text="OK", font=("Segoe UI", 11), width=10, command=close, relief="flat", bg="#e8e8e8", activebackground="#d5d5d5", bd=1, highlightthickness=1)
ok_btn.place(x=WIN_W-140, y=WIN_H-55)
ok_btn.focus_set()
root.bind('<Return>', close)

root.mainloop()

