<template>
  <div class="main_content">
    <div id="interestpie"></div>
    <div id="interestbar"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import '../../node_modules/echarts/theme/infographic.js'

  export default {
    data() {
      return {
        chart: null,
        course: ['数电', '模电', '全没兴趣', '体育', '人文选修', '复变', '数据结构', '大物', '电路实验'],
        courseInter: [
          {value:18, name:'数电'},
          {value:17, name:'模电'},
          {value:10, name:'全没兴趣'},
          {value:6, name:'体育'},
          {value:4, name:'人文选修'},
          {value:4, name:'复变'},
          {value:3, name:'数据结构'},
          {value:3, name:'大物'},
          {value:2, name:'电路实验'}
        ],
        courseData: [18, 17, 10, 6, 4, 4, 3, 3, 2]
      }
    },
    methods: {
      drawpie(id) {
        this.chart = echarts.init(document.getElementById(id), 'infographic')
        this.chart.setOption({
          title: {
            text: '电信大二上学生最感兴趣课程调查结果',
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
              data: this.course,
          },
          calculable: true,
          series: [
            {
              name: '人数',
              type: 'pie',
              radius: [60, 240],
              center: ['50%', '60%'],
              roseType: 'radius',
              data: this.courseInter,
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
        this.chart = echarts.init(document.getElementById(id), 'infographic')
        this.chart.setOption({
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c}"
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            right: 15,
            top: 10
          },
          xAxis: {
            data: this.course,
            axisLabel: {
              textStyle: {
                color: '#dcf7a1',
              }
            },
            splitLine: {
              show: false
            }
          },
          yAxis: {
            name: '人数',
            nameLocation: 'middle',
            nameGap: 28,
            nameTextStyle: {
              fontWeight: 200,
              fontSize: 14
            },
            max: 20,
            axisLine: {
              show: true
            }
          },
          series: [
            {
              name: '人数',
              type: 'bar',
              data: this.courseData,
              barWidth: 40,
              itemStyle: {
                normal: {
                  barBorderRadius: 20,
                  color: '#dcf7a1',
                  shadowColor: 'rgba(0, 0, 0, 0.4)',
                  shadowBlur: 20
                }
              }
            }
          ]
        }) 
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawpie('interestpie')
        this.drawbar('interestbar')
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
#interestpie,
#interestbar {
  position: relative;
  left: 50%;
  margin-left: -400px;
  width: 800px;
  height: 620px;
  border: solid #00AD7C 1px;
  box-shadow: 0 0 8px #52D681;
  border-radius: 10px;
}   
#interestbar {
  margin-top: 30px;
  margin-bottom: 70px;
}
@media screen and (max-width: 1090px) {
  #interestpie,
  #interestbar {
    position: absolute;
    left: 415px;
  }
  #interestbar {
    top: 622px;
  }
}
</style>