<template>
  <div class="main_content">
    <div id="single"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    data() {
      return {
        chart: null,
        course: ['是', '否'],
        courseDiff: [
          {value:72, name:'是'},
          {value:23, name:'否'}
        ]
      }
    },
    mounted() {
      this.chart = echarts.init(document.getElementById('single'))
      this.chart.setOption({
        title: {
          text: '是否单身调查结果',
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
          }
        },
        legend: {
            orient: 'vertical',
            left: 'left',
            data: this.course,
        },
        series: [
          {
            name: '是否单身',
            type: 'pie',
            radius: [60, 240],
            center: ['50%', '60%'],
            roseType: 'radius',
            data: this.courseDiff,
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
#single {
  position: relative;
  left: 50%;
  margin-left: -400px;
  width: 800px;
  height: 600px;
}   
@media screen and (max-width: 1060px) {
  #single {
    position: absolute;
    left: 408px;
  }
}
</style>