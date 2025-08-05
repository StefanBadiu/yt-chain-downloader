import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL


def GUI():
    def choose_download_path():
        folder_selected = filedialog.askdirectory(title="Select download folder")
        download_path_var.set(folder_selected)

    def download_callback():
        url = url_entry.get()
        path = download_path_var.get()

        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
        if not path:
            messagebox.showerror("Error", "Please choose a download path")
            return

        try:
            download_audio_from_link(url, path)
            messagebox.showinfo("Success", "Download complete!")
        except Exception as e:
            messagebox.showerror("Download Failed", str(e))

    root = tk.Tk()
    root.title("YouTube Downloader")
    root.geometry("400x250")

    # Download path variable
    download_path_var = tk.StringVar()

    # URL entry
    tk.Label(root, text="Enter YouTube video/playlist URL:").pack(pady=(10, 0))
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5)

    # Path picker
    tk.Button(root, text="Choose Download Path", command=choose_download_path).pack(pady=10)
    tk.Label(root, textvariable=download_path_var).pack()

    # Submit button
    tk.Button(root, text="Download", command=download_callback).pack(pady=10)

    root.mainloop()

def choose_download_path():
    folder_selected = filedialog.askdirectory(title="Select download folder")
    return folder_selected

def download_audio_from_link(playlist_url, download_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'audio_format': 'mp3',  # convert to mp3
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'ignoreerrors': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
GUI()