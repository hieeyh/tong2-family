import Vue from 'vue'

export default {
  state: {
    islogin: false,
    hasLogin: false
  },
  mutations: {
    enableLogin(state) {
      state.islogin = true
    },
    disableLogin(state) {
      state.islogin = false
    },
    loginSuccess(state) {
      state.hasLogin = true
    },
    loginFail(state) {
      state.hasLogin = false
    }
  },
  actions: {
    enableLogin({commit}) {
      commit('enableLogin')
    },
    disableLogin({commit}) {
      commit('disableLogin')
    },
    loginSuccess({commit}) {
      commit('loginSuccess')
    },
    loginFail({commit}) {
      commit('loginFail')
    },
  }
}