var express = require('express');
var app = express();
var path = require('path');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const URL = process.env.URL || 'http://localhost:4000/api';

app.get('/', async function(req, res) {
    try {
        const response = await fetch(URL, { method: 'GET' });
        const data = await response.json();
        res.render('index', { data: data });
    } catch (err) {
        console.error('Error fetching API:', err);
        res.status(500).json({ msg: 'Error fetching data' });
    }
});

app.listen(3000, function() {
    console.log('App listening on port 3000!');
});