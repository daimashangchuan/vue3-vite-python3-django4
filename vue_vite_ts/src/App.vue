<template>
  <div id="app">
    <el-config-provider :locale="AppLocaleStatus === 'zh' ? zhCN : AppLocaleStatus === 'en' ? enGB : jaJP">
      <router-view v-slot="{ Component }">
        <Transition name="fade" mode="out-in">
          <component :is="Component" />
        </Transition>
      </router-view>
    </el-config-provider>
  </div>
</template>

<script lang="ts" setup>
import { Transition } from "vue";
import { useCustomStore } from "./utils/customHook";

import zhCN from "element-plus/lib/locale/lang/zh-cn";
import enGB from "element-plus/lib/locale/lang/en";
import jaJP from "element-plus/lib/locale/lang/ja";

const { AppLocaleStatus } = useCustomStore();

</script>

<style>
@import url("./assets/styles/app.scss");
</style>
