<template>
  <div id="app-layout">
    <el-container>
      <!-- 公共头 -->
      <el-header id="app-header">
        <AppHeader />
      </el-header>

      <el-container :style="{ height: windowHeight + 'px' }">
        <!-- 公共侧边栏 -->
        <el-aside id="app-aside" width="200px">
          <AppAside />
        </el-aside>

        <!-- 公共内容 -->
        <el-main id="app-main">
          
          <!-- 标题 -->
          <h4>{{ title }}</h4>
          <el-divider></el-divider>

          <!-- tab切换 -->
          <AppLayoutTabs />

          <!-- 主体内容 -->
          <div id="app-content">
            <keep-alive>
              <router-view v-if="$route.meta.keepAlive" />
            </keep-alive>
            <router-view v-if="!$route.meta.keepAlive" />
          </div>

        </el-main>

      </el-container>
      
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { ref, toRef } from "vue";
import { useRouter, onBeforeRouteUpdate } from "vue-router";
import AppHeader from "../../components/AppHeader/index.vue";
import AppAside from "../../components/AppAside/index.vue";
import AppLayoutTabs from "../components/AppLayoutTabs/index.vue";

const windowHeight = ref(window.innerHeight - 80);

const route = useRouter().currentRoute.value;
const title = toRef(route.meta.title);

onBeforeRouteUpdate((to) => {
  title.value = to.meta.title;
});
</script>

<style lang="scss" scoped>
#app-layout {
  background: $bgfff;

  #app-header {
    width: 100vw;
    height: 80px;
    background-color: $bginit;
  }

  #app-aside,
  #app-main {
    background: $bgfff;
    overflow-y: scroll;
    position: relative;
    border-right: 2px solid $bordc7c;
    padding-top: 0;
  }

  #app-content {
    padding: 20px;
  }
}
</style>
