<template>
  <div>
    <div v-if="isqqRight" id="myactivetime"></div>
    <div v-else="isqqRight" class="prompt">
     用通信1502班同学的qq号登录才能查看本页
    </div>
  </div>
</template>

<script>
  import echarts from 'echarts';
  import qqs from 'static/data/index2QQ_id.json';
  import activeTime from 'static/data/dayVectors.json';

  export default {
    data() {
      return {
        user: {},
        isqqRight: false,
        chart: null,
        times: ['00:00', '00:30', '01:00', '01:30', '02:00','02:30','03:00','03:30','04:00','04:30','05:00','05:30','06:00','06:30','07:00','07:30','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00','23:30']
      };
    },
    computed: {
      user() {
        return this.$store.state.user;
      },
      isqqRight() {
        return this.isqqExist(qqs);
      }
    },
    methods: {
      getId(object) {
        for (var i in object) {
          if(object[i] == this.user.qq) {
            return i;
          } 
        }
        return false;
      },
      isqqExist(object) {
        for (var i in object) {
          if(object[i] == this.user.qq) {
            return true;
          } 
        }
        return false;
      },
      computeMyTotalSpeak(arr, index) {
        var mySpeakData = arr[index];
        var result = new Array(48);
        for (var i = 0; i < 48; i++) {
          result[i] = 0;
          for (var j = 0; j < 5; j++) {
            result[i] += mySpeakData[5*i+j];
          }
        }
        return result;
      },
      drawLine(id) {
        this.chart = echarts.init(document.getElementById(id));
        this.chart.setOption({
          tooltip: {
            trigger: 'axis'
          },
          toolbox: {
            feature: {
              saveAsImage: {},
              dataView: {}
            },
            left: 16,
            top: 8
          },
          xAxis: {
            data: this.times
          },
          yAxis: {
            splitLine: {
                show: false
            }
          },
          dataZoom: [{
            startValue: '00：00'
          }, {
            type: 'inside'
          }],
          visualMap: {
            top: 10,
            right: 10,
            pieces: [{
              gt: 0,
              lte: 10,
              color: '#096'
            }, {
              gt: 10,
              lte: 20,
              color: '#ffde33'
            }, {
              gt: 20,
              lte: 30,
              color: '#ff9933'
            }, {
              gt: 30,
              lte: 40,
              color: '#cc0033'
            }, {
              gt: 40,
              lte: 70,
              color: '#660099'
            }, {
              gt: 70,
              color: '#7e0023'
            }],
            outOfRange: {
              color: '#999'
            }
          },
          series: {
            name: '发言量',
            type: 'line',
            data: this.computeMyTotalSpeak(activeTime, this.getId(qqs)),
            markLine: {
              silent: true,
              data: [{
                yAxis: 10
              }, {
                yAxis: 20
              }, {
                yAxis: 30
              }, {
                yAxis: 40
              }, {
                yAxis: 70
              }]
            }
          }
        });
      }
    },
    mounted() {
      this.$nextTick(function() {
        if(this.isqqRight) {
          this.drawLine('myactivetime');
          var that = this;
          var resizeTimer = null;
          window.onresize = function() {
            if (resizeTimer) clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function() {
              that.drawLine('myactivetime');
            }, 100);
          }
        } 
      });  
    }
  }
</script>

<style scoped>
  #myactivetime {
    position: relative;
    left: 50%;
    width: 90%;
    height: 600px;
    margin-left: -45%;
    box-shadow: 0 0 10px #EDE68A;
    border-radius: 10px;
  } 
  .prompt {
    position: relative;
    left: 50%;
    width: 400px;
    height: 40px;
    margin-left: -200px;
    box-shadow: 0 0 6px #BF382A;
    border-radius: 8px;
    line-height: 40px;
    text-align: center;
  }
  @media screen and (max-width: 420px) {
    .prompt {
      width: 310px;
      margin-left: -155px;
      font-size: 15px;
    }
  }
</style>