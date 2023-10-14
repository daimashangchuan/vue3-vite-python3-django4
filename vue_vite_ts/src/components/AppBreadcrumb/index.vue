<template>
  <el-breadcrumb class="app-breadcrumb" separator=">">
    <el-breadcrumb-item
      v-for="(item, index) in list"
      :key="index"
      @click="onBreadcrumb(item, index)"
    >
      <span :class="index + 1 !== list.length ? 'link' : ''">
        {{ item.name ? item.name : item }}
      </span>
    </el-breadcrumb-item>
  </el-breadcrumb>
</template>

<script lang="ts" setup>
import { toRefs } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const props = defineProps({
  list: { type: Object, default: () => [] },
});

const { list } = toRefs(props);

const onBreadcrumb = (item: any, index: string) => {
  const goIndex = Number(index) + 1 - list.value.length;
  item.path ? router.push(item.path) : router.go(goIndex);
};
</script>

<style lang="scss" scoped>
.app-breadcrumb {
  padding-bottom: 20px;

  .link {
    color: $colinit;
  }
}
</style>
