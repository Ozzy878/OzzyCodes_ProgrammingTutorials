from bottle import route, run, template


@route('/hello/<user>')
def index(user):
    return template('<h2>Hello World from {{user}}!</h2>', user=user)


run(host='localhost', port=1234, debug=True)

# Go to browser and point to (http://localhost:1234/hello/ozzycodes)
