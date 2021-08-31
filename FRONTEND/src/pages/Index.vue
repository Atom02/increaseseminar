<template>
  <q-page class="q-pa-none">
    <!-- <div> -->
    <!-- <template v-slot:media>
        <img src="~assets/img/radar.gif" style="filter: brightness(40%);" />
      </template> -->
    <div id="sect0" ref="announcement" class="sect q-py-md">
      <div class="row q-mb-md">
        <div class="col-12 text-center text-h4">
          <span class="text-red-14" style="border-bottom:thin solid">
            <b>Announcement</b>
          </span>
        </div>
      </div>
      <q-separator />
      <div class="row justify-center">
        <div class="col-12 text-center q-pa-sm">
          <!-- <q-icon
            v-if="isUpdate('2021-08-31')"
            class="text-red blink"
            name="mdi-new-box"
            size="xl"
          /> -->
          <q-btn color="primary">
            <a
              href="/pdf/Announcement_to _all_participants_20210831.pdf"
              download="video submission, abstract list and FAQ.pdf"
              style="text-decoration:none"
              class="text-white"
            >
              Video Submission, Abstract List and Frequently Asked Questions
            </a>
            <q-badge
              v-if="isUpdate('2021-08-31')"
              color="red"
              floating
              class="blink"
            >
              New
              <!-- <q-icon
                  v-if="isUpdate('2021-08-31')"
                  class="text-white blink"
                  name="mdi-new-box"
                  size="md"
                /> -->
            </q-badge>
          </q-btn>
          <!-- <q-btn
            class="text-h6 q-mb-md"
            size="sm"
            color="primary"
            @click="openAnnouncement"
            label="Video Submission"
          >
            <q-badge v-if="isUpdate('2021-08-31')" color="red" floating>
              New
            </q-badge>
          </q-btn> -->
        </div>
      </div>
    </div>
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
                <s
                  >Hybrid Meeting online and onsite in Padang, 20-22 September
                  2021</s
                > </i
              ><br />
              <i
                ><b>Full Online Meeting, 20-22 September 2021<sup>*</sup></b></i
              >
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
          <div class="text-h6 text-weight-regular q-mt-lg">
            <center>
              <sup>*</sup>)&nbsp; considering the circumstances due to Covid-19,
              we decide to change into Full Online Meeting
            </center>
          </div>
        </div>
      </div>
    </div>
    <div id="sect2" ref="about" class="sect q-py-md">
      <div class="row justify-center items-start content-center q-mt-md">
        <div class="gt-xs col-sm-4 q-pa-sm q-px-lg text-right">
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
        <div class="col-12 col-md-6 q-pa-sm q-pt-xl q-px-lg">
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
          <p class="text-h5">
            Selected paper will be published on
            <b class="text-red">SPRINGER PROCEEDINGS</b> in Physics<br />
            <span class="text-h5 text-red"><b>FREE OF CHARGE</b></span>
          </p>
          <p ref="register">
            <q-btn
              size="lg"
              style="background: #F0F0F0; color: grey"
              disable
              label="Submit Abstract"
              class="q-mr-md"
            ></q-btn>
            <span style="display:inline-block;" class="q-mr-md">OR</span>
            <q-btn
              class="blink"
              size="xl"
              flat
              label="join as participant (FREE)"
              style="color:#FF0080"
              @click="openDialog"
            ></q-btn>
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
        <div class="col-11 col-md-3 text-white text-h5 q-pa-sm dateBox">
          15 March 2021
        </div>
        <div class="col-11 col-md-7 text-white text-h5 q-pa-sm">
          First announcement
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-md-3 text-white text-h5 q-pa-sm dateBox">
          <s style="color:#ff8639">15 April 2021</s>
          30 April 2021
        </div>
        <div class="col-11 col-md-7 text-white text-h5 q-pa-sm">
          Second announcement
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-md-3 text-white text-h5 q-pa-sm dateBox">
          1 May - 15 July 2021
        </div>
        <div class="col-11 col-md-7 text-white text-h5 q-pa-sm">
          <strike>Abstract submission</strike>&nbsp; <b>CLOSED</b>
          <!-- <q-btn
            class="q-ml-md"
            size="lg"
            style="background: #FF0080; color: white"
            @click="
              openhref(
                'https://easychair.org/conferences/?conf=increaseand6tharn'
              )
            "
            label="SUBMIT NOW!!!"
          /> -->
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-md-3 text-white text-h5 q-pa-sm dateBox">
          31 July 2021
        </div>
        <div class="col-11 col-md-7 text-white text-h5 q-pa-sm">
          Abstract Acceptance Announcement
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-md-3 text-white text-h5 q-pa-sm dateBox">
          20 September 2021
        </div>
        <div class="col-11 col-md-7 text-white text-h5 q-pa-sm">
          Full Paper Submission
          <q-separator class="xs" color="white" />
        </div>
      </div>
      <div class="row justify-center items-start content-center q-mt-lg">
        <div class="col-11 col-md-3 text-white text-h5 q-pa-sm dateBox">
          20 - 22 September 2021
        </div>
        <div class="col-11 col-md-7 text-white text-h5 q-px-none q-pt-none">
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
        <div class="col-11 col-md-5 q-pa-sm text-body1">
          <div class="text-h5 text-primary">Keynote Speakers</div>
          <div class="text-h6">
            <ul>
              <li>
                Prof. Shigeo Yoden (Kyoto Univ, Japan)
              </li>
              <li>
                Prof. J.Y. Liu (NCU, Taiwan)
              </li>
              <li>Dr. Didi Satiadi (LAPAN, Indonesia)</li>
            </ul>
          </div>
        </div>
        <div class="col-11 col-md-5 q-pa-sm text-body1">
          <div class="text-h5 text-primary">Invited Speakers</div>
          <div class="text-h6">
            <ul>
              <li>Prof. Hiroyuki Hashiguchi (Kyoto Univ, Japan)</li>
              <li>Dr. Wahyudi Hasbi (LAPAN, Indonesia)</li>
              <li>Dr. Marzuki (Andalas Univ, Indonesia)</li>
              <li>
                Dr. Yasunobu Miyoshi (Kyushu Univ, Japan)
              </li>
              <li>
                Prof. Manabu D. Yamanaka (Kobe Univ, Japan)
              </li>
              <li>Prof. Ninong Komala (LAPAN, Indonesia)</li>
              <li>
                Prof. Masatomo Fujiwara (Hokkaido Univ, Japan)
              </li>
              <li>Dr. Acep Purqon (ITB dan ITERA, Indonesia)</li>
              <li>Prof. Toshiaki Umezawa (Kyoto University, Japan)</li>
              <li>Prof. Sulaeman Yusuf (LIPI, Indonesia)</li>
            </ul>
          </div>
        </div>
      </div>
      <!-- <div class="row">
        <div class="col-12 text-red q-pa-sm text-h6">
          * to be confirmed
        </div>
      </div> -->
    </div>
    <div id="sect5" ref="schedule" class="sect q-py-md text-white">
      <div class="row justify-center items-center content-center q-mt-md">
        <div class="col-11">
          <span class="text-h4">Schedule</span>
        </div>
      </div>
      <div class="row justify-center q-mt-md">
        <div class="col-12 col-md-11 q-pa-sm dateBox text-h5">
          DAY 1
        </div>
      </div>
      <div class="row justify-center">
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <template v-for="(item, index) in chunkArray(scheduleDay1, 2)[0]">
            <div :key="'d10' + index" class="q-mb-sm">
              <span class="scheduleTime">
                {{ item.time }}
              </span>
              <span class="scheduleAct">
                {{ item.act }}
                <template v-if="'sub' in item">
                  <br />
                  <span class="subAct text-h5">{{ item.sub }}</span>
                </template>
              </span>
            </div>
          </template>
        </div>
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <template v-for="(item, index) in chunkArray(scheduleDay1, 2)[1]">
            <div :key="'d11' + index" class="q-mb-sm">
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
        <div class="col-12 col-md-11 q-pa-sm dateBox text-h5">
          DAY 2 (Paralel Session)
        </div>
      </div>
      <div class="row justify-center">
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <template v-for="(item, index) in chunkArray(scheduleDay2, 2)[0]">
            <div :key="'d10' + index" class="q-mb-sm">
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
            <div :key="'d11' + index" class="q-mb-sm">
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
        <div class="col-12 col-md-11 q-pa-sm dateBox text-h5">
          DAY 3
        </div>
      </div>
      <div class="row justify-center">
        <div class="col-12 col-md-5 q-pa-sm text-h6">
          <div class="q-mb-sm">
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
    <q-dialog
      v-model="dialog"
      persistent
      :maximized="maximizedToggle"
      transition-show="slide-up"
      transition-hide="slide-down"
    >
      <q-card style="min-width: 50vw;">
        <q-bar class="bg-primary text-white">
          <q-space />
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-white text-primary">Close</q-tooltip>
          </q-btn>
        </q-bar>

        <q-card-section>
          <div class="text-h6">Register as Participant (FREE)</div>
        </q-card-section>
        <q-card-section class="q-pt-md">
          <q-form
            @submit="register"
            class="q-gutter-md"
            autocorrect="off"
            autocapitalize="off"
            autocomplete="off"
          >
            <div class="row">
              <div class="col-12">
                <q-input
                  v-model="participantForm.name"
                  label="Full Name *"
                  :rules="[
                    val => (val && val.length > 0) || 'Please type something'
                  ]"
                  autocorrect="off"
                  autocapitalize="off"
                  autocomplete="off"
                  lazy-rules
                  :disable="registerLoading == true"
                ></q-input>
                <q-input
                  v-model="participantForm.email"
                  type="email"
                  label="Email *"
                  autocorrect="off"
                  autocapitalize="off"
                  autocomplete="off"
                  :rules="[
                    val => !!val || 'Please Type a Valid Email',
                    isValidEmail
                  ]"
                  lazy-rules
                  ref="formemail"
                  @focus="clearFieldError('email')"
                  :error="isFieldError('email')"
                  :error-message="getFieldError('email')"
                  :disable="registerLoading == true"
                ></q-input>
                <q-input
                  v-model="participantForm.aff"
                  label="Affiliation *"
                  :rules="[
                    val =>
                      (val && val.length > 0) ||
                      'Please fill in Your Organization or University'
                  ]"
                  autocorrect="off"
                  autocapitalize="off"
                  autocomplete="off"
                  hint="Organization or University"
                  lazy-rules
                  :disable="registerLoading == true"
                ></q-input>
                <q-select
                  class="q-mt-sm"
                  clearable
                  label="Nationality/Country of Origin *"
                  filled
                  v-model="participantForm.nationality"
                  use-input
                  hide-selected
                  fill-input
                  input-debounce="0"
                  :options="countryList"
                  @filter="filterFn"
                  hint="Type To filter"
                  lazy-rules
                  :rules="[
                    val => (val && val !== null) || 'Please Select One Option'
                  ]"
                  :disable="registerLoading == true"
                >
                  <template v-slot:no-option>
                    <q-item>
                      <q-item-section class="text-grey">
                        No results
                      </q-item-section>
                    </q-item>
                  </template>
                </q-select>
              </div>
            </div>
            <!-- <div class="row q-pt-sm">
              <div class="col-12">
                <vue-recaptcha
                  ref="recaptcha"
                  @verify="onVerify"
                  @expired="onExpired"
                  sitekey="6Lc4rM8aAAAAABWLxAFOSpaRhSHJhshyWA_Kg55P"
                  :loadRecaptchaScript="true"
                >
                </vue-recaptcha>
              </div>
            </div> -->
            <div class="row q-pt-lg">
              <!-- <div class="col-2">
              <q-btn
                  @click="resendConfirmationEmail"
                  color="primary"
                  size="lg"
                  flat
                ></q-btn>
              </div>                 -->
              <div class="col-12">
                <q-btn
                  color="primary"
                  size="md"
                  class="float-right"
                  type="submit"
                  label="Register As Participant"
                  :loading="registerLoading"
                >
                  <template v-slot:loading>
                    <q-spinner-hourglass class="on-left" />
                    Registering...
                  </template>
                </q-btn>
                <q-btn
                  v-if="registerLoading == false"
                  @click="resetformregister"
                  color="warning"
                  size="md"
                  class="float-right"
                  flat
                  label="Cancel"
                ></q-btn>
              </div>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog
      v-model="anouncementDialog"
      persistent
      :maximized="maximizedToggle"
      transition-show="slide-up"
      transition-hide="slide-down"
    >
      <component v-bind:is="compAnouncement"></component>
      <!-- <q-card style="min-width: 45vw;">
        <q-bar class="bg-primary text-white">
          <q-space />
          <q-btn dense flat icon="close" size="md" v-close-popup>
            <q-tooltip content-class="bg-white text-primary text-h6"
              >Close</q-tooltip
            >
          </q-btn>
        </q-bar>
        <q-card-section style="max-height: 80vh" class="scroll">
          
        </q-card-section>
      </q-card> -->
    </q-dialog>
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
            v-on="
              item.hasOwnProperty('clickFunc')
                ? { click: () => item.clickFunc(parms) }
                : {
                    click: () =>
                      scrollToElement(item.scrollTo, item.negativeOffset)
                  }
            "
          >
            <q-badge
              v-if="isUpdate(item.updateDate)"
              color="red"
              label="update"
              class="blink"
              floating
            />
          </q-fab-action>
        </template>
      </q-fab>
      <q-badge
        color="red"
        label="update"
        floating
        style="z-index:995"
        v-if="isAnyUpdate"
        class="blink"
      />
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
            v-on="
              item.hasOwnProperty('clickFunc')
                ? { click: () => item.clickFunc(parms) }
                : {
                    click: () =>
                      scrollToElement(item.scrollTo, item.negativeOffset)
                  }
            "
          >
            <q-badge
              v-if="isUpdate(item.updateDate)"
              class="blink"
              color="red"
              label="update"
              floating
            />
          </q-fab-action>
        </template>
      </q-fab>
      <q-badge
        color="red"
        label="update"
        floating
        style="z-index:995"
        class="blink"
        v-if="isAnyUpdate"
      />
    </q-page-sticky>
  </q-page>
</template>
<style scoped>
#sect0 {
  /* background: linear-gradient(180deg, rgba(255,255,255,0.9) 5%, rgba(0,0,0,0.6) 100%),
    url("~assets/img/conference.jpg"); */
  background: linear-gradient(
      rgba(255, 255, 255, 0.7),
      rgba(255, 255, 255, 0.7)
    ),
    url("~assets/img/announcement.jpg");
  /* background-repeat: no-repeat; */
  background-size: cover;
  background-position: center;
  /* min-height: 400px; */
}
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
.blink {
  animation: blinker 1s step-start infinite;
}

@keyframes blinker {
  50% {
    opacity: 0;
  }
}
a {
  cursor: pointer;
}
</style>
<script>
import _ from "lodash";
import { Flipped } from "vue-flip-toolkit";
import { scroll, openURL, Cookies, Notify, exportFile } from "quasar";
const { getScrollTarget, setScrollPosition } = scroll;
import { DateTime as LuxonDT } from "luxon";
import VueRecaptcha from "vue-recaptcha";
import VideoSubmission from "components/VideoSubmission.vue";
// Vue.use(VueSocialSharing);
export default {
  // meta: {
  //   meta: {
  //     description: { name: "description", content: "Page 1" }
  //   }
  // },
  layout: "Empty",
  name: "PageIndex",
  components: {
    // Flipped
    // "vue-recaptcha": VueRecaptcha
    "video-submission": VideoSubmission
  },
  data() {
    return {
      fab1: true,
      forceCloseFab: false,
      floatingButton: [
        {
          label: "Register",
          color: "positive",
          scrollTo: "register",
          hasUpdate: false,
          updateDate: "2021-05-11",
          negativeOffset: -150
          // clickFunc: this.openDialog
        },
        {
          label: "Announcement",
          color: "negative",
          scrollTo: "announcement",
          hasUpdate: false,
          updateDate: "2021-08-31",
          negativeOffset: -150
        },
        {
          label: "About The Conference",
          color: "primary",
          scrollTo: "about",
          hasUpdate: false,
          updateDate: "2021-05-20",
          negativeOffset: 0
        },
        {
          label: "Important Dates",
          color: "secondary",
          scrollTo: "importantDates",
          hasUpdate: false,
          updateDate: "2021-07-19",
          negativeOffset: 0
        },
        {
          label: "Speakers",
          color: "accent",
          scrollTo: "keyNoteSpeaker",
          hasUpdate: true,
          updateDate: "2021-05-26",
          negativeOffset: 0
        },
        {
          label: "Schedule",
          color: "dark",
          scrollTo: "schedule",
          hasUpdate: true,
          updateDate: "2021-05-03",
          negativeOffset: 0
        },
        {
          label: "Contact",
          color: "secondary",
          scrollTo: "otherInfo",
          hasUpdate: false,
          updateDate: "",
          negativeOffset: 0
        }
      ],
      updateDay: 7,
      scheduleDay1: [],
      scheduleDay2: [],
      dialog: false,
      maximizedToggle: false,
      participantFormErrors: {},
      participantForm: {
        name: null,
        email: null,
        aff: null,
        nationality: null
      },
      participantFormRobot: false,
      registerLoading: false,
      countryList: [],
      countryListimt: [],
      anouncementDialog: false,
      anouncementDialogDay: 7,
      compAnouncement: null
    };
  },
  computed: {
    isAnyUpdate() {
      const t = this;
      // this.floatingButton.forEach((element, index, arr) => {
      //   let cdate = isUpdate(element.updateDate)

      // });
      let up = false;
      let diff = 9999;
      for (const fb of t.floatingButton) {
        // try {
        //   // console.log(LuxonDT)
        //   const start = LuxonDT.fromISO(fb.updateDate);
        //   const end = LuxonDT.now();
        //   const tmpdif = end.diff(start, "days");
        //   diff = tmpdif.toObject().days;
        //   // console.log(diff)
        // } catch (err) {
        //   console.log(err);
        // }
        // console.log("IS DIFF", diff);

        // let cdate = diff < 7;
        let cdate = t.isUpdate(fb.updateDate);
        // console.log("UP? :", fb.label, cdate);
        if (cdate == true) {
          up = true;
          break;
        }
      }
      return up;
    }
  },
  methods: {
    filterFn(val, update) {
      const t = this;
      if (val === "") {
        update(() => {
          this.countryList = this.countryListimt;

          // with Quasar v1.7.4+
          // here you have access to "ref" which
          // is the Vue reference of the QSelect
        });
        return;
      }

      update(() => {
        const needle = val.toLowerCase();
        // this.countryList = this.countryListimt.filter(
        //   v => v.toLowerCase().indexOf(needle) > -1
        // );
        this.countryList = _.filter(t.countryListimt, function(o) {
          return o.label.toLowerCase().indexOf(needle) > -1;
        });
      });
    },
    scrollToElement(refId, ofs) {
      this.forceCloseFab = false;
      const el = this.$refs[refId];
      const target = getScrollTarget(el);
      const offset = el.offsetTop - (30 - ofs);
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
    },
    isValidEmail(val) {
      const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
      return emailPattern.test(val) || "Invalid email";
    },
    async openDialog() {
      await this.$api("/site/");
      this.dialog = true;
    },
    register() {
      // console.log(this.participantForm);
      const t = this;
      t.registerLoading = true;
      // setTimeout(() => {
      // console.log("TRIGGER TOKEN");
      // t.$recaptcha("login").then(token => {
      // console.log("captcha token", token);
      // console.log("EVERYTHING IS GOOD");
      // console.log(this.participantForm);
      // console.log("CSRF", Cookies.get("CSRF-TOKEN"));
      const bodyFormData = new FormData();
      bodyFormData.append("name", t.participantForm.name);
      bodyFormData.append("email", t.participantForm.email);
      bodyFormData.append("affiliation", t.participantForm.aff);
      bodyFormData.append("nationality", this.participantForm.nationality.id);

      t.$api({
        method: "post",
        url: "/peserta/register",
        data: bodyFormData,
        headers: {
          "Content-Type": "multipart/form-data",
          "X-CSRF-TOKEN": Cookies.get("CSRF-TOKEN")
        }
      })
        .then(function(response) {
          //handle success
          console.log(response);
          const res = response.data;
          const status = res.status;
          if (status == true) {
            // t.$q.notify({
            //   type: "positive",
            //   message:
            //     "Registration Complete <br/> Check Your Email (inbox and spam folder) For Registration Confirmation <br/> Check This Website And Your Emails From Time To Time For Updates",
            //   position: "center",
            //   progress: true,
            //   html: true
            // });
            t.$q.notify({
              type: "positive",
              message:
                "Registration Complete <br/> Check Your Email (inbox and spam folder) For Registration Confirmation <br/> Check This Website And Your Emails From Time To Time For Updates",
              position: "center",
              progress: true,
              html: true,
              // closeBtn:true,
              actions: [
                { label: "Dismiss", color: "white", handler: () => {} }
              ],
              timeout: 10000
            });
            // setTimeout(() => {
            //   if (t.dialog == true) {
            t.dialog = false;
            //   }
            // }, 5000);
          } else {
            _.forEach(res.errors, (v, k) => {
              t.participantFormErrors[k] = v;
              // const el = t.$refs["form" + v];
            });
            console.log(t.participantFormErrors);
          }
        })
        .catch(function(response) {
          //handle error
          console.log(response);
        })
        .finally(() => {
          t.registerLoading = false;
        });
      // });
      // }, 10000);
    },
    onVerify(response) {
      console.log(response);
      if (response) {
        this.participantFormRobot = true;
      }
    },
    onExpired() {},
    resetRecaptcha() {
      this.$refs.recaptcha.reset(); // Direct call reset method
    },
    isFieldError(fi) {
      if (this.participantFormErrors[fi] !== null) {
        return true;
      } else {
        return false;
      }
    },
    getFieldError(fi) {
      if (this.participantFormErrors[fi] !== null) {
        return this.participantFormErrors[fi];
      } else {
        return "";
      }
    },
    clearFieldError(fi) {
      this.participantFormErrors[fi] = null;
    },
    resetformregister() {
      // this.participantForm = {
      //   name: "",
      //   email: "",
      //   aff: "",
      //   nationality: ""
      // };
      this.dialog = false;
    },
    openAnnouncement() {
      const t = this;
      t.compAnouncement = "video-submission";
      t.anouncementDialog = true;
    },
    download(target, cnt) {
      exportFile(target, cnt);
    }
  },
  mounted() {
    const t = this;
    this.$api
      .get("/country/getall/")
      .then(res => {
        console.log(res);
        const tmpCountry = [];
        // console.log(res.data)
        _.forEach(res.data, function(v, k) {
          tmpCountry.push(v);
        });
        t.countryList = tmpCountry;
        t.countryListimt = tmpCountry;
        const fnd = _.filter(t.countryListimt, function(o) {
          return o.label.toLowerCase().indexOf("ind") > -1;
        });
        console.log(fnd);
      })
      .catch(err => {
        console.log(err);
      });

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

    if (this.$q.screen.lt.md) {
      this.maximizedToggle = true;
    } else {
      console.log("IS BIG");
    }

    this.participantFormErrors = _.cloneDeep(this.participantForm);
    // this.participantForm = {
    //   name: "Candra Nur Ihsan",
    //   email: "candra.nurihsan9@gmail.com",
    //   aff: "LAPAN",
    //   nationality: {
    //     id: 100,
    //     label: "Indonesia (ID)",
    //     nicename: "Indonesia"
    //   }
    // };

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
