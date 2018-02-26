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
						<select name="filter">
							<option value="">Show: All</option>
							<option value="WHERE completed = 1">Show: Completed</option>
							<option value="WHERE completed = 0">Show: To Do</option>
						</select>
		
						<select name="sort">
							<option value="ORDER BY posted">Sort By: Posted</option>
							<option value="ORDER BY lastUpdated">Sort By: Last Updated</option>
							<option value="ORDER BY due">Sort By: Due</option>
						</select>

						<input type="submit" name="save" value="save">
					</form>
							
				</div>
			</div>
			<div class="col-sm-3 sidenav">
				<h2 class="text-center marker underlined">Resources</h2><br>
				<ol style="padding-right:30px;">
					<li>
						How to create a custom AngularJS filter for <a href="https://stackoverflow.com/questions/14478106/angularjs-sorting-by-property">order by</a>
						table attribute
					</li><br>
					<li>
						How to use <a href="https://www.w3schools.com/angular/ng_ng-disabled.asp">ng-disabled</a>
						to disable textareas conditionally
					</li><br>
					<li>
						Getting and setting JS objects from <a href="https://stackoverflow.com/questions/2010892/storing-objects-in-html5-localstorage">local storage</a>
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