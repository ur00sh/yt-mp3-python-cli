from pytubefix import YouTube
import os


#url import
yt = YouTube (str(input("Insert the link here: ")))

#extracts audio
video = yt.streams.filter(only_audio =  True).first()

#destination
destination = "/path/of/your/own/choice" #insert your own path where do you want to download the mp3 file

#download
out_file = video.download(output_path = destination)

#save
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

#result
print(yt.title + " has been succesfully downloaded.")
