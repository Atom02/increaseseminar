<template>
  <q-page class="q-pa-none">
    <!-- <div> -->
    <!-- <template v-slot:media>
        <img src="~assets/img/radar.gif" style="filter: brightness(40%);" />
      </template> -->
    <div id="sect1" class="sect q-py-md">
      <div class="row justify-center items-center content-center q-mt-lg">
        <div class="col-11 col-sm-8 text-white">
          <Flipped flip-id="ear20">
            <div>
              <span class="xs text-h4">EAR 20<sup>th</sup> Anniversary</span>
              <span class="gt-xs text-h2">EAR 20<sup>th</sup> Anniversary</span>
            </div>
          </Flipped>
          <p class="text-body1">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Non
            pulvinar neque laoreet suspendisse interdum consectetur libero id
            faucibus. Eget sit amet tellus cras adipiscing enim eu. Purus in
            mollis nunc sed id semper. At elementum eu facilisis sed odio morbi
            quis commodo. Ut sem nulla pharetra diam sit amet. Ullamcorper
            dignissim cras tincidunt lobortis. Dolor sit amet consectetur
            adipiscing elit duis tristique. Justo laoreet sit amet cursus.
            Volutpat sed cras ornare arcu dui vivamus. Sed sed risus pretium
            quam vulputate dignissim suspendisse in.
          </p>
        </div>
      </div>
      <div class="row justify-center items-center content-center  q-mb-lg">
        <div class="col-11 col-sm-8 text-right">
          <q-btn
            rounded
            color="primary"
            label="Read More"
            size="md"
            icon-right="mdi-arrow-right-bold"
            @click="$router.push('/ear20')"
          ></q-btn>
        </div>
      </div>
    </div>
    <div id="sect2" class="sect q-py-md">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11 col-sm-8">
          <Flipped flip-id="symposium">
            <div>
              <span class="xs text-h4">
                6<sup>th</sup> Asia Research Node Symposium For Humanosphere
                Science
              </span>
              <span class="gt-xs text-h2">
                6<sup>th</sup> Asia Research Node Symposium For Humanosphere
                Science
              </span>
            </div>
          </Flipped>
          <p class="text-body1">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Non
            pulvinar neque laoreet suspendisse interdum consectetur libero id
            faucibus. Eget sit amet tellus cras adipiscing enim eu. Purus in
            mollis nunc sed id semper. At elementum eu facilisis sed odio morbi
            quis commodo. Ut sem nulla pharetra diam sit amet. Ullamcorper
            dignissim cras tincidunt lobortis. Dolor sit amet consectetur
            adipiscing elit duis tristique. Justo laoreet sit amet cursus.
            Volutpat sed cras ornare arcu dui vivamus. Sed sed risus pretium
            quam vulputate dignissim suspendisse in.
          </p>
        </div>
      </div>
      <div class="row justify-center items-center content-center  q-mb-lg">
        <div class="col-11 col-sm-8 text-right">
          <q-btn
            rounded
            color="primary"
            label="Read More"
            size="md"
            icon-right="mdi-arrow-right-bold"
            @click="$router.push('/symposium')"
          ></q-btn>
        </div>
      </div>
    </div>
    <div id="sect3" class="sect q-py-md">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11 col-sm-8 text-white">
          <span class="xs text-h4">INCREASE</span>
          <span class="gt-xs text-h2">INCREASE</span>
          <p class="text-body1">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Non
            pulvinar neque laoreet suspendisse interdum consectetur libero id
            faucibus. Eget sit amet tellus cras adipiscing enim eu. Purus in
            mollis nunc sed id semper. At elementum eu facilisis sed odio morbi
            quis commodo. Ut sem nulla pharetra diam sit amet. Ullamcorper
            dignissim cras tincidunt lobortis. Dolor sit amet consectetur
            adipiscing elit duis tristique. Justo laoreet sit amet cursus.
            Volutpat sed cras ornare arcu dui vivamus. Sed sed risus pretium
            quam vulputate dignissim suspendisse in.
          </p>
        </div>
      </div>
      <div class="row justify-center items-center content-center  q-mb-lg">
        <div class="col-11 col-md-8 text-right">
          <q-btn
            rounded
            color="primary"
            label="Read More"
            size="md"
            icon-right="mdi-arrow-right-bold"
          ></q-btn>
        </div>
      </div>
    </div>
    <div id="sect4" class="sect q-py-md">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11 col-sm-8">
          <span class="xs text-h4">Location</span>
          <span class="gt-xs text-h2">Location</span>
        </div>
      </div>
      <div class="row justify-center items-start content-start q-mb-lg">
        <div class="col-11 col-sm-4">
          <div class="text-h5">Online Via</div>
          <div class="text-body1">Zoom</div>
          <div class="text-body1">YouTube</div>
        </div>
        <div class="col-11 col-sm-4">
          <div class="text-h5">Offline at</div>
          <div id="map" style="width:100%;height:400px">MAP</div>
          <a class="float-right" href='https://goo.gl/maps/x6t39qdLNhMxQAW27' target='blank'>Open On Google Map</a>
        </div>
      </div>
    </div>
    <div id="sect5" class="sect q-py-md text-white">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11 col-sm-8">
          <span class="xs text-h4">Schedule</span>
          <span class="gt-xs text-h2">Schedule</span>
          <p class="text-body1">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Non
            pulvinar neque laoreet suspendisse interdum consectetur libero id
            faucibus. Eget sit amet tellus cras adipiscing enim eu. Purus in
            mollis nunc sed id semper. At elementum eu facilisis sed odio morbi
            quis commodo. Ut sem nulla pharetra diam sit amet. Ullamcorper
            dignissim cras tincidunt lobortis. Dolor sit amet consectetur
            adipiscing elit duis tristique. Justo laoreet sit amet cursus.
            Volutpat sed cras ornare arcu dui vivamus. Sed sed risus pretium
            quam vulputate dignissim suspendisse in.
          </p>
        </div>
      </div>
    </div>
  </q-page>
</template>
<style scoped>
#sect1 {
  /* background-image: url(~assets/img/radar.gif); */
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("~assets/img/radar.gif");
  /* background-repeat: no-repeat; */
  background-size: cover;
  background-position: center;
  /* min-height: 400px; */
}
#sect3 {
  /* background-image: url(~assets/img/conference.jpg); */
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("~assets/img/conference.jpg");
  /* background-repeat: no-repeat; */
  background-size: cover;
  background-position: bottom;
  /* min-height: 400px; */
}

#sect5 {
  /* background-image: url(~assets/img/conference.jpg); */
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
    url("~assets/img/schedule.png");
  /* background-repeat: no-repeat; */
  background-size: cover;
  background-position: center;
  /* min-height: 400px; */
}
.sect {
  min-height: 200px;
}
</style>
<script>
import { Flipped } from "vue-flip-toolkit";
export default {
  layout: "Empty",
  name: "PageIndex",
  components: {
    Flipped
  },
  mounted() {
    const L = require("leaflet");
    require("leaflet/dist/leaflet.css");
    delete L.Icon.Default.prototype._getIconUrl;
    L.Icon.Default.mergeOptions({
      iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
      iconUrl: require("leaflet/dist/images/marker-icon.png"),
      shadowUrl: require("leaflet/dist/images/marker-shadow.png")
    });
    // -6.8964647,107.5882276 google coord

    // -6.89459,107.58662 osm coord
    const map = L.map("map", {
      dragging: false,
      scrollWheelZoom: false
    }).setView([-6.89459, 107.58662], 27);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([-6.89459, 107.58662])
      .addTo(map)
      .bindPopup(
        "Some Place.<br> Easily customizable.<br> <a href='https://goo.gl/maps/x6t39qdLNhMxQAW27' target='blank'>Open On Google Map</a>"
      )
      .openPopup();
  }
};
</script>
