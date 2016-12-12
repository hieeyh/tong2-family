<template>
  <div>
    <div id="word_cloud1"></div>
    <div id="word_cloud2"></div>
  </div>
</template>

<script>
  import echarts from 'echarts';
  import 'echarts-wordcloud';
  import data from 'static/data/data.json';
  
  export default {
    data () {
      return {
        chart: null
      };
    },
    methods: {
      drawCloud (id, myshape) {
        this.chart = echarts.init(document.getElementById(id));
        this.chart.setOption({
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            right: 20,
            top: 20
          },
          series: [{
            type: 'wordCloud',
            shape: myshape,
            // shape: 'cardioid',
            // shape: 'pentagon',
            // shape: 'circle',
            left: 'center',
            top: 30,
            width: '75%',
            height: '80%',
            right: null,
            bottom: null,
            sizeRange: [12, 75],
            rotationRange: [-90, 90],
            rotationStep: 45,
            gridSize: 8,
            textStyle: {
              normal: {
                fontFamily: 'Microsoft Yahei',
                fontWeight: 'bold',
                color: function() {
                  return 'rgb(' + [
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160),
                    Math.round(Math.random() * 160)
                  ].join(',') + ')'
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
              }
            },
            data: data.cloud.wordContent
          }]
        });
      }
    },
    mounted() {
      // 保证this.$el已经插入文档
      this.$nextTick(function() {
        this.drawCloud('word_cloud1', 'cardioid');
        this.drawCloud('word_cloud2', 'pentagon');
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            that.drawCloud('word_cloud1', 'cardioid');
            that.drawCloud('word_cloud2', 'pentagon');
          }, 100);
        }
      })
    }
  }
</script>
<style scoped>
  #word_cloud1,
  #word_cloud2 {
    position: relative;
    left: 50%;
    width: 90%;
    height: 560px;
    margin-left: -45%;
    border: solid #9E579D 1px;
    box-shadow: 0 0 8px #FC85AE;
    border-radius: 10px;
  }
  #word_cloud2 {
    margin-top: 15px;
    height: 480px;
  }
</style>

