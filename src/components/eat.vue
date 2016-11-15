<template>
  <div class="main_content">
    <div id="eat"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    data() {
      return {
        chart: null,
        money: ['10元', '15元', '20元', '25元', '30元', '35元', '40元'],
        number: [2, 11, 30, 30, 16, 2, 4]
      }
    },
    methods: {
      drawBar (id) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          title: {
            text: '每天在校吃饭花销',
            left: 'center',
            top: 10,
            textStyle: {
              fontSize: 24,
              fontFamily: 'Helvetica',
              fontWeight: 400
            }
          },
          tooltip: {
            trigger: 'axis'
          },
          toolbox: {
            feature: {
              magicType:{show: true, type: ['line', 'bar']},
              saveAsImage: {show: true},
              dataView: {show: true, readOnly: false}            
            },
            top: 10,
            right: 15
          },
          calculable: true,
          grid: {
            left: '3%',
            right: '6%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              data: this.money
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: '人数',
              max: 35
            }
          ],
          series: [
            {
              name: '起床时间',
              type: 'bar',
              markPoint: {
                data: [
                  {type: 'max', name: '最大值'},
                  {type: 'min', name: '最小值'}
                ]
              },
              markLine: {
                data: [
                  {type: 'average', name: '平均值'}
                ]
              },
              itemStyle: {
                normal: {
                  barBorderRadius: 20,
                  color: '#726dd1',
                  shadowColor: 'rgba(0, 0, 0, 0.4)',
                  shadowBlur: 20
                }
              },
              data: this.number
            }
          ]
        })
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawBar('eat')
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
#eat {
  position: relative;
  left: 50%;
  margin-left: -400px;
  margin-bottom: 70px;
  width: 800px;
  height: 600px;
  box-shadow: 0 0 10px #726dd1;
  border-radius: 10px;
}   
@media screen and (max-width: 1090px) {
  #eat {
    position: absolute;
    left: 415px;
  }
}
</style>