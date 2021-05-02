import music_tag
import os
import datetime

def get_all_audio():
  audio_files = list(filter(filter_mp3, os.listdir("./static/audio")))

  fileDict = {}

  for f in audio_files:
    fileDict[f.replace(".mp3", "")] = {
      "data": music_tag.load_file("./static/audio/" + f),
      "modifDate": datetime.datetime.fromtimestamp(os.stat("./static/audio/" + f).st_mtime).strftime("%a, %d %b %Y %H:%M:%S +0200")
    }
  
  return fileDict

def get_one_audio(slug):
  audio_files = list(filter(filter_mp3, os.listdir("./static/audio")))

  print()

  if slug in audio_files:
    return {
      "data": music_tag.load_file("./static/audio/" + slug),
      "modifDate": datetime.datetime.fromtimestamp(os.stat("./static/audio/" + slug).st_mtime).strftime("%a, %d %b %Y %H:%M:%S +0200")
    }
  else:
    return None

def filter_mp3(file):
  if file.endswith(".mp3"):
    return True
  else:
    return False