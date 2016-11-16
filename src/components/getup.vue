<template>
  <div class="main_content">
    <div id="getupbar"></div>
    <div id="getuppie"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import '../../node_modules/echarts/theme/vintage.js'

  export default {
    data() {
      return {
        chart: null,
        time: ['6点', '6点半', '7点', '7点15', '7点半', '8点', '8点半及以后'],
        number: [2, 5, 18, 11, 17, 1, 3],
        numberData: [
          {value:2, name:'6点'},
          {value:5, name:'6点半'},
          {value:18, name:'7点'},
          {value:11, name:'7点15'},
          {value:17, name:'7点半'},
          {value:1, name:'8点'},
          {value:3, name:'8点半及以后'}
        ],
      }
    },
    methods: {
      drawbar(id) {
        this.chart = echarts.init(document.getElementById(id), 'vintage')
        this.chart.setOption({
          title: {
            text: '工作日起床时间调查结果',
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
              magicType: {
                type: ['line', 'bar']
              },
              saveAsImage: {},
              dataView: {}             
            },
            right: 15,
            top: 10
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              boundrayGap: false,
              data: this.time
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: '人数',
              max: 20
            }
          ],
          series: [
            {
              name: '起床时间',
              type: 'bar',
              label: {
                normal: {
                  show: true,
                  position: 'top'
                }
              },
              markPoint: {
                data: [
                  {type: 'max', name: '最大值'},
                  {type: 'min', name: '最小值'}
                ]
              },
              data: this.number
            }
          ]
        })
      },
      drawpie(id) {
        this.chart = echarts.init(document.getElementById(id), 'vintage')
        this.chart.setOption({
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
            data: this.time,
          },
          series: [
            {
              name: '人数',
              type: 'pie',
              radius: '70%',
              center: ['50%', '60%'],
              data: this.numberData,
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
        this.drawbar('getupbar')
        this.drawpie('getuppie')
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
#getupbar,
#getuppie {
  position: relative;
  left: 50%;
  margin-left: -400px;
  width: 800px;
  height: 600px;
  box-shadow: 0 0 10px #BF382A;
  border-radius: 10px;
}  
#getuppie {
  margin-top: 60px;
  margin-bottom: 70px;
}
@media screen and (max-width: 1090px) {
  #getupbar,
  #getuppie {
    position: absolute;
    left: 415px;
  }
  #getuppie {
    top: 600px;
  }
}
</style>