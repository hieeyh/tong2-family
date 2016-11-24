<template>
<div id="nav-list">
  <ul class="nav-left">
    <li class="nav-item" v-for="(item, index) in items">
      <!-- <a href="#">{{item.name}}</a> -->
      <router-link v-bind:to="'/' + item.add" v-bind:class="{active: isActive[index]}">{{item.name}}</router-link>
    </li>
  </ul>
</div>
</template>

<script>
export default {
  data () {
    return {
      items: [
        {name: '通信1502班关键词分析', add: 'wordcloud'},
        {name: '最喜爱建筑分布', add: 'building'},
        {name: '最喜爱食堂分布', add: 'canteen'},
        {name: '最常自习地点分布', add: 'selfstudy'},
        {name: '课程难度调查', add: 'difficult'},
        {name: '课程兴趣调查', add: 'interest'},
        {name: '寝室学习氛围', add: 'bedroom'},
        {name: '毕业展望', add: 'graduate'},
        {name: '工作日起床时间', add: 'getup'},
        {name: '工作日睡觉时间', add: 'gotobed'},
        {name: '每日在校吃饭花销', add: 'eat'},
        {name: '周末娱乐方式', add: 'amuse'},
        {name: '目前是否单身', add: 'single'},
        {name: '班群聊天记录分析', add: 'chat'},
        {name: '我的群聊活跃时间', add: 'onlyme'}
      ],
      isActive: [true, false,false,false,false,false,false,false,false,false,false,false,false,false,false]
    }
  }
}
</script>

<style scoped>
#nav-list {
  position: fixed;
  left: 0;
  bottom: 0;
  top: 60px;
  padding: 20px 40px;
  line-height: 40px;
  background-color: #293c55;
  overflow-y: auto;
  z-index: 15;
}
.nav-left {
  width: 168px;
  font-family: "Microsoft Yahei", sans-serif;
}
.nav-item a {
  color: #b2b2b2;
  size: 14px;
}
.nav-item a:hover {
  color: rgba(255, 255, 255, 0.8);
}
a.router-link-active {
  color: rgba(255, 255, 255, 0.9);
}
</style>