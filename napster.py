from url_reads import url_reader
from song_downloader import preview_download_napster
import urllib.request
import pprint



print('welcome to Napster-US-preview-song-downloader')
print('Copyright (c) by Suresh Pandiyan')
print(' ')
ask_music_url = str(input('enter the playlist for get a downloadable links \n'))
print(' ')


# read the napster urls
url_reader(ask_music_url)

# download song (preview only)
preview_download_napster(url_reader(ask_music_url))

