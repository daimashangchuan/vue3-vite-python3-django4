<template>
  <AppTabs
    type="card"
    :model="tabModel"
    :data="AppTabList"
    :closable="AppTabList.length > 1 ? true : false"
    @onTabClick="onTabClick"
    @onTabRemove="onTabRemove"
  />
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { useRouter, onBeforeRouteUpdate } from "vue-router";
import AppTabs from "../../../components/AppTabs/index.vue";
import { useCustomStore } from "../../../utils/customHook"

const router = useRouter();
const route = router.currentRoute.value;
// 切换tab的value
const tabModel = ref(route.fullPath);

// 解构 useCustomStore 返回的对象，显式指定属性类型
const store: any = useCustomStore();
const { AppTabList, setAppTabList } = store;

// 设置 tab 需要的参数
const initTab = (data: any) => ({
  label: data.meta.title,
  name: data.fullPath,
  key: data.path,
});

// 初始化
const init = () => {
  setAppTabList(initTab(route));
};
init();

// 切换路路由
onBeforeRouteUpdate((to) => {
  setAppTabList(initTab(to));
  tabModel.value = to.fullPath;
});

// tab切换
const onTabClick = (val: any) => {
  const url = val.props.name;
  router.push(url);
};
// tab删除
const onTabRemove = (val: any) => {
  if (tabModel.value === val && AppTabList.value[0]) {
    const url = AppTabList.value[0]?.name;
    router.push(url || "/");
  }
  setAppTabList(val);
};
</script>

<style lang="scss" scoped></style>
