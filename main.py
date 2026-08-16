"""Baixador de música/áudio via yt-dlp (YouTube e centenas de outros sites)."""

import os
import sys

import imageio_ffmpeg
import yt_dlp

DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")


def baixar_audio(url: str, pasta: str = DOWNLOAD_DIR) -> None:
    os.makedirs(pasta, exist_ok=True)

    opcoes = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(pasta, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "ffmpeg_location": imageio_ffmpeg.get_ffmpeg_exe(),
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else input("Cole o link do vídeo/música: ").strip()
    if not url:
        print("Nenhum link informado.")
        return

    try:
        baixar_audio(url)
        print(f"Concluído! Arquivo salvo em: {DOWNLOAD_DIR}")
    except yt_dlp.utils.DownloadError as erro:
        print(f"Erro ao baixar: {erro}")


if __name__ == "__main__":
    main()
