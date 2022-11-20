<template>
  <div>
    {{model}}
  </div>
  <div ref="map-root"
        style="width: 100%; height: 100%">
  </div>
</template>

<script>
  import Map from 'ol/Map';
  import Point from 'ol/geom/Point';
  import View from 'ol/View';
  import { LineString } from 'ol/geom';
  import {Stroke, Style} from 'ol/style';
  import {OSM, Vector as VectorSource} from 'ol/source';
  import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
  import {useGeographic} from 'ol/proj';
  import Feature from 'ol/Feature';

  import 'ol/ol.css'

  useGeographic();


var coords = [
    [20.73998593, 48.21339894],
    [20.73998763, 48.21340378],
    [20.74002805, 48.21352366]
]

var current_coord = [20.74002805, 48.21352366, 0.555499611]

 var lineString = new LineString(coords);

var layerRoute =  new VectorLayer({
    source: new VectorSource({
        features: [
            new Feature({geometry: lineString})
        ]
    }),
    style: [
        new Style({
            stroke: new Stroke({
                width: 3, color: 'rgba(0, 0, 0, 1)',
            }),zIndex: 2 }),
    ],
    updateWhileAnimating: true
});


  export default {
    name: 'MapContainer',
    components: {},
    props: ['model'],
    data() {
    return {
        coordinates: null, // I want to pass the the model arrays data here
     }
    },
    watch: {
      model(newVal, oldVal) {
        console.log(newVal)
        this.coordinates = [...newVal] // if model is an array
        current_coord = this.coordinates
      }
   },
    mounted() {
      new Map({
        target: this.$refs['map-root'],
        layers: [
          new TileLayer({
            source: new OSM()
          }),
          layerRoute
        ],
        view: new View({
          zoom: 16,
          center: [20.73998593, 48.21339894],
          constrainResolution: true
        }),
      })
    },
  }
</script>