# tong2-family

> 使用vue、vuex、vue-router、echarts搭建的一个班级数据展示平台   
> 不支持IE8及其以下版本，单页面应用

## 运行步骤

``` bash
# 安装依赖
npm install

# 在本地启动服务，并且通过localhost:8080地址进行访问
npm run dev

# 编译并压缩代码便于发布
npm run build

# 运行单元测试
npm run unit
``` 
## 在线访问
[]()

## 源码说明
```
.
|-- config                           // 项目开发环境配置
|   |-- index.js                     // 项目打包部署配置
|-- src                              // 源码目录
|   |-- components                   // 公共组件
|       |-- header.vue               // 页面头部公共组件
|       |-- index.js                 // 加载各种公共组件
|   |-- config                       // 路由配置和程序的基本信息配置
|       |-- routes.js                // 配置页面路由
|   |-- css                          // 各种css文件
|       |-- common.css               // 全局通用css文件
|   |-- iconfont                     // 各种字体图标
|   |-- images                       // 公共图片
|   |-- less                         // 各种less文件
|       |-- common.less              // 全局通用less文件
|   |-- pages                        // 页面组件
|       |-- home                     // 个人中心
|       |-- index                    // 网站首页
|       |-- login                    // 登录
|       |-- signout                  // 退出
|   |-- store                        // vuex的状态管理
|       |-- index.js                 // 加载各种store模块
|       |-- user.js                  // 用户store
|   |-- template                     // 各种html文件
|       |-- index.html               // 程序入口html文件
|   |-- util                         // 公共的js方法，vue的mixin混合
|   |-- app.vue                      // 页面入口文件
|   |-- main.js                      // 程序入口文件，加载各种公共组件
|-- .babelrc                         // ES6语法编译配置
|-- gulpfile.js                      // 启动，打包，部署，自动化构建
|-- webpack.config.js                // 程序打包配置
|-- server.js                        // 代理服务器配置
|-- README.md                        // 项目说明
|-- package.json                     // 配置项目相关信息，通过执行 npm init 命令创建
.
```

## 教程
我的博客：[]()

**IM_analyze**文件夹中是python写的分析群聊数据的相关代码
