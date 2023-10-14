<template>
  <div>
    <template v-for="(menu, index) in data">
      <!-- 有下一级 -->
      <el-sub-menu
        v-if="menu?.children?.length > 0"
        :key="index"
        :index="menu.path"
      >
        <template #title>
          <el-icon>
            <component :is="menu.icon" />
          </el-icon>
          {{ menu.title }}
        </template>

        <MenuItem :data="menu.children"></MenuItem>
      </el-sub-menu>

      <!-- 最后一级 -->
      <el-menu-item v-else :key="menu.path" :index="menu.path">
        <template #title>
          <el-icon>
            <component :is="menu.icon" />
          </el-icon>
          {{ menu.title }}
        </template>
      </el-menu-item>
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import type { PropType } from "vue";

export default defineComponent({
  name: "MenuTree",

  props: {
    data: {
      type: Array as unknown as PropType<any[]>,
      required: true,
      default: () => [],
    },
  },
});
</script>
