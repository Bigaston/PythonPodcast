from bottle import run
import index

run(host='localhost', port=8080, debug=True, reloader=True)
