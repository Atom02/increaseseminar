<template>
  <div id="q-app">
    <!-- <span>{{ key }}</span> -->
    <Flipper :flip-key="key" spring="stiff">
      <keep-alive max="5">
        <router-view />
      </keep-alive>
    </Flipper>
  </div>
</template>
<script>
import { Flipper } from "vue-flip-toolkit";
export default {
  name: "App",
  components: {
    Flipper
  },
  computed: {
    key() {
      return this.$route.path;
    }
  }
};
</script>
