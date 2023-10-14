<template>
  <div class="user-updata-container">
    <AppForm ref="AppFormRef" :rules="rules" :model="userModel">
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
        placeholder="请输入11位手机号"
      />

      <AppFormItem
        type="select"
        :data="roleList"
        :model="userModel"
        prop="roleId"
        label="角色"
        placeholder="请选择角色"
      />

      <AppFormItem
        type="select"
        :data="genderList"
        :model="userModel"
        prop="gender"
        label="性别"
        placeholder="请选择性别"
      />

      <AppFormItem
        type="number"
        :model="userModel"
        prop="age"
        label="年龄"
        placeholder="请输入年龄"
      />

      <AppFormItem
        type="cascader"
        :data="regionData"
        :model="userModel"
        prop="region"
        label="省市区"
        placeholder="请选择省市区"
      />

      <AppFormItem
        :model="userModel"
        prop="address"
        label="详细地址"
        placeholder="请输入详细地址"
      />

      <AppFormItem
        :model="userModel"
        inputType="textarea"
        prop="detail"
        label="账号说明"
        placeholder="请输入账号说明"
        maxlength="200"
        showWordLimit
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
import { regionData } from "element-china-area-data";
import AppForm from "../../../components/AppForm/index.vue";
import AppFormItem from "../../../components/AppFormItem/index.vue";
import {
  reqUserInsert,
  reqPutUserUpdata,
  reqGetUserDetail,
} from "../../../api/user";
import { reqGetRoleList } from "../../../api/role";
import { genderList } from "../../../components/data";

const router = useRouter();
const id = router.currentRoute.value.query.id;

const AppFormRef = ref();
const roleList = ref<any[]>([]);
const userModel = reactive({
  phone: "", // 账号
  name: "", // 姓名
  roleId: null, // 用户角色
  gender: null, // 性别
  age: null, // 年龄
  region: [], // 省市区
  address: "", // 详细地址
  detail: "", // 账号说明
});

// const userModel = reactive({
//   phone: "18888888888",  // 账号
//   name: "张三",   // 姓名
//   roleId: 7,  // 用户角色
//   gender: 2,  // 性别
//   age: 28,   // 年龄
//   region: ["11","1101","110102"], // 省市区
//   address: "详细地址",   // 详细地址
//   detail: "账号说明",   // 账号说明
// });

const rules = reactive({
  phone: [
    {
      required: true,
      pattern: /^1[3456789]\d{9}$/,
      message: "请输入正确的手机号",
      trigger: ["change"],
    },
  ],
  name: [{ required: true, message: "请输入姓名", trigger: ["change"] }],
  roleId: [
    {
      type: Number,
      required: true,
      message: "请选择用户角色",
      trigger: ["change"],
    },
  ],
  age: [{ type: Number }],
  gender: [{ type: Number }],
  region: [{ type: Array }],
});

// 获取全部的角色列表
const initGetRoleList = async () => {
  const data: any = await reqGetRoleList();
  const { body } = data;
  roleList.value = body || [];
};

// 获取账号详情
const initGetUserDetail = async () => {
  const data: any = await reqGetUserDetail({ id });
  const { body } = data;
  userModel.name = body.name || "";
  userModel.phone = body.phone || "";
  userModel.roleId = body.roleId || null;
  userModel.gender = body.gender || null;
  userModel.age = body.age || null;
  userModel.region = body.region ? body.region.split(",") : [];
  userModel.address = body.address || "";
  userModel.detail = body.detail || null;
};

const init = () => {
  initGetRoleList();
  id && initGetUserDetail();
};
init();

const submitForm = () => {
  const formRef = AppFormRef.value?.getAppFormRef().value;
  if (!formRef) return;

  formRef.validate(async (valid: Boolean) => {
    if (valid) {
      ElMessageBox.confirm("确定要保存吗？", "提示", {
        type: "warning",
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      }).then(async () => {
        const params = {
          ...userModel,
          region:
            userModel.region && userModel.region.length > 0
              ? userModel.region.join(",")
              : "",
        };
        id
          ? await reqPutUserUpdata({ ...params, id })
          : await reqUserInsert(params);
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
.user-updata-container {
  width: 500px;
}
</style>
