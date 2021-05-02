from bottle import get, run, template, response, static_file
import datetime

config = __import__("config")

@get('/rss')
def send_rss():
  base_rss = open("./basic_rss.xml", "r", encoding="utf8").read()

  print(config.podcast["title"])

  response.set_header("content-type", "text/xml")
  return template(base_rss, {
    "config": config,
    "build_date": datetime.datetime.today().strftime("%a, %d %b %Y %H:%M:%S GMT")
  })

@get("/static/<file>")
def send_static(file):
  return static_file(file, "./static")

run(host='localhost', port=8080, debug=True, reloader=True)