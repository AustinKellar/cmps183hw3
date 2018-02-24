import sqlite3
import bottle
from bottle import route, run, static_file, template, request

bottle.TEMPLATE_PATH.insert(0, 'templates')

@route('/index')
def index():
    return static_file('index.html', root='./')

@route('/list')
def todo():
	if(not request.GET.save):
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute('SELECT * from tasks ORDER BY posted')
		result = c.fetchall()
		return template('todo', rows=result)
	else:
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute('SELECT * from tasks ' + request.GET.filter.strip() + ' ' + request.GET.sort.strip())
		result = c.fetchall()
		return template('todo', rows=result)

@route('/edit/<no:int>')
def edit(no):
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute('SELECT * from tasks WHERE id = ?', str(no))
	result = c.fetchone()
	return template('edit', rows=result)

@route('/delete/<no:int>')
def delete(no):
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute('DELETE from tasks WHERE id=?', str(no))
	conn.commit()
	bottle.redirect('/list')

@route('/css/<filename:path>')
def send_static(filename):
    return static_file(filename, root='css/')

@route('/images/<filename:path>')
def send_static(filename):
    return static_file(filename, root='images/')

run(host='localhost', port=8080, debug=True)
