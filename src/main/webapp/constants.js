function randomString(length) {
	var text = "";
	var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
	for (var i = 0; i < length; i++)
		text += possible.charAt(Math.floor(Math.random() * possible.length));
	return text;
}

var connectionInfo = {
	host: "broker.mqttdashboard.com",
	port: 8000,
	clientID: "knobGaugeClient-" + randomString(10),
	topic: "bastide/grove/potentiometer"
};