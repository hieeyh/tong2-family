<template>
  <div class="main_content">
    <div id="bedroom"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    data() {
      return {
        chart: null,
        opinion: ['学习氛围差', '学习氛围一般', '学习氛围很好'],
        opinionData: [
          {value:26, name:'学习氛围差'},
          {value:31, name:'学习氛围一般'},
          {value:8, name:'学习氛围很好'}
        ]
      }
    },
    mounted() {
      this.chart = echarts.init(document.getElementById('bedroom'))
      this.chart.setOption({
        title: {
          text: '寝室学习氛围情况调查',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatte: "{b}: {c} ({d}%)"
        },
        toolbox: {
          feature: {
            saveAsImage: {},
            dataView: {}
          },
          right: 15
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: this.opinion,
        },
        series: [
          {
            name: '寝室学习氛围',
            type: 'pie',
            radius: ['50%', '70%'],
            center: ['50%', '60%'],
            avoidLabelOverlap: false,
            label: {
              emphasis: {
                show: true,
                textStyle: {
                  fontSize: '24',
                  fontWeight: 'bold'
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data: this.opinionData,
            itemStyle: {
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
  }
</script>

<style>
.main_content {
  position: relative;
  margin-left: 245px;
  margin-top: 100px;
}
#bedroom {
  position: relative;
  left: 50%;
  margin-left: -400px;
  width: 800px;
  height: 600px;
}   
@media screen and (max-width: 1060px) {
  #bedroom {
    position: absolute;
    left: 408px;
  }
}
</style>