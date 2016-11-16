<template>
  <div class="main_content">
    <div id="difficultpie"></div>
    <div id="difficultbar"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import '../../node_modules/echarts/theme/vintage.js'
  export default {
    data() {
      return {
        chart: null,
        course: ['模电', '都很难', '全不难', '数电', '复变', '电路实验', '大物'],
        courseDiff: [
          {value:13, name:'模电'},
          {value:5, name:'都很难'},
          {value:5, name:'全不难'},
          {value:3, name:'数电'},
          {value:2, name:'复变'},
          {value:2, name:'电路实验'},
          {value:1, name:'大物'}
        ],
        courseBar: [13, 5, 5, 3, 2, 2, 1]
      }
    },
    methods: {
      drawpie(id) {
        this.chart = echarts.init(document.getElementById(id), 'vintage')
        this.chart.setOption({
          title: {
            text: '电信大二上课程难度调查结果',
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
            top: 15,
            data: this.course,
          },
          series: [
            {
              name: '人数',
              type: 'pie',
              radius: '70%',
              center: ['50%', '60%'],
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
      },
      drawbar(id) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          backgroundColor: '#faf6f3',
          tooltip: {
            trigger: 'axis',
            formatter: "{a} <br/>{b} : {c}",
            axisPointer: {
              type: 'shadow'
            }
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            right: 15,
            top: 10
          },
          grid: {
            top: 65,
            bottom: 30
          },
          xAxis: {
            type: 'value',
            name: '人数',
            nameLocation: 'middle',
            nameGap: 28,
            nameTextStyle: {
              color: '#682d19',
              fontWeight: 200,
              fontSize: 16
            },
            position: 'top',
            splitLine: {
              lineStyle: {
                type: 'solid',
                color: '#cfc3bd'
              }
            }
          },
          yAxis: {
            type: 'category',
            axisLabel: {
              show: true,
              rotate: 0,
              textStyle: {
                color: '#682d19'
              }
            },
            splitLine: {
              lineStyle: {
                type: 'solid',
                color: '#cfc3bd'
              }
            },
            data: this.course
          },
          series: [
            {
              name: '人数',
              type: 'bar',
              stack: '课程',
              label: {
                normal: {
                  show: true,
                  position: 'top'
                }
              },
              barCategoryGap: 0,
              itemStyle: {
                normal: {
                  color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                    offset: 0,
                    color: 'transparent'
                  }, {
                    offset: 0.5,
                     color: 'transparent'
                  }, {
                    offset: 0.8,
                    color: 'rgba(0, 0, 0, 0.05)'
                  }, {
                    offset: 0.92,
                    color: 'rgba(0, 0, 0, 0.08)'
                  }, {
                    offset: 1,
                    color: 'rgba(0, 0, 0, 0.2)'
                  }])
                }
              },
              data: this.courseBar
            },
            {
              type: 'bar',
              stack: '课程',
              silent: true,
              data: [0, 0, 0, 0, 0, 0, 0],
              itemStyle: {
                normal: {
                  color: '#ff5a00',
                  shadowColor: 'rgba(0, 0, 0, 0.3)',
                  shadowBlur: 10,
                  shadowOffsetX: -4
                }
              },
              barMinHeight: 4
            }
          ]
        })
      }
    },
    mounted() {
      this.$nextTick(function() {
        // console.log(this.$route)
        this.drawpie('difficultpie')
        this.drawbar('difficultbar')
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
#difficultpie,
#difficultbar {
  position: relative;
  left: 50%;
  margin-left: -400px;
  width: 800px;
  height: 600px;
  border: solid #faf6f3 2px;
  box-shadow: 0 0 10px #F7D098;
  border-radius: 10px;
}  
#difficultbar {
  margin-top: 40px;
  margin-bottom: 80px;
}
@media screen and (max-width: 1090px) {
  #difficultpie,
  #difficultbar {
    position: absolute;
    left: 415px;
  }
  #difficultbar {
    top: 604px;
  }
}
</style>