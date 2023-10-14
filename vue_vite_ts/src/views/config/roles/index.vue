<template>
  <div class="config-role-container">
    <AppForm ref="AppFormRef" :model="roleModel" inline>
      <AppFormItem
        :model="roleModel"
        prop="name"
        label="角色名称"
        placeholder="请输入角色名称"
      />
      <el-form-item>
        <el-button type="primary" @click="onSearch()">查询</el-button>
        <el-button plain @click="onSearch('reset')">重置</el-button>
      </el-form-item>
    </AppForm>

    <el-button type="primary" @click="onRoleUpdata">
      <el-icon><Plus /></el-icon>
    </el-button>

    <AppTable
      :columnList="columnList"
      :data="tableData"
      :page="page"
      :pageSize="pageSize"
      :total="total"
      @onPaginationChange="onPaginationChange"
    >
      <template #default="{ scope }">
        <el-button type="primary" @click="onRoleUpdata(scope.row)">
          <!-- 编辑 -->
          <el-icon><Edit /></el-icon>
        </el-button>
        <el-button type="danger" @click="onDeleteRoleDelete(scope.row)">
          <!-- 删除 -->
          <el-icon><Delete /></el-icon>
        </el-button>
      </template>
    </AppTable>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { ElMessageBox, ElMessage } from "element-plus";
import AppForm from "../../../components/AppForm/index.vue";
import AppFormItem from "../../../components/AppFormItem/index.vue";
import AppTable from "../../../components/AppTable/index.vue";
import { reqGetRoleList, reqDeleteRoleDelete } from "../../../api/role";
import { columnList } from "./data";

const router = useRouter();

// 搜索
const AppFormRef = ref();
const roleModel = reactive({ name: "" });

const tableData = ref();
const total = ref(0);
const page = ref(1);
const pageSize = ref(10);

const onSearch = async (type?: string | number) => {
  if (type === "reset") {
    const formRef = AppFormRef.value?.getAppFormRef().value;
    if (!formRef) return;
    await formRef.resetFields();
  }
  page.value = 1;
  initGetRoleList();
};

const initGetRoleList = async () => {
  const data: any = await reqGetRoleList({
    page: page.value,
    pageSize: pageSize.value,
    name: roleModel.name,
  });
  tableData.value = data?.body?.list;
  total.value = data?.body?.total;
};

const onPaginationChange = (type: string, val: number) => {
  if (type === "page") {
    page.value = val;
  } else if (type === "pageSize") {
    page.value = 1;
    pageSize.value = val;
  }
  initGetRoleList();
};

// 添加 & 编辑  用户
const onRoleUpdata = (row: any) => {
  const url =
    row && row.id ? `/config/roles/edit?id=${row.id}` : `/config/roles/create`;
  router.push(url);
};

// 删除角色
const onDeleteRoleDelete = async (row: any) => {
  ElMessageBox.confirm("确定要删除吗？", "删除", {
    type: "warning",
    confirmButtonText: "确定",
    cancelButtonText: "取消",
  }).then(async () => {
    const data: any = await reqDeleteRoleDelete({ id: row.id });
    if (data.code === 0) {
      ElMessage.success("删除成功！");
      initGetRoleList();
    }
  });
};

const init = () => {
  initGetRoleList();
};
init();
</script>

<style lang="scss" scoped></style>
