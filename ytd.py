
from pytube import YouTube


link=input("Paste Youtube Link  : ")

print("\n")
yt=YouTube(link)
print(yt.title)
print("\n")
print(yt.thumbnail_url)
print("\n")


print("[1].All Formats")
print("[2].Only Audio")
print("[3].Only Video")
print("[4].Video with Audio")
print("[0].Exit")
choices=int(input("Enter Choice:"))
video=yt.streams


#-------download audio only-------
if choices==2:
    video=video.filter(only_audio=True)
    vid=list(enumerate(video))
    for i in vid:
         print(i)

    strm=int(input("Enter  : "))
    video[strm].download()
    print("Succesfully Downloaded..... ")
    
    
elif choices==1:
    video=video.all()
    vid=list(enumerate(video))
    for i in vid:
     print(i)

    strm=int(input("Enter  : "))
    video[strm].download()
    print("Succesfully Downloaded..... ")
    
elif choices==0:
    exit()

    
elif choices==3:
    video=video.filter(only_video=True)
    vid=list(enumerate(video))
    for i in vid:
         print(i)

    strm=int(input("Enter  : "))
    video[strm].download()
    print("Succesfully Downloaded..... ") 
    
    
elif choices==4:
    video=video.filter(progressive=True)
    vid=list(enumerate(video))
    for i in vid:
         print(i)

    strm=int(input("Enter  : "))
    video[strm].download()
    print("Succesfully Downloaded..... ")     
    
else:
    print("Wrong Choice...\n Exitting...")
    
    exit()