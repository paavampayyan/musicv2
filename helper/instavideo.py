from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types.messages_and_media.message import Message
from instagrapi import Client as kinsey
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagrapi import exceptions as instae
import os


s = {'uuids': {'phone_id': 'a1c7ae30-a40a-44f6-824e-16ca4d971aaf', 'uuid': 'b39c63d7-3ce3-46ba-ac9c-b06a65fb5cf4', 'client_session_id': 'ab7c060d-62a2-4f3f-884f-26d068836906', 'advertising_id': 'eeacf432-b048-449f-8ad6-e4bbea050b32', 'android_device_id': 'android-e71f68ab84e53084', 'request_id': '2eef9ec6-20d3-4ebd-a30c-42ef03c44e70', 'tray_session_id': '0c34714f-dc54-4d9f-bdce-a047e7035597'}, 'mid': 'Ytrf2QABAAF3pRPHhMWrgPJq9zTZ', 'ig_u_rur': None, 'ig_www_claim': None, 'authorization_data': {'ds_user_id': '53857278844', 'sessionid': '53857278844%3A6qV30wROHpu7iz%3A29%3AAYd8Oj-UVHKviwU0iBLDk8oP5oE_uF3c_2lW7Qv23Q'}, 'cookies': {}, 'last_login': 1658511329.0828562, 'device_settings': {'app_version': '203.0.0.29.118', 'android_version': 26, 'android_release': '8.0.0', 'dpi': '480dpi', 'resolution': '1080x1920', 'manufacturer': 'Xiaomi', 'device': 'capricorn', 'model': 'MI 5s', 'cpu': 'qcom', 'version_code': '314665256'}, 'user_agent': 'Instagram 203.0.0.29.118 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 314665256)', 'country': 'US', 'country_code': 1, 'locale': 'en_US', 'timezone_offset': -14400}

def insta_bot(m):
    m1 = m.reply_text("Getting data..")
    cl = kinsey(s)
    # cl.login_by_sessionid('53857278844%3AiwTNXCEQEJACKq%3A2')

    url = m.text
    k = url.split('/?')[0]
    h = k.split('/')
    last_elem = h.pop()
    try:
        media_pk = cl.media_pk_from_code(last_elem)
        m1.edit("Downloading....⏬")
        video = cl.video_download(media_pk)
        media_path = cl.media_oembed(f'https://www.instagram.com/p/{last_elem}/').dict()
        auth = media_path["author_name"]

        old_name = f"{auth}_{media_pk}.mp4"
        new_name = f"uploaded_by_Kinsey_{auth}_{m.id}.mp4"
        print(old_name, new_name)
        os.rename(old_name, new_name)
        m1.edit("Uploading....⏫")
        m.reply_video(video=new_name, caption="MMC - Video Download Group 🌿")
        m1.delete()
        os.remove(new_name)
    except instae.PrivateError:
        m1.edit("maybe you are sending a video link that I can't access. or something wrong happening. if this error shows continuously, please inform my owner (@nousername_psycho) to fix it. and kindly stop spamming.")
    except instae.VideoNotDownload:
        m1.edit("Sorry, Video not available...")
    except instae.ClientLoginRequired:
        m1.edit("Serious Error! Contact Admin.")
    except instae.ClientError:
        m1.edit("Error...")
    except Exception as e:
        print(e)
        m1.edit("looks like an image not video!")

    