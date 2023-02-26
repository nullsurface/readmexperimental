const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");


const app = express();
app.set('view engine', 'ejs');

// EXPRESS' built-in body parser
app.use(express.json());
app.use(express.urlencoded({
  extended: true
}));

app.use(express.static("public"));



app.get("/", function(req, res){
  res.render("index");
});

let port = process.env.PORT;
if(port == null || port == ""){
  port = 3000;
}
app.listen(port, function() {
  console.log("Server started successfully.");
});