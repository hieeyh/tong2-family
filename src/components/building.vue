<template>
  <div class="main_content">
    <div id="building"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'
  import '../../node_modules/echarts/dist/extension/bmap.min.js'

  export default {
    data() {
      return {
        chart: null,
        buildContent: [
          {name: '爱因斯坦广场', value: 1},
          {name: '校史馆', value: 1},
          {name: '亮胜楼', value: 1},
          {name: '醉晚亭', value: 1},
          {name: '光谷体育馆', value: 2},
          {name: '机械大楼', value: 2},
          {name: '东园', value: 2},
          {name: '青年园', value: 2},
          {name: '管理学院', value: 2},
          {name: '大学四年顶个球', value: 3},
          {name: '西十二教学楼', value: 3},
          {name: '毛爷爷像', value: 3},
          {name: '东九教学楼', value: 8},
          {name: '图书馆', value: 9}
        ],
        geoCoordMap: {
          '爱因斯坦广场':[114.442057,30.519878],
          '校史馆':[114.420044,30.517681],
          '亮胜楼':[114.43721,30.515064],
          '醉晚亭':[114.422819,30.516359],
          '光谷体育馆':[114.4248,30.513827],
          '机械大楼':[114.424104,30.518836],
          '东园':[114.442479,30.519365],
          '青年园':[114.415718,30.518307],
          '管理学院':[114.422712,30.520671],
          '大学四年顶个球':[114.416015,30.519217],
          '西十二教学楼':[114.413697,30.514749],
          '毛爷爷像':[114.420017,30.514725],
          '东九教学楼':[114.433451,30.519458],
          '图书馆':[114.418508,30.518443],  		
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
            text: '学生最喜爱学校建筑分布',
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
            // 百度地图中心经纬度
            center: [114.427877, 30.517249],
            // 地图缩放
            zoom: 15,
            roam: true,
            mapStyle: {
                style: 'light'
            }
          },
          series: [
            {
              name: '最喜爱建筑',
              type: 'scatter',
              coordinateSystem: 'bmap',
              data: this.convertData(this.buildContent),
              symbolSize: function (val) {
                return (val[2] + 2) * 3;
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
                  color: 'rgba(11, 110, 72, 1)'
                }
              }
            },
            {
              name: 'Top 5',
              type: 'effectScatter',
              coordinateSystem: 'bmap',
              data: this.convertData(this.buildContent.sort(function (a, b) {
                return b.value - a.value;
              }).slice(0, 6)),
              symbolSize: function (val) {
                return (val[2] + 2) * 3;
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
        this.drawMap('building')
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
#building {
  position: relative;
  left: 50%;
  margin-left: -400px;
  margin-bottom: 70px;
  width: 800px;
  height: 600px;
  box-shadow: 0 0 10px #A6E3E9;
  border-radius: 10px;
}	
@media screen and (max-width: 1090px) {
  #building {
    position: absolute;
    left: 415px;
  }
}
</style>