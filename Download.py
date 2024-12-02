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
            progress_bar.set(percent / 100)  # Update progress bar
        elif d['status'] == 'finished':
            progress_label.configure(text="Download complete.")
            progress_bar.set(1)  # Complete the progress bar

    try:
        # Set up yt-dlp options and the progress hook
        ydl_opts = {
            'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Output template for filename
            'progress_hooks': [progress_hook],  # Set the progress hook
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
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("YouTube Video Downloader")
root.geometry("500x400")

# Add background color or image
root.configure(bg="#f0f0f0")  # Light gray background

# URL entry field
url_label = ctk.CTkLabel(root, text="Enter YouTube URL:", font=("Arial", 14, "bold"), text_color="#4e4e4e")
url_label.pack(pady=10)

url_entry = ctk.CTkEntry(root, width=400, placeholder_text="Paste YouTube video URL here", font=("Arial", 12))
url_entry.pack(pady=5)

# Folder selection field
folder_label = ctk.CTkLabel(root, text="Select Folder to Save:", font=("Arial", 14, "bold"), text_color="#4e4e4e")
folder_label.pack(pady=10)

folder_frame = ctk.CTkFrame(root, corner_radius=8)
folder_frame.pack(pady=5)

folder_entry = ctk.CTkEntry(folder_frame, width=300, placeholder_text="Select folder", font=("Arial", 12))
folder_entry.pack(side="left", padx=5)

folder_button = ctk.CTkButton(folder_frame, text="Browse", command=select_folder, font=("Arial", 12, "bold"), fg_color="#3b9d9b", hover_color="#6fc5b8")
folder_button.pack(side="left", padx=5)

# Download button
download_button = ctk.CTkButton(root, text="Download Video", command=start_download, font=("Arial", 14, "bold"), fg_color="#4caf50", hover_color="#81c784")
download_button.pack(pady=20)

# Status label
status_label = ctk.CTkLabel(root, text="", font=("Arial", 12), text_color="#388e3c")
status_label.pack(pady=5)

# Progress label
progress_label = ctk.CTkLabel(root, text="", font=("Arial", 12), text_color="green")
progress_label.pack(pady=5)

# Add progress bar
progress_bar = ctk.CTkProgressBar(root, width=400, height=20, corner_radius=3)
progress_bar.pack(pady=20)

# Run the customtkinter event loop
root.mainloop()

