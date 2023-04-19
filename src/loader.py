from PIL import Image
from src import motdtoimage
from base64 import b64decode
from io import BytesIO
from mcstatus import JavaServer


def loadandrun(servername, serverip):
    try:
        status = JavaServer.lookup(serverip, 2)
    except Exception as e:
        print(e)
        status = JavaServer(serverip)
    status = status.status()
    try:
        logo = Image.open(BytesIO(b64decode(status.favicon.partition(",")[2])))
    except:
        logo = Image.open(BytesIO(b64decode("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")))
    # r = requests.get(url=f"https://api.mcsrvstat.us/2/{serverip}")
    # r=r.json()
    # html = r['motd']['html']
    onlineplayers = str(status.players.online)
    playerstotal = str(status.players.max)
    motd = status.description
# Define a dictionary to map Minecraft color codes to HTML color codes
    color_map = {
        "0": "#000000",  # Black
        "1": "#0000AA",  # Dark Blue
        "2": "#00AA00",  # Dark Green
        "3": "#00AAAA",  # Dark Aqua
        "4": "#AA0000",  # Dark Red
        "5": "#AA00AA",  # Dark Purple
        "6": "#FFAA00",  # Gold
        "7": "#AAAAAA",  # Gray
        "8": "#555555",  # Dark Gray
        "9": "#5555FF",  # Blue
        "a": "#55FF55",  # Green
        "b": "#55FFFF",  # Aqua
        "c": "#FF5555",  # Red
        "d": "#FF55FF",  # Light Purple
        "e": "#FFFF55",  # Yellow
        "f": "#FFFFFF",  # White
    }
    zamns = motd.split("\u00a7")
# Bolding and italics
    total = 0
    for index, section in enumerate(zamns):
        first = section[:1].lower()
        if first in color_map.keys():
            count = len(
                list(filter(lambda word: "<span style='" in word, zamns[:index])))
            count2 = len(
                list(filter(lambda word: "</span>" in word, zamns[:index])))
            zamns[index] = f"<span style='color:{color_map[first]}'>"+section[1:]
            total += 1
            for i in range(count-count2):
                zamns[index] = "</span>"+zamns[index]
                total -= 1
        elif first == "l":
            zamns[index] = "<span style='font-weight:bold;'>" + section[1:]
            total += 1
        elif first == "o":
            zamns[index] = "<span style='font-style:italic;'>"+section[1:]
            total += 1

    zamns = "".join(zamns)
    if total != 0:
        for i in range(abs(total)):
            zamns += "</span>"
            total -= 1
    motd = zamns
    return motdtoimage.getmotdtoimg(
        motd, logo, (onlineplayers, playerstotal), servername)
