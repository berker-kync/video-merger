# https://www.bannerbear.com/blog/how-to-use-ffmpeg-in-python-with-examples/
# ffmpeg'in çalışırlığını kontrol etmek için test projeler

import ffmpeg

input_file = "/Users/berkerkoyuncu/Desktop/Project/Videos/Video1.mp4"
output_file = "/Users/berkerkoyuncu/Desktop/Project/Videos/output.avi"

ffmpeg.input(input_file).output(output_file).run() 



# import subprocess

# command = ["ffmpeg", "-i", "/Users/berkerkoyuncu/Desktop/Project/Videos/Video1.mp4", "-c:v", "libx264", "-c:a", "copy", "/Users/berkerkoyuncu/Desktop/Project/Videos/output.avi"]

# subprocess.run(command)