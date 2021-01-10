from pytube import YouTube

def progress_function(stream, chunk, bytes_remaining):
    print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...',end="\r")

link = input("give the url of youtube video")
yt = YouTube(link, on_progress_callback=progress_function)
videos = yt.streams.all()
i=1
for stream in videos:
    print(str(i) +" "+str(stream))
    i += 1

stream_number = int(input("enter number"))
video = videos[stream_number-1]


video.download("D:/mit differential lectures")
print("Downloaded")