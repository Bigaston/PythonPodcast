import mutagen
import os
import datetime
import math

def get_all_audio():
  audio_files = list(filter(filter_mp3, os.listdir("./public/audio")))

  fileDict = {}

  for f in audio_files:
    fileDict[f.replace(".mp3", "")] = get_one_audio(f)

  return fileDict

def get_one_audio(slug):
  audio_files = list(filter(filter_mp3, os.listdir("./public/audio")))

  if slug in audio_files:
    audio = mutagen.File("./public/audio/" + slug)

    dataDict = {
      "title": audio.tags.get("TIT2"),
      "duration": sToHms(audio.info.length)
    }

    if (len(audio.tags.getall("COMM")) != 0):
      dataDict["description"] = audio.tags.getall("COMM")[0].text[0]
    else:
      dataDict["description"] = ""

    if (audio.tags.getall("APIC") != 0):
      dataDict["img"] = {
        "mime": audio.tags.getall("APIC")[0].mime,
        "data": audio.tags.getall("APIC")[0].data
      }
    else:
      dataDict["img"] = None

    return {
      "data": dataDict,
      "modifDate": datetime.datetime.fromtimestamp(os.stat("./public/audio/" + slug).st_mtime).strftime("%a, %d %b %Y %H:%M:%S +0200"),
      "fileSize": os.stat("./public/audio/" + slug).st_size
    }
  else:
    return None

def filter_mp3(file):
  if file.endswith(".mp3"):
    return True
  else:
    return False

def sToHms(seconds):
  nbSec = seconds

  heure = math.trunc(nbSec / 3600)
  if heure < 10:
    heure = "0" + str(heure)
  else:
    heure = str(heure)

  nbSec = nbSec % 3600
  minute = math.trunc(nbSec / 60)

  if minute < 10:
    minute = "0" + str(minute)
  else:
    minute = str(minute)

  nbSec = nbSec % 60

  seconde = math.trunc(nbSec)

  if seconde < 10:
    seconde = "0" + str(seconde)
  else:
    seconde = str(seconde)

  return heure + ":" + minute + ":" + seconde
