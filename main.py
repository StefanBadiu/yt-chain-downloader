import tkinter as tk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL


def GUI():
    download_path_var = ""  # Outer variable

    def choose_download_path():
        nonlocal download_path_var  # Use nonlocal to modify the outer variable
        folder_selected = filedialog.askdirectory(title="Select download folder")
        download_path_var = folder_selected
        download_path_display.set("PATH: \"" + download_path_var + "\"")

    def download_callback():
        url = url_entry.get()
        path = download_path_var

        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
        if not path:
            messagebox.showerror("Error", "Please choose a download path.")
            return

        try:
            download_audio_from_link(url, path)
            messagebox.showinfo("Success", "Download complete!")
        except Exception as e:
            messagebox.showerror("Download Failed", str(e))

    root = tk.Tk()
    root.resizable(True, True)
    root.title("YouTube Downloader")
    root.geometry("500x250")
    root.minsize(400, 160)
    root.maxsize(800, 300)

    # Download path variable
    download_path_display = tk.StringVar(value = "PATH: Not set")

    # URL entry
    root.columnconfigure(0, weight=1)
    tk.Label(root, text="Enter YouTube video/playlist URL:").grid(row=0, column=0, padx=0, pady=5)

    entry_frame = tk.Frame(root)
    entry_frame.grid(row=1, column=0, padx=10, pady=0, sticky="ew")
    root.columnconfigure(0, weight=1)
    entry_frame.columnconfigure(0, weight=1)
    url_entry = tk.Entry(entry_frame, justify="center")
    url_entry.grid(row=0, column=0, sticky="ew", ipady=3)

    # Path picker
    tk.Button(root, text="Choose Download Path", command=choose_download_path).grid(row=2, column=0, padx=10, pady=5)
    tk.Label(root, textvariable=download_path_display).grid(row=3, column=0, padx=10, pady=5)

    # Submit button
    tk.Button(root, text="Download", command=download_callback).grid(row=4, column=0, padx=10, pady=5)

    root.mainloop()

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
        'retries': 3,
        #'verbose': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
GUI()