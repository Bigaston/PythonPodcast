import mutagen
import os
import datetime
import math
import json
from functools import cmp_to_key

config = __import__("config")

def get_all_audio():
  audio_files = list(filter(filter_mp3, os.listdir("./public/audio")))

  files = list()

  for f in audio_files:
    files.append(get_one_audio(f))

  files.sort(key=cmp_to_key(filterByDate))

  return files

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

    if os.path.isfile("./public/audio/" + slug.replace(".mp3", "") + ".json"):
      rawData = open("./public/audio/" + slug.replace(".mp3", "") + ".json", "r", encoding="utf8")
      otherData = json.load(rawData)

      for key in otherData:
        dataDict[key] = otherData[key]

    return {
      "data": dataDict,
      "modifDate": datetime.datetime.fromtimestamp(os.stat("./public/audio/" + slug).st_mtime),
      "fileSize": os.stat("./public/audio/" + slug).st_size,
      "slug": slug.replace(".mp3", "")
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

def filterByDate(elem1, elem2):
  modificator = 0

  if config.podcast["itunes_type"] == "episodic":
    modificator = 1
  else:
    modificator = 0

  if elem1["modifDate"] > elem2["modifDate"]:
    return 1 * modificator
  elif elem1["modifDate"] < elem2["modifDate"]:
    return -1 * modificator
  else:
    return 0