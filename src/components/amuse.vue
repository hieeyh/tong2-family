<template>
  <div>
    <div id="amuse"></div>
  </div>
</template>

<script>
  import echarts from 'echarts';
  import data from 'static/data/data.json';

  export default {
    data() {
      return {
        chart: null,
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
      };
    },
    methods: {
      drawPie (id, radius0, radius1, radius2, radius3, radius4, radius5, radius6, centery) {
        this.chart = echarts.init(document.getElementById(id));
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
              data: data.amuse.amuse,
          },
          series: [
            {
              name: data.amuse.amuseData[0].name,
              type: 'pie',
              clockWise:false,
              radius: [radius1, radius0],
              center: ['50%', centery],
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
                data.amuse.amuseData[0],
                {
                  value: 4,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: data.amuse.amuseData[1].name,
              type: 'pie',
              clockWise:false,
              radius: [radius2, radius1],
              center: ['50%', centery],
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
                data.amuse.amuseData[1],
                {
                  value: 14,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: data.amuse.amuseData[2].name,
              type: 'pie',
              clockWise: false,
              radius: [radius3, radius2],
              center: ['50%', centery],
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
                data.amuse.amuseData[2],
                {
                  value: 18,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: data.amuse.amuseData[3].name,
              type: 'pie',
              clockWise:false,
              radius: [radius4, radius3],
              center: ['50%', centery],
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
                data.amuse.amuseData[3],
                {
                  value: 20,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: data.amuse.amuseData[4].name,
              type: 'pie',
              clockWise:false,
              radius: [radius5, radius4],
              center: ['50%', centery],
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
                data.amuse.amuseData[4],
                {
                  value: 28,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            },
            {
              name: data.amuse.amuseData[5].name,
              type: 'pie',
              clockWise:false,
              radius: [radius6, radius5],
              center: ['50%', centery],
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
                data.amuse.amuseData[5],
                {
                  value: 28,
                  name: 'invisible',
                  itemStyle: this.placeHolderStyle
                }
              ]
            }
          ]
        });
      }
    },
    mounted() {
      this.$nextTick(function() {
        if (document.body.clientWidth < 530) {
          this.drawPie('amuse', 140, 120, 100, 80, 60, 40, 20, '60%');
        } else {
          this.drawPie('amuse', 240, 220, 200, 180, 160, 140, 120, '55%');
        }
        
        var that = this;
        var resizeTimer = null;
        window.onresize = function() {
          if (resizeTimer) clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            if (document.body.clientWidth < 530) {
              that.drawPie('amuse', 140, 120, 100, 80, 60, 40, 20, '60%');
            } else {
              that.drawPie('amuse', 240, 220, 200, 180, 160, 140, 120, '55%');
            }
          }, 100);
        }
      });
    }
  }
</script>

<style scoped>
  #amuse {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    box-shadow: 0 0 10px #a2b4ba;
    border-radius: 10px;
  }   
  @media screen and (max-width: 530px) {
    #amuse {
      height: 500px;
    }
  }
</style>