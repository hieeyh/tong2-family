<template>
  <div id="login">
    <div class="title">
      <h3>登录</h3>
    </div>    
    <div class="loginMess">
      <input class="message" type="text" name="name" placeholder="请输入你的姓名">
      <input class="message" type="password" name="pass" placeholder="请输入你的学号">
    </div>
    <div class="button">
      <button v-on:click="toQuit">取消</button>
      <!-- <button>取消</button> -->
      <button>确定</button>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        isquit: false
      }
    },
    methods: {
      toQuit() {
        // this.isquit = true;
        // this.$parent.$emit('to-quit', { text: this.isquit})
        this.$store.commit('disableLogin')
      }
    }
  }
</script>

<style scoped>
#login {
  position:fixed;
  width: 420px;
  height: 250px;
  z-index:1000; 
  margin-left: -210px; 
  margin-top: -125px;
  left: 50%;
  top: 50%;
  background-color: #fff;
}
.title {
  height: 56px;
  background-color: #f80016;
}
h3 {
  padding-left: 35px;
  line-height: 56px;
  color: #fff;
  font-weight: 300;
}
.loginMess {
  padding-top: 20px;
  padding-left: 30px;

}
.message {
  display: block;
  width: 360px;
  height: 35px;
  margin-bottom: 10px;
  font-size: 15px;
}
.button {
    margin-left: 268px;
    margin-top: 20px;
}
button {
  width: 58px;
  height: 34px;
  margin-right: 5px;
  border: 0;
  background-color: #f80016;
  color: #fff; 
  font-size: 14px;
}
</style>