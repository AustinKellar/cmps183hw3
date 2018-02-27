<!DOCTYPE html>
<html ng-app="app">
	<head>
		<link rel="stylesheet" type="text/css" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Permanent+Marker" />
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
			<div class="col-sm-9 form" style="padding-top: 40px; padding-left: 40px; padding-right: 40px">
				<form action="/add" method="post">
					<div class="row">
						<div class="col-sm-4">
							<label>Task Title:</label><br>
							<textarea name="title"></textarea>
						</div>
						<div class="col-sm-4">
							<label>Due Date:</label><br>
							<input name="due" type="date">
						</div>
						<div class="col-sm-4">
							<label>Notes:</label><br>
							<textarea name="notes"></textarea>
						</div>
					</div>
					<div class="row">
						<br>
						<input type="submit" name="submit" value="submit" style="position:relative; left:15px;" class="marker">
					</div>
					<div class="row">
						<div class="col-sm-8">
							<br>
							%if(alert == 'missing'):
								<label>Please fill out all of the fields!</label>
							%elif(alert == 'bad date'):
								<label>Make sure your due date is not in the past</label>
							%end
						</div>
					</div>
				</form>
			</div>
			<div class="col-sm-3 sidenav">
				<h2 class="text-center marker underlined">Notes</h2><br>
				<ol style="padding-right:30px;">
					<li>
						This page was fairly simple to create
					</li><br>
					<li>
						I don't really have anything to link here because I didn't look anything up
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