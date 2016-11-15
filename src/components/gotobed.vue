<template>
  <div class="main_content">
    <div id="gotobedbar"></div>
    <div id="gotobedpie"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    data() {
      return {
        chart: null,
        time: ['11点', '11点半', '12点', '12点半', '1点及以后'],
        number: [4, 9, 32, 14, 4],
        numberData: [
          {value:4, name:'11点'},
          {value:9, name:'11点半'},
          {value:32, name:'12点'},
          {value:14, name:'12点半'},
          {value:4, name:'1点及以后'}
        ]
      }
    },
    methods: {
      drawbar(id) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          title: {
            text: '工作日睡觉时间调查结果',
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
              max: 35
            }
          ],
          series: [
            {
              name: '睡觉时间',
              type: 'bar',
              stack: '总量',
              label: {
                normal: {
                  show: true,
                  position: 'top'
                }
              },
              itemStyle: {
                normal: {
                  barBorderRadius: 20,
                  color: 'purple',
                  shadowColor: 'rgba(0, 0, 0, 0.4)',
                  shadowBlur: 20
                }
              },
              areaStyle: {normal: {}},
              data: this.number
            }
          ]
        })
      },
      drawpie(id) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
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
              selectedMode: 'single',
              radius: '70%',
              center: ['50%', '60%'],
              data: this.numberData,
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
        this.drawbar('gotobedbar')
        this.drawpie('gotobedpie')
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
#gotobedbar,
#gotobedpie {
  position: relative;
  left: 50%;
  margin-left: -400px;
  width: 800px;
  height: 600px;
  box-shadow: 0 0 10px #884EA2;
  border-radius: 10px;
}  
#gotobedpie {
  margin-top: 60px;
  margin-bottom: 70px;
} 
@media screen and (max-width: 1090px) {
  #gotobedbar,
  #gotobedpie {
    position: absolute;
    left: 415px;
  }
  #gotobedpie {
    top: 600px;
  }
}
</style>