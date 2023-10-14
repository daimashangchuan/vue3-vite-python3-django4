<template>
  <div class="login-container flex-content-content">
    <div class="login-body">
      <h3 class="login-title">社区疫情管理系统</h3>
      <AppForm ref="AppFormRef" :rules="rules" :model="loginModel">
        <AppFormItem
          :model="loginModel"
          prop="phone"
          label="账号"
          maxlength="11"
          placeholder="请输入账号"
        />

        <AppFormItem
          text="passWord"
          :model="loginModel"
          prop="passWord"
          label="密码"
          placeholder="请输入密码"
          showPassword
        />

        <div class="flex-around-content">
          <el-button
            round
            type="primary"
            style="width: 40%; margin: auto"
            @click="submitForm"
            >登录</el-button
          >

          <!-- <el-button 
            round plain
            type="primary" 
            style="width: 40%;margin: auto;"
            @click="submitForm"
          >注册</el-button> -->
        </div>
      </AppForm>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { Md5 } from "ts-md5";
import { useCustomStore } from "../../utils/customHook";
import AppForm from "../../components/AppForm/index.vue";
import AppFormItem from "../../components/AppFormItem/index.vue";
import { reqPostLogin } from "../../api/auth";
import { AppPathList } from "../../components/data"

const { setUserInfo, setAppList } = useCustomStore();
const AppFormRef = ref();

const loginModel = reactive({
  phone: "18847139686",
  passWord: "123456",
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
  passWord: [
    {
      required: true,
      message: "请输入密码，密码不能为空",
      trigger: ["change"],
    },
  ],
});

const router = useRouter();

const submitForm = () => {
  const formRef = AppFormRef.value?.getAppFormRef().value;
  if (!formRef) return;
  formRef.validate(async (valid: Boolean) => {
    if (valid) {
      const data: any = await reqPostLogin({
        ...loginModel,
        passWordMd5: Md5.hashAsciiStr(loginModel.passWord),
      });
      const { body = null } = data;
      body && setUserInfo(body);
      // 获取全部的路由
      const list = body?.type === 1 ? AppPathList : body?.role?.pathList ? JSON.parse(body.role.pathList) : [];
      setAppList(list)
      const url = list[0]?.children?.length>0 ? list[0].children[0].path : list[0].path;
      router.replace(url)
    }
  });
};
</script>

<style lang="scss" scoped>
.login-container {
  width: 100vw;
  height: 100vh;
  background: url(../../assets/images/banner.png) center center no-repeat;
  background-size: 100% 100%;

  .login-body {
    width: 380px;
    padding: 50px;
    background-color: $bgfff;

    .login-title {
      text-align: center;
    }
  }
}
</style>
