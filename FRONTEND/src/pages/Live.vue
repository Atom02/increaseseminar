<template>
  <q-page class="q-pa-sm">
    <div class="row">
      <div class="col-12 text-center">
        <Flipped flip-id="symposium">
          <div>
            <q-img
              src="~assets/img/Logo Increase 3.png"
              spinner-color="white"
              style="width:60px"
              contain
            />
            &nbsp;
            <q-img
              src="~assets/img/ARN_rogo_100_0524-150x150.png"
              spinner-color="white"
              style="width:60px"
              contain
            />
          </div>
        </Flipped>
      </div>
    </div>
    <div class="row q-py-sm q-my-md">
      <div class="col-12 text-center">
        <embed-youtube></embed-youtube>
      </div>
    </div>
    <div class="row text-center">
      <div class="col-12">
        <q-img
          src="~assets/img/new_brinlogo.png"
          spinner-color="white"
          style="width:60px"
          contain
          title="Badan Riset dan Inovasi Nasional"
        />
        &nbsp;
        <q-img
          src="~assets/img/logo_baru_lapan.jpg"
          spinner-color="white"
          style="width:60px"
          contain
          title="LAPAN"
        />
        &nbsp;
        <q-img
          src="~assets/img/kyotouniv_logo.jpg"
          spinner-color="white"
          style="width:60px"
          contain
          title="KYOTO UNIVERSITY"
        />&nbsp;
        <q-img
          src="~assets/img/Logo_RISH.jpeg"
          spinner-color="white"
          style="width:60px"
          contain
          title="esearch Institute for Sustainable Humanosphere"
        />
      </div>
    </div>
  </q-page>
</template>
<script>
import { Flipped } from "vue-flip-toolkit";
import EmbedYoutube from "components/EmbedYoutube.vue";
export default {
  layout: "Empty",
  name: "PageLive",
  components: {
    Flipped,
    "embed-youtube": EmbedYoutube
  }
};
</script>
