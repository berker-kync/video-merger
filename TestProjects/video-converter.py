import subprocess

command = ["ffmpeg", "-i", "/Users/berkerkoyuncu/Desktop/Project/Videos/Video1.mp4", "-c:v", "libx264", "-c:a", "copy", "/Users/berkerkoyuncu/Desktop/Project/Videos/output.avi"]

subprocess.run(command)