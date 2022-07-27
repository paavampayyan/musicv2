from pyrogram import *
from pyrogram.types import *
from helper.m_dfunc import *
from helper.no_limi import no_limit_download
from helper.v_dfunc import *
from helper.recognition import *
from helper.instavideo import *
import os
import heroku3
from helper.link_song import *

heroku_conn = heroku3.from_key('931684b2-0ad8-4b13-a12d-62af6e688527')
happ = heroku_conn.apps()['kiensy-v2']

app = Client('baby', api_id=7834184,
api_hash='9599543ce14c4b04599900e5ae19c55f',
bot_token='2104461159:AAH0okRzBoeW9J389LbnPdzE7j3_BWn6-ck')

ex_text = InlineKeyboardMarkup([[InlineKeyboardButton("Examples 📓", callback_data="ex_b")]])

start_img = 'https://telegra.ph/file/46afce7b8d597048fcc25.jpg'

start_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Look inside 👀", callback_data="start_inside")]])
callinside_markup = InlineKeyboardMarkup([[InlineKeyboardButton("How To use?", callback_data="start_how"),
                                          InlineKeyboardButton("Contact Owner", callback_data="start_owner"),
                                          InlineKeyboardButton("Whats New?", callback_data="start_new")],
                                          [InlineKeyboardButton("Back 🔙", callback_data="start_back")]])
back_one = InlineKeyboardMarkup([[InlineKeyboardButton("Back 🔙", callback_data="back_one")]])

ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"

music_group = -1001316272916
video_group = -1001668676447
instargex = r"https://www.instagram.com/"

@app.on_message(filters.regex(ytregex) & (filters.chat(music_group)))
def link_conv_song(__, m:Message):
    link_to_song(app, m)

@app.on_message(filters.regex(instargex) & filters.chat(video_group)) 
def get_insta_video(__, m:Message):
    insta_bot(m)


@app.on_callback_query(filters.regex('dw_c'))
def download_c(__, c:CallbackQuery):
    c.message.delete()
    c_user_id = c.from_user.id
    user_name = c.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(c_user_id) + ")"
    c_message_user_id = c.message.reply_to_message.from_user.id
    c_song_name = c.message.reply_to_message.text.replace('/song ', '')
    print(c_user_id, c_message_user_id, c_song_name)
    if c_message_user_id == c_user_id:
        no_limit_download(app, c_song_name, c.message.reply_to_message, mention)
    else:
        c.answer(f"I'm not asking you 😠, {user_name} can reply.", show_alert=True)

@app.on_callback_query(filters.regex('dw_r'))
def download_c(__, c:CallbackQuery):
    c_user_id = c.from_user.id
    user_name = c.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(c_user_id) + ")"
    c_message_user_id = c.message.reply_to_message.from_user.id
    c_song_name = c.message.reply_to_message.text.replace('/song ', '')
    print(c_user_id, c_message_user_id, c_song_name)
    if c_message_user_id == c_user_id:
        c.edit_message_reply_markup()
        c.edit_message_text(f"Yeah.. {user_name} it's wrong.. 😌")
    else:
        c.answer(f"I'm not asking you 😠, {user_name} can reply.", show_alert=True)

@app.on_message(filters.regex(ytregex) & (filters.chat(video_group) | filters.user("nousername_psycho")))
def yt_video(__, m:Message):
    youtube_shots(m.text, m)

@app.on_message(filters.command('song') & (filters.chat(music_group) | filters.user("nousername_psycho")))
def song(__, m:Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    user_name = m.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    query = ''
    for i in m.command[1:]:
        query += ' ' + str(i)        
    song_name = str(query)  
    if song_name == "":
        m.reply_text("Syntax error ⛔️.\nWanna see some examples?",
                     reply_markup=ex_text)
        return     
    req_song = download(app, song_name, m, mention)

@app.on_message(filters.command('start') & filters.private)
def start(__, m:Message):
    user_id = m.from_user.id
    user_name = m.from_user.first_name
    usr_mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    if len(m.command)==2:
        app.copy_message(m.chat.id, -1001743584734, int(m.command[1]), caption=f'Here is ur song have a great day {m.from_user.first_name} 😙',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Back to Group", url='https://t.me/+TnS7FGBZOxtdev6i')],
                [InlineKeyboardButton("Invite Friend's 👥", switch_inline_query='Friend Invite')]
            ]
        ))
        return
    else:
        m.reply_photo(photo=start_img,
                            caption=f"Hello {usr_mention} 👋, Private usage strictly restricted."
                                    "if you want to download any song you should join our group Mallu Music Corner "
                                    "\n\nAre you intrested in bots? We can make bots with your own needs. contact us : @nousername_psycho",
                            reply_markup=start_markup)
    
        
@app.on_inline_query(filters.regex('Friend Invite'))
def invite_friend(__, n:InlineQuery):
    n.answer(results=[
        InlineQueryResultAnimation(animation_url='https://telegra.ph/file/a2d23a4bbe120b31aea5b.gif',
            id="Friend Invite",
            description="Tap Here.. !",
            title="Friend Invite",
            caption='**Hai i found a stunning group that provides awesome features. here you can download songs, youtube shorts, insta reels or any insta video instantly. Also we can recognize original songs of short video clips🔥🔥.\n\n join Now 👇🏻👇🏻**',
            reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Join Now ❤️", url='https://t.me/+TnS7FGBZOxtdev6i')]
            ]
        ))])




    
@app.on_callback_query(filters.regex("start_inside"))
async def cal_start_inside(__, c:CallbackQuery):
    await c.message.delete()
    await c.message.reply_text("Oh wow 🤩, I'm glad you want to know more about me. "
                               "Well, I am a telegram bot running on python3 with pyrogram framework. "
                               "We are using Youtube Dl For downloading Music and elephant Sql For Database.\n",
                               reply_markup=callinside_markup)
    
@app.on_callback_query(filters.regex("start_how"))
async def cal_start_how(__, c:CallbackQuery):
    await c.message.delete()
    await c.message.reply_text("**Okay, I will help you. ✋**\n\n"
                               "First of all you should know the process happening behind the bot. "
                               "If you type `/song - song name`, bot will catch song name and it will try to get results from YouTube with that keyword. "
                               "And the first result return as an audio. Cool? "
                               "But the problem is if you type wrong song name it will act like same and the result is absolutely wrong. "
                               "So we added a new specific features. What's that? "
                               "If you don't know the song name correctly just copy YouTube video link and paste it in our group. Bot will fetch the audio"
                               "\n\n**Song Command - Examples** "
                               "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n"
                                "⌊ `/song closer` \n"
                                "⌊ `/song Justin Bieber - Sorry` \n"
                                "⌊ `/song Alan Walker - Faded` \n"
                                "⌊ `/song Imagine Dragons - Thunder` \n"
                                "⌊ `/song Doja Cat - Boss B*tch ` \n"
                                "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n"
                                "\n**Song Request Tips**"
                                "\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n"
                                "⌊ if you type song name only it will fetch the full song, but song name + lyric will fetch the lyric song. "
                                "So you can avoid cinematic dialogue from the song.\n"
                                "\n⌊ You can use `@vid` as inline for search, YouTube video links (it will help you to get the song name correctly) \n"
                                "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\n"
                                "©️ MalluMusicCorner",
                               reply_markup=back_one)

@app.on_callback_query(filters.regex("back_one"))
async def back1(__, c:CallbackQuery):
    await c.message.edit("Oh wow 🤩, I'm glad you want to know more about me. "
                               "Well, I am a telegram bot running on python3 with pyrogram framework. "
                               "We are yousing Youtube Dl For downloading Music and elephant Sql For Database.\n",
                               reply_markup=callinside_markup)
    
@app.on_callback_query(filters.regex("start_owner"))
async def owner(__, c:CallbackQuery):
    await c.message.edit("Hai 👋 conatact us if you want to create you own bot. (paid) else contact me in our group\n\n my id: @nousername_psycho",
                               reply_markup=back_one)
    
@app.on_callback_query(filters.regex("start_new"))
async def new(__, c:CallbackQuery):
    await c.message.edit("**Whats new? 🆕**\n\n"
                         "⌊ Recently we added new Song Recognition🔥\n"
                         "⌊ Added Database (Speed Up Bot)🔥\n"
                         "⌊ Increased Bot Upload Speed🔥\n"
                         "⌊ More in Future \n"
                         "\n\n**What is Song Recognition?**"
                         "\n\nIdentify Song from a Video.? it's also possible, just send "
                         "a short video in our group, then type `/find` cmd reply to your video. Bot will try to fetch the song.",
                               reply_markup=back_one)
    
@app.on_callback_query(filters.regex("start_back"))
async def main(__, c:CallbackQuery):
    user_id = c.from_user.id
    user_name = c.from_user.first_name
    usr_mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    await c.message.delete()
    await c.message.reply_photo(photo=start_img,
                        caption=f"Hello {usr_mention} 👋, Private usage strictly restricted."
                                "if you want to download any song you should join our group "
                                "\n\nAre you intrested in bots? We can make bots with your own needs. contact us : @nousername_pycho",
                        reply_markup=start_markup)


@app.on_message(filters.command('find') & (filters.chat(music_group) | filters.user("nousername_psycho")))
async def get_song_one(___, m: Message):
    chat_id = m.chat.id
    user_id = m.from_user.id
    user_name = m.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    v_file_name = f"videos/newvideo_{m.id}_01.mp4"
    if not m.reply_to_message:
        await m.reply_text("Seriously? This command only works if you reply to a message. 💁🏻‍♀️")
        return
    if not m.reply_to_message.video:
        await m.reply_text("Hello please reply to a short video which you want to find song. 😇")
        return
    else:
        b_r1 = await m.reply_text("Analysing video 🔎")
        await m.reply_to_message.download(file_name=v_file_name)
        
        
        fst_res = await find_song(b_r1, v_file_name)
        print(fst_res)
        os.remove(v_file_name)
        if fst_res == False:
            return
        else:
            await b_r1.edit("Yeah! Got it 😎")
            try:
                results = YoutubeSearch(f"{fst_res}", max_results=1).to_dict()
                title = results[0]['title'][:30]
                duration = results[0]['duration']
                thumbnail = results[0]['thumbnails'][0]
                t1 = title.replace('|', '')
                t2 = t1.replace('/', '')
            except Exception:
                await b_r1.edit(f"Oh Actually I didn't get the song from youtube. but the song name is {fst_res}. find it somewhere else. thank you.")
                
            urllib.request.urlretrieve(thumbnail, f"sample_image{m.id}.jpg")
            link = "https://youtube.com" + results[0]["url_suffix"]
            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
                print(dur)
            try:
                audio = YouTube(link).streams.filter(only_audio=True).get_by_itag('140')
                audio.download(filename=f"MMC-{t2}.mp3")
                await b_r1.edit('✨ Uploading... ⏫')
                xm = await app.send_audio(-1001743584734, audio=f"MMC-{t2}.mp3", thumb=f"sample_image{m.id}.jpg",
                      duration=dur,
                      title=title,
                      performer="🅼🅼🅲 - ᴳʳᵒᵘᵖ",
                      caption=f"⌜ Title: {title}"
                            f"\n﹂ Duration: `{duration}`"
                            f"\n﹂ Link: [Watch Video]({link})"
                            f"\n﹂ Requested by: {mention} "

                            "\n\n🌿 MalluMusicCorner")
                await xm.copy(m.chat.id, reply_to_message_id=m.id, reply_markup=InlineKeyboardMarkup(
                                    [
                                        [InlineKeyboardButton("Send Personally  🍂", url=f'https://t.me/MMC_musicbot?start={xm.id}')]
                                    ]
                                ))
                await b_r1.delete()
                os.remove(f"MMC-{t2}.mp3")
                os.remove(f"sample_image{m.id}.jpg")
            except exceptions.VideoUnavailable:
                await b_r1.edit("Are you sure? Looks like an invalid URL..")
            except exceptions.LiveStreamError:
                await b_r1.edit("How Can i Download Live stream videos?")
            except exceptions as e:
                await b_r1.edit("Hmmm, maybe something went wrong. Wait, I will try to fix it myself.")
                await happ.restart()
app.run()
