<template>
  <div class="app-table">
    <el-table
      :data="data"
      :height="height"
      :size="size"
      :header-cell-style="headerCellStyle"
      :cellStyle="cellStyle"
    >
      <el-table-column type="index" :index="1" label="序号" width="60" />
      <el-table-column
        v-for="column in columnList"
        :key="column.id"
        :label="column.label"
        :prop="column.prop"
        :width="column.width"
        :formatter="column.formatter"
      />
      <el-table-column fixed="right" label="操作" :width="columnWidth">
        <template #default="scope">
          <slot :scope="scope"></slot>
        </template>
      </el-table-column>
    </el-table>
    <div></div>

    <div class="app-pagination">
      <el-pagination
        v-if="isPagination"
        background
        :layout="layout"
        :current-page="page"
        :page-size="pageSize"
        :total="total"
        class="pagination"
        :page-sizes="pageSizes"
        @size-change="onSizeChange"
        @current-change="onCurrentPage"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { toRefs } from "vue";

interface TableColumn {
  id?: number;
  label?: string;
  prop?: string;
  width?: number | string;
  formatter?: Function;
}

const props = defineProps({
  // table
  data: { type: Array, default: () => [] },
  // table 的高度
  height: { type: String || Number, default: null },
  // Table 的尺寸	string	large / default /small
  size: { type: String, default: "large" },
  // 标头css样式
  headerCellStyle: {
    type: Object,
    default: () => ({ "text-align": "center" }),
  },
  // 每一个 cell 样式
  cellStyle: { type: Object, default: () => ({ "text-align": "center" }) },

  // table column
  columnList: { type: Array as () => TableColumn[], default: () => [] },
  // column操作的 width
  columnWidth: { type: String, default: "200" },

  // pagination
  // 是否开启分页
  isPagination: { type: Boolean, default: true },
  // 组件布局，子组件名用逗号分隔
  layout: { type: String, default: "prev, pager, next, jumper, sizes, total" },
  // 每页显示条目个数
  pageSize: { type: Number, default: 10 },
  // 总条目数
  total: { type: Number, default: 10 },
  // 当前页数
  page: { type: Number, default: 1 },
  // 每页显示个数选择器的选项设置
  pageSizes: { type: Array, default: () => [10, 20, 50, 100] },
  // pageSizes: { type: Array, default: () => [1, 2] },
});

const {
  // table
  data,
  height,
  size,
  columnList,
  layout,
  pageSize,
  total,
  page,
  pageSizes,
  isPagination,
} = toRefs(props);

const emits = defineEmits(["onPaginationChange"]);

// 每页显示条数改变
const onSizeChange = (val: string) => {
  emits("onPaginationChange", "pageSize", val);
};

// 页数改变
const onCurrentPage = (val: string) => {
  emits("onPaginationChange", "page", val);
};
</script>

<style lang="scss" scoped>
.app-pagination {
  float: right;
  margin: 15px;
  background-color: $bgfff;
}
</style>
