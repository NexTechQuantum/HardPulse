import tkinter
import customtkinter
from PIL import Image
from ctkdlib import *

# تنظیم حالت ظاهری
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# ابعاد پنجره
HEIGHT = 600
WIDTH = 600

# ساخت پنجره اصلی
root = customtkinter.CTk()
root.title("Hard Pulse")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

# فریم بالایی (هدر)
header_frame = customtkinter.CTkFrame(master=root, width=591, height=49, corner_radius=16)
header_frame.place(x=5, y=6)

header_label = customtkinter.CTkLabel(
    master=header_frame,
    bg_color=["gray86", "gray17"],
    font=customtkinter.CTkFont('Roboto', size=20, weight='bold'),
    text="Nex Tech Quantum",
    text_color="#400040",
    text_color_disabled="#400040"
)
header_label.place(relx=0.5, rely=0.5, anchor="center")  # مرکزچین

# فریم سایدبار
sidebar_frame = customtkinter.CTkFrame(master=root, width=170, height=532, corner_radius=16)
sidebar_frame.place(x=7, y=61)

# دکمه‌های سایدبار
btn_system_info = customtkinter.CTkButton(master=sidebar_frame, text="System Info")
btn_system_info.place(x=15, y=10)

btn_cpu_test = customtkinter.CTkButton(master=sidebar_frame, text="CPU Stress Test")
btn_cpu_test.place(x=15, y=60)

btn_ram_test = customtkinter.CTkButton(master=sidebar_frame, text="RAM Stress Test")
btn_ram_test.place(x=15, y=110)

btn_gpu_test = customtkinter.CTkButton(master=sidebar_frame, text="GPU Stress Test")
btn_gpu_test.place(x=15, y=160)

btn_hdd_test = customtkinter.CTkButton(master=sidebar_frame, text="HDD Stress Test")
btn_hdd_test.place(x=15, y=210)

btn_sound_test = customtkinter.CTkButton(master=sidebar_frame, text="Sound Test")
btn_sound_test.place(x=15, y=260)

btn_microphone_test = customtkinter.CTkButton(master=sidebar_frame, text="Microphone Test")
btn_microphone_test.place(x=15, y=310)

btn_battery = customtkinter.CTkButton(master=sidebar_frame, text="Battery")
btn_battery.place(x=15, y=360)

# فریم اصلی (صفحه محتوا)
content_frame = customtkinter.CTkFrame(master=root, width=405, height=532, corner_radius=16)
content_frame.place(x=188, y=61)

# لیبل UUID
uuid_label = customtkinter.CTkLabel(master=content_frame, bg_color=['gray86', 'gray17'], text="UUID:")
uuid_label.place(x=20, y=20)

uuid_entry = customtkinter.CTkEntry(master=content_frame, bg_color=['gray86', 'gray17'], width=322)
uuid_entry.place(x=80, y=20)

# Meterهای CPU و RAM
cpu_meter = CTkMeter(master=content_frame, bg_color=['gray86', 'gray17'], width=150, height=150)
cpu_meter.place(x=30, y=80)

cpu_label = customtkinter.CTkLabel(master=content_frame, bg_color=['gray86', 'gray17'], text="CPU")
cpu_label.place(x=90, y=140)

ram_meter = CTkMeter(master=content_frame, bg_color=['gray86', 'gray17'], width=150, height=150)
ram_meter.place(x=220, y=80)

ram_label = customtkinter.CTkLabel(master=content_frame, bg_color=['gray86', 'gray17'], text="RAM")
ram_label.place(x=285, y=140)

# اجرای حلقه اصلی
root.mainloop()
