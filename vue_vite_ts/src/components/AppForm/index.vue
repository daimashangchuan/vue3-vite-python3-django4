<template>
  <!-- ref="formRef" -->
  <el-form
    ref="formRef"
    :model="model"
    :rules="rules"
    :inline="inline"
    :label-position="labelPosition"
    :label-width="labelWidth"
    :status-icon="statusIcon"
    :disabled="disabled"
    :scroll-to-error="scrollToError"
    :scroll-into-view-options="scrollIntoViewOptions"
    autocomplete="off"
  >
    <slot></slot>
  </el-form>
</template>

<script lang="ts" setup>
import { toRefs, ref } from "vue";

const formRef = ref();

const getAppFormRef = () => {
  if (formRef.value) return formRef;
  return null;
};

defineExpose({
  getAppFormRef,
});

const props = defineProps({
  model: { type: Object, default: {} },
  rules: { type: Object, default: {} },
  inline: { type: Boolean, default: false },
  labelPosition: { type: String, default: "right" },
  labelWidth: { type: String, default: "auto" },
  statusIcon: { type: Boolean, default: false },
  // 是否禁用该表单内的所有组件。 如果设置为 true, 它将覆盖内部组件的 disabled 属性
  disabled: { type: Boolean, default: false },
  // 当校验失败时，滚动到第一个错误表单项
  scrollToError: { type: Boolean, default: true },
  // 当校验有失败结果时，滚动到第一个失败的表单项目 可通过 scrollIntoView 配置
  scrollIntoViewOptions: {
    type: Object,
    default: { behavior: "smooth", block: "end", inline: "nearest" },
  },
});

const {
  model,
  rules,
  inline,
  labelPosition,
  labelWidth,
  statusIcon,
  disabled,
  scrollToError,
  scrollIntoViewOptions,
} = toRefs(props);
</script>

<style lang="scss" scoped></style>
