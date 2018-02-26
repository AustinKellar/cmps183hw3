import sqlite3
import bottle
from bottle import route, run, static_file, template, request
import datetime
from datetime import datetime

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


		return template('todo', rows=list_dict)
	else:
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
		return template('todo', rows=list_dict)

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
	last_updated = str(datetime.strptime(request.POST.lastUpdated, '%Y-%m-%d'))
	due = str(datetime.strptime(request.POST.due, '%Y-%m-%d'))
	completed = request.POST.completed
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	print('ID: '+str(request.POST.id))
	print("UPDATE tasks SET title="+title+",notes="+notes+",posted="+posted+",lastUpdated="+last_updated+",due="+due+",completed="+completed+" WHERE id="+str(request.POST.id))
	c.execute("UPDATE tasks SET title=?, notes=?, posted=?, lastUpdated=?, due=?, completed=? WHERE id=?", (title, notes, posted, last_updated, due, completed, str(request.POST.id)))
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
