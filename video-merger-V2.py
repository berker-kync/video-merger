# tkinter'ın macosta çalılması için xquartz kuruldu
# https://www.youtube.com/watch?v=pJkWU-0gWTw
# klasörden tkinter arayüz ile 2 video seçimi yapma
# filedialog https://docs.python.org/3/library/dialog.html

import tkinter as tk
from tkinter import filedialog
import subprocess

def choose_video():
  global video1_path, video2_path
  video1_path = filedialog.askopenfilename(title="birinci Video")
  video2_path = filedialog.askopenfilename(title="ikinci Vide")

  if video1_path and video2_path:
    merge()

def merge():
  global video1_path, video2_path, output_path
  output_path = filedialog.asksaveasfilename(title="Çıkış Dosyasını Seç", defaultextension=".mp4")

  if output_path:
    command = [
      "ffmpeg",
      "-i", video1_path,
      "-i", video2_path,
      "-filter_complex", "concat=n=2:v=1:a=0[v]",  
      "-map", "[v]",
      output_path
    ]

    subprocess.run(command)
    print("Tamamlandı")

pencere = tk.Tk()
pencere.title("Video Birleştirme")

secim_butonu = tk.Button(pencere, text="Video seçimi", command=choose_video)
secim_butonu.pack()

birlestir_butonu = tk.Button(pencere, text="birleştirme başlat", command=merge)
birlestir_butonu.pack()

pencere.mainloop()