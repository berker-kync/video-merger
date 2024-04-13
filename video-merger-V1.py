
# demuxer / -c:copy incele
# https://stackoverflow.com/questions/39928710/why-is-there-no-tkinter-distribution-found


import subprocess


video1_path = "/Users/berkerkoyuncu/Desktop/Project/Videos/Video1.mp4"
video2_path = "/Users/berkerkoyuncu/Desktop/Project/Videos/Video2.mp4"
output_path = "/Users/berkerkoyuncu/Desktop/Project/Videos/output.mp4"  

command = ["ffmpeg",
           "-i", video1_path,
           "-i", video2_path,
           "-filter_complex", "[0:v:0][0:a:0][1:v:0][1:a:0]concat=n=2:v=1:a=1[v][a]", 
           "-map", "[v]","-map", "[a]",
           output_path]


subprocess.run(command)


print("tamamlandı")