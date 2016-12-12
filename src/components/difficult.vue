<template>
  <div>
    <div id="difficultpie"></div>
    <div id="difficultbar"></div>
  </div>
</template>

<script>
  import echarts from 'echarts';
  import '../../node_modules/echarts/theme/vintage.js';
  import data from 'static/data/data.json';

  export default {
    data() {
      return {
        chart: null
      };
    },
    methods: {
      drawpie(id, radius, centery) {
        this.chart = echarts.init(document.getElementById(id), 'vintage');
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
            top: 15,
            data: data.difficult.course,
          },
          series: [
            {
              name: '人数',
              type: 'pie',
              radius: radius,
              center: ['50%', centery],
              data: data.difficult.courseDiff,
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffset: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        });
      },
      drawbar(id) {
        this.chart = echarts.init(document.getElementById(id));
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
            data: data.difficult.course
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
              data: data.difficult.courseData
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
        });
      }
    },
    mounted() {
      this.$nextTick(function() {
        if (document.body.clientWidth < 420) {
          this.drawpie('difficultpie', '65%', '68%');
        } else {
          this.drawpie('difficultpie', '70%', '60%');
        }
        this.drawbar('difficultbar');
        
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          // console.log(window.screen.availWidth, document.body.clientWidth)
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            if (document.body.clientWidth < 420) {
              that.drawpie('difficultpie', '65%', '68%');
            } else {
              that.drawpie('difficultpie', '70%', '60%');
            }
            that.drawbar('difficultbar');
          }, 100);
        }
      });     
    }
  }
</script>

<style scoped>
  #difficultpie,
  #difficultbar {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    border: solid #faf6f3 2px;
    box-shadow: 0 0 10px #F7D098;
    border-radius: 10px;
  }  
  #difficultbar {
    margin-top: 30px;
  }
  @media screen and (max-width: 420px) {
    #difficultpie {
      height: 500px;
    }
  }
</style>