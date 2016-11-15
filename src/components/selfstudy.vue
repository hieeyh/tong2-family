<template>
  <div class="main_content">
    <div id="selfstudy"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import '../../node_modules/echarts/dist/extension/bmap.min.js'

  export default {
    data() {
      return {
        chart: null,
        studyContent: [
          {name: '西五', value: 3},
          {name: '图书馆', value: 14},
          {name: '东十二', value: 35},
          {name: '东九', value: 43}
        ],
        geoCoordMap: {
          '西五':[114.416517,30.51651],
          '图书馆':[114.418508,30.518443],
          '东十二':[114.440574,30.517961],
          '东九':[114.433451,30.519458]  
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
            text: '学生最常自习地点分布',
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
              data: this.convertData(this.studyContent),
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
              data: this.convertData(this.studyContent.sort(function (a, b) {
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
        })
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawMap('selfstudy')
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
#selfstudy {
  position: relative;
  left: 50%;
  margin-left: -400px;
  margin-bottom: 70px;
  width: 800px;
  height: 600px;
  box-shadow: 0 0 10px #D15385;
  border-radius: 10px;
} 
@media screen and (max-width: 1090px) {
  #selfstudy {
    position: absolute;
    left: 415px;
  }
}  
</style>