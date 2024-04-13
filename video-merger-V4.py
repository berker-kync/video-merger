# https://docs.python.org/3/library/argparse.html
# aegparse komutuyla


import tkinter as tk
from tkinter import filedialog
import subprocess
import argparse

def merge_videos(video_paths, output_path): 
    command = ["ffmpeg"]
    for i, video_path in enumerate(video_paths):
        command.extend(["-i", video_path])
    command.extend(["-filter_complex", f"concat=n={len(video_paths)}:v=1:a=0[v]", "-map", "[v]", output_path])
    subprocess.run(command)
    print("Completed")

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="video merge uygulaması.")
    parser.add_argument("input_videos", nargs="+", help="yardım??")
    parser.add_argument("-o", "--output", required=True, help="Output file path")

    args = parser.parse_args()

    merge_videos(args.input_videos, args.output)


# komut python3 video-merger-V4.py Videos/video1.mp4 Videos/video2.mp4 -o Videos/merged_output.mp4 

