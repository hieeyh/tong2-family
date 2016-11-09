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
      <button v-on:click="toQuit">取消</button>
      <!-- <button>取消</button> -->
      <button v-on:click="toSubmit">确定</button>
    </div>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
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
      }
    },
    methods: {
      ...mapActions(['disableLogin', 'logIn', 'loginSuccess']),
      toQuit() {
        // this.isquit = true;
        // this.$parent.$emit('to-quit', { text: this.isquit})
        this.disableLogin()
      },
      toSubmit() {
        this.issubmit = true

        if(!this.form.qq || !this.form.name) return
        this.form.hasLogin = true
        this.disableLogin() 
        this.logIn(this.form)
        this.loginSuccess()  
        this.$router.replace({path: '/'})
      }
    }
  }
</script>

<style scoped>
#login {
  position:fixed;
  width: 420px;
  height: 270px;
  z-index:1000; 
  margin-left: -210px; 
  margin-top: -135px;
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
  margin-bottom: 5px;
  font-size: 15px;
}
.warn {
  color: red;
  font-size: 12px;
  margin-bottom:10px;
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