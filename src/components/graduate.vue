<template>
  <div class="main_content">
    <div id="graduate"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import '../../node_modules/echarts/theme/roma.js'

  export default {
    data() {
      return {
        chart: null,
        opinion: ['国内读研', '工作', '出国深造', '创业'],
        opinionData: [
          {value:58, name:'国内读研', selected: true},
          {value:26, name:'工作'},
          {value:10, name:'出国深造'},
          {value:1, name:'创业'}
        ]
      }
    },
    methods: {
      drawPie (id) {
        this.chart = echarts.init(document.getElementById(id), 'roma')
        this.chart.setOption({
          title: {
            text: '毕业展望调查结果',
            left: 'center',
            top: 10,
            textStyle: {
              fontSize: 24,
              fontFamily: 'Helvetica',
              fontWeight: 400
            }
          },
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            right: 15,
            top: 10
          },
          legend: {
              orient: 'vertical',
              left: 5,
              top: 10,
              data: this.opinion,
          },
          series: [
            {
              name: '人数',
              type: 'pie',
              selectedMode: 'single',
              radius: '70%',
              center: ['50%', '60%'],
              data: this.opinionData,
              itemStyle: {
                normal: {
                  borderWidth: 0.5,
                  borderColor: '#ffffff'
                },
                emphasis: {
                  shadowBlur: 10,
                  shadowOffset: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        })
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawPie('graduate')
      }) 
    }
  }
</script>

<style scoped>
.main_content {
  position: relative;
  margin-left: 245px;
  margin-top: 100px;
}
#graduate {
  position: relative;
  left: 50%;
  margin-left: -400px;
  margin-bottom: 70px;
  width: 800px;
  height: 600px;
  border: solid #E3670C 1px;
  box-shadow: 0 0 8px #FBB448;
  border-radius: 10px;
}   
@media screen and (max-width: 1090px) {
  #graduate {
    position: absolute;
    left: 415px;
  }
}
</style>