from bottle import get, template, response, static_file, abort, run, Bottle
import datetime
import mimetypes
import sys

app = application = Bottle()

config = __import__("config")
audio = __import__("audio")

@app.get('/rss')
def send_rss():
  base_rss = open("./template/basic_rss.xml", "r", encoding="utf8").read()

  audioFiles = audio.get_all_audio()

  response.set_header("content-type", "text/xml")
  return template(base_rss, {
    "config": config,
    "build_date": datetime.datetime.today().strftime("%a, %d %b %Y %H:%M:%S +0200"),
    "episodes": audioFiles
  })

@app.get("/img/<slug>")
def get_episode_image(slug):
  audioInfo = audio.get_one_audio(slug + ".mp3")

  if audioInfo == None:
    abort(404, "No episode called " + slug)

  response.set_header("content-type", audioInfo["data"]["img"]["mime"])
  return audioInfo["data"]["img"]["data"]  

@app.get("/public/<file:path>")
def send_public(file):
  return static_file(file, "./public")

@app.get("/ep/<slug>")
def send_episode(slug):
  audioInfo = audio.get_one_audio(slug + ".mp3")

  if audioInfo == None:
    abort(404, "No episode called " + slug)

  base_html = open("./template/episode.html", "r", encoding="utf8").read()

  response.set_header("content-type", "text/html")
  return template(base_html, {
    "config": config,
    "episode": audioInfo
  })

@app.get("/")
def send_index():
  base_html = open("./template/index.html", "r", encoding="utf8").read()

  audioFiles = audio.get_all_audio()

  response.set_header("content-type", "text/html")
  return template(base_html, {
    "config": config,
    "episodes": audioFiles
  })

class StripPathMiddleware(object):
    '''
    Get that slash out of the request
    '''
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == "__main__":
  if (len(sys.argv) > 1):
    run(app=StripPathMiddleware(app), host='localhost', port=8080, debug=True, reloader=True)
  else:
    run(app=StripPathMiddleware(app), server='paste', port=7890)