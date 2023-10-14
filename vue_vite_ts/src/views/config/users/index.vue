<template>
  <div class="config-users-container">
    <AppForm ref="AppFormRef" :model="userModel" inline>
      <AppFormItem
        :model="userModel"
        prop="name"
        label="姓名"
        placeholder="请输入姓名"
      />
      <AppFormItem
        :model="userModel"
        prop="phone"
        label="账号"
        placeholder="请输入账号"
      />
      <el-form-item>
        <el-button type="primary" @click="onSearch">查询</el-button>
        <el-button plain @click="onSearch('reset')">重置</el-button>
      </el-form-item>
    </AppForm>

    <el-button type="primary" @click="onUserUpdata">
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
        <el-button type="primary" @click="onUserUpdata(scope.row)">
          <el-icon><Edit /></el-icon>
        </el-button>
        <el-button type="danger" @click="onDeleteUserDelete(scope.row)">
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
import { reqGetUserList, reqDeleteUserDelete } from "../../../api/user";
import { columnList } from "./data";

const router = useRouter();
// 搜索
const AppFormRef = ref();

const userModel = reactive({
  name: "",
  phone: "",
});

const tableData = ref();
const total = ref(0);
const page = ref(1);
const pageSize = ref(10);

const onSearch = async (type?: string | number) => {
  if (type === "reset") {
    const formRef = AppFormRef.value.getAppFormRef()?.value;
    if (!formRef) return;
    await formRef.resetFields();
  }
  page.value = 1;
  initGetUserList();
};

const initGetUserList = async () => {
  const data: any = await reqGetUserList({
    page: page.value,
    pageSize: pageSize.value,
    ...userModel,
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
  initGetUserList();
};

// 添加 & 编辑  用户
const onUserUpdata = (row: any) => {
  const url =
    row && row.id ? `/config/users/edit?id=${row.id}` : `/config/users/create`;
  router.push(url);
};

// 删除用户
const onDeleteUserDelete = async (row: any) => {
  ElMessageBox.confirm("确定要删除吗？", "删除", {
    type: "warning",
    confirmButtonText: "确定",
    cancelButtonText: "取消",
  }).then(async () => {
    const data: any = await reqDeleteUserDelete({ id: row.id });
    if (data.code === 0) {
      ElMessage.success("删除成功！");
      initGetUserList();
    }
  });
};

const init = () => {
  initGetUserList();
};
init();
</script>

<style lang="scss" scoped></style>
