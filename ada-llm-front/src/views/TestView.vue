<template>
    <pre v-html="highlightedCode"></pre>
  </template>
  
  <script>
  import 'highlight.js/styles/github-dark.css';
  import hljs from 'highlight.js';
  
  export default {
    data() {
      return {
        // 原始代码字符串
        code: `
  #include <iostream>
  
  int main() {
      int num1, num2;
      std::cout << "Enter two integers: ";
      std::cin >> num1 >> num2;
  
      if (num1 > num2) {
          std::cout << "The larger number is: " << num1 << std::endl;
      } else if (num2 > num1) {
          std::cout << "The larger number is: " << num2 << std::endl;
      } else {
          std::cout << "Both numbers are equal." << std::endl;
      }
  
      return 0;
  }`,
        // 用于存储高亮后的代码
        highlightedCode: '',
      };
    },
    mounted() {
      this.highlightCode();
    },
    methods: {
      highlightCode() {
        // 替换 HTML 实体为它们的文本形式
        const codeToHighlight = this.code.replace(/&lt;/g, '<').replace(/&gt;/g, '>');
        // 使用 highlight.js 进行高亮
        this.highlightedCode = hljs.highlight('cpp', codeToHighlight).value;
      },
    },
  };
  </script>