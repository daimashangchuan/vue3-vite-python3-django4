<template>
  <div class="role-updata-container">
    <AppForm ref="AppFormRef" :rules="rules" :model="roleModel">
      <AppFormItem
        :model="roleModel"
        prop="name"
        label="角色名称"
        placeholder="请输入角色名称"
      />

      <AppFormItem
        :model="roleModel"
        inputType="textarea"
        prop="detail"
        label="角色说明"
        placeholder="请输入角色说明"
        maxlength="200"
        showWordLimit
      />

      <AppFormItem
        type="tree"
        label="角色权限"
        :model="roleModel"
        nodeKey="path"
        :defaultCheckedKeys="permission"
        :data="AppPermissionList"
        :treeProps="treeProps"
        @onTreeCheck="onTreeCheck"
      />
    </AppForm>

    <div class="flex-around-content">
      <el-button
        round
        plain
        type="primary"
        style="width: 30%; margin: auto"
        @click="router.go(-1)"
      >
        返回
      </el-button>

      <el-button
        round
        type="primary"
        style="width: 30%; margin: auto"
        @click="submitForm"
      >
        保存
      </el-button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { ElMessageBox, ElMessage } from "element-plus";
import AppForm from "../../../components/AppForm/index.vue";
import AppFormItem from "../../../components/AppFormItem/index.vue";
import { useCustomStore } from "../../../utils/customHook";
import { defaultTreeProps } from "./data";
import {
  reqRoleInsert,
  reqPutRoleUpdata,
  reqGetRoleDetail,
} from "../../../api/role";
import { getPathList } from "../../../utils";

const router = useRouter();
const id = router.currentRoute.value.query.id;
const AppFormRef = ref();

const { AppList, AppPermissionList } = useCustomStore();

const treeProps = ref(defaultTreeProps);
const roleModel = reactive({
  name: "",
  detail: "",
});

const permission = ref(["/config/userInfo"]);

const rules = reactive({
  name: [{ required: true, message: "请输入角色名称", trigger: ["change"] }],
});

const onTreeCheck = (_: any, data: any) => {
  permission.value = data.checkedKeys;
};

const initGetRoleDetail = async () => {
  const data: any = await reqGetRoleDetail({ id });
  const { body } = data;
  roleModel.name = body.name || "";
  roleModel.detail = body.detail || "";
  permission.value = body.permission ? JSON.parse(body.permission) : [];
};

const init = () => {
  id && initGetRoleDetail();
};
init();

const submitForm = () => {
  const formRef = AppFormRef.value?.getAppFormRef().value;
  if (!formRef) return;

  formRef.validate(async (valid: Boolean) => {
    if (valid) {
      if (permission.value.length <= 0) {
        ElMessage.info("请选择权限列表，权限为必选项！");
        return;
      }
      ElMessageBox.confirm("确定要保存吗？", "提示", {
        type: "warning",
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      }).then(async () => {
        const pathList = getPathList(AppList, permission.value);
        const params = {
          ...roleModel,
          permission:
            permission.value.length > 0 ? JSON.stringify(permission.value) : "",
          pathList: pathList.length > 0 ? JSON.stringify(pathList) : "",
        };
        id
          ? await reqPutRoleUpdata({ ...params, id })
          : await reqRoleInsert(params);
        router.go(-1);
        ElMessage.success("操作成功！");
      });
    } else {
      ElMessage.info("请完善信息！");
      return false;
    }
  });
};
</script>

<style lang="scss" scoped>
.role-updata-container {
  width: 500px;
}
</style>
