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
    methods: {
      drawPie (id) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          title: {
            text: '是否单身调查结果',
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
            formatte: "{b}: {c} ({d}%)"
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
              data: this.course,
          },
          series: [
            {
              name: '是否单身',
              type: 'pie',
              radius: [60, 220],
              center: ['50%', '55%'],
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
    },
    mounted() {
      this.$nextTick(function() {
        this.drawPie('single')
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
#single {
  position: relative;
  left: 50%;
  margin-left: -400px;
  margin-bottom: 70px;
  width: 800px;
  height: 600px;
  box-shadow: 0 0 10px #2A769A;
  border-radius: 10px;
}   
@media screen and (max-width: 1090px) {
  #single {
    position: absolute;
    left: 415px;
  }
}
</style>