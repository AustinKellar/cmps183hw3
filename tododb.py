import sqlite3
import datetime

conn = sqlite3.connect('todo.db')
c = conn.cursor()

def drop_table():
	c.execute('DROP TABLE tasks')
	conn.commit()

def create_table():
	c.execute('CREATE TABLE tasks(id INTEGER PRIMARY KEY, title varchar(255), notes varchar(255), posted DATE, lastUpdated DATE, due DATE, completed BOOLEAN)')
	conn.commit()

def insert_data():
	title = 'Create a profile for Peter Parker'
	notes = 'These are the notes for creating such a profile'
	posted = datetime.datetime(2018, 2, 2, 0, 0)
	lastUpdated = datetime.datetime(2018, 2, 3, 0, 0)
	due = datetime.datetime(2018, 2, 5, 0, 0)
	completed = False
	c.execute("INSERT INTO tasks(title, notes, posted, lastUpdated, due, completed) VALUES(?,?,?,?,?,?)", (title, notes, posted, lastUpdated, due, completed))
	conn.commit()

	title = 'Create a todo list for Peter Parker'
	notes = 'These are the notes for creating such a todo list'
	posted = datetime.datetime(2018, 3, 2, 0, 0)
	lastUpdated = datetime.datetime(2018, 3, 3, 0, 0)
	due = datetime.datetime(2018, 3, 5, 0, 0)
	completed = True
	c.execute("INSERT INTO tasks(title, notes, posted, lastUpdated, due, completed) VALUES(?,?,?,?,?,?)", (title, notes, posted, lastUpdated, due, completed))
	conn.commit()

	title = 'Create a submit form for todo list'
	notes = 'These are the notes for creating such a form'
	posted = datetime.datetime(2018, 4, 2, 0, 0)
	lastUpdated = datetime.datetime(2018, 4, 3, 0, 0)
	due = datetime.datetime(2018, 4, 5, 0, 0)
	completed = False
	c.execute("INSERT INTO tasks(title, notes, posted, lastUpdated, due, completed) VALUES(?,?,?,?,?,?)", (title, notes, posted, lastUpdated, due, completed))
	conn.commit()

	title = 'Make some lunch'
	notes = 'Remember to buy food before making lunch'
	posted = datetime.datetime(2018, 5, 2, 0, 0)
	lastUpdated = datetime.datetime(2018, 5, 3, 0, 0)
	due = datetime.datetime(2018, 5, 5, 0, 0)
	completed = True
	c.execute("INSERT INTO tasks(title, notes, posted, lastUpdated, due, completed) VALUES(?,?,?,?,?,?)", (title, notes, posted, lastUpdated, due, completed))
	conn.commit()

	title = 'Eat some lunch'
	notes = 'Eat the lunch I just made'
	posted = datetime.datetime(2018, 6, 2, 0, 0)
	lastUpdated = datetime.datetime(2018, 6, 3, 0, 0)
	due = datetime.datetime(2018, 6, 5, 0, 0)
	completed = False
	c.execute("INSERT INTO tasks(title, notes, posted, lastUpdated, due, completed) VALUES(?,?,?,?,?,?)", (title, notes, posted, lastUpdated, due, completed))
	conn.commit()

	title = 'Turn in this assignment'
	notes = 'This assignment is due soon'
	posted = datetime.datetime(2018, 7, 2, 0, 0)
	lastUpdated = datetime.datetime(2018, 7, 3, 0, 0)
	due = datetime.datetime(2018, 7, 5, 0, 0)
	completed = False
	c.execute("INSERT INTO tasks(title, notes, posted, lastUpdated, due, completed) VALUES(?,?,?,?,?,?)", (title, notes, posted, lastUpdated, due, completed))
	conn.commit()

def query():
	c.execute('SELECT title FROM tasks WHERE id=3')
	print(c.fetchone()[0])

drop_table()
create_table()
insert_data()


