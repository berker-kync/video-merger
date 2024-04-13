# Path girilen videonun çalıştırılması

import subprocess 
# ffplay çalışması için gerekli

def run_video():
    video_path = input("Videonun tam dosya yolunu girin: ")
    if not video_path:  
        print("Lütfen bir dosya yolu girin.")
        return

    command = ["ffplay", "-autoexit", video_path]
    try:
        subprocess.run(command)
    except FileNotFoundError:
        print(f"Belirtilen dosya yolu bulunamadı: {video_path}")

if __name__ == "__main__":
    run_video()
