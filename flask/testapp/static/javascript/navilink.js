function sendPost(event) {
	// alert("aaaaaaaaaaaaa")
	event.preventDefault();
	var form = document.createElement('form');
	form.action = event.target.href;
	form.method = 'post';
	document.body.appendChild(form);
	form.submit();
}
