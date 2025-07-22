import tkinter as tk
from tkinter import filedialog
from yt_dlp import YoutubeDL

def choose_download_path():
    root = tk.Tk()
    root.withdraw()  #hide GUI window
    folder_selected = filedialog.askdirectory(title="Select download folder")
    return folder_selected

def download_audio_from_playlist(playlist_url, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio_format': 'mp3',  # convert to mp3
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
playlist_url = input("Paste YouTube playlist URL: ")
download_path = choose_download_path()
download_audio_from_playlist(playlist_url, download_path)
