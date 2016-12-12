<template>
  <div>
    <div id="graduate"></div>
  </div>
</template>

<script>
  import echarts from 'echarts';
  import '../../node_modules/echarts/theme/roma.js';
  import data from 'static/data/data.json';

  export default {
    data() {
      return {
        chart: null
      };
    },
    methods: {
      drawPie (id) {
        this.chart = echarts.init(document.getElementById(id), 'roma');
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
              data: data.graduate.opinion,
          },
          series: [
            {
              name: '人数',
              type: 'pie',
              selectedMode: 'single',
              radius: '70%',
              center: ['50%', '60%'],
              data: data.graduate.opinionData,
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
        });
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawPie('graduate');
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            that.drawPie('graduate');
          }, 100);
        }
      });
    }
  }
</script>

<style scoped>
  #graduate {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    border: solid #E3670C 1px;
    box-shadow: 0 0 8px #FBB448;
    border-radius: 10px;
  }   
  @media screen and (max-width: 470px) {
    #graduate {
      height: 500px;
    }
  }
</style>