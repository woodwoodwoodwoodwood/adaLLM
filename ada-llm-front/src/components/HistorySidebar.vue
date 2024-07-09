<template>
  <div class="history-sidebar">
    <div class="history-header">
      Chat History
    </div>
    <ul class="history-list">
      <li v-for="(message, index) in history" :key="index" class="history-item" @click="refreshPage">
        {{ message }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HistorySidebar',
  props: {
    history: {
      type: Array,
      required: true,
    },
  },
  methods: {
    refreshPage() {
      window.location.reload();
    },
  },
};
</script>

<style scoped>
.history-sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15vw;
  background-color: #f9f9f9;
  border-left: 1px solid #ccc;
  padding: 20px;
  overflow-y: auto;
}

.history-header {
  font-weight: bold;
  font-size: larger;
  padding-bottom: 10px;
  border-bottom: 1px solid #ccc;
  margin-bottom: 10px;
}

.history-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.history-item {
  padding: 5px;
  border-radius: 5px;
  background-color: #f0ecec;
  margin-bottom: 5px;
  height: 4vh;
  font-size: large;
  transition: background-color 0.0s;
  /* 添加过渡效果 */
  cursor: pointer;
  /* 鼠标悬停时变为手形 */
}

.history-item:hover {
  background-color: #cfcfcf;
  /* 鼠标悬停时的背景颜色 */
}
</style>
