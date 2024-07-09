<template>
  <div class="chat-window">
    <div v-for="(message, index) in this.messages" :key="index" class="message-container">
      <div v-if="message.isBot" class="avatar-container">
        <img src="../assets/images/ustc.png" alt="Avatar" class="avatar" />
      </div>
      <div :class="{ 'bot-message': message.isBot, 'user-message': !message.isBot }" class="message">
        {{ message.text }}
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'ChatWindow',
  props: {
    messages: {
      type: Array,
      required: true,
    },
  },
  setup(props) {
    return {
      messages: props.messages,
    };
  },
};
</script>

<style scoped>
.chat-window {
  flex: 1;
  overflow-y: auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 10px;
  background: #f9f9f9;
  width: 60%;
}

.message-container {
  display: flex;
  align-items: flex-start;
  /* Align items to the top */
}

.avatar-container {
  margin-right: 10px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.message {
  margin: 10px 0;
  padding: 10px;
  border-radius: 8px;
  max-width: 60%;
  font-size: large;
  border-radius: 30px;
  /* 圆角 */
}

.bot-message {
  background: #e0f7fa;
}

.user-message {
  background: #e1bee7;
  margin-left: auto;
  /* 让用户消息靠右对齐 */
}
</style>