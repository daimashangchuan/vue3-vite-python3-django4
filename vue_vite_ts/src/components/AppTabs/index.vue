<template>
  <div class="app-tabs">
    <el-tabs
      v-model="model"
      :type="type"
      :closable="closable"
      @tab-click="onTabClick"
      @tab-remove="onTabRemove"
    >
      <el-tab-pane
        v-for="(item, index) in data"
        :key="index"
        :label="item.label"
        :name="item.name"
      />
    </el-tabs>
  </div>
</template>

<script lang="ts" setup>
import { ref, toRefs, watch } from "vue";

interface TabsItem {
  label?: string;
  name?: string;
}

const props = defineProps({
  type: { type: String, default: null },
  model: { type: String || Number, default: null },
  closable: { type: Boolean, default: false },
  data: { type: Array as () => TabsItem[], default: () => [] },
});

const emits = defineEmits(["onTabClick", "onTabRemove"]);

const model = ref(props.model);
const { type, data, closable } = toRefs(props);

watch(
  () => props.model,
  (newVal) => {
    model.value = newVal;
  }
);

// tab切换的变化
const onTabClick = (val: any) => {
  emits("onTabClick", val);
};
const onTabRemove = (val: any) => {
  emits("onTabRemove", val);
};
</script>

<style lang="scss" scoped></style>
