<template>
  <q-page class="q-pa-none">
    <Flipped flip-id="symposium">
      <div>
        <span class="xs text-h4">
          6<sup>th</sup> Asia Research Node Symposium For Humanosphere Science
        </span>
        <span class="gt-xs text-h2">
          6<sup>th</sup> Asia Research Node Symposium For Humanosphere Science
        </span>
      </div>
    </Flipped>
  </q-page>
</template>

<script>
import { Flipped } from "vue-flip-toolkit";
export default {
  layout: "Empty",
  name: "PageSymposium",
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
