<template>
  <div>
    <div id="interestpie"></div>
    <div id="interestbar"></div>
  </div>
</template>

<script>
  import echarts from 'echarts';
  import '../../node_modules/echarts/theme/infographic.js';
  import data from 'static/data/data.json';

  export default {
    data() {
      return {
        chart: null
      };
    },
    methods: {
      drawpie(id, small, big, centery) {
        this.chart = echarts.init(document.getElementById(id), 'infographic');
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
              data: data.interest.course,
          },
          calculable: true,
          series: [
            {
              name: '人数',
              type: 'pie',
              radius: [small, big],
              center: ['55%', centery],
              roseType: 'radius',
              data: data.interest.courseInter,
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
      drawbar(id, gap, barwidth) {
        this.chart = echarts.init(document.getElementById(id), 'infographic');
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
            data: data.interest.course,
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
            nameGap: gap,
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
              data: data.interest.courseData,
              barWidth: barwidth,
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
        }); 
      }
    },
    mounted() {
      this.$nextTick(function() {
        if (document.body.clientWidth < 560) {
          this.drawpie('interestpie', 30, 100, '70%');
          this.drawbar('interestbar', 20, 25);
        } else {
          this.drawpie('interestpie', 60, 240, '60%');
          this.drawbar('interestbar', 28, 40);
        }
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            if (document.body.clientWidth < 560) {
              that.drawpie('interestpie', 30, 100, '70%');
              that.drawbar('interestbar', 20, 25);
            } else {
              that.drawpie('interestpie', 60, 240, '60%');
              that.drawbar('interestbar', 28, 40);
            }
          }, 100);
        }
      });
    }
  }
</script>

<style scoped>
  #interestpie,
  #interestbar {
    position: relative;
    left: 50%;
    width: 90%;
    height: 620px;
    margin-left: -45%;
    border: solid #00AD7C 1px;
    box-shadow: 0 0 8px #52D681;
    border-radius: 10px;
  }   
  #interestbar {
    margin-top: 30px;
  }
  @media screen and (max-width: 560px) {
    #interestpie {
      height: 500px;
    }
  }
</style>