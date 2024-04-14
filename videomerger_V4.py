
import subprocess
import argparse
import logging


logging.basicConfig(level=logging.DEBUG, filename="merger.log", filemode="a")


# tek video dosyası bulunduğunda bile işlemi gerçekleştirdiği için "en az 2" videonun karşılanması için bu şekilde düzenledim.
def merge_videos(video_paths, output_path):
    if len(video_paths) < 2:  
        logging.error("Birleştirme için yeterli video bulunamadı.")
        return 


# FFmpeg komutunu için döngüyle her video dosyası için dosya yolu eklenit ve  birleştirilmiş videonun çıktısını belirtir.
    command = ["ffmpeg"]
    for i, video_path in enumerate(video_paths):
        command.extend(["-i", video_path])
    command.extend(["-filter_complex", f"concat=n={len(video_paths)}:v=1:a=0[v]", "-map", "[v]", output_path])

    try:
        subprocess.run(command, check=True)
        logging.info("Video birleştirme başarılı")
        print(f"Videonun kaydedildiği konum: {output_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Video birleştirme hatası: {e}")
    except FileNotFoundError as e:
        logging.error(f"Dosya bulunamadı - {e}")




# argparse library ile kullanıcı komutunu alıyoruz.
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="video merge uygulaması.")
    parser.add_argument("input_videos", nargs="+", help="videoların konumlarını Videos/'video ismi' şeklinde girebilirsiniz")
    parser.add_argument("-o", "--output", required=True, help="Birleştirilmiş videonun yükleneceği yolu belirtin")

    args = parser.parse_args()

    merge_videos(args.input_videos, args.output)


# çalıştırma komutu python3 videomerger_V3.2.py Videos/video1.mp4 Videos/video2.mp4 -o Videos/merged_output.mp4 

