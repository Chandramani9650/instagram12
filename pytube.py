from pytube import YouTube
vidlink = "https://www.youtube.com/watch?v=5LHyK9zMhMM"
youtub = YouTube(vidlink)
print(youtub.thumbnail_url)
print(youtub.title)
videos = youtub.streams.all()
video_quality  = list(enumerate(videos))
print("select video quality : ")
for i in video_quality:
    print(i)
print()
serialno = int(input("enter serial no"))
videos[serialno].download()
print("video download successful")