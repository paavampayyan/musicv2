from logging import exception
from pyrogram import Client as bot
from pyrogram.types import *
from pyrogram.types.messages_and_media.message import Message
import urllib.request
from pytube import YouTube, exceptions
import os

import re



def convert(seconds):
    if seconds >= 3600:
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        return "%d:%02d:%02d" % (hour, min, sec)
    else:
        min, sec = divmod(seconds, 60)
        hour, min = divmod(min, 60)
        return "%02d:%02d" % (min, sec)

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

def link_to_song(app, m):
    chat_id = m.chat.id
    user_id = m.from_user.id
    user_name = m.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    link = m.text
    m1 = m.reply_text("✨ Downloading ⏬")
    try:
        yt = YouTube(link)
        title = yt.title[:30]
        d = yt.length
        duration = convert(d)
        thumbnail = yt.thumbnail_url
        t1 = title.replace('|', '')
        t2 = t1.replace('/', '')
        
        urllib.request.urlretrieve(thumbnail, f"sample_image{m.id}.jpg")
        audio = YouTube(link).streams.filter(only_audio=True).get_by_itag('140')
        audio.download(filename=f"MMC-{t2}.mp3")
        m1.edit("✨ Uploading... ⏫")
        xm = app.send_audio(-1001743584734, audio=f"MMC-{t2}.mp3", thumb=f"sample_image{m.id}.jpg",
                      duration=d,
                      title=title,
                      performer="🅼🅼🅲 - ᴳʳᵒᵘᵖ",
                      caption=f"⌜ Title: {title}"
                            f"\n﹂ Duration: `{duration}`"
                            f"\n﹂ Link: [Watch Video]({link})"
                            f"\n﹂ Requested by: {mention} "

                            "\n\n🌿 MalluMusicCorner")
        xm.copy(m.chat.id, reply_to_message_id=m.id, reply_markup=InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("Send Personally  🍂", url=f'https://t.me/MMC_musicbot?start={xm.id}')]
                            ]
                        ))
        m1.delete()
        os.remove(f"MMC-{t2}.mp3")
        os.remove(f"sample_image{m.id}.jpg")
        
    except exceptions.VideoUnavailable:
        m1.edit("Are you sure? Looks like an invalid URL..")
    except exceptions.LiveStreamError:
        m1.edit("How Can i Download Live stream videos?")
    except Exception as e:
        m1.edit("Hmmm, maybe something went wrong. Wait, I will try to fix it myself.")