import tkinter as tk
from tkinter import filedialog
import subprocess

video_paths = []

def choose_video():
    global video_paths
    chosen_video_path = filedialog.askopenfilename(title="video seç")
    if chosen_video_path:
        video_paths.append(chosen_video_path)
        print(f"Eklenen: {chosen_video_path}")

def merge():
    global video_paths, output_path
    output_path = filedialog.asksaveasfilename(title="output klasör seçimi", defaultextension=".mp4")
    if output_path and video_paths:
        command = ["ffmpeg"]
        for i, video_path in enumerate(video_paths):
            command.extend(["-i", video_path])
        command.extend(["-filter_complex", f"concat=n={len(video_paths)}:v=1:a=0[v]", "-map", "[v]", output_path])
        subprocess.run(command)
        print("Completed")


pencere = tk.Tk()
pencere.title("Video Birleştirm")

secim_butonu = tk.Button(pencere, text="Ekleme yap", command=choose_video)
secim_butonu.pack()

birlestir_butonu = tk.Button(pencere, text="Birleştir", command=merge)
birlestir_butonu.pack()

pencere.mainloop()