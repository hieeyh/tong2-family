<template>
  <div id="login">
    <div class="title">
      <h3>登录</h3>
    </div>    
    <div class="loginMess">
      <input class="message" type="text" name="name" placeholder="请输入你的姓名" v-model="form.name">
      <div class="warn" v-show="issubmit && !form.name">姓名不能为空</div>
      <input class="message" type="text" name="pass" placeholder="请输入你的QQ号" v-model="form.qq">
      <div class="warn" v-show="issubmit && !form.qq">qq号不能为空</div>
    </div>
    <div class="button">
      <button @click="toQuit">取消</button>
      <!-- <button>取消</button> -->
      <button @click="toSubmit">确定</button>
    </div>
  </div>
</template>

<script>
  import { mapActions } from 'vuex';
  export default {
    // data() {
    //   return {
    //     isquit: false
    //   }
    // },
    data() {
      return {
        issubmit: false,
        form: {
          name: '',
          qq: '',
          hasLogin: false
        }
      };
    },
    methods: {
      ...mapActions(['disableLogin', 'logIn', 'loginSuccess']),
      toQuit() {
        // this.isquit = true;
        // this.$parent.$emit('to-quit', { text: this.isquit})
        this.disableLogin();
      },
      toSubmit() {
        this.issubmit = true;

        if(!this.form.qq || !this.form.name) return;
        this.form.hasLogin = true;
        this.disableLogin();
        this.logIn(this.form);
        this.loginSuccess(); 
        this.$router.replace({path: '/'});
      }
    }
  }
</script>

<style scoped>
  #login {
    position:fixed;
    left: 50%;
    top: 50%;
    width: 410px;
    height: 270px;
    margin-top: -135px;
    margin-left: -205px; 
    z-index:1000; 
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
    margin-bottom: 5px;
    font-size: 15px;
  }
  .warn {
    margin-bottom:10px;
    color: red;
    font-size: 12px;
  }
  .button {
    margin-top: 20px;
    margin-left: 268px;
  }
  button {
    width: 58px;
    height: 34px;
    margin-right: 5px;
    border: 0;
    font-size: 14px;
    background-color: #f80016;
    color: #fff; 
  }
  @media screen and (max-width: 430px) {
    #login {
      width: 300px;
      height: 264px;
      margin-top: -120px;
      margin-left: -150px; 
    }
    .message {
      width: 240px;
      font-size: 14px;
    }
    .button {
      margin-left: 160px;
    }
  }
</style>