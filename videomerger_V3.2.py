# https://docs.python.org/3/library/argparse.html
# https://www.youtube.com/watch?v=urrfJgHwIJA
# logging test


import tkinter as tk
from tkinter import filedialog
import subprocess
import argparse
import logging

# logging.basicConfig(level=logging.ERROR, filename="merger.log", filemode="w")
logging.basicConfig(level=logging.DEBUG, filename="merger.log", filemode="a")


def merge_videos(video_paths, output_path):
    if len(video_paths) < 2:
        logging.error("Birleştirme için yeterli video bulunamadı.")
        return

    command = ["ffmpeg"]
    for i, video_path in enumerate(video_paths):
        command.extend(["-i", video_path])
    command.extend(["-filter_complex", f"concat=n={len(video_paths)}:v=1:a=0[v]", "-map", "[v]", output_path])

    try:
        subprocess.run(command, check=True)
        logging.info("Video birleştirme başarılı")
    # except subprocess.CalledProcessError as e:
    #     logging.error(f"Video birleştirme hatası: {e}")
    # except FileNotFoundError as e:
    #     logging.error(f"dosya bulunamadı - {e}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Video birleştirme hatası: {e}")
    except FileNotFoundError as e:
        logging.error(f"Dosya bulunamadı - {e}")
    finally:
        print("İşlem sonlandı")




if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="video merge uygulaması.")
    parser.add_argument("input_videos", nargs="+", help="videoların konumlarını Videos/'video ismi' şeklinde girebilirsiniz")
    parser.add_argument("-o", "--output", required=True, help="Birleştirilmiş videonun yükleneceği yolu belirtin")

    args = parser.parse_args()

    merge_videos(args.input_videos, args.output)


# komut python3 videomerger_V3.2.py Videos/video1.mp4 Videos/video2.mp4 -o Videos/merged_output.mp4 

