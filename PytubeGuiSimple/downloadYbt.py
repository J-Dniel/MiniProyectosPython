from pytube import YouTube
from pytube.cli import on_progress


def multipleDownload(link, destino, video, audio):

    links = open(link,'r')

    for i in links:
        i = i.strip()
        try:
            yt = YouTube(i, on_progress_callback=on_progress)
        except:
            print("Connection Error")

        try:
            if(video):
                vi = yt.streams.filter(mime_type='video/mp4', res='720p', progressive=True).first()
                vi.download(destino)

            if(audio):
                au = yt.streams.filter(type='audio').first()
                au.download(destino)

            print("\nDownLoad Completed")
        except:
            print("Error")

    print("Completed!!!")


def simpleDownload(url, destino, video, audio):
   
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
    except:
        print("Connection Error")

    try:
        if(video):
            vi = yt.streams.filter(mime_type='video/mp4', res='720p', progressive=True).first()
            vi.download(destino)

        if(audio):
            au = yt.streams.filter(type='audio').first()
            au.download(destino)

        print("\nDownLoad Completed")
    except:
        print("Error")



