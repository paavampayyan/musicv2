from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types.messages_and_media.message import Message
from pytube import YouTube, exceptions
import subprocess
import os
import time


def youtube_shots(url_text, m:Message):
    r1 = m.reply_text("Analysing....🔎")
    url = url_text
    try:
        video = YouTube(url).streams.filter(progressive=False).get_by_itag('401')
        yt = YouTube(url)
        dur = yt.length
        if dur >= 60 and m.from_user.id != 1445436774:
            r1.edit("Here you can only download status videos, which means the video length should be 30-60 seconds. Contact Admins.🌿 ")      
            return
        title = yt.title[:30]
        t1 = title.replace('|', '-')
        f_title = t1.replace('/', '-')
        if not video:
            video = YouTube(url).streams.filter(progressive=False).get_by_itag('400')
        if not video:
            video = YouTube(url).streams.filter(progressive=False).get_by_itag('137')
        if not video:
            video = YouTube(url).streams.filter(progressive=False).get_by_itag('136')
        if not video:
            video = YouTube(url).streams.filter(progressive=False).get_by_itag('299')
        if not video:
            video = YouTube(url).streams.filter(progressive=False).first()    
        r1.edit("Downloading....⏬")
        video.download(filename=f"{m.id}.mp4")
        audio = YouTube(url).streams.filter(only_audio=True).get_by_itag('140')
        audio.download(filename=f"{m.id}.mp3")
    except exceptions.VideoUnavailable:
        r1.edit("Video Not available")
    except Exception as e:
        print(e)
        r1.edit("Error.. ")
    else:
        time.sleep(1)
        res = f"ffmpeg -i {m.id}.mp4 -i {m.id}.mp3 -c:v copy -c:a aac MMC-Video-{m.id}.mp4"
        x = subprocess.check_output(res, shell=True)
        r1.edit("Uploading....⏫")
        vid_msg = m.reply_video(video=f"MMC-Video-{m.id}.mp4", caption="MMC - Video Download Group 🌿", supports_streaming=True)
        r1.delete()
        os.remove(f"{m.id}.mp4")
        os.remove(f"{m.id}.mp3")
        os.remove(f"MMC-Video-{m.id}.mp4")