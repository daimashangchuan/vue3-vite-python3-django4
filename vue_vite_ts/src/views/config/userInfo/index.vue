<template>
  <div class="config-userInfo-container">
    <div class="config-userInfo-form">
      <AppForm ref="AppFormRef" :rules="rules" :model="userInfoModel">
        <AppFormItem
          :model="userInfoModel"
          prop="name"
          label="姓名"
          placeholder="请输入姓名"
        />

        <AppFormItem
          :model="userInfoModel"
          prop="phone"
          label="账号"
          readonly
          placeholder="请输入11位手机号"
        />

        <AppFormItem
          v-if="type == 2"
          type="slot"
          :model="userInfoModel"
          label="角色"
        >
          <span>{{ userInfoModel?.role?.name }}</span>
        </AppFormItem>

        <AppFormItem
          type="select"
          :data="genderList"
          :model="userInfoModel"
          prop="gender"
          label="性别"
          placeholder="请选择性别"
        />

        <AppFormItem
          type="number"
          :model="userInfoModel"
          prop="age"
          label="年龄"
          placeholder="请输入年龄"
        />

        <AppFormItem
          type="cascader"
          :data="regionData"
          :model="userInfoModel"
          prop="region"
          label="省市区"
          placeholder="请选择省市区"
        />

        <AppFormItem
          :model="userInfoModel"
          prop="address"
          label="详细地址"
          placeholder="请输入详细地址"
        />

        <AppFormItem
          :model="userInfoModel"
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
          type="primary"
          style="width: 30%; margin: auto"
          @click="submitForm"
        >
          保存
        </el-button>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive } from "vue";
import { ElMessageBox, ElMessage } from "element-plus";
import { regionData } from "element-china-area-data";
import AppForm from "../../../components/AppForm/index.vue";
import AppFormItem from "../../../components/AppFormItem/index.vue";
import { reqPutUserInfoUpdata, reqGetUserInfoDetail } from "../../../api/auth";
import { genderList } from "../../../components/data";

const AppFormRef = ref();

const type = ref(2); // 用户类型 ((1, '内置'), (2, '创建'))

const userInfoModel = reactive({
  phone: "", // 账号
  name: "", // 姓名
  role: { name: "" }, // 角色内容
  roleId: null, // 用户角色
  gender: null, // 性别
  age: null, // 年龄
  region: [], // 省市区
  address: "", // 详细地址
  detail: "", // 账号说明
});

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


// 获取账号详情
const initGetUserInfoDetail = async () => {
  const data: any = await reqGetUserInfoDetail();
  const { body } = data;
  userInfoModel.name = body.name || "";
  userInfoModel.phone = body.phone || "";
  userInfoModel.roleId = body.roleId || null;
  userInfoModel.role = body.role || null;
  userInfoModel.gender = body.gender || null;
  userInfoModel.age = body.age || null;
  userInfoModel.region = body.region ? body.region.split(",") : [];
  userInfoModel.address = body.address || "";
  userInfoModel.detail = body.detail || null;
  type.value = body.type || 2;
};

const init = () => {
  initGetUserInfoDetail();
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
          ...userInfoModel,
          region:
            userInfoModel.region && userInfoModel.region.length > 0
              ? userInfoModel.region.join(",")
              : "",
        };
        await reqPutUserInfoUpdata(params);
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
.config-userInfo-form {
  width: 500px;
}
</style>
