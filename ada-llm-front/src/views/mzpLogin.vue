<template>
    <div class="login">
        <img
        alt=""
        src="../assets/homeBackground.png"
        class="lazyload-img background fullImage"
        style="height: 100vh; background-size: cover"
        />
        <div class="login-register">
        <div class="contain">
            <div class="big-box" :class="{ active: isLogin }">
            <div class="big-contain" v-if="isLogin">
                <div class="btitle">账户登录</div>
                <div class="buserForm">
                <input type="text" placeholder="用户名(4-20个字符)" />
                <input
                    type="password"
                    placeholder="密码(8-20个字符,包含数字,字母与下划线)"
                    v-model="userForm.password"
                />
                </div>
                <button class="bbutton" @click="login">登录</button>
            </div>
            <div class="big-contain" v-else>
                <div class="btitle">创建账户</div>
                <div class="buserForm">
                <input type="text" placeholder="用户名(4-20个字符)"  />
                <input
                    type="password"
                    placeholder="密码(8-20个字符,包含数字,字母与下划线)"
                    
                />
                </div>
                <button class="bbutton" @click="register">注册</button>
            </div>
            </div>
            <div class="small-box" :class="{ active: isLogin }">
            <!-- 注册 -->
            <div class="small-contain" v-if="isLogin">
                <div class="stitle"></div>
                <p class="scontent">中国科学技术大学计算机学院</p>
                <button class="sbutton" @click="changeType">注册</button>
            </div>
            <!-- 登录 -->
            <div class="small-contain" v-else>
                <div class="stitle">欢迎回来!</div>
                <p class="scontent">与我们保持联系，请登录你的账户</p>
                <button class="sbutton" @click="changeType">登录</button>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import router from '@/router'
import { ref, reactive } from 'vue'
// import { useStore } from 'vuex'

// const store = useStore()
const isLogin = ref(true)
const userForm = reactive({
  username: '',
  password: ''
})

// 更换登录还是注册页面
const changeType = () => {
  isLogin.value = !isLogin.value
  userForm.username = ''
  userForm.password = ''
}
</script>



<style scoped>
.login {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-color: transparent;
  color: #fff;
  user-select: none;
  background-size: cover;
}
.lazyload-img.fullImage {
  animation: reveal 1s ease-out;
}
.login .login-register {
  position: absolute;
  left: 25%;
  top: 25%;
  width: 50vw;
  height: 50vh;
  box-sizing: border-box;
  /* background-color: #eee; */
  background-color: transparent;
}

.contain {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0%;
  left: 0%;
  transuserform: translate(-50%, -50%);
  /* background-color: #fff; */
  border-radius: 20px;
  box-shadow:
    0 0 3px #f0f0f0,
    0 0 6px #f0f0f0;
}
.login .background {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
.big-box {
  width: 70%;
  height: 100%;
  position: absolute;
  border-top-right-radius: inherit;
  border-bottom-right-radius: inherit;
  /* background: linear-gradient(rgb(230, 181, 181), rgb(157, 213, 235)); */
  background-color: rgb(0, 0, 0, 0.3);
  top: 0;
  left: 30%;
  transuserform: translateX(0%);
  transition: all 1s;
}

.big-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.btitle {
  font-size: 3vh;
  font-weight: bold;
  color: whitesmoke;
}

.buserForm {
  width: 100%;
  height: 40%;
  padding: 2em 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.buserForm .errTips {
  display: block;
  width: 50%;
  text-align: left;
  color: whitesmoke;
  font-size: 0.7em;
  margin-left: 1em;
}

.buserForm input {
  width: 50%;
  height: 30px;
  border: none;
  outline: none;
  border-radius: 10px;
  padding-left: 2em;
  background-color: #f0f0f0;
}

.bbutton {
  width: 30%;
  height: 40px;
  border-radius: 24px;
  border: none;
  outline: none;
  background-color: RGB(106, 120, 141);
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

.small-box {
  width: 30%;
  height: 100%;
  background: linear-gradient(to bottom, #a6b3c4 30%, #6a788d 100%);
  /* background: rgb(189,236,236);
background: radial-gradient(circle, rgba(189,236,236,1) 0%, rgba(120,175,241,1) 100%); */
  opacity: var(--opacity, 0.95);
  position: relative;
  top: 0;
  left: 0;
  transuserform: translateX(0%);
  transition: all 1s;
  border-top-left-radius: inherit;
  border-bottom-left-radius: inherit;
}

/* 
* Prevents issues when the parent creates a 
* stacking context. (For example, using the transuserForm
* property )
*/

.small-contain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.stitle {
  font-size: 3vh;
  font-weight: bold;
  color: #fff;
}

.scontent {
  font-size: 1.5vh;
  color: #fff;
  text-align: center;
  padding: 2em 4em;
  line-height: 1.7em;
}

.sbutton {
  width: 60%;
  height: 40px;
  border-radius: 24px;
  border: 1px solid #fff;
  outline: none;
  background-color: transparent;
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

/* 滑动动作 */
.big-box.active {
  left: 0;
  transition: all 0.5s;
  border-top-left-radius: inherit;
  border-bottom-left-radius: inherit;
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.small-box.active {
  left: 70%;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-top-right-radius: inherit;
  border-bottom-right-radius: inherit;
  transuserform: translateX(-100%);
  transition: all 1s;
}
</style>