import time
import requests
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types.messages_and_media.message import Message
from instagrapi import Client as kinsey
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from instagrapi import exceptions 
import os
import urllib.request 
from os import getenv



s = {'uuids': {'phone_id': 'ea5ccd75-8932-4913-8223-96e352943cf3', 'uuid': 'cbe050b9-b2c5-499e-bb69-10c74fe21e9f', 'client_session_id': 'b04bd615-6724-42c8-ac86-17b676ef48c9', 'advertising_id': '06263ddc-de96-4ea1-bb42-3e080e6d0266', 'android_device_id': 'android-11a9901e09977f0c', 'request_id': '52d55951-9edc-4424-bf90-8b6eabf8d4f2', 'tray_session_id': '696e538d-e71e-47ae-9ad4-1083f3d06cac'}, 'mid': 'Y0Uw1wABAAEnFw4Luz4-XGyG2Y6_', 'ig_u_rur': None, 'ig_www_claim': None, 'authorization_data': {'ds_user_id': '55367371390', 'sessionid': '55367371390%3AtUBMVaSlKxyiV3%3A0%3AAYfmDU4mib3c2I21ZSHZOihH7780zbjQ9aQJXjwD9w'}, 'cookies': {}, 'last_login': 1665478889.1796923, 'device_settings': {'app_version': '203.0.0.29.118', 'android_version': 26, 'android_release': '8.0.0', 'dpi': '480dpi', 'resolution': '1080x1920', 'manufacturer': 'Xiaomi', 'device': 'capricorn', 'model': 'MI 5s', 'cpu': 'qcom', 'version_code': '314665256'}, 'user_agent': 'Instagram 203.0.0.29.118 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 314665256)', 'country': 'US', 'country_code': 1, 'locale': 'en_US', 'timezone_offset': -14400}

def insta_bot(m, app):
    m1 = m.reply_text("Getting data..")
    cl = kinsey(s)
    # cl.login_by_sessionid('w4VKxF4cm9KfruEbk8QVh9KF1P0aiV8Qg6GUDA')
    # cl.login("kannan_063", "9744anandhu*68")

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
    except exceptions.PrivateError:
        m1.edit("Insta Got Crashed! bcz too many Requests. Try Again Later!")
        time.sleep(6)
        m1.delete()
        m.delete()
    except exceptions.VideoNotDownload:
        m1.edit("Sorry, Video not available...")
    except exceptions.ClientError:
        m1.edit("Error...")
    except Exception as e:
        print(e)
        m1.edit("Insta got crashed!! plz try again later!!")
        time.sleep(5)
        m.delete()
        m1.delete()

    
    # m1 = m.reply_text("Getting data..")
    # # cl.login_by_sessionid('53857278844:1DaBN6eGHeFGVG:11:AYfMP-J9X6gITPziqFqJJwYll-0KGd9YobGUVmAkwA')

    # insta_link = m.text
    # url = f"https://igdl.in/test.php?link={insta_link}"

    # try:
    #     res = requests.get(url)
    #     result = res.json()
    #     print(result)
    #     url_link = result['media']
    #     m1.edit("Downloading....")
    #     file_name = f"MMC_Video_{m.id}.mp4"
    #     urllib.request.urlretrieve(url_link, file_name)
    #     m1.edit("Uploading...") 
    #     m.reply_video(video=file_name, caption="MMC - Video Download Group 🌿")
    #     m1.delete()
    #     os.remove(file_name)

    # except Exception as e:
    #     print(e)

    #     m1.edit("Really bro! something is wrong with this url. i can only download videos. make sure you sending video links which is not private!")
    #     time.sleep(6)
    #     m1.delete()

    

    