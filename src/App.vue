<template>
<div id="#app">
<!-- 导航栏 -->
  <my-head></my-head>
  <my-nav></my-nav>
  <transition>
    <router-view></router-view>
  </transition>
  <my-mask v-if="canlogin"></my-mask>
  <my-login v-if="canlogin"></my-login>
  <my-foot></my-foot>
</div>
</template>

<script>
import myHead from './components/header'
import myNav from './components/nav'
import myMask from './components/mask'
import myLogin from './components/login'
import myFoot from './components/foot'

export default {
  name: 'app',
  components: {
    myHead,
    myNav,
    myMask,
    myLogin,
    myFoot
  },
  data() {
    return {
      canlogin: false
    }
  },
  computed: {
    canlogin() {
      return this.$store.state.login.islogin
    }
  }
  // methods: {
  //   toLogin(islogin) {
  //     this.canlogin = islogin;
  //   },
  //   toQuit(isquit) {
  //     this.canlogin = !isquit;
  //   }
  // },
  // data() {
  //   return {
  //     canlogin: false
  //   }
  // },
  // created() {
  //   this.$on('to-login', this.toLogin)
  //   this.$on('to-quit', this.toQuit)
  // },
  // beforeDestroy() {
  //   this.$off('to-login', this.toLogin)
  //   this.$off('to-quit', this.toQuit)
  // }
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
  font-family: "Microsoft Yahei", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  width: 100%;
  overflow: hidden;
}
</style>
