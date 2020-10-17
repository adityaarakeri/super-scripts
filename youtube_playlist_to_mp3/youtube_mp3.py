from __future__ import unicode_literals
import youtube_dl

urls  = ['https://www.youtube.com/watch?v=kXYiU_JCYtU&list=PLZ1dJqY6KWOXGGeIlZqleztqta23wHMGG']

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ignoreerrors': True,
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for url in urls:
		ydl.download([url])