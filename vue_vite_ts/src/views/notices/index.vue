<template>
  <div class="notice-container">
    <AppForm ref="AppFormRef" :model="noticeModel" inline>
      <AppFormItem
        :model="noticeModel"
        prop="title"
        label="通知标题"
        placeholder="请输入姓名"
      />
      <el-form-item>
        <el-button type="primary" @click="onSearch">查询</el-button>
        <el-button plain @click="onSearch('reset')">重置</el-button>
      </el-form-item>
    </AppForm>

    <el-button type="primary" @click="onNoticeUpdata(1)">
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
        <el-button type="primary" @click="onNoticeUpdata(2, scope.row)">
          <el-icon><Edit /></el-icon>
        </el-button>
        <el-button type="danger" @click="onNoticeUpdata(3, scope.row)">
          <el-icon><Delete /></el-icon>
        </el-button>
      </template>
    </AppTable>

    <!-- :before-close="handleClose" -->
    <el-dialog
      v-if="dialogVisible !==0"
      v-model="dialogShow"
      :title="dialogVisible===1?'添加':dialogVisible===1?'编辑':''"
      width="30%"
      :before-close="onDialogClose"
    >
      <AppForm 
        ref="AppUpdataFormRef" 
        :model="noticeUpdataModel" 
        :rules="noticeUpdataRules"
      >
        <AppFormItem
          :model="noticeUpdataModel"
          prop="title"
          label="通知标题"
          placeholder="请输入通知标题"
        />

        <AppFormItem
          inputType="textarea"
          :model="noticeUpdataModel"
          prop="detail"
          label="通知详情"
          placeholder="请输入通知详情"
          maxlength="200"
          showWordLimit
        />

      </AppForm>
      <template #footer>
        <span class="dialog-footer">
          <el-button plain type="primary" @click="onDialogClose">关闭</el-button>
          <el-button type="primary" @click="submitForm">保存</el-button>
        </span>
      </template>
    </el-dialog>

  </div>

  
</template>

<script lang="ts" setup>
import { reactive, ref } from "vue";
import { ElMessageBox, ElMessage } from "element-plus";
import AppForm from "../../components/AppForm/index.vue";
import AppFormItem from "../../components/AppFormItem/index.vue";
import AppTable from "../../components/AppTable/index.vue";
import { reqNoticeInsert, reqDeleteNoticeDelete, reqPutNoticeUpdata, reqGetNoticeList } from "../../api/notice";
import { columnList } from "./data";

// 搜索
const AppFormRef = ref();
// 添加&编辑
const AppUpdataFormRef = ref()

const noticeModel = reactive({ title: "" });

const noticeUpdataModel = reactive({
  title: "",
  detail: "",
});
const noticeUpdataRules = reactive({
  title: [
    { required: true, message: "请输入标题名称", trigger: ["change"] },
  ],
});

const dialogVisible = ref(0)
const dialogShow = ref(true)
const currentRowId = ref(0);

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
  initGetNoticeList();
};

// 通知列表
const initGetNoticeList = async () => {
  const data: any = await reqGetNoticeList({
    page: page.value,
    pageSize: pageSize.value,
    ...noticeModel 
  });
  tableData.value = data?.body?.list;
  total.value = data?.body?.total;
};

// 分页
const onPaginationChange = (type: string, val: number) => {
  if (type === "page") {
    page.value = val;
  } else if (type === "pageSize") {
    page.value = 1;
    pageSize.value = val;
  }
  initGetNoticeList();
};

// 添加1 & 编辑2 & 删除3
const onNoticeUpdata = (num:number, row?: any) => {
  if(num === 3) {
    ElMessageBox.confirm("确定要删除吗？", "删除", {
      type: "warning",
      confirmButtonText: "确定",
      cancelButtonText: "取消",
    }).then(async () => {
      const data: any = await reqDeleteNoticeDelete({ id: row.id });
      if (data.code === 0) {
        ElMessage.success("删除成功！");
        initGetNoticeList();
      }
    });
  } else {
    dialogVisible.value = num;
    currentRowId.value = row?.id || 0;
    noticeUpdataModel.title = row?.title || "";
    noticeUpdataModel.detail = row?.detail || "";
  }
};

//  关闭弹窗
const onDialogClose = async () => {
  dialogVisible.value = 0;
  currentRowId.value = 0;
  const formRef = AppUpdataFormRef?.value?.getAppFormRef()?.value;
  if (!formRef) return; 
  await formRef.resetFields();
}

const submitForm = () => {
  const formRef = AppUpdataFormRef?.value?.getAppFormRef()?.value;
  if (!formRef) return;

  formRef.validate(async (valid: Boolean) => {
    if (valid) {

      currentRowId.value ? 
        await reqPutNoticeUpdata({ ...noticeUpdataModel, id: currentRowId.value }) : 
        await reqNoticeInsert(noticeUpdataModel);

        onDialogClose()
        initGetNoticeList()

    } else {
      ElMessage.info("请完善信息！");
      return false;
    }
  });
};

const init = () => {
  initGetNoticeList();
};
init();
</script>

<style lang="scss" scoped></style>
