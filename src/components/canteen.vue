<template>
  <div>
    <div id="canteen"></div>
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
          let geoCoord = data.canteen.geoCoordMap[oldData[i].name];
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
            center: [114.427461, 30.51729],
            zoom: 15,
            roam: true,
            mapStyle: {
                style: 'normal'
            }
          },
          series: [
            {
              name: '最喜爱食堂',
              type: 'scatter',
              coordinateSystem: 'bmap',
              data: this.convertData(data.canteen.canteenContent),
              symbolSize: function (val) {
                return (val[2] + 3) * 2;
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
              name: 'Top 3',
              type: 'effectScatter',
              coordinateSystem: 'bmap',
              data: this.convertData(data.canteen.canteenContent.sort(function (a, b) {
                return b.value - a.value;
              }).slice(0, 4)),
              symbolSize: function (val) {
                return (val[2] + 3) * 2;
              },
              showEffectOn: 'render',
              rippleEffect: {
                scale: 2,
                brushType: 'fill'
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
        this.drawMap('canteen');
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            that.drawMap('canteen');
          }, 100);
        }
      });
    }
  }
</script>

<style scoped>
  #canteen {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    box-shadow: 0 0 8px #FBD157;
    border-radius: 10px;
  } 
</style>