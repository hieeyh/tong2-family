<template>
  <div id="app">
  <!-- 导航栏 -->
    <my-head></my-head>
    <my-nav></my-nav>
    <router-view class="main_content"></router-view>
    <!-- 遮罩层 -->
    <my-mask v-if="canlogin"></my-mask>
    <!-- 登录界面 -->
    <my-login v-if="canlogin"></my-login>
    <my-foot></my-foot>
</div>
</template>

<script>
  import myHead from 'components/header';
  import myNav from 'components/nav';
  import myMask from 'components/mask';
  import myLogin from 'components/login';
  import myFoot from 'components/foot';

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
      };
    },
    computed: {
      canlogin() {
        return this.$store.state.login.islogin;
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
  }
  .main_content {
    position: relative;
    top: 80px;
    width: 100%;
    margin-bottom: 135px;
    padding-left: 248px;
    box-sizing: border-box;
  }
  @media screen and (max-width: 964px) {
    .main_content {
      padding-left: 0;
    }
  }
</style>
