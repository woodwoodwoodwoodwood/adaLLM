<template>
  <div class="container">
    <div class="sidebar-left">
      <HistorySidebar :history="chatHistory" />
    </div>
    <div class="chat-container">
      <ChatWindow :messages="messages" />
      <div class="input-container">
        <el-input v-model="userInput" placeholder="Type your message..." @keyup.enter="sendMessage" class="chat-input"
          clearable style="width: 300px; font-size: large;" />
        <el-button type="primary" @click="sendMessage" style="height: 100%;">Send</el-button>
      </div>
    </div>
    <div class="sidebar-right">
      <h3>你的文件库</h3>
      <el-upload
        class="upload-demo"
        action="http://localhost:5000/upload"
        :on-success="handleUploadSuccess"
        :on-error="handleUploadError"
        :before-upload="beforeUpload"
        :file-list="fileList"
        multiple
        drag
        list-type="text"
        style="margin-bottom: 20px;"
      > 
        <el-button type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">支持拖拽文件上传</div>
      </el-upload>
      <ul class="file-list">
        <li v-for="file in uploadedFiles" :key="file">
          <a :href="`http://localhost:5000/uploads/${file}`" target="_blank">{{ file }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import ChatWindow from '../../components/ChatWindow.vue';
import HistorySidebar from '../../components/HistorySidebar.vue';
import { ref, onMounted } from 'vue';
import { sendPromptMessage } from '@/api/sparkAPI';
import {fetchFiles} from '@/api/fileAPI';
import { UploadFilled } from '@element-plus/icons-vue'
// import axios from 'axios';
// import marked from 'marked';


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

    const fileList = ref([]);
    const uploadedFiles = ref([]);

    const sendMessage = async () => {
      if (userInput.value.trim() !== '') {
        messages.value.push({ text: userInput.value, isBot: false });
        // 获取用户输入并清空输入框
        const userMessage = userInput.value;
        userInput.value = '';

        // // Simulate bot response
        // setTimeout(() => {
        //   messages.value.push({ text: 'This is a response from AI-assistant.', isBot: true });
        // }, 1000);

        try {
          // 调用后端接口发送消息
          const res = await sendPromptMessage({ prompt: userMessage });
          console.log('Response from AI:', res);

          // 将AI响应添加到消息列表
          messages.value.push({ text: res.response, isBot: true });
        } catch (error) {
          console.error('Error sending message:', error);
          messages.value.push({ text: 'There was an error getting the response from the AI.', isBot: true });
        }

      }
    };

    const beforeUpload = (file) => {
      console.log('Before upload:', file);
      return true;
    };

    const handleUploadSuccess = (response, file, fileList) => {
      console.log('Upload success:', response);
      uploadedFiles.value.push(file);
    };

    const handleUploadError = (error, file, fileList) => {
      console.error('Upload error:', error);
    };

    const loadFiles = async () => {
      try {
        const files = await fetchFiles();
        uploadedFiles.value = files;
      } catch (error) {
        console.error('Error fetching files:', error);
      }
    };

    onMounted(() => {
      loadFiles();
    });

    return {
      userInput,
      messages,
      chatHistory,
      sendMessage,
      fileList,
      uploadedFiles,
      beforeUpload,
      handleUploadSuccess,
      handleUploadError
    };
  },
};
</script>

<style scoped>
.container {
  display: flex;
  height: 95vh;
  width: 100vw;
  padding: 20px;
}

.sidebar-left {
  width: 20%;
  padding: 20px;
  overflow-y: auto;
  border-right: 1px solid #ebeef5;
}

.chat-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 0 20px;
  width: 60%;
}

.input-container {
  display: flex;
  margin-top: 20px;
  width: 90%;
  height: 4%;
}

.chat-input {
  flex: 1;
  margin-right: 10px;
}

.el-button {
  width: 100px;
}

.sidebar-right {
  width: 20%;
  padding: 20px;
  overflow-y: auto;
  border-left: 1px solid #ebeef5;
  background-color: #f9f9f9;
}

.upload-demo {
  margin-bottom: 20px;
}

.file-list {
  list-style: none;
  padding: 0;
}

.file-list li {
  margin: 5px 0;
}
</style>