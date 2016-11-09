import Vue from 'vue'

export default {
  // JSON.parse方法将一个字符串解析成一个JSON对象
  state: JSON.parse(sessionStorage.getItem('user')) || {},
  mutations: {
    logIn(state, user) {
      // 从一个对象中解析出字符串
      sessionStorage.setItem('user', JSON.stringify(user))
      // ES6语法，从一个对象复制所有的属性到另一个对象，返回state对象 
      Object.assign(state, user)
    },
    logOut(state) {
      sessionStorage.removeItem('user')
      Object.keys(state).forEach(k => Vue.delete(state, k))
      Object.assign(state, {})
    }
  },
  actions: {
    logIn({commit}, user) {
      commit('logIn', user)
    },
    logOut({commit}) {
      commit('logOut')
    }
  }
}