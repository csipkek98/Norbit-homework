<template>
  <div id="app">
    <div class="cell cell-map">
      <MapContainer :model="curr_cord" />
    </div>
    <div class="cell cell-edit">
      List of recordings:
    </div>
    <div class="cell cell-inspect">
      <button ref="recordButton" @click="startRecording()">RECORD</button>
    </div>
  </div>
</template>

<script>
import MapContainer from './components/MapContainer.vue';
import { ref } from 'vue'
var CONFIG = require('./config.json');
const socket = io('http://' + CONFIG.backend_server_address + ':' + CONFIG.backend_server_port)

socket.on('connection')
socket.on('message', (data) => {
  console.log(data)
})
socket.on('recordCoordinates', (data) => {
  console.log(data)
})
socket.on('new_ship_coordinate', (data) => {
  if (CONFIG.print_new_coordinate) {
    console.log("NEW COORDINATE: " + JSON.stringify(data))
  }
  current_coordinate = [data["lon"], data["lat"], data["heading"]]
})
socket.on('recording', (data) => {
  const recordButton = ref(null)
  test(recordButton)
  function test(button) {
    if (button === undefined) {
      setTimeout(() => { console.log("Wait for render.."); }, 1000);
    } else {
      manageButton(button)
    }
  }
  function manageButton(button) {
    if (data["status"]) {
      console.log(button)
      button.disabled
    } else {
      button.disabled = false
    }
  }
})

var current_coordinate = [20.74002805, 48.21352366, 0.555499611]


export default {

  name: "App",
  components: { MapContainer },
  data: () => ({
    curr_cord: current_coordinate
  }),
  methods: {
    startRecording() {
      socket.emit('recording')
    }
  },
  watch: {
    curr_cord: {
      handler(val) {
        console.log(val);
      },
      deep: true,
    },
  },
} 
</script>

<style>
html,
body {
  height: 100%;
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  height: 100%;
  display: grid;
  grid-template-columns: 100vh;
  grid-auto-rows: 1fr;
  grid-gap: 1rem;
  padding: 1rem;
  box-sizing: border-box;
}

.cell {
  color: black;
  border-radius: 4px;
  background-color: lightgrey;
}

.cell-map {
  grid-column: 1;
  grid-row-start: 1;
  grid-row-end: 3;
}

.cell-edit {
  grid-column: 2;
  grid-row: 1;
}

.cell-inspect {
  grid-column: 2;
  grid-row: 2;
}
</style>
