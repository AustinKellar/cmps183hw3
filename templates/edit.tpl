<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="../css/style.css">
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
			<form action='/update' method='post'>
				<div class="row" style="padding-left: 20px;">
					<div class="col-sm-4">
						<label>ID:   </label>
						<input style="background-color:#f21f1f; border: none;" name="id" size="2" value="{{row['id']}}">
					</div>
				</div><br>
				<div class="row" style="padding-left: 20px;">
					<div class="col-sm-4">
						<label>Title</label><br>
						<textarea name="title">{{row['title']}}</textarea>
					</div>
					<div class="col-sm-4">
						<label>Notes</label><br>
						<textarea name="notes">{{row['notes']}}</textarea>
					</div>
					<div class="col-sm-4">
						<label>Status</label><br>
						%if(not row['completed']):
							<select name="completed">
								<option value="0">Not Completed</option>
								<option value="1">Completed</option>
							</select>
						%else:
							<select name="completed">
								<option value="1">Completed</option>
								<option value="0">Not Completed</option>
							</select>
						%end
					</div>
				</div><br>
				<div class="row" style="padding-left: 20px;">
					<div class="col-sm-4">
						<label>Posted</label><br>
						<input name="posted" type="date" value="{{row['posted']}}">
					</div>
					<div class="col-sm-4">
						<label>Last Updated</label><br>
						<input name="lastUpdated" type="date" value="{{row['lastUpdated']}}">
					</div>
					<div class="col-sm-4">
						<label>Due</label><br>
						<input name="due" type="date" value="{{row['due']}}">
					</div>
				</div>
				<div class="row" style="padding-left: 20px;">
					<div class="col-sm-4">
						<br>
						<input type="submit" name="save" value="save">
					</div>
				</div>
			</form>
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