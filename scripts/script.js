function clickCheckbox(cb, id) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", '/toggle', true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify({
	    id: id
	}));
}