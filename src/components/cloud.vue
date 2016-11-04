<template>
  <div class="main_content">
    <div id="word_cloud1"></div>
    <div id="word_cloud2"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import 'echarts-wordcloud'
  
  export default {
    data () {
      return {
        chart: null,
        title: '通信1502班群聊记录关键词',
        wordContent: [
          { name: '通信1502班', value: 80 },
          { name: '阳阳', value: 50 },
          { name: '超东', value: 50 },
          { name: '秀秀', value: 50 },
          { name: '东哥', value: 40 },
          { name: '鑫鑫', value: 40 },
          { name: '路远', value: 40 },
          { name: '越越', value: 40 },
          { name: '小金', value: 35 },
          { name: '班班', value: 35 },
          { name: '邓鸡蛋', value: 35 },
          { name: '启迪', value: 35 },
          { name: '星星', value: 35 },
          { name: '佳佳', value: 35 },
          { name: '洲哥', value: 35 },
          { name: '露露', value: 35 },
          { name: '帅殷', value: 35 },
          { name: '小灰灰', value: 30 },
          { name: '嘉成', value: 30 },
          { name: '良良', value: 30 },
          { name: '宇航', value: 30 },
          { name: '莘然', value: 30 },
          { name: '若非', value: 30 },
          { name: '年年', value: 30 },
          { name: '大黄', value: 30 },
          { name: '翔渣', value: 30 },
          { name: '高谭', value: 30 },
          { name: '弱鸡', value: 30 },
          { name: '楠神', value: 30 },
          { name: '千赫', value: 30 },
          { name: '金晖', value: 30 },
          { name: '啦啦啦', value: 50 },
          { name: '寝室', value: 40 },
          { name: '红包', value: 40 },
          { name: '学渣', value: 40 },
          { name: '选课', value: 40 },
          { name: '厉害勒', value: 30 },
          { name: '有毒', value: 30 },
          { name: '实验', value: 30 },
          { name: '生日快乐', value: 30 },
          { name: '优秀', value: 20 },
          { name: '微积分', value: 20 },
          { name: '电路', value: 20 },
          { name: '选修', value: 20 },
          { name: '物理', value: 20 },
          { name: '自习', value: 20 },
          { name: '秋游', value: 20 },
          { name: '宝宝', value: 20 },
          { name: '好困哇', value: 16 },
          { name: '上课', value: 16 },
          { name: '嘿嘿嘿', value: 16 },
          { name: '投票', value: 16 },
          { name: '义工', value: 16 },
          { name: '可怕', value: 16 },
          { name: '请吃饭', value: 16 },
          { name: '英语', value: 16 },
          { name: '妹子', value: 16 },
          { name: '加油', value: 12 },
          { name: '羡慕', value: 12 },
          { name: '我去', value: 12 },
          { name: '啧啧啧', value: 12 }
        ],
        option: {
          
        }
      }
    },
    methods: {
      setOptions (id, title, myshape) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          title: {
            text: title,
            textStyle: {
              fontSize: 26,
              fontFamily: 'Helvetica',
              fontWeight: 400
            },
            left: 'center'
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            right: 20
          },
          series: [{
            type: 'wordCloud',
            shape: myshape,
            // shape: 'cardioid',
            // shape: 'pentagon',
            // shape: 'circle',
            left: 'center',
            top: 0,
            width: '75%',
            height: '80%',
            right: null,
            bottom: null,
            sizeRange: [12, 75],
            rotationRange: [-90, 90],
            rotationStep: 45,
            gridSize: 8,
            textStyle: {
              normal: {
                fontFamily: 'Microsoft Yahei',
                fontWeight: 'bold',
                color: function() {
                  return 'rgb(' + [
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160)
                  ].join(',') + ')'
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
              }
            },
            data: this.wordContent
          }]
        })
      }
    },
    mounted() {
      this.setOptions('word_cloud1',this.title, 'cardioid')
      this.setOptions('word_cloud2','', 'pentagon')
    }
  }
</script>
<style>
.main_content {
  position: relative;
  margin-left: 245px;
  margin-top: 100px;
}
#word_cloud1,
#word_cloud2 {
  position: relative;
  left: 50%;
  margin-left: -400px;
  width: 800px;
  height: 600px;
}
@media screen and (max-width: 1060px) {
  #word_cloud1,
  #word_cloud2 {
    position: absolute;
    left: 408px;
  }
  #word_cloud2 {
    top: 610px;
  }
}
</style>

