import Vue from "vue";
import axios from "axios";

import { setupCache } from "axios-cache-adapter";
const cache = setupCache({
  maxAge: 15 * 60 * 1000
});
let baseUrl;
if (process.env.DEV) {
  baseUrl =
    window.location.protocol + "//" + window.location.hostname + ":8090/api";
} else {
  baseUrl = window.location.protocol + "//" + window.location.host + "/api";
}
console.log("APIURL", window.location);
const axiosInstance = axios.create({
  baseURL: baseUrl,
  adapter: cache.adapter,
  progress: true,
  withCredentials: true
});

Vue.prototype.$api = axiosInstance;
Vue.prototype.$axios = axios;
