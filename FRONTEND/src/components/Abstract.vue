<template>
  <q-card style="min-width: 50vw;">
    <q-bar class="bg-primary text-white q-py-md" style="max-height: 5vh">
      <div class="text-h5">Abstract</div>
      <q-space />
      <q-btn dense flat icon="close" v-close-popup>
        <q-tooltip content-class="bg-white text-primary">Close</q-tooltip>
      </q-btn>
    </q-bar>

    <q-card-section style="max-height: 95vh" class="scroll">
      <template v-for="(item, index) in links">
        <div class="q-mb-md text-h6" :key="index">
          <a :href="item.link" target="_blank">
            {{ item.label }}
          </a>
        </div>
      </template>
    </q-card-section>

    <q-separator />

    <!-- <q-card-actions align="right">
          <q-btn flat label="Close" color="primary" v-close-popup />
        </q-card-actions> -->
  </q-card>
</template>
<script>
export default {
  name: "Abstract",
  data() {
    return {
      links: [
        {
          link: "pdf/ABSTRACT_INCREASE_invited.pdf",
          label: "Abstract of INCREASE and 6th ARN Symposium (INVITED SPEAKERS)"
        },
        {
          link: "pdf/ASBTRACT_AUTHOR.pdf",
          label: "Abstract of INCREASE and 6th ARN Symposium"
        },
      ]
    };
  }
};
</script>
<style scoped>
div {
  text-align: justify;
  text-justify: inter-word;
  margin-bottom: 0.5vw;
}
</style>
