<template>
  <q-card style="min-width: 50vw;">
    <q-bar class="bg-primary text-white q-py-md" style="max-height: 5vh">
      <div class="text-h5">Follow the Event on Youtube</div>
      <q-space />
      <q-btn dense flat icon="close" v-close-popup>
        <q-tooltip content-class="bg-white text-primary">Close</q-tooltip>
      </q-btn>
    </q-bar>

    <q-card-section style="max-height: 95vh" class="scroll">
      <div class="text-h6 q-mb-lg">
        Commermoration Ceremony of the 20<sup>th</sup> Anniversary of Equatorial
        Atmosphere Radar:
        <a href="https://www.youtube.com/watch?v=zcH-iuS67ZQ" target="_blank">
          https://www.youtube.com/watch?v=zcH-iuS67ZQ
        </a>
      </div>
      <div class="text-h6">
        Symposium (INCREASE and 6<sup>th</sup> ARN):
        <a href="https://youtu.be/UAbiej7kVwI" target="_blank">
          https://youtu.be/UAbiej7kVwI
        </a>
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
  name: "EventYoutube",
  data() {
    return {};
  }
};
</script>
<style scoped></style>
