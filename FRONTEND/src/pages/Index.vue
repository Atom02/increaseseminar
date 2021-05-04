<template>
  <q-page class="q-pa-none">
    <!-- <div> -->
    <!-- <template v-slot:media>
        <img src="~assets/img/radar.gif" style="filter: brightness(40%);" />
      </template> -->
    <div id="sect1" class="sect q-py-md">
      <div
        class="row justify-center items-center content-center q-mt-lg"
        style="background-color:white"
      >
        <div class="col-11 col-sm-4 text-center">
          <q-img
            src="~assets/img/Logo Increase 3.png"
            spinner-color="white"
            style="width:30%"
          />
          &nbsp;
          <q-img
            src="~assets/img/ARN_rogo_100_0524-150x150.png"
            spinner-color="white"
            style="width:30%"
          />
          &nbsp;
          <q-img
            src="~assets/img/Logo_RISH.jpeg"
            spinner-color="white"
            style="width:30%"
          />
        </div>
      </div>
      <div class="row justify-center items-center content-center q-mt-xl">
        <div class="col-11 col-sm-10 text-white">
          <center>
            <span class="text-h6 text-weight-regular">
              <i>
                Hybrid Meeting online and onsite in Padang, 20-22 September 2021
              </i>
            </span>
            <br />
            <span class="text-h5 text-weight-bold">
              Equatorial Atmosphere Radar (EAR) <br />
              20<sup>th</sup> Anniversary
            </span>
          </center>
          <div class="text-h6 text-weight-regular q-mt-md">
            <center>
              LAPAN - Kyoto University <br />
              International Symposium for Equatorial Atmosphere
            </center>
          </div>
        </div>
      </div>
    </div>
    <div id="sect2" ref="about" class="sect q-py-md">
      <div class="row justify-center items-start content-center q-mt-md">
        <div class="gt-xs col-sm-5 q-pa-sm q-px-lg text-right">
          <q-img
            class=""
            src="~assets/img/groupp.png"
            spinner-color="white"
            style="width:80%"
          />
        </div>
        <div class="xs col-12 q-pa-sm q-px-lg">
          <center>
            <q-img
              class=""
              src="~assets/img/groupp.png"
              spinner-color="white"
              style="width:80%"
            />
          </center>
        </div>
        <div class="col-12 col-sm-5 q-pa-sm q-pt-xl q-px-lg">
          <div class="text-h4">About The Conference</div>
          <p class="text-body1">
            Joint program of INternational Conference on Radioscience,
            Equatorial Atmospheric Science and Environment (INCREASE) and The
            6th Asia Research Node (ARN) Symposium on Humanosphere Science
          </p>
          <p class="text-body1">
            Scope: <b class="text-h6">'Humanosphere Science'</b> including:
            <br />
            <span class="text-h6">
              Atmospheric Science, Environmental Science, Oceanography, Space
              Science, Material Science, Plant Science, Entomology,
              Microbiology, Ecology, Forestry, Wood Science, Chemistry,
              Biochemistry, Molecular Biology, Architecture, Electromagnetic
              Engineering, Agriculture, Ocean Science, etc
            </span>
          </p>
          <p>
            <q-btn
              size="xl"
              style="background: #FF0080; color: white"
              @click="openhref('https://easychair.org/cfp/INCREASEand6thARN')"
              label="More Info"
            />
          </p>
        </div>
      </div>
      <!-- <div class="row justify-center items-center content-center q-mt-md">
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
      </div> -->
    </div>
    <div id="sect3" ref="importantDates" class="sect q-py-md">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11 text-white">
          <span class="text-h4">Important Dates </span>
          <!-- <q-separator color="white" /> -->
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-sm-3 text-white text-h5 q-pa-sm dateBox">
          15 March 2021
        </div>
        <div class="col-11 col-sm-7 text-white text-h5 q-pa-sm">
          First announcement
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-sm-3 text-white text-h5 q-pa-sm dateBox">
          <s style="color:#ff8639">15 April 2021</s>
          30 April 2021
        </div>
        <div class="col-11 col-sm-7 text-white text-h5 q-pa-sm">
          Second announcement
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-sm-3 text-white text-h5 q-pa-sm dateBox">
          1 May - 15 July 2021
        </div>
        <div class="col-11 col-sm-7 text-white text-h5 q-pa-sm">
          Abstract submission
          <q-btn
            size="xl"
            style="background: #FF0080; color: white"
            @click="
              openhref(
                'https://easychair.org/conferences/?conf=increaseand6tharn'
              )
            "
            label="SUBMIT NOW!!!"
          />
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-sm-3 text-white text-h5 q-pa-sm dateBox">
          20 September 2021
        </div>
        <div class="col-11 col-sm-7 text-white text-h5 q-pa-sm">
          Full Paper Submission
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-sm-3 text-white text-h5 q-pa-sm dateBox">
          20 - 22 September 2021
        </div>
        <div class="col-11 col-sm-7 text-white text-h5 q-px-none q-pt-none">
          <!-- MAIN EVENT, <br /> -->
          <ul style="margin-top:0">
            <li>Ceremonial EAR 20th Anniversary</li>
            <li>
              Joint program of <b>IN</b>ternational <b>C</b>onference on
              <b>R</b>adioscience, <b>E</b>quatorial <b>A</b>tmospheric
              <b>S</b>cience and <b>E</b>nvironment (<b>INCREASE</b>) and The
              6th Asia Research Node (ARN) Symposium on Humanosphere Science
            </li>
            <li>
              EAR excursion
            </li>
          </ul>

          <q-separator class="xs" color="white" />
        </div>
      </div>
    </div>
    <div id="sect4" ref="keyNoteSpeaker" class="sect q-py-md">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11">
          <span class="text-h4">Speakers </span>
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-md">
        <div class="col-12 col-md-5 q-pa-sm text-body1">
          <div class="text-h5 text-primary">Keynote Speakers</div>
          <div class="text-h6">
            <ul>
              <li>
                Prof. Shigeo Yoden (Kyoto Univ, Japan)
              </li>
              <li>
                Prof. J.Y. Liu (NCU, Taiwan)<span class="text-red">*</span>
              </li>
              <li>Dr. Didi Satiadi (LAPAN, Indonesia)</li>
            </ul>
          </div>
        </div>
        <div class="col-12 col-sm-5 q-pa-sm text-body1">
          <div class="text-h5 text-primary">Invited Speakers</div>
          <div class="text-h6">
            <ul>
              <li>Prof. Hiroyuki Hashiguchi (Kyoto Univ, Japan)</li>
              <li>Dr. Wahyudi Hasbi (LAPAN, Indonesia)</li>
              <li>
                Prof. Tsuyoshi Yoshimura (Kyoto Univ, Japan)
                <span class="text-red">
                  *
                </span>
              </li>
              <li>Dr. Marzuki (Andalas Univ, Indonesia)</li>
              <li>
                Dr. Yasunobu Miyoshi (Kyushu Univ, Japan)
              </li>
              <li>
                Prof. Manabu D. Yamanaka (Kyoto Univ, Japan)
              </li>
              <li>Prof. Ninong Komala (LAPAN, Indonesia)</li>
              <li>
                Dr. Takuya Tsugawa (Kyoto Univ, Japan)
                <span class="text-red">
                  *
                </span>
              </li>
              <li>Dr. Acep Purqon (ITB dan ITERA, Indonesia)</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 text-red q-pa-sm text-h6">
          * to be confirmed
        </div>
      </div>
    </div>
    <div id="sect5" ref="schedule" class="sect q-py-md text-white">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11">
          <span class="text-h4">Schedule</span>
        </div>
      </div>
      <div class="row justify-center q-mt-md">
        <div class="col-12 col-sm-11 q-pa-sm dateBox text-h5">
          DAY 1
        </div>
      </div>
      <div class="row justify-center">
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <template v-for="(item, index) in chunkArray(scheduleDay1, 2)[0]">
            <div :key="'d10' + index">
              <span class="scheduleTime">
                {{ item.time }}
              </span>
              <span class="scheduleAct">
                {{ item.act }}
              </span>
            </div>
          </template>
        </div>
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <template v-for="(item, index) in chunkArray(scheduleDay1, 2)[1]">
            <div :key="'d11' + index">
              <span class="scheduleTime">
                {{ item.time }}
              </span>
              <span class="scheduleAct">
                {{ item.act }}
              </span>
            </div>
          </template>
        </div>
      </div>
      <div class="row justify-center q-mt-md">
        <div class="col-12 col-sm-11 q-pa-sm dateBox text-h5">
          DAY 2 (Paralel Session)
        </div>
      </div>
      <div class="row justify-center">
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <template v-for="(item, index) in chunkArray(scheduleDay2, 2)[0]">
            <div :key="'d10' + index">
              <span class="scheduleTime">
                {{ item.time }}
              </span>
              <span class="scheduleAct">
                {{ item.act }}
              </span>
            </div>
          </template>
        </div>
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <template v-for="(item, index) in chunkArray(scheduleDay2, 2)[1]">
            <div :key="'d11' + index">
              <span class="scheduleTime">
                {{ item.time }}
              </span>
              <span class="scheduleAct">
                {{ item.act }}
              </span>
            </div>
          </template>
        </div>
      </div>
      <div class="row justify-center q-mt-md">
        <div class="col-12 col-sm-11 q-pa-sm dateBox text-h5">
          DAY 3
        </div>
      </div>
      <div class="row justify-center">
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <div>
            <span class="scheduleTime">
              09:00 - 12:00
            </span>
            <span class="scheduleAct">
              Visit the EAR site (selected participants)
            </span>
          </div>
        </div>
        <div class="col-12 col-md-5 q-pa-sm text-h6">&nbsp;</div>
      </div>
    </div>
    <div id="sectLast" ref="otherInfo" class="sect q-py-md">
      <div class="row justify-center items-start content-center q-mt-md">
        <div class="col-12 col-sm-4 q-pa-sm text-body1">
          <div>Organized by:</div>
          <div class="text-weight-bold">
            Pusat Sains dan Teknologi Atmosfer (PSTA) <br />
            Research Institute for Sustainable Humanosphere (RISH)
          </div>
          <div class="q-mt-sm">Supported by:</div>
          <div class="text-weight-bold">
            Lembaga Penerbangan dan Antariksa Nasional (LAPAN) <br />
            Kyoto University
          </div>
          <div>
            <q-img
              src="~assets/img/logo_baru_lapan.jpg"
              spinner-color="white"
              style="width:20%"
            />
            <!-- &nbsp;
            <q-img
              src="~assets/img/ARN_rogo_100_0524-150x150.png"
              spinner-color="white"
              style="width:20%"
            />
            &nbsp;
            <q-img
              src="~assets/img/Logo_RISH.jpeg"
              spinner-color="white"
              style="width:20%"
            /> -->
            &nbsp;
            <q-img
              src="~assets/img/kyotouniv_logo.jpg"
              spinner-color="white"
              style="width:20%"
            />
          </div>
          <div class="q-mt-sm">Related Link:</div>
          <div class="text-weight-bold">
            <a href="http://www.rish.kyoto-u.ac.jp/arn6/" target="_blank">
              www.rish.kyoto-u.ac.jp/arn6/
            </a>
          </div>
        </div>
        <div class="col-12 col-sm-4 q-pa-sm text-body1">
          <div>contact:</div>
          <div class="text-weight-bold">
            <a href="mailto:increase@lapan.go.id" target="_blank">
              <q-icon name="mdi-email-box" /> increase@lapan.go.id
            </a>
          </div>
          <div class="q-mt-md">resources:</div>
          <div class="text-caption">
            <a href="http://www.rish.kyoto-u.ac.jp" target="_blank">
              www.rish.kyoto-u.ac.jp
            </a>
            <br />
            <a href="http://psta.lapan.go.id" target="_blank">
              psta.lapan.go.id
            </a>
            <br />
            <a href="https://www.freepik.com/vectors/business" target="_blank">
              Business vector created by vectorjuice - www.freepik.com
            </a>
            <br />
            <a href="https://www.freepik.com/photos/calendar" target="_blank">
              Calendar photo created by rawpixel.com - www.freepik.com
            </a>
            <a href="https://www.freepik.com/photos/technology" target="_blank"
              >Technology photo created by pressfoto - www.freepik.com</a
            >
          </div>
        </div>
        <div class="col-12 col-sm-4 q-pa-sm text-body1">
          <ShareNetwork
            network="facebook"
            url="https://ear20.lapan.go.id"
            title="Ear 20th Anniversary"
            description="Equatorial Atmosphere Radar (EAR) 
  20th Anniversary
  LAPAN - Kyoto University 
  International Symposium for Equatorial Atmosphere"
            quote="Joint program of INternational Conference on Radioscience, Equatorial Atmospheric Science and Environment (INCREASE) and The 6th Asia Research Node (ARN) Symposium on Humanosphere Science"
            hashtags="ear20anniversary,lapan,increase,seminar"
            media="https://ear20.lapan.go.id/img/radar.7d21f604.gif"
            style="text-decoration:none"
          >
            <q-btn
              class="q-ma-sm"
              icon="mdi-facebook"
              label="share on facebook"
              style="background-color:#3b5998"
              text-color="white"
            ></q-btn>
          </ShareNetwork>
          <br />
          <ShareNetwork
            network="twitter"
            url="https://ear20.lapan.go.id"
            title="Ear 20th Anniversary"
            description="Equatorial Atmosphere Radar (EAR) 
  20th Anniversary
  LAPAN - Kyoto University 
  International Symposium for Equatorial Atmosphere"
            quote="Joint program of INternational Conference on Radioscience, Equatorial Atmospheric Science and Environment (INCREASE) and The 6th Asia Research Node (ARN) Symposium on Humanosphere Science"
            hashtags="ear20anniversary,lapan,increase,seminar"
            media="https://ear20.lapan.go.id/img/radar.7d21f604.gif"
            style="text-decoration:none"
          >
            <q-btn
              class="q-ma-sm"
              icon="mdi-twitter"
              label="share on twitter"
              style="background-color:#00acee"
              text-color="white"
            ></q-btn>
          </ShareNetwork>
          <br />
          <ShareNetwork
            network="whatsapp"
            url="https://ear20.lapan.go.id"
            title="Ear 20th Anniversary"
            description="Equatorial Atmosphere Radar (EAR) 
  20th Anniversary
  LAPAN - Kyoto University 
  International Symposium for Equatorial Atmosphere"
            quote="Joint program of INternational Conference on Radioscience, Equatorial Atmospheric Science and Environment (INCREASE) and The 6th Asia Research Node (ARN) Symposium on Humanosphere Science"
            hashtags="ear20anniversary,lapan,increase,seminar"
            media="https://ear20.lapan.go.id/img/radar.7d21f604.gif"
            style="text-decoration:none"
          >
            <q-btn
              class="q-ma-sm"
              icon="mdi-whatsapp"
              label="share on whatsapp"
              style="background-color:#25d366"
              text-color="white"
            ></q-btn>
          </ShareNetwork>
          <br />
          <a href="https://info.flagcounter.com/MASZ">
            <img
              src="https://s01.flagcounter.com/countxl/MASZ/bg_FFFFFF/txt_000000/border_CCCCCC/columns_3/maxflags_12/viewers_0/labels_1/pageviews_1/flags_0/percent_0/"
              alt="Flag Counter"
              border="0"
            />
          </a>
        </div>
      </div>
    </div>
    <q-page-sticky position="top-right" :offset="[18, 18]" class="desktop-only">
      <q-fab
        v-model="fab1"
        label="section"
        glossy
        color="purple"
        icon="keyboard_arrow_down"
        direction="down"
        vertical-actions-align="right"
      >
        <template v-for="(item, index) in floatingButton">
          <q-fab-action
            :key="index"
            :label="item.label"
            :color="item.color"
            @click="scrollToElement(item.scrollTo)"
          >
            <q-badge
              v-if="isUpdate(item.updateDate)"
              color="red"
              label="update"
              floating
            />
          </q-fab-action>
        </template>
      </q-fab>
    </q-page-sticky>
    <q-page-sticky
      position="bottom-right"
      :offset="[18, 18]"
      class="mobile-only"
    >
      <q-fab
        ref="mobileFab"
        :persistent="true"
        v-model="fab1"
        label="section"
        glossy
        color="purple"
        icon="keyboard_arrow_up"
        direction="up"
        vertical-actions-align="right"
        @hide="preventFabHide('mobileFab')"
      >
        <template v-for="(item, index) in floatingButton.slice().reverse()">
          <q-fab-action
            :key="index"
            :label="item.label"
            :color="item.color"
            @click="scrollToElement(item.scrollTo)"
          >
            <q-badge
              v-if="isUpdate(item.updateDate)"
              color="red"
              label="update"
              floating
            />
          </q-fab-action>
        </template>
      </q-fab>
    </q-page-sticky>
  </q-page>
</template>
<style scoped>
#sect1 {
  /* background: linear-gradient(
      180deg,
      rgba(0, 0, 0, 0.6278886554621849) 80%,
      rgba(255, 255, 255, 1) 89%
    ),
    url("~assets/img/radar.gif"); */
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
    url("~assets/img/radar.gif");
  /* background-repeat: no-repeat; */
  background-size: cover;
  background-position: center;
  /* min-height: 400px; */
}
#sect3 {
  /* background: linear-gradient(180deg, rgba(255,255,255,0.9) 5%, rgba(0,0,0,0.6) 100%),
    url("~assets/img/conference.jpg"); */
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
    url("~assets/img/scheduleLite.jpg");
  /* background-repeat: no-repeat; */
  background-size: cover;
  background-position: center;
  /* min-height: 400px; */
}
#sect5 {
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 7)),
    url("~assets/img/rundown.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  color: $text-white;
}

.sect {
  min-height: 200px;
}
.dateBox {
  background-color: #ff6807;
}
</style>

<script>
import { Flipped } from "vue-flip-toolkit";
import { scroll, openURL } from "quasar";
const { getScrollTarget, setScrollPosition } = scroll;
import { DateTime as LuxonDT } from "luxon";
// Vue.use(VueSocialSharing);
export default {
  // meta: {
  //   meta: {
  //     description: { name: "description", content: "Page 1" }
  //   }
  // },
  layout: "Empty",
  name: "PageIndex",
  data() {
    return {
      fab1: true,
      forceCloseFab: false,
      floatingButton: [
        {
          label: "About The Confrence",
          color: "primary",
          scrollTo: "about",
          hasUpdate: false,
          updateDate: "2021-05-03"
        },
        {
          label: "Important Dates",
          color: "secondary",
          scrollTo: "importantDates",
          hasUpdate: false,
          updateDate: "2021-05-03"
        },
        {
          label: "Speakers",
          color: "accent",
          scrollTo: "keyNoteSpeaker",
          hasUpdate: true,
          updateDate: "2021-04-30"
        },
        {
          label: "Schedule",
          color: "dark",
          scrollTo: "schedule",
          hasUpdate: true,
          updateDate: "2021-05-03"
        },
        {
          label: "Contact",
          color: "secondary",
          scrollTo: "otherInfo",
          hasUpdate: false,
          updateDate: ""
        }
      ],
      updateDay: 7,
      scheduleDay1: [],
      scheduleDay2: []
    };
  },
  components: {
    // Flipped
  },
  methods: {
    scrollToElement(refId) {
      this.forceCloseFab = false;
      const el = this.$refs[refId];
      const target = getScrollTarget(el);
      const offset = el.offsetTop;
      const duration = 500;
      setScrollPosition(target, offset, duration);
    },
    openhref(url) {
      // alert("GO TO " + url);
      openURL(url);
    },
    preventFabHide(fabName) {
      return;
      // console.log("PREV HIDE?", this.forceCloseFab);
      if (this.forceCloseFab === false) {
        this.$refs[fabName].show();
      }
    },
    fabClicked(fabName) {
      this.forceCloseFab = true;
      // this.$refs[fabName].toggle();
    },
    isUpdate(date) {
      let diff = 999;
      try {
        // console.log(LuxonDT)
        const start = LuxonDT.fromISO(date);
        const end = LuxonDT.now();
        const tmpdif = end.diff(start, "days");
        diff = tmpdif.toObject().days;
        // console.log(diff)
      } catch (err) {
        console.log(err);
      }
      // console.log("IS DIFF", diff);
      return diff < 7;
    },
    chunkArray(arr, n) {
      var chunkLength = Math.max(arr.length / n, 1);
      var chunks = [];
      for (var i = 0; i < n; i++) {
        if (chunkLength * (i + 1) <= arr.length)
          chunks.push(arr.slice(chunkLength * i, chunkLength * (i + 1)));
      }
      return chunks;
    }
  },
  mounted() {
    const t = this;
    this.$axios
      .get("scheduleDay1.json")
      .then(res => {
        // console.log(res.data);
        t.scheduleDay1 = res.data;
      })
      .catch(err => {
        console.log(err);
      });

    this.$axios
      .get("scheduleDay2.json")
      .then(res => {
        // console.log(res.data);
        t.scheduleDay2 = res.data;
      })
      .catch(err => {
        console.log(err);
      });
    // const L = require("leaflet");
    // require("leaflet/dist/leaflet.css");
    // delete L.Icon.Default.prototype._getIconUrl;
    // L.Icon.Default.mergeOptions({
    //   iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
    //   iconUrl: require("leaflet/dist/images/marker-icon.png"),
    //   shadowUrl: require("leaflet/dist/images/marker-shadow.png")
    // });
    // // -6.8964647,107.5882276 google coord
    // // -6.89459,107.58662 osm coord
    // const map = L.map("map", {
    //   dragging: false,
    //   scrollWheelZoom: false,
    //   closePopupOnClick: false,
    //   doubleClickZoom: false
    // }).setView([-6.89459, 107.58662], 27);
    // L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    //   attribution:
    //     '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    // }).addTo(map);
    // L.marker([-6.89459, 107.58662])
    //   .addTo(map)
    //   .bindPopup(
    //     "Some Place.<br> Easily customizable.<br> <a href='https://goo.gl/maps/x6t39qdLNhMxQAW27' target='blank'>Open On Google Map</a>"
    //   )
    //   .openPopup();
  }
};
</script>
