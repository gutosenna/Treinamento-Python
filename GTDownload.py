import youtube_dl
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# os.chdir("C:\\Users\\GUTO SENNA\\OneDrive\\Música")

def Widgets():
    link_label = Label(root,
                       text="YouTube link  :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=55,
                          textvariable=video_Link)
    root.linkText.grid(row=1,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Destino   :",
                              bg="#E8D579")
    destination_label.grid(row=2,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=2,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Pasta",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=2,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Baixar",
                        command=Download,
                        width=20,
                        bg="#05E8E0")
    Download_B.grid(row=3,
                    column=1,
                    pady=3,
                    padx=3)

    chkAudio = Radiobutton(root, text="Audio", variable=var, value=1, command=select)
    chkAudio.grid(row=3,
                    column=2,
                    pady=3,
                    padx=3)

    chkVideo = Radiobutton(root, text="Video", variable=var, value=2, command=select)
    chkVideo.grid(row=3,
                    column=3,
                    pady=3,
                    padx=3)

    saida = Button(root,
                        text="Sair",
                        command=sair,
                        width=10,
                        bg="#05E8E0")
    saida.grid(row=4,
                    column=1,
                    pady=3,
                    padx=3)


def Browse():
    download_Directory = filedialog.askdirectory(initialdir="C:\\Users\\GUTO SENNA\\OneDrive\\Música")
    download_Path.set(download_Directory)
    os.chdir(download_Directory)
    print(download_Directory)


def select():
    return var.get()
    # if var.get() == 1:
    #     txt = 'Audio'
    # else:
    #     txt = 'Video'
    # # selection = f"You selected the option {txt}" + str(var.get())
    # messagebox.showinfo(message=selection)


def sair():
    quit()

def Download():
    video_info = None
    try:
        video_url = video_Link.get()
        if var.get() == 1:
            video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        elif var.get() == 2:
            with youtube_dl.YoutubeDL({}) as ydl:
                ydl.download([f'{video_url}'])
        filename = f"{video_info['title']}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
    except (youtube_dl.utils.PostProcessingError, youtube_dl.utils.DownloadError):
        pass
    except KeyboardInterrupt:
        messagebox.showinfo(message='Cancelado!')
    finally:
        messagebox.showinfo(message='Download Concluído!')


root = tk.Tk()

root.geometry("600x120")
root.resizable(False, False)
root.title("YouTube_Audio_Video_Downloader")
root.config(background="#000000")

video_Link = StringVar()
download_Path = StringVar()

var = IntVar()

Widgets()

root.mainloop()

