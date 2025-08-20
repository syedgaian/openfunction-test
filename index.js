// express-server.js
const express = require("express");
const app = express();
const port = 8080;

app.get("/", (req, res) => {
	res.send("Hello World!");
});

exports.expressApp = (req, res) => {
	app(req, res);
};
