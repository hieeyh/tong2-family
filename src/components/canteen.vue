<template>
  <div class="main_content">
      <div id="canteen"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import '../../node_modules/echarts/dist/extension/bmap.min.js'

  export default {
    data() {
      return {
        chart: null,
        canteenContent: [
          {name: '喻园', value: 1},
          {name: '西边小吃城', value: 1},
          {name: '百景园', value: 2},
          {name: '东教工', value: 3},
          {name: '韵苑', value: 7},
          {name: '学一', value: 7},
          {name: '学二', value: 7},
          {name: '东一', value: 8},
          {name: '西一', value: 10},
          {name: '东园', value: 22}
        ],
        geoCoordMap: {
          '喻园':[114.421391,30.521893],
          '西边小吃城':[114.413288,30.520419],
          '百景园':[114.414703,30.521854],
          '东教工':[114.438279,30.512687],
          '韵苑':[114.43845,30.520026],
          '学一':[114.438459,30.517035],
          '学二':[114.438203,30.517693],
          '东一':[114.425905,30.516678],
          '西一':[114.412439,30.520045],
          '东园':[114.442483,30.519353]
        }
      }
    },
    methods: {
      convertData (data) {
        let res = []
        for (let i = 0; i < data.length; i++) {
          let geoCoord = this.geoCoordMap[data[i].name]
          if (geoCoord) {
            res.push({
              name: data[i].name,
              value: geoCoord.concat(data[i].value)
            });
          }
        }
          return res
      },
      drawMap (id) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          title: {
            text: '学生最喜爱学生食堂分布',
            left: 'center',
            top: 15,
            textStyle: {
              fontSize: 24,
              fontFamily: 'Helvetica',
              fontWeight: 400
            }
          },
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
              data: this.convertData(this.canteenContent),
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
              data: this.convertData(this.canteenContent.sort(function (a, b) {
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
        })
      }        
    },
    mounted() {
      this.$nextTick(function() {
        this.drawMap('canteen')
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
#canteen {
  position: relative;
  left: 50%;
  margin-left: -400px;
  margin-bottom: 70px;
  width: 800px;
  height: 600px;
  box-shadow: 0 0 8px #FBD157;
  border-radius: 10px;
} 
@media screen and (max-width: 1090px) {
  #canteen {
    position: absolute;
    left: 415px;
  }
}      
</style>