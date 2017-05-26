'use strict';

require('dotenv').config();

var incan_client = require('node-incandescent-client').client;

var client = new incan_client(process.env.uid, process.env.api_key);

var prettyjson = require('prettyjson');

client.addImageUrl('https://s3-us-west-2.amazonaws.com/incandescantapisample/andy.jpg');

client.assemble();

client.sendRequest(function(projectId) {
	console.log(projectId);

	client.getResults(projectId, function(data) {
		console.log(prettyjson.render(data, {}));
	})
});
