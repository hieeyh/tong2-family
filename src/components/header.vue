<template>
<header class="top-container">
  <div class="top-bar clearfix">
    <div class="topbar-nav">
      <ul class="nav-wrap">
        <li class="nav">华科电信小范围调查结果展示平台</li>
      </ul>
    </div>
    <div class="topbar-info">
      <a href="#" v-on:click="toLogin">登录</a>
    </div>
  </div>
</header>
</template>

<script>
  export default {
    data() {
      return {
        islogin: false
      }
    },
    methods: {
      toLogin() {
        // this.islogin = true;
        // // 给父组件传递信息
        // this.$parent.$emit('to-login', { text: this.islogin})  
        this.$store.commit('enableLogin')     
      }
    }
  }
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
.top-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;
  background-color: #fff;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
  z-index: 100;
}
.topbar-nav {
  float: left;
  margin-left: 40px;
  display: inline-block;
  height: 60px;
  line-height: 60px;
  overflow: hidden;
}
.nav {
  font-size: 20px;
}
.topbar-info {
  position: absolute;
  top: 0;
  right: 40px;
  height: 60px;
  line-height: 60px;
}
.topbar-info a {
  color: #919191;
  text-decoration: none;
}
.topbar-info a:hover {
  color: #000;
}
.topbar-info span {
  color: #919191;
}
</style>
