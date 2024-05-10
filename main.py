import tkinter
import customtkinter
from pytube import YouTube


def start_download(download_type):
    try:
        ytlink = link.get()
        yt_object = YouTube(ytlink, on_progress_callback=on_progress)
        title.configure(text=yt_object.title, text_color="white")

        if download_type == "video":
            stream = yt_object.streams.get_highest_resolution()
        elif download_type == "audio":
            stream = yt_object.streams.get_audio_only()

        stream.download()
        finish_label.configure(text="Downloaded!", text_color="white")
    except:
        finish_label.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    p_percentage.configure(text=per + '%')
    p_percentage.update()

    # Update Progress Bar
    progress_bar.set(float(percentage_of_completion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Progress Percentage
p_percentage = customtkinter.CTkLabel(app, text="0%")
p_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=0)

# Download Buttons
download_video = customtkinter.CTkButton(app, text="Download Video", command=lambda: start_download("video"))
download_video.pack(padx=10, pady=10)

download_audio = customtkinter.CTkButton(app, text="Download Audio", command=lambda: start_download("audio"))
download_audio.pack(padx=10, pady=10)

# Run App
app.mainloop()
