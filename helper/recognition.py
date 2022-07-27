from shazamio import Shazam
shazam = Shazam()

async def find_song(m, file_name):
    await m.edit("Hmmm Let me try... 💁🏻‍♀️")
    out = await shazam.recognize_song(file_name)
    try:
        item = out.get("track")
        title = item.get("title")
        artist = item.get("subtitle")
        query = (f"{title} - {artist}")
        return query
    except Exception: 
        await m.edit("Oh sorry I don't know this song.. ☹️ ")
        return False