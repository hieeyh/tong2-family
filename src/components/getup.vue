<template>
  <div>
    <div id="getupbar"></div>
    <div id="getuppie"></div>
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
      drawbar(id) {
        this.chart = echarts.init(document.getElementById(id), 'vintage');
        this.chart.setOption({
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
              data: data.getup.time
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
              data: data.getup.number
            }
          ]
        });
      },
      drawpie(id, centery) {
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
            top: 10,
            data: data.getup.time,
          },
          series: [
            {
              name: '人数',
              type: 'pie',
              radius: '70%',
              center: ['50%', centery],
              data: data.getup.numberData,
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
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawbar('getupbar');
        if (document.body.clientWidth < 470) {
          this.drawpie('getuppie', '70%');
        } else {
          this.drawpie('getuppie', '60%');
        }
        
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            that.drawbar('getupbar');
            if (document.body.clientWidth < 470) {
              that.drawpie('getuppie', '70%');
            } else {
              that.drawpie('getuppie', '60%');
            }
          }, 100);
        }
      });
    }
  }
</script>

<style scoped>
  #getupbar,
  #getuppie {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    box-shadow: 0 0 10px #BF382A;
    border-radius: 10px;
  }  
  #getuppie {
    margin-top: 30px;
  }
  @media screen and (max-width: 470px) {
    #getuppie {
      height: 500px;
    }
  }
</style>