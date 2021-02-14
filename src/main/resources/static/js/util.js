function randomString(length) {
	var text = "";
	var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
	for (var i = 0; i < length; i++)
		text += possible.charAt(Math.floor(Math.random() * possible.length));
	return text;
}

function connectionInfo(loc) {
	return {
		host: "test.mosquitto.org",
		//host: 'broker.hivemq.com',
		//port: 1883,
		port: loc.protocol == 'http:' ? 8080 : 8081,
		clientID: "knobGaugeClient-" + randomString(10),
		topic: "bastide/grove/potentiometer"
	}
};