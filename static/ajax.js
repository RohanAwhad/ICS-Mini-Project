$('#rohan').submit(function(event){
	event.preventDefault();
	var formData = $(this).serialize();
	$.post('/rohan', formData, function(data){
		var obj = JSON.parse(data);
		$('#rohan #encrypted-msg-rohan')[0]['value'] = obj['ciphertext'];
		$('#rohan #sent-msg-rohan')[0]['value'] = '';
		$('#shivdeep #received-msg-shivdeep')[0]['value'] = obj['ciphertext'];
		$('#shivdeep #decrypted-msg-shivdeep')[0]['value'] = obj['plaintext'];
	})
});

$('#shivdeep').submit(function(event){
	event.preventDefault();
	var formData = $(this).serialize();
	$.post('/shivdeep', formData, function(data){
		var obj = JSON.parse(data);
		$('#shivdeep #encrypted-msg-shivdeep')[0]['value'] = obj['ciphertext'];
		$('#shivdeep #sent-msg-shivdeep')[0]['value'] = '';
		$('#rohan #received-msg-rohan')[0]['value'] = obj['ciphertext'];
		$('#rohan #decrypted-msg-rohan')[0]['value'] = obj['plaintext'];
	})
});
