<template>
  <div class="BigBox">
    <div class="box">
      <!-- 滑动盒子 -->
      <div ref="preRef" class="pre-box">
        <h1>WELCOME</h1>
        <p>JOIN US!</p>
        <div class="img-box">
          <img src="../../assets/images/ustc.png" alt="">
        </div>
      </div>
      <!-- 注册盒子 -->
      <div class="register-form">
        <!-- 标题盒子 -->
        <div class="title-box">
          <h1>注册</h1>
        </div>
        <!-- 输入框盒子 -->
        <div ref="login-box" class="input-box">
          <el-form ref="registerForm" class="login_form" :model="registerForm" :rules="registerRules" auto-complete="on"
            label-position="left">

            <el-form-item name="username">

              <el-input v-model="register_username" style="width: 200px;" placeholder="用户名" clearable
                class="custom-el-input" />

            </el-form-item>

            <el-form-item name="password">
              <el-input v-model="register_password" style="width: 200px;" type="password" placeholder="密码" show-password
                class="custom-el-input" />
            </el-form-item>

            <el-form-item name="confirm_password">
              <el-input v-model="register_confirm_password" style="width: 200px" type="password" placeholder="确认密码"
                show-password class="custom-el-input" />

            </el-form-item>

          </el-form>
          <!-- 按钮盒子 -->
          <div class="btn-box">
            <button @click="handleRegister">注册</button>
            <!-- 绑定点击事件 -->
            <p @click="mySwitch">已有账号?去登录</p>
          </div>
        </div>


      </div>
      <!-- 登录盒子 -->
      <div class="login-form">
        <!-- 标题盒子 -->
        <div class="title-box">
          <h1>登录</h1>
        </div>
        <!-- 输入框盒子 -->
        <div ref="login-box" class="input-box">
          <el-form ref="loginForm" class="login_form" :model="loginForm" :rules="loginRules" auto-complete="on"
            label-position="left">
            <el-form-item name="username">
              <el-input v-model="login_username"
                style="width: 10vw; height: 2.5vh; border-radius: 20px; background-color: rgba(255, 255, 255, 0.5)"
                placeholder="请输入用户名" clearable class="custom-el-input" />
            </el-form-item>

            <el-form-item name="password">
              <el-input v-model="login_password" style="width: 10vw; height: 2.5vh" type="password" placeholder="请输入密码"
                show-password class="custom-el-input" />
            </el-form-item>

          </el-form>
          <!-- 按钮盒子 -->
          <div class="btn-box">
            <button @click.prevent="handleLogin">登录</button>
            <!-- 绑定点击事件 -->
            <p @click="mySwitch">没有账号?去注册</p>
          </div>
        </div>

      </div>
    </div>
  </div>

</template>





<style lang="scss" scoped>
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg: #283443;
$light_gray: #fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */

/* Custom styles */
.custom-el-input {
  width: 10vw !important;
  height: 2.5vh !important;
  border-radius: 40px;
}

.BigBox {
  width: 100vw;
  height: 100vh;
  /* 溢出隐藏 */
  overflow-x: hidden;
  display: flex;
  /* 渐变方向从左到右 */
  background: linear-gradient(to right, rgb(247, 209, 215), rgb(191, 227, 241));
}

@keyframes myMove {
  0% {
    transform: translateY(0%);
    opacity: 1;
  }

  50% {
    transform: translate(10%, -1000%);
  }

  75% {
    transform: translate(-20%, -1200%);
  }

  99% {
    opacity: .9;
  }

  100% {
    transform: translateY(-1800%) scale(1.5);
    opacity: 0;
  }
}

/* 最外层的大盒子 */
.box {
  width: 60%;
  /* 相对于视口宽度的百分比 */
  //   max-width: 2050px; /* 最大宽度限制 */
  height: 60vh;
  /* 相对于视口高度的百分比 */
  display: flex;
  /* 相对定位 */
  position: relative;
  z-index: 2;
  margin: auto;
  /* 设置圆角 */
  border-radius: 8px;
  /* 设置边框 */
  border: 1px solid rgba(255, 255, 255, .6);
  /* 设置盒子阴影 */
  box-shadow: 2px 1px 19px rgba(0, 0, 0, .1);
}

/* 滑动的盒子 */
.pre-box {
  /* 宽度为大盒子的一半 */
  width: 50%;
  /* width: var(--width); */
  height: 100%;
  /* 绝对定位 */
  position: absolute;
  /* 距离大盒子左侧为0 */
  left: 0;
  /* 距离大盒子顶部为0 */
  top: 0;
  z-index: 99;
  border-radius: 4px;
  background-color: #edd4dc;
  box-shadow: 2px 1px 19px rgba(0, 0, 0, .1);
  /* 动画过渡，先加速再减速 */
  transition: 0.5s ease-in-out;
}

/* 滑动盒子的标题 */
.pre-box h1 {
  margin-top: 25%;
  text-align: center;
  /* 文字间距 */
  letter-spacing: 5px;
  color: white;
  /* 禁止选中 */
  user-select: none;
  /* 文字阴影 */
  text-shadow: 4px 4px 3px rgba(0, 0, 0, .1);
}

/* 滑动盒子的文字 */
.pre-box p {
  height: 5%;
  line-height: 30px;
  text-align: center;
  margin: 3% 0;
  /* 禁止选中 */
  user-select: none;
  font-weight: bold;
  color: white;
  text-shadow: 4px 4px 3px rgba(0, 0, 0, .1);
}

/* 图片盒子 */
.img-box {
  width: 40%;
  height: 40%;
  margin: 20px auto;
  /* 设置用户禁止选中 */
  user-select: none;
  overflow: hidden;
}

/* 图片 */
.img-box img {
  width: 100%;
  transition: 0.5s;
}

/* 登录和注册盒子 */
.login-form,
.register-form {
  flex: 1;
  height: 100%;
}

/* 标题盒子 */
.title-box {
  height: 300px;
  line-height: 500px;

}

/* 标题 */
.title-box h1 {
  text-align: center;
  color: white;
  /* 禁止选中 */
  user-select: none;
  letter-spacing: 5px;
  text-shadow: 4px 4px 3px rgba(0, 0, 0, .1);

}

/* 输入框盒子 */
.input-box {
  display: flex;
  /* 纵向布局 */
  flex-direction: column;
  /* 水平居中 */
  align-items: center;
  height: "40%";
  width: "40%"
}


.login_form {
  width: 60%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

// .login_form>>>.el-form-item {
//   width: 80%;
//   margin-bottom: 10px;
// }

// .login_form>>>.login-input-username .el-input__inner {
//   border-radius: 20px;
//   background-color: rgba(255, 255, 255, 0.5);
// }

input:focus {
  /* 光标颜色 */
  color: #b0cfe9;

}

/* 聚焦时隐藏文字 */
input:focus::placeholder {
  opacity: 0;
}

/* 按钮盒子 */
.btn-box {
  display: flex;
  justify-content: center;
  width: 10vw;
  height: 3vh;
}

/* 按钮 */
button {
  width: 40%;
  height: 70%;
  margin: 0 7px;
  line-height: 30px;
  border: none;
  border-radius: 4px;
  background-color: #69b3f0;
  color: white;
  font-size: large;
}

/* 按钮悬停时 */
button:hover {
  /* 鼠标小手 */
  cursor: pointer;
  /* 透明度 */
  opacity: .8;
}

/* 按钮文字 */
.btn-box p {
  // width: 60%;
  height: 70%;
  line-height: 30px;
  /* 禁止选中 */
  user-select: none;
  font-size: large;
  color: white;
}

.btn-box p:hover {
  cursor: pointer;
  border-bottom: 1px solid white;
}
</style>

<!-- --------------------------------------------------------------------------------------- -->

<script lang="ts" setup>
import { ref, toRefs } from 'vue';
import { toRefs as _toRefs } from '@vue/reactivity';
import { useRouter } from 'vue-router'; // 导入 useRouter

const preRef = ref(null);
const flag = ref(false);

const login_username = ref('');
const login_password = ref('');
const register_username = ref('');
const register_password = ref('');
const register_confirm_password = ref('');

const { preRef: pre, flag: f } = toRefs({ preRef, flag });

const passwordType = ref('password');
const registerForm = ref({
  username: '',
  password: '',
  confirm_password: ''
});
const registerRules = ref({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ],
  confirm_password: [
    { required: true, message: '请再次输入密码', trigger: 'blur' }
  ]
});

const loginForm = ref({
  username: '',
  password: ''
});
const loginRules = ref({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ]
});

const router = useRouter(); // 使用 useRouter 钩子
const handleLogin = () => {
  // 登录逻辑
  router.push('/chat'); // 跳转到 login 路由
};

const handleRegister = () => {
  // 注册逻辑
};

const showPwd = () => {
  passwordType.value = passwordType.value === 'password' ? 'text' : 'password';
};

const mySwitch = () => {
  if (f.value) {
    pre.value.style.background = '#c9e0ed';
    pre.value.style.transform = 'translateX(100%)';
  } else {
    pre.value.style.background = '#edd4dc';
    pre.value.style.transform = 'translateX(0%)';
  }
  f.value = !f.value;
};
</script>