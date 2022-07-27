from xml.etree.ElementInclude import LimitedRecursiveIncludeError
from pytube import YouTube, exceptions
from youtube_search import YoutubeSearch
from pyrogram.types import *
import os
import time
import requests
import urllib.request
import heroku3

heroku_conn = heroku3.from_key('931684b2-0ad8-4b13-a12d-62af6e688527')
happ = heroku_conn.apps()['kiensy-v2']

pm_button = InlineKeyboardMarkup([[InlineKeyboardButton("Save to DM", callback_data="dm_s")]])
dur_button = InlineKeyboardMarkup([[InlineKeyboardButton("Continue", callback_data="dw_c"), InlineKeyboardButton("No it's Wrong", callback_data='dw_r')]])

def download(app, song_name, m, user):
    r1 = m.reply_text("✨ Downloading ⏬")
    try:
        results = YoutubeSearch(song_name, max_results=1).to_dict()
        title = results[0]['title'][:30]
        duration = results[0]['duration']
        thumbnail = results[0]['thumbnails'][0]
        t1 = title.replace('|', '')
        t2 = t1.replace('/', '')
    except Exception:
        print('Error')
        return False
   
    urllib.request.urlretrieve(thumbnail, f"sample_image{m.id}.jpg")
    link = "https://youtube.com" + results[0]["url_suffix"]
    secmul, dur, dur_arr = 1, 0, duration.split(':')
    for i in range(len(dur_arr)-1, -1, -1):
        dur += (int(dur_arr[i]) * secmul)
        secmul *= 60
        print(dur)
    if dur >= 600:
        limt = "dur_limi"
        r1.edit("Are you so sure?😲😲 the result is too long approx 10 minutes above. I'm not sure it's a song! what you think?",
        reply_markup=dur_button)
        return limt
    try:
        audio = YouTube(link).streams.filter(only_audio=True).get_by_itag('140')
        audio.download(filename=f"MMC-{t2}.m4a")
        r1.edit('✨ Uploading... ⏫')
        xm = app.send_audio(-1001743584734, audio=f"MMC-{t2}.m4a", thumb=f"sample_image{m.id}.jpg",
                      duration=dur,
                      title=title,
                      performer="🅼🅼🅲 - ᴳʳᵒᵘᵖ",
                      caption=f"⌜ Title: {title}"
                            f"\n﹂ Duration: `{duration}`"
                            f"\n﹂ Link: [Watch Video]({link})"
                            f"\n﹂ Requested by: {user} "

                            "\n\n🌿 MalluMusicCorner")
        xm.copy(m.chat.id, reply_to_message_id=m.id, reply_markup=InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton("Send Personally  🍂", url=f'https://t.me/MMC_musicbot?start={xm.id}')]
                            ]
                        ))
        r1.delete()
        os.remove(f"MMC-{t2}.m4a")
        os.remove(f"sample_image{m.id}.jpg")
    except exceptions.VideoUnavailable:
        r1.edit("Are you sure? Looks like an invalid URL..")
    except exceptions.LiveStreamError:
        r1.edit("How Can i Download Live stream videos?")
    except exceptions.PytubeError as pe:
        print(pe)
        r1.edit("Serious error! Has to fix by dev to continue. I truly apologize for the inconvenience and ask everyone to stop spamming. Contact @nousername_psycho.")
    except Exception as e:
        r1.edit("Hmmm, maybe something went wrong. Wait, I will try to fix it myself.")
        print(e)
        happ.restart()