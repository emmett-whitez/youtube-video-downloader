from pytube import YouTube
import win10toast
import time

toaster = win10toast.ToastNotifier()

url = input('Enter the url: ')
yt = YouTube(url)
print(f'Video Information\nTitle: {yt.title}\nViews: {yt.views}\nVideo Length: {yt.length} seconds')

ys = yt.streams.get_highest_resolution()

# print('Downloading video...')

toaster.show_toast(
    'YouTube Downloader',
    'Downloading video...',
    icon_path=None,
    duration=4,
    threaded=False
)

# print('Successfully downloaded!')

ys.download()
toaster.show_toast(
    'YouTube Downloader',
    'Successfully downloaded!',
    icon_path=None,
    duration=4,
    threaded=False
)
