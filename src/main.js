import Vue from 'vue';
import App from './App';
import VueRouter from 'vue-router';
import store from './store/store';

Vue.use(VueRouter);

// 定义路由组件
const Worldcloud = require('components/cloud.vue');
const Building = require('components/building.vue');
const Canteen = require('components/canteen.vue');
const Selfstudy = require('components/selfstudy.vue');
const Difficult = require('components/difficult.vue');
const Interest = require('components/interest.vue');
const Bedroom = require('components/bedroom.vue');
const Graduate = require('components/graduate.vue');
const Getup = require('components/getup.vue');
const Gotobed = require('components/gotobed.vue');
const Eat = require('components/eat.vue');
const Amuse = require('components/amuse.vue');
const Single = require('components/single.vue');
const Chat = require('components/chat.vue');
const Onlyme = require('components/onlyme.vue');

// 定义路由
const routes = [
  { path: '/', redirect: '/wordcloud' },
  { path: '/wordcloud', component: Worldcloud },
  { path: '/building', component: Building },
  { path: '/canteen', component: Canteen },
  { path: '/selfstudy', component: Selfstudy },
  { path: '/difficult', component: Difficult },
  { path: '/interest', component: Interest },
  { path: '/bedroom', component: Bedroom },
  { path: '/graduate', component: Graduate },
  { path: '/getup', component: Getup },
  { path: '/gotobed', component: Gotobed },
  { path: '/eat', component: Eat },
  { path: '/amuse', component: Amuse },
  { path: '/single', component: Single },
  { path: '/chat', component: Chat },
  { path: '/onlyme', component: Onlyme }
];

// 创建router实例
const router = new VueRouter({
  routes
});

// const store = new Vuex.Store({
//   state: {
//     islogin: false
//   },
//   mutations: {
//     enableLogin(state) {
//       state.islogin = true
//     },
//     disableLogin(state) {
//       state.islogin = false
//     }
//   }
// })

/* eslint-disable no-new */
new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router,
  store
});




