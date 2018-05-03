var express = require('express');
var path = require('path')
var bp = require('body-parser');

var app = express();
app.set('view engine', 'ejs');
app.use(bp());
app.get('/', function(req, res){
   // res.sendFile('index.html', {root: path.join(__dirname, './html')})
   res.render('index.ejs')
});

app.post('/', function(req, res){
  console.log(req.body);

    var acre_arr = new Array("N/A - GQ/not a one-family house or mobile home",
                             "House on less than one acre",
                             "House on one to less than ten acres",
                             "House on ten or more acres");

    var ten_arr = new Array("N/A - GQ/vacant",
                            "Owned with mortgage or loan",
                            "Owned free and clear",
                            "Rented",
                            "Occupied without payment of rent");

    var year_arr = new Array("N/A - GQ", "1939 or earlier", "1940 to 1949",
                             "1950 to 1959", "1960 to 1969", "1970 to 1979",
                             "1980 to 1989", "1990 to 1999", "2000 to 2004",
                             "2005", "2006", "2007", "2008", "2009", "2010",
                             "2011", "2012", "2013", "2014", "2015", "2016");


    var spawn = require('child_process').spawn;
    var process = spawn('python3', ["./models_function.py",
      req.body.age,
      req.body.mar,
      req.body.nfm,
      req.body.wage,
      req.body.edu,
      req.body.mot,
      req.body.sex,
      req.body.eth,
      req.body.nov,
      req.body.dis,
      req.body.tfi,
      req.body.ctz
    ]);

    process.stdout.on('data', function(data) {
      console.log(data.toString());
      var values = data.toString();
      var r = values.split(',');
      if ( r[3] == "True"){
        r[3] = "Yes"
      }
      else{
        r[3] = "No"
      }
      console.log(r);
      res.render('response.ejs', {acres:acre_arr[r[0].trim()], beds:r[1], mort:r[2],
                                  wat:r[3], ten:ten_arr[r[4].trim()], year:year_arr[r[5].trim()]});

      // res.writeHead(200, {
      //   'Content-Type': 'text/plain'
      // });
      // res.write(data.toString());
      // res.end();
      // res.send(data.toString());
      // res.end(JSON.stringify(req.body));
    });

});

app.listen(6622, function() {
  console.log('Server Running - Listening at port 6622');
});
