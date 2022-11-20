const sio = require("socket.io-client");

var express = require('express');
const app = express()
const server = require('http').createServer(app)
const io = require('socket.io')(server, {cors: { origin: "*"}})
var isRecording = false
var recordingCoordinates = {"coords": [["test","data"],["another","coord"]]}
var recordStatus = {"status": isRecording}
var CONFIG = require('./config.json');

function load_cfg(){

}

load_cfg()

const socket = sio('http://'+CONFIG.coordinate_server_address+':'+CONFIG.coordinate_server_port)
socket.on('connect', () =>{
  console.log("Connected to Coordinate provider server!")
})
socket.on("ship_data", (data) => {
  if (CONFIG.print_new_coordinate){
    console.log("New coordinate: "+ JSON.stringify(data))
  }
  io.emit('new_ship_coordinate', data)
})

server.listen(CONFIG.backend_server_port, () => {
  console.log("Server running and listening..")
})

io.on('connection', (socket) => {
  console.log("User connected with id: "+ socket.id)
  if(isRecording){
    io.to(socket.id).emit('recording',recordStatus)
    io.to(socket.id).emit('recordCoordinates',recordingCoordinates)
  }
  socket.on("recording", (data) => {
    if (!isRecording){
      console.log("Recording started!")
      socket.broadcast.emit('message', "Somebody started the recording!")
      isRecording = true
    }else{
      console.log("Recording already started!")
    }
  })

})