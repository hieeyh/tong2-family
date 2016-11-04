<template>
<div id="#app">
<!-- 导航栏 -->
  <my-head></my-head>
  <my-nav></my-nav>
  <transition>
    <router-view></router-view>
  </transition>
  
</div>
</template>

<script>
import myHead from './components/header'
import myNav from './components/nav'

export default {
  name: 'app',
  components: {
    myHead,
    myNav
    // myContainer
  }
}
</script>

<style>
ul {
  list-style: none;
}
a {
  text-decoration: none;
}
#app {
  font-family: Helvetica, Arial, "Microsoft Yahei", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  width: 100%;
  overflow: hidden;
}
</style>
