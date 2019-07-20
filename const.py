WEBRIP1 = {"ffmpeg_params": [
    "-c:a libfdk_aac -afterburner:a 1 -vbr:a 1 -profile:a aac_low -ac 1",
    # "-c:v libx265 -preset:v slower -crf:v 28 -profile:v main",
    "-c:v libx264 -preset:v veryslow -crf:v 28 -profile:v high -level:v 3.1",
    "-filter:v scale=720:-2 -sws_flags lanczos",
],
    "output_format": "mkv"}
