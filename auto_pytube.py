import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    """Downloads a YouTube video using yt-dlp and saves it to the specified directory."""
    try:
        ydl_opts = {
            'outtmpl': f"{save_path}/%(title)s.%(ext)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")

def open_file_dialog():
    """Opens a file dialog to select a folder for saving the downloaded video."""
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    folder = filedialog.askdirectory(title="Select Download Folder")
    if folder:
        print(f"Selected folder: {folder}")
        return folder
    return None

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    save_dir = open_file_dialog()

    if video_url and save_dir:
        print("Downloading video...")
        download_video(video_url, save_dir)
    else:
        print("Invalid video URL or save location. Please try again.")
