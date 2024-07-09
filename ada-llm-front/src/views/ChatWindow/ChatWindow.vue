<template>
  <div class="chat-container">
    <ChatWindow :messages="messages" />
    <div class="input-container">
      <el-input v-model="userInput" placeholder="Type your message..." @keyup.enter="sendMessage" class="chat-input"
        clearable style="width: 300px; font-size: large;" />
      <el-button type="primary" @click="sendMessage" style="height: 100%;">Send</el-button>
    </div>
    <HistorySidebar :history="chatHistory" />
  </div>
</template>

<script>
import ChatWindow from '../../components/ChatWindow.vue';
import HistorySidebar from '../../components/HistorySidebar.vue';
import { ref } from 'vue';

export default {
  name: 'ChatView',
  components: {
    ChatWindow,
    HistorySidebar,
  },
  setup() {
    const userInput = ref('');
    const messages = ref([
      { text: 'Hello! How can I help you today?', isBot: true }
    ]);

    const chatHistory = ref([
      'Message 1',
      'Message 2',
      'Message 3',
      'Message 4',
      'Message 5',
    ]);

    const sendMessage = () => {
      if (userInput.value.trim() !== '') {
        messages.value.push({ text: userInput.value, isBot: false });
        userInput.value = '';
        // Simulate bot response
        setTimeout(() => {
          messages.value.push({ text: 'This is a response from AI-assistant.', isBot: true });
        }, 1000);
      }
    };

    return {
      userInput,
      messages,
      chatHistory,
      sendMessage,
    };
  },
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 95vh;
  width: 70vw;
  padding: 20px;
  margin-left: 40%;
  justify-content: center;
  /* 仅在水平方向上居中 */
}

.input-container {
  display: flex;
  margin-top: 20px;
  width: 60%;
  height: 3%;
}

.chat-input {
  flex: 1;
  margin-right: 10px;
}

.el-button {
  width: 20%;
}
</style>