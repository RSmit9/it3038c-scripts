const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
	  myHostName=os.hostname();
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
	
	
	
	
	
	
	sec = os.uptime();
	min = sec/60;
	hour = min/60;
	day = hour /24;
	
	sec= Math.floor(sec);
	min = Math.floor(min);
	hour = Math.floor(hour);
	day = Math.floor(day);
	
	day = day%24
	hour = hour%60
	min = min%60
	sec = sec%60
	
	
	
	
	
	
	
	
	
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
  <p>Server Uptime: ${day} Days ${hour} hours ${min} minutes ${sec} seconds  </p>
        <p>Total Memory: ${os.totalmem()/ 1000000} MB </p>
        <p>Free Memory: ${os.freemem()/1000000} MB </p>
        <p>Number of CPUs: ${os.cpus().length} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
