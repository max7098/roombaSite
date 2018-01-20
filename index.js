const express = require('express')
const app = express()
const http = require('http').Server(app)

//index
app.get('/',mainPage)
function mainPage(req,res){
    res.sendFile(__dirname+'/index.html')
}

//drive
app.get('/drive',drivePage)
function drivePage(req,res){
    res.sendFile(__dirname+'/public/drive.html')
}

http.listen((process.env.PORT || 3000), function(){
    console.log('listening on *:3000')  
})
