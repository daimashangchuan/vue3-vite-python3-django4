import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { pinia } from "./pinia";

// 引入全部的图表
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

// message 提示样式需要单独引入
import "element-plus/theme-chalk/el-message.css";
import "element-plus/theme-chalk/el-message-box.css";

// 重置样式表
import "normalize.css"

const app = createApp(App);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(router);
app.use(pinia);
app.mount('#root');


