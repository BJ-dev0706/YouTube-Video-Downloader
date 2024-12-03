# YouTube Video Downloader

A simple and stylish YouTube video downloader GUI built using `customtkinter` and `yt-dlp`. The app allows users to download YouTube videos by pasting a URL and selecting a folder to save the video, with real-time progress tracking.

## Features

- **Enter YouTube URL**: Paste the URL of the video you want to download.
- **Select Folder**: Choose a folder where the video will be saved.
- **Download Video**: Start downloading the video with progress tracking.
- **Progress Bar**: View the download progress in percentage with a progress bar.
- **Multithreaded**: Keeps the UI responsive while downloading.
- **Error Handling**: Displays error messages if the URL or folder is not provided or if an issue occurs during the download.

## Requirements

To run this project, you need the following libraries:

- `yt-dlp`: A powerful YouTube video downloader.
- `customtkinter`: A modern Tkinter library for a stylish GUI.
- `threading`: Used for managing the download process in a separate thread.

### Install Dependencies

Run the following command to install the dependencies:

```bash
pip install -r requirements.txt

python Download.py
```


### Changes made:
- Added `requirements.txt` section to specify dependencies.
- Added installation and usage instructions for the project.
- Mentioned the specific versions for `yt-dlp` and `customtkinter` for consistency.

Feel free to copy and paste this updated version into your `README.md`.
