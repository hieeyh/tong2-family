<template>
  <div id="nav-list">
    <ul class="nav-left">
      <li class="nav-item" v-for="(item, index) in items">
        <!-- <a href="#">{{item.name}}</a> -->
        <router-link :to="'/' + item.ad">{{item.name}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: [
        {name: '通信1502班关键词分析', ad: 'wordcloud'},
        {name: '最喜爱建筑分布', ad: 'building'},
        {name: '最喜爱食堂分布', ad: 'canteen'},
        {name: '最常自习地点分布', ad: 'selfstudy'},
        {name: '课程难度调查', ad: 'difficult'},
        {name: '课程兴趣调查', ad: 'interest'},
        {name: '寝室学习氛围', ad: 'bedroom'},
        {name: '毕业展望', ad: 'graduate'},
        {name: '工作日起床时间', ad: 'getup'},
        {name: '工作日睡觉时间', ad: 'gotobed'},
        {name: '每日在校吃饭花销', ad: 'eat'},
        {name: '周末娱乐方式', ad: 'amuse'},
        {name: '目前是否单身', ad: 'single'},
        {name: '班群聊天记录分析', ad: 'chat'},
        {name: '我的群聊活跃时间', ad: 'onlyme'}
      ]
    };
  }
}
</script>

<style scoped>
  #nav-list {
    position: fixed;
    top: 50px;
    bottom: 0;
    left: 0;
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
    size: 14px;
    color: #b2b2b2;
  }
  .nav-item a:hover {
    color: rgba(255, 255, 255, 0.8);
  }
  a.router-link-active {
    color: rgba(255, 255, 255, 0.9);
  }
  @media screen and (max-width: 964px) {
    #nav-list {
      position: relative;
      width: 100%;
      padding: 5px 20px;
      box-sizing: border-box;
      line-height: 20px;
    }
    .nav-left {
      width: 100%;
    }
    .nav-left .nav-item {
      display: inline-block;
      margin: 5px 0;
      padding: 0 8px;
      border-right: solid 1px #b2b2b2;
    }
    .nav-item:last-child {
      border-right: none;
    }
  }
</style>