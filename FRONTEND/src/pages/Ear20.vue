<template>
  <q-page class="q-pa-none">
    <Flipped flip-id="ear20">
      <div>
        <span class="xs text-h4">EAR 20<sup>th</sup> Anniversary</span>
        <span class="gt-xs text-h2">EAR 20<sup>th</sup> Anniversary</span>
      </div>
    </Flipped>
  </q-page>
</template>

<script>
import { Flipped } from "vue-flip-toolkit";
export default {
  layout: "Empty",
  name: "PageEar20",
  components: {
    Flipped
  },
  computed: {},
  methods: {}
};
</script>
<style scoped>
.square {
  height: 50px;
  width: 200px;
  background: pink;
  align-items: center;
  padding: 16px;
}
.square.expanded {
  height: 200px;
  width: 250px;
  text-align: center;
}
</style>
