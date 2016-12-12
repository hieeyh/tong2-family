<template>
  <div>
    <div id="selfstudy"></div>
  </div>
</template>

<script>
  import echarts from 'echarts';
  import '../../node_modules/echarts/dist/extension/bmap.min.js';
  import data from 'static/data/data.json';

  export default {
    data() {
      return {
        chart: null
      };
    },
    methods: {
      convertData (oldData) {
        let res = [];
        for (let i = 0; i < oldData.length; i++) {
          let geoCoord = data.selfstudy.geoCoordMap[oldData[i].name];
          if (geoCoord) {
            res.push({
              name: oldData[i].name,
              value: geoCoord.concat(oldData[i].value)
            });
          }
        }
        return res;
      },
      drawMap (id) {
        this.chart = echarts.init(document.getElementById(id));
        this.chart.setOption({
          tooltip: {
            trigger: 'item'
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            right: 15,
            top: 10
          },
          bmap: {
            center: [114.428545, 30.517984],
            zoom: 15,
            roam: true,
            mapStyle: {
                style: 'pink'
            }
          },
          series: [
            {
              name: '自习地点',
              type: 'scatter',
              coordinateSystem: 'bmap',
              data: this.convertData(data.selfstudy.studyContent),
              symbolSize: function (val) {
                return (val[2] + 2) * 2;
              },
              label: {
                normal: {
                  formatter: '{b}',
                  position: 'right',
                  show: true
                },
                emphasis: {
                  show: true
                }
              },
              itemStyle: {
                normal: {
                  color: 'purple'
                }
              }
            },
            {
              name: 'Top 5',
              type: 'effectScatter',
              coordinateSystem: 'bmap',
              data: this.convertData(data.selfstudy.studyContent.sort(function (a, b) {
                return b.value - a.value;
              }).slice(0, 2)),
              symbolSize: function (val) {
                return val[2] * 2;
              },
              showEffectOn: 'render',
              rippleEffect: {
                brushType: 'stroke'
              },
              hoverAnimation: true,
              label: {
                normal: {
                  formatter: '{b}',
                  position: 'right',
                  show: true
                }
              },
              itemStyle: {
                normal: {
                  color: 'purple',
                  shadowBlur: 10,
                  shadowColor: '#333'
                }
              },
              zlevel: 1
            }
          ]
        });
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawMap('selfstudy');
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            that.drawMap('selfstudy');
          }, 100);
        }
      });
    }
  }
</script>

<style scoped>
  #selfstudy {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    box-shadow: 0 0 10px #D15385;
    border-radius: 10px;
  } 
</style>