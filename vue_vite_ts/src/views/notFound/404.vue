<template>
  <div class="error-container flex-content-content">
    <el-button type="primary" @click="goBack">返回上一页</el-button>
    <!-- <el-button type="primary" @click="goHome">返回首页</el-button> -->
  </div>
</template>

<script setup lang="ts">

import { useRouter } from "vue-router";
const router = useRouter();

const goBack = () => router.go(-1)
// const goHome = () => router.replace('/home')

</script>

<style lang="scss" scoped>
.error-container {
  width: 100vw;
  height: 100vh;
  background: url(../../assets/images/404-error.png) center center no-repeat;
  background-size: 100% 100%;
}
</style>
