<template>
  <div class="main_content">
    <div id="amuse"></div>
  </div>
</template>

<script>
  import echarts from 'echarts'

  export default {
    data() {
      return {
        chart: null,
        amuse: ['打游戏', '刷微博朋友圈', '看剧', '运动', '听歌', '看小说'],
        amuseData: [
          {value:26, name:'打游戏'},
          {value:16, name:'刷微博朋友圈'},
          {value:12, name:'看剧'},
          {value:10, name:'运动'},
          {value:2, name:'听歌'},
          {value:2, name:'看小说'}
        ],
        placeHolderStyle: {
          normal : {
            color: 'rgba(0,0,0,0)',
            label: {show:false},
            labelLine: {show:false}
          },
          emphasis : {
            color: 'rgba(0,0,0,0)'
          }
        },
        color: ['#a2b4ba', '#85b6b2', '#6d4f8d', '#cd5e7e', '#e38980', '#f7db88']
      }
    },
    methods: {
      drawPie (id) {
        this.chart = echarts.init(document.getElementById(id))
        this.chart.setOption({
          title: {
            text: '周末休闲娱乐方式调查',
            left: 'center',
            top: 10,
            textStyle: {
              fontSize: 24,
              fontFamily: 'Helvetica',
              fontWeight: 400
            }
          },
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
              data: this.amuse,
          },
          series: [
            {
              name: '打游戏',
              type: 'pie',
              clockWise:false,
              radius: [220, 240],
              itemStyle: {
                normal: {
                  color: this.color[0],
                  label: {show:false},
                  labelLine: {show:false},
                  shadowBlur: 40,
                  shadowColor: 'rgba(40, 40, 40, 0.5)',
                }
              },
              hoverAnimation: false,
              data: [
                this.amuseData[0],
                {
                  value: 4,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: '刷微博朋友圈',
              type: 'pie',
              clockWise:false,
              radius: [200, 220],
              itemStyle: {
                normal: {
                  color: this.color[1],
                  label: {show:false},
                  labelLine: {show:false},
                  shadowBlur: 40,
                  shadowColor: 'rgba(40, 40, 40, 0.5)',
                }
              },
              hoverAnimation: false,
              data: [
                this.amuseData[0],
                {
                  value: 14,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: '看剧',
              type: 'pie',
              clockWise: false,
              radius: [180, 200],
              itemStyle: {
                normal: {
                  color: this.color[2],
                  label: {show:false},
                  labelLine: {show:false},
                  shadowBlur: 40,
                  shadowColor: 'rgba(40, 40, 40, 0.5)',
                }
              },
              hoverAnimation: false,
              data: [
                this.amuseData[0],
                {
                  value: 18,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: '运动',
              type: 'pie',
              clockWise:false,
              radius: [160, 180],
              itemStyle: {
                normal: {
                  color: this.color[3],
                  label: {show:false},
                  labelLine: {show:false},
                  shadowBlur: 40,
                  shadowColor: 'rgba(40, 40, 40, 0.5)',
                }
              },
              hoverAnimation: false,
              data: [
                this.amuseData[0],
                {
                  value: 20,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: '听歌',
              type: 'pie',
              clockWise:false,
              radius: [140, 160],
              itemStyle: {
                normal: {
                  color: this.color[4],
                  label: {show:false},
                  labelLine: {show:false},
                  shadowBlur: 40,
                  shadowColor: 'rgba(40, 40, 40, 0.5)',
                }
              },
              hoverAnimation: false,
              data: [
                this.amuseData[0],
                {
                  value: 28,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: '看小说',
              type: 'pie',
              clockWise:false,
              radius: [120, 140],
              itemStyle: {
                normal: {
                  color: this.color[5],
                  label: {show:false},
                  labelLine: {show:false},
                  shadowBlur: 40,
                  shadowColor: 'rgba(40, 40, 40, 0.5)',
                }
              },
              hoverAnimation: false,
              data: [
                this.amuseData[0],
                {
                  value: 28,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            }
          ]
        })
      }
    },
    mounted() {
      this.$nextTick(function() {
        this.drawPie('amuse')
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
#amuse {
  position: relative;
  left: 50%;
  margin-left: -400px;
  margin-bottom: 70px;
  width: 800px;
  height: 660px;
  box-shadow: 0 0 10px #a2b4ba;
  border-radius: 10px;
}   
@media screen and (max-width: 1090px) {
  #amuse {
    position: absolute;
    left: 415px;
  }
}
</style>