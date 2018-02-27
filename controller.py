import sqlite3
import bottle
from bottle import route, run, static_file, template, request
import datetime
from datetime import datetime

bottle.TEMPLATE_PATH.insert(0, 'templates')

@route('/index')
def index():
    return static_file('index.html', root='./')

@route('/new')
def new():
	return template('todoForm', alert='none')

@route('/list')
def list():
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute('SELECT * FROM filters')
	result = c.fetchone()
	last_filter = result[1]
	last_sort = result[2]
	if(not request.GET.save and not last_filter and not last_sort):
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute('SELECT * from tasks ORDER BY posted')
		result = c.fetchall()
		list_dict = [];
		for row in result:
			list_dict.append({
					'id': row[0],
					'title': row[1],
					'notes': row[2],
					'posted': datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S').date(),
					'lastUpdated': datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S').date(),
					'due': datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S').date(),
					'completed': row[6]
				})


		return template('todo', rows=list_dict, filterby=last_filter, sortby=last_sort)
	elif((not request.GET.save) and last_filter and last_sort):
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute('SELECT * from tasks ' + str(last_filter) + ' ' + str(last_sort))
		result = c.fetchall()
		list_dict = [];
		for row in result:
			list_dict.append({
					'id': row[0],
					'title': row[1],
					'notes': row[2],
					'posted': row[3],
					'lastUpdated': row[4],
					'due': row[5],
					'completed': row[6]
				})
		return template('todo', rows=list_dict, filterby=last_filter, sortby=last_sort)
	else:
		last_filter = request.GET.filter.strip()
		last_sort = request.GET.sort.strip()
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute('SELECT * from tasks ' + request.GET.filter.strip() + ' ' + request.GET.sort.strip())
		result = c.fetchall()
		list_dict = [];
		for row in result:
			list_dict.append({
					'id': row[0],
					'title': row[1],
					'notes': row[2],
					'posted': row[3],
					'lastUpdated': row[4],
					'due': row[5],
					'completed': row[6]
				})
		c.execute('UPDATE filters SET filter=?, sort=? WHERE id=1', (request.GET.filter.strip(), request.GET.sort.strip()))
		conn.commit()
		return template('todo', rows=list_dict, filterby=last_filter, sortby=last_sort)

@route('/toggle', method="POST")
def toggle():
	post_data = request.json;
	print('ID: ' + str(post_data['id']))
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute('SELECT * from tasks WHERE id = ?', (str(post_data['id']),))
	result = c.fetchone()
	data = {
		'id': result[0],
		'title': result[1],
		'notes': result[2],
		'posted': datetime.strptime(result[3], '%Y-%m-%d %H:%M:%S').date(),
		'lastUpdated': datetime.strptime(result[4], '%Y-%m-%d %H:%M:%S').date(),
		'due': datetime.strptime(result[5], '%Y-%m-%d %H:%M:%S').date(),
		'completed': result[6]
	}
	task_completed = 1
	if(data['completed']):
		task_completed = 0
	c = conn.cursor()
	c.execute('UPDATE tasks SET completed=? WHERE id=?', (str(task_completed), str(post_data['id'])))
	conn.commit()
	bottle.redirect('/list')

@route('/edit/<no:int>')
def edit(no):
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute('SELECT * from tasks WHERE id = ?', str(no))
	result = c.fetchone()
	data = {
		'id': result[0],
		'title': result[1],
		'notes': result[2],
		'posted': datetime.strptime(result[3], '%Y-%m-%d %H:%M:%S').date(),
		'lastUpdated': datetime.strptime(result[4], '%Y-%m-%d %H:%M:%S').date(),
		'due': datetime.strptime(result[5], '%Y-%m-%d %H:%M:%S').date(),
		'completed': result[6]
	}
	return template('edit', row=data)

@route('/update', method='POST')
def update():
	title = request.POST.title
	notes = request.POST.notes
	posted = str(datetime.strptime(request.POST.posted, '%Y-%m-%d'))
	last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	due = str(datetime.strptime(request.POST.due, '%Y-%m-%d'))
	completed = request.POST.completed
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("UPDATE tasks SET title=?, notes=?, posted=?, lastUpdated=?, due=?, completed=? WHERE id=?", (title, notes, posted, last_updated, due, completed, str(request.POST.id)))
	conn.commit()
	bottle.redirect('/list')

@route('/add', method='POST')
def add():
	if(not request.POST.title or not request.POST.notes or not request.POST.due):
		return template('todoForm', alert='missing')
	elif(datetime.strptime(request.POST.due, '%Y-%m-%d') < datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')):
		return template('todoForm', alert='bad date')
	else:
		title = request.POST.title
		notes = request.POST.notes
		posted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		last_updated = posted
		due = str(datetime.strptime(request.POST.due, '%Y-%m-%d'))
		completed = 0
		conn = sqlite3.connect('todo.db')
		c = conn.cursor()
		c.execute('INSERT INTO tasks(title, notes, posted, lastUpdated, due, completed) VALUES(?,?,?,?,?,?)', (title, notes, posted, last_updated, due, completed))
		conn.commit()
		bottle.redirect('/list')

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

@route('/scripts/<filename:path>')
def send_static(filename):
    return static_file(filename, root='scripts/')

run(host='localhost', port=8080, debug=True)
