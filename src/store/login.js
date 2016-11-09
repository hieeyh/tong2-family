import Vue from 'vue'

export default {
  state: {
    islogin: false
  },
  mutations: {
    enableLogin(state) {
      state.islogin = true
    },
    disableLogin(state) {
      state.islogin = false
    }
  },
  actions: {
    enableLogin({commit}) {
      commit('enableLogin')
    },
    disableLogin({commit}) {
      commit('disableLogin')
    }
  }
}