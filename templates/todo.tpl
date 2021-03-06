<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Permanent+Marker" />
		<script src="scripts/script.js"></script>
		<title>HW3</title>
		<meta charset="utf-8"/>
	</head>
	<body>
		<div class="row">
			<header class="marker">
				<h1>CMPS 183: Homework 3</h1>
			</header>
		</div>
		<div class="row">
			<div class="navbar white marker">
				<ul>
					<li><a href="/index">Home</a></li>
					<li><a href="/list">To Do</a></li>
					<li><a href="/new">To Do Form</a></li>
				</ul>
			</div>
		</div>
		<div class="main-body">
			<div class="col-sm-9 todo" style="padding-top: 20px;">
				<div class="col-sm-12">
					<h2 class="text-center marker">To Do List</h2>
					<table style="display: block; margin: auto;">
						<tr>
							<th>ID</th>
							<th>Task Title</th>
							<th>Notes</th>
							<th>Posted</th>
							<th>Last Updated</th>
							<th>Due Date</th>
							<th>Completed</th>
							<th>Edit</th>
							<th>Delete</th>
						</tr>
						%for row in rows:
							<tr>
								<td>{{row['id']}}</td>
								<td>{{row['title']}}</td>
								<td>{{row['notes']}}</td>
								<td>{{row['posted']}}</td>
								<td>{{row['lastUpdated']}}</td>
								<td>{{row['due']}}</td>
								%if(row['completed']):
									<td><input type="checkbox" style="margin: auto; display: block;" onclick='clickCheckbox(this, {{row['id']}});' checked></td>
								%else:
									<td><input type="checkbox" style="margin: auto; display: block;" onclick='clickCheckbox(this, {{row['id']}});'></td>
								%end
								<td><a href="/edit/{{row['id']}}">Edit</a></td>
								<td><a href="/delete/{{row['id']}}">Delete</a></td>
							</tr>
						%end
					</table>
					<form action="/list" method="get">
						%if(not filterby or filterby == ''):
							<select name="filter">
								<option value="" selected="selected">Show: All</option>
								<option value="WHERE completed = 1">Show: Completed</option>
								<option value="WHERE completed = 0">Show: To Do</option>
							</select>
						%elif(filterby=='WHERE completed = 1'):
							<select name="filter">
								<option value="">Show: All</option>
								<option value="WHERE completed = 1" selected="selected">Show: Completed</option>
								<option value="WHERE completed = 0">Show: To Do</option>
							</select>
						%else:
							<select name="filter">
								<option value="">Show: All</option>
								<option value="WHERE completed = 1">Show: Completed</option>
								<option value="WHERE completed = 0" selected="selected">Show: To Do</option>
							</select>
						%end

						%if(sortby == 'ORDER BY posted'):
							<select name="sort">
								<option value="ORDER BY posted" selected="selected">Sort By: Posted</option>
								<option value="ORDER BY lastUpdated">Sort By: Last Updated</option>
								<option value="ORDER BY due">Sort By: Due</option>
							</select>
						%elif(sortby == 'ORDER BY lastUpdated'):
							<select name="sort">
								<option value="ORDER BY posted">Sort By: Posted</option>
								<option value="ORDER BY lastUpdated" selected="selected">Sort By: Last Updated</option>
								<option value="ORDER BY due">Sort By: Due</option>
							</select>
						%else:
							<select name="sort">
								<option value="ORDER BY posted">Sort By: Posted</option>
								<option value="ORDER BY lastUpdated">Sort By: Last Updated</option>
								<option value="ORDER BY due" selected="selected">Sort By: Due</option>
							</select>
						%end

						<input type="submit" name="save" value="save" class="marker">
					</form>
							
				</div>
			</div>
			<div class="col-sm-3 sidenav">
				<h2 class="text-center marker underlined">Resources</h2><br>
				<ol style="padding-right:30px;">
					<li>
						How to send a <a href="https://www.w3schools.com/xml/ajax_xmlhttprequest_send.asp">post</a>
						request with plain JavaScript
					</li><br>
					<li>
						How to  <a href="https://www.w3schools.com/sql/sql_orderby.asp">sort</a>
						the results of an SQL query
					</li><br>
					<li>
						How to use <a href="https://docs.python.org/2/library/datetime.html">datetime</a>
						objects in Python
					</li>
				</ol>
			</div>
		</div>
		<div class="row">
			<footer class="footer">
				<div class="footer-navbar white">
					<ul>
						<li><a href="#">About Us</a></li>
						<li><a href="#">Privacy</a></li>
						<li><a href="#">Credits</a></li>
						<li><a href="#">Contact Us</a></li>
					</ul>
				</div>
			</footer>
		</div>
	</body>
</html>