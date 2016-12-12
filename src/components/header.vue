<template>
  <header class="top-container">
    <div class="top-bar clearfix">
      <div class="topbar-nav">
        <ul class="nav-wrap">
          <li class="nav">一个班主任对学生做的小调查</li>
        </ul>
      </div>
      <div v-if="hasLogin" class="topbar-info">
        <span>{{user.name}}欢迎你</span>
        <span>|</span>
        <button @click="toLogout">退出</button>
      </div>
      <div v-else class="topbar-info">
        <button @click="toLogin">登录</button>
      </div>
    </div>
  </header>
</template>

<script>
  import { mapActions } from 'vuex';
  // import { mapState } from 'vuex'
  export default {
    data() {
      return {
        user: {},
        hasLogin: this.$store.state.user.hasLogin
      };
    },
    computed: { 
      hasLogin() {
        return this.$store.state.login.hasLogin ? this.$store.state.login.hasLogin : this.$store.state.user.hasLogin;
      },
      user() {
        return this.$store.state.user;
      }
    },
    methods: {
      ...mapActions(['enableLogin', 'logOut', 'loginFail']),
      toLogin() {
        // this.islogin = true;
        // // 给父组件传递信息
        // this.$parent.$emit('to-login', { text: this.islogin})  
        this.enableLogin();
      },
      toLogout() {
        this.logOut();
        this.loginFail();
        this.$router.replace({path: '/'});
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
    height: 50px;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
    background-color: #fff;
    z-index: 100;
    font-family: "Microsoft Yahei", sans-serif;
  }
  .topbar-nav {
    display: inline-block;
    float: left;
    height: 50px;
    margin-left: 40px;
    line-height: 50px;
    overflow: hidden;
  }
  .nav {
    font-size: 20px;
  }
  .topbar-info {
    position: absolute;
    top: 0;
    right: 40px;
    height: 50px;
    line-height: 50px;
  }
  button {
    border: none;
    font-size: 16px;
    color: #919191;
    background-color: #fff;
  }
  button:hover {
    color: #000;
  }
  .topbar-info span {
    color: #919191;
  }
  @media screen and (max-width: 500px) {
    .topbar-nav {
      margin-left: 25px;
    }
    .nav {
      font-size: 15px;
    }
    .topbar-info {
      right: 25px;
    }
    button {
      font-size: 15px;
    }
  }
</style>
