from pytube import YouTube

link = input("Enter the YouTube link: ")
video = YouTube(link)

data = "{video.title}'s YouTube Data\nViewcount: {video.views}\nRating: {video.rating:.2f} \nDuration: {video.length / 60:.2f} minutes"

print(data)

youtube_filter = yt.filter('mp4')
yt.set_filename(video.title)

folder = "C:\example\example\example"

video = yt.get(youtube_filter[-1].extension, youtube_filter[-1].resolution)

video.download(folder)

print("Video successfully downloaded!")
