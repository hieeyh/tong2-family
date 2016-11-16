import Vue from 'vue'
import Vuex from 'vuex'
import Header from 'src/components/header'

describe('header.vue test', () => {
  // 检查原始组件选项
  it('has data as function', () => {
    expect(Header.data).to.be.a('function')
  })
  it('has computed as object', () => {
    expect(Header.computed).to.be.an('object')
  })
  it('has methods as object', () => {
    expect(Header.methods).to.be.an('object')
  })
})