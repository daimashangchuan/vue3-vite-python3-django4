# 搭建 vue + vite + ts 项目


## 项目初始化
```
创建vite项目
npm init vite@latest 项目名
选择 vue
选择 TypeScript
cd vite-project
npm install
打开 package.json文件  dev修改为start
npm start  启动项目
```

## 配置  vue-router

```
npm i vue-router -S
在src目录下新建router文件夹，router下新建index.js和routes.js，向index.js写入下面代码

import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'
const routerHistory = createWebHistory()
const router = createRouter({
   history: routerHistory,
   routes
})
export default router

routes.js 向中写入下面代码：
const routes = [
    // 这是一个例子
    {
      path: '/',
      component: () => import('../views/home.vue'),
      //meta可以不写
      meta: {
          icon: 'Odometer',
          title: '首页'
      }
    }
]
export default routes


最后在main.js中引入：
import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'

const app = createApp(App).use(router)
app.mount('#app')

```