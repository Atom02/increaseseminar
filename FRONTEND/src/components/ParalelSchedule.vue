<template>
  <q-card style="min-width: 50vw;">
    <q-bar class="bg-primary text-white q-py-md" style="max-height: 5vh">
      <div class="text-h5">Paralel Schedule</div>
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
  name: "ParalelSchedule",
  data() {
    return {
      links: [
        {
          link: "pdf/schedule/AllRoomSchedule.pdf",
          label: "Ear20 All Room Schedule"
        },
        {
          link: "pdf/schedule/ScheduleRoom1.pdf",
          label: "Ear20 Room 1 Schedule"
        },
        {
          link: "pdf/schedule/ScheduleRoom2.pdf",
          label: "Ear20 Room 2 Schedule"
        },
        {
          link: "pdf/schedule/ScheduleRoom3.pdf",
          label: "Ear20 Room 3 Schedule"
        },
        {
          link: "pdf/schedule/ScheduleRoom4.pdf",
          label: "Ear20 Room 4 Schedule"
        },
        {
          link: "pdf/schedule/ScheduleRoom5.pdf",
          label: "Ear20 Room 5 Schedule"
        },
        {
          link: "pdf/schedule/ScheduleRoom6.pdf",
          label: "Ear20 Room 6 Schedule"
        },
        {
          link: "pdf/schedule/ScheduleRoom7.pdf",
          label: "Ear20 Room 7 Schedule"
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
