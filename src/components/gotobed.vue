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
            left: 'center'
          },
          tooltip: {
            trigger: 'axis'
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {},
              magicType: {
                type: ['line', 'bar']
              }
            }
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
      drawpie() {

      }
    },
    mounted() {
      this.drawbar('gotobedbar')
    }
  }
</script>

<style>
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
}  
#gotobedpie {
  margin-top: 60px;
  margin-bottom: 40px;
} 
@media screen and (max-width: 1060px) {
  #gotobedbar,
  #gotobedpie {
    position: absolute;
    left: 408px;
  }
  #gotobedpie {
    top: 610px;
  }
}
</style>