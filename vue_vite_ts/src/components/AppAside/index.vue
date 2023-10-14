<template>
  <el-menu :default-active="defaultActive" router>
    <MenuItem :data="menuList"></MenuItem>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref, computed } from "vue";
import MenuItem from "./MenuItem.vue";
import { useRouter } from "vue-router";
import { useCustomStore } from "../../utils/customHook";

const { AppPermissionList } = useCustomStore();
let menuList = ref();
menuList.value = AppPermissionList;

const defaultActive = computed(() => {
  const router = useRouter();
  const permissionPath = router.currentRoute.value.meta.permissionPath;
  const fullPath = router.currentRoute.value.fullPath;

  if (permissionPath) return permissionPath;
  return fullPath;
});
</script>
