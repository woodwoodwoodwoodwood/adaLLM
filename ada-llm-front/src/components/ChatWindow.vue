<template>
  <div class="chat-window">
    <div v-for="(message, index) in messages" :key="index" class="message-container">
      <div v-if="message.isBot" class="avatar-container">
        <img src="../assets/images/ustc.png" alt="Avatar" class="avatar" />
      </div>
      <div :class="getMessageClass(message)" class="message">
        <div v-html="renderMarkdown(message.text)"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick, watch } from 'vue';
import { marked } from 'marked';
import hljs from 'highlight.js';
import "highlight.js/styles/monokai-sublime.css"; // 引入高亮样式 这里我用的是sublime样式
import VueClipboard from 'vue-clipboard2';

/* <div class="code-header">
          <button class="copy-button" v-clipboard:copy="codeWithoutFence" v-clipboard:success="onCopySuccess" v-clipboard:error="onCopyError">
            复制
          </button>
        </div> */

export default {
  name: 'ChatWindow',
  props: {
    messages: {
      type: Array,
      required: true,
    },
  },
  setup(props) {
    // 使用 VueClipboard 插件
    VueClipboard.config.autoSetContainer = true;

    // 配置 marked 和 highlight.js
    const renderer = new marked.Renderer();
    renderer.code = (code, language) => {
      const codeWithoutFence = code.raw.replace(/^```.*\n/, '').replace(/\n```.*$/, '');
      const highlighted = hljs.highlight(codeWithoutFence, { language: code.lang || 'plaintext' }).value;
      return `<pre>
        
        <code class="hljs language-${language || 'plaintext'}">${highlighted}</code>
      </pre>`;  
    };

    marked.setOptions({
      renderer: renderer,
      gfm: true,
      tables: true,
      breaks: false,
      sanitize: false,
      smartLists: true,
    });

    // 渲染 Markdown 文本
    const renderMarkdown = (text) => {
      const textAsString = String(text);
      return marked(textAsString);
    };

    const getMessageClass = (message) => {
      return {
        'bot-message': message.isBot,
        'user-message': !message.isBot,
      };
    };

    // 定义复制成功的回调函数
    const onCopySuccess = () => {
      alert('代码复制成功');
      // 或者使用其他方式提醒用户复制成功
    };

    // 定义复制失败的回调函数
    const onCopyError = () => {
      alert('代码复制失败');
      // 或者使用其他方式提醒用户复制失败
    };

    // 在 DOM 渲染完毕后注册按钮事件
    const markdownContent = ref(null);
    const updateCopyButtons = () => {
      nextTick(() => {
        const copyButtons = document.querySelectorAll('.copy-button');
        copyButtons.forEach(button => {
          button.addEventListener('click', () => {
            button.innerText = '复制成功';
            setTimeout(() => {
              button.innerText = '复制';
            }, 1000);
          });
        });
      });
    };

    // 监听 messages 变化，在变化后更新按钮事件
    watch(() => props.messages, updateCopyButtons, { deep: true, immediate: true });

    return {
      getMessageClass,
      renderMarkdown,
      onCopySuccess,
      onCopyError,
      markdownContent,
    };
  },
};
</script>

<style >
.chat-window {
  flex: 1;
  overflow-y: auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 10px;
  background: #f9f9f9;
  
  width: 90%;
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
  max-width: 80%;
  font-size: 20px;
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

.copy-button {
  background: #f9f9f9;
  border: 1px solid #ccc;
  padding: 2px 5px; /* 减少内边距 */
  border-radius: 5px;
  font-size: 12px; /* 减小字体大小 */
  cursor: pointer;
  /* 如果需要固定宽度和高度，可以取消注释以下两行 */
  /* width: 60px; */
  /* height: 20px; */
}
</style>
