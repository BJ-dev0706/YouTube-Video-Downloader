import customtkinter as ctk
from tkinter import filedialog, messagebox
import yt_dlp as ytdlp
from threading import Thread

# Function to download YouTube video using yt-dlp with progress callback
def download_video():
    url = url_entry.get().strip()
    folder = folder_entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return
    if not folder:
        messagebox.showerror("Error", "Please select a folder to save the video.")
        return

    # Define the progress hook function
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            progress_label.configure(text=f"Progress: {percent:.2f}%")
            progress_bar.set(percent / 100)
        elif d['status'] == 'finished':
            progress_label.configure(text="Download complete.")
            progress_bar.set(1)

    try:
        # Initialize progress bar at 0%
        progress_bar.set(0)
        progress_label.configure(text="Progress: 0.00%")

        # Set up yt-dlp options and the progress hook
        ydl_opts = {
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }

        # Download the video with yt-dlp
        status_label.configure(text="Starting download...")
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video downloaded successfully.")
        status_label.configure(text="Download complete.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.configure(text="Download failed.")

# Function to start download in a separate thread
def start_download():
    Thread(target=download_video).start()

# Function to open folder dialog
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, ctk.END)
        folder_entry.insert(0, folder_path)

# Create the main customtkinter window
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("YouTube Video Downloader")
root.geometry("600x500")
root.configure(bg="#333333")

# Center the window
window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position to center the window
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Apply the position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Title label
title_label = ctk.CTkLabel(root, text="YouTube Video Downloader", font=("Helvetica", 20, "bold"), text_color="#ffffff")
title_label.pack(pady=(40, 25))

# URL section
url_frame = ctk.CTkFrame(root, corner_radius=10, fg_color="#444444")
url_frame.pack(pady=(0, 15), padx=30, fill="x")

url_label = ctk.CTkLabel(url_frame, text="Enter YouTube URL:", font=("Helvetica", 14, "bold"), text_color="#ffffff")
url_label.pack(pady=5, padx=20)

url_entry = ctk.CTkEntry(url_frame, width=500, placeholder_text="Paste YouTube video URL here", font=("Arial", 12))
url_entry.pack(pady=5, padx=20)

# Folder section
folder_frame = ctk.CTkFrame(root, corner_radius=10, fg_color="#444444")
folder_frame.pack(pady=(0, 15), padx=30, fill="x")

folder_label = ctk.CTkLabel(folder_frame, text="Select Folder to Save:", font=("Helvetica", 14, "bold"), text_color="#ffffff")
folder_label.pack(pady=5, padx=20)

folder_entry = ctk.CTkEntry(folder_frame, width=380, placeholder_text="Select folder", font=("Arial", 12))
folder_entry.pack(side="left", padx=20, pady=5)

folder_button = ctk.CTkButton(folder_frame, text="Browse", command=select_folder, font=("Arial", 12, "bold"), fg_color="#1f9c9c", hover_color="#6fc5b8")
folder_button.pack(side="right", padx=20, pady=5)

# Download button
download_button = ctk.CTkButton(root, text="Download Video", command=start_download, font=("Helvetica", 16, "bold"), fg_color="#4caf50", hover_color="#81c784")
download_button.pack(pady=20)

# Status label
status_label = ctk.CTkLabel(root, text="", font=("Arial", 12), text_color="#4caf50")
status_label.pack(pady=1)

# Progress label
progress_label = ctk.CTkLabel(root, text="", font=("Arial", 12), text_color="yellow")
progress_label.pack(pady=5)

# Add progress bar
progress_bar = ctk.CTkProgressBar(root, width=500, height=25, corner_radius=5)
progress_bar.pack(pady=10)

# Run the customtkinter event loop
root.mainloop()

