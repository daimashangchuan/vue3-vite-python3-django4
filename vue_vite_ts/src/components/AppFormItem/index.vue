<template>
  <!-- :rules="rules[prop]" -->
  <el-form-item
    :prop="prop"
    :label="label"
    :label-width="labelWidth"
    :rules="rules"
  >
    <el-input
      v-if="type === 'input'"
      :type="inputType"
      v-model="model[prop]"
      :maxlength="maxlength"
      :minlength="minlength"
      :show-word-limit="showWordLimit"
      :placeholder="placeholder"
      :clearable="clearable"
      :show-password="showPassword"
      :readonly="readonly"
      :disabled="disabled"
      :autosize="autosize"
    />

    <el-input-number
      v-else-if="type === 'number'"
      v-model="model[prop]"
      :min="min"
      :max="max"
      :step="step"
      :placeholder="placeholder"
      :precision="precision"
      :readonly="readonly"
      :disabled="disabled"
    />

    <el-tree
      v-else-if="type === 'tree'"
      :data="data"
      :node-key="nodeKey"
      :default-checked-keys="defaultCheckedKeys"
      :show-checkbox="showCheckbox"
      :default-expand-all="defaultExpandAll"
      :props="treeProps"
      @check="onTreeCheck"
    />

    <el-select
      v-else-if="type === 'select'"
      v-model="model[prop]"
      :placeholder="placeholder"
      :clearable="clearable"
      :disabled="disabled"
    >
      <el-option
        v-for="(item, index) in data"
        :key="index"
        :label="item.name"
        :value="item.id"
      />
    </el-select>

    <el-cascader
      v-else-if="type === 'cascader'"
      :options="data"
      v-model="model[prop]"
      :placeholder="placeholder"
      :clearable="clearable"
      :CascaderProps="CascaderProps"
      :disabled="disabled"
    />

    <template v-else-if="type === 'slot'">
      <slot></slot>
    </template>
  </el-form-item>
</template>

<script lang="ts" setup>
import { toRefs, Ref } from "vue";

interface DataInterface {
  id?: number;
  name?: string;
}

const props = defineProps({
  // 需要渲染的类型
  type: { type: String, default: "input" },
  // form-item
  prop: { type: String, default: "" },
  label: { type: String, default: "" },
  labelWidth: { type: String, default: "auto" },
  rules: { type: Object, default: {} },

  // el-contents common
  // 展示数据
  data: { type: Array, default: () => [] },
  // form的model
  model: { type: Object, default: {} },
  // 输入框提示
  placeholder: { type: String, default: "" },
  // 是否禁用
  disabled: { type: Boolean, default: false },
  // 是否显示清除按钮
  clearable: { type: Boolean, default: true },

  /**
   * type === input
   *  */
  // input的type类型
  inputType: { type: String, default: "text" },
  // 最大长度
  maxlength: { type: String || Number, default: null },
  // 最小长度
  minlength: { type: String || Number, default: null },
  // 是否显示统计字数, 需要设置 maxlength 只在 type 为 'text' 或 'textarea' 的时候生效
  showWordLimit: { type: Boolean, default: false },
  // 是否显示切换密码图标
  showPassword: { type: Boolean, default: false },
  // 只读模式
  readonly: { type: Boolean, default: false },
  // 高度适应
  autosize: { type: Object, default: { minRows: 4 } },

  /**
   * type === number
   *  */
  // 最小值
  min: { type: Number, default: 0 },
  // 最大值
  max: { type: Number, default: 999 },
  // 数字精度
  precision: { type: Number, default: 0 },
  // 计数器步长
  step: { type: Number, default: 1 },

  /**
   * type === tree
   *  */
  // 选中的 key
  nodeKey: { type: String, default: "id" },
  // 使用复选框
  showCheckbox: { type: Boolean, default: true },
  // 默认选中
  defaultCheckedKeys: { type: Array, default: () => [] },
  // 是否全部展开
  defaultExpandAll: { type: Boolean, default: true },
  // 渲染的数据
  treeProps: { type: Object, default: () => null },

  /**
   * type === number
   *  */
  // 选项的数据源 value 和 label 可以通过 CascaderProps 修改
  CascaderProps: { type: Object, default: () => null },
});

const {
  // form-item
  type,
  prop,
  label,
  labelWidth,
  rules,

  // el-contents common
  model,
  placeholder,
  disabled,

  /**
   * type === input
   *  */
  inputType,
  maxlength,
  minlength,
  showWordLimit,
  clearable,
  showPassword,
  readonly,
  autosize,

  /**
   * type === number
   *  */
  min,
  max,
  precision,
  step,

  /**
   * type === tree
   *  */
  nodeKey,
  showCheckbox,
  defaultCheckedKeys,
  defaultExpandAll,
  treeProps,
} = toRefs(props);

const data = toRefs(props).data as Ref<DataInterface[]>;

const emits = defineEmits(["onTreeCheck"]);
const onTreeCheck = (val: any, data: any) => {
  emits("onTreeCheck", val, data);
};
</script>

<style lang="scss" scoped></style>
