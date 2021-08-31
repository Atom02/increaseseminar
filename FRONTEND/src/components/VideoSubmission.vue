<template>
  <q-card style="min-width: 50vw;">
    <q-bar class="bg-primary text-white q-py-md" style="max-height: 5vh">
      <div class="text-h5">Video Submission</div>
      <q-space />
      <q-btn dense flat icon="close" v-close-popup>
        <q-tooltip content-class="bg-white text-primary">Close</q-tooltip>
      </q-btn>
    </q-bar>

    <q-card-section style="max-height: 95vh" class="scroll">
      <div style="text-align:right">
        <a
          href="~assets/pdf/1_scansplit_Announcement_to _all_participants_20210831.pdf"
          download="increase video submission.pdf"
          class="q-pa-md bg-primary text-white"
        >
          Download Full PDF
        </a>
      </div>
      <div>Dear participants of INCREASE and 6th ARN Symposium 2021</div>
      <div>Thank you for submitting your abstract.</div>
      <div>
        For all presenters, <b class="bg-yellow-4">except</b> Keynote/Invited
        speakers, please kindly prepare a 10-minute presentation video and
        upload it on Youtube (see FAQ section). The video link is then sent to
        the INCREASE email address (increase@lapan.go.id) by
        <b class="bg-yellow-4">10 September 2021</b>.
      </div>
      <div>
        We encourage participants to share the video link via URL shortener such
        as bitly (https://bitly.com/). If you decide to use bitly, here are the
        steps of creating the link:<br />
        <ol>
          <li>Register to bitly,</li>
          <li>Login,</li>
          <li>Create your link by pressing the 'CREATE' button,</li>
          <li>Put your YouTube link in the empty form, and press 'CREATE',</li>
          <li>
            Share the shortened link (for example: bit.ly/my_presentation_video)
            to INCREASE committee,
          </li>
          <li>
            Participants are allowed to revise the video link for updating or
            replacing the video content, as long as the shortened link remains
            the same.
          </li>
        </ol>
      </div>
      <div>
        Furthermore, your presentation file may only contain 10 slides of
        presentation pages and the presentation file should be uploaded to
        Easychair in PDF form by
        <b class="bg-yellow-4">10 September 2021.</b>
      </div>
      <div>
        If any participant wants to improve their abstract (title/content), they
        are allowed to do so through their Easychair account. The deadline for
        this improvement is <b class="bg-yellow-4">10 September 2021.</b>
      </div>
      <div>
        In addition, if you wish to proceed to the publication process, the
        deadline for submitting your full paper is
        <b class="bg-yellow-4">
          20 September 2021 at 23.59 UTC or 21 September 2021 at 06.59 WIB
          (Local Western Indonesia Time).
        </b>
        Regarding your manuscript, there is no specific page limit for the full
        paper. We suggest you to follow the guidelines and key points provided
        in the links below for the preparation of the manuscript:
        <ol>
          <li>
            <a
              href="https://www.springer.com/gp/authors-editors/book-authors-editors/your-publication-journey/manuscript-preparation"
              target="blank"
            >
              Instructions for Authors: Manuscript Guidelines
            </a>
          </li>
          <li>
            <a
              href="https://resource-cms.springernature.com/springer-cms/rest/v1/content/3322/data/Key+style+points"
              target="blank"
            >
              https://resource-cms.springernature.com/springer-cms/rest/v1/content/3322/
              data/Key+style+points
            </a>
          </li>
        </ol>
      </div>
      <div>
        Lastly, please ensure that the email address registered in Easychair
        system is correct (especially the corresponding author's email address)
        since our announcements is delivered to the author(s) through the email
        address.
      </div>
      <div>
        Further information related to technical matters of the presentation at
        the conference will be informed later.
      </div>
      <div>
        Should you have any inquiries, please kindly contact us at
        <a target="blank" href="mailto:increase@lapan.go.id">
          increase@lapan.go.id.
        </a>
      </div>
      <div>
        <b class="bg-yellow-4">
          NOTE: all submitted abstracts are accepted for oral presentation.
        </b>
      </div>
    </q-card-section>

    <q-separator />

    <!-- <q-card-actions align="right">
          <q-btn flat label="Close" color="primary" v-close-popup />
        </q-card-actions> -->
  </q-card>
</template>
<script>
export default {
  name: "VideoSubmission"
};
</script>
<style scoped>
div {
  text-align: justify;
  text-justify: inter-word;
  margin-bottom: 0.5vw;
}
</style>
