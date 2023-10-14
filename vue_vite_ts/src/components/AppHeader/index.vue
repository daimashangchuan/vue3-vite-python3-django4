<template>
  <div class="header-container flex-between-center">
    <div class="logo flex-between-center">
      <img src="../../assets/images/logo.png" /> &nbsp;&nbsp;
      <span>社区疫情管理系统</span>
    </div>

    <el-dropdown class="dropdown">
      <div class="user-name">{{ userInfo?.name || "设置" }}</div>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item @click="onJump">个人中心</el-dropdown-item>
          <el-dropdown-item @click="onVisible(true)">修改密码</el-dropdown-item>
          <el-dropdown-item @click="onLogout">退出</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>

    <el-dialog v-model="dialogVisible" title="修改密码" width="500px">
      <AppForm ref="AppFormRef" :model="passwordModel" :rules="rules">
        <AppFormItem
          text="passWord"
          :model="passwordModel"
          prop="passWord"
          label="旧密码"
          placeholder="请输入旧密码"
          showPassword
        />

        <AppFormItem
          text="passWord"
          :model="passwordModel"
          prop="newPassWord"
          label="新密码"
          placeholder="请输入新密码"
          showPassword
        />

        <AppFormItem
          text="passWord"
          :model="passwordModel"
          prop="confirmNewPassWord"
          label="确认密码"
          placeholder="请确认密码，与新密码一致"
          showPassword
        />
      </AppForm>
      <template #footer>
        <span class="dialog-footer">
          <el-button plain type="primary" @click="onVisible(false)"
            >关闭</el-button
          >
          <el-button type="primary" @click="submitForm">保存</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { useCustomStore } from "../../utils/customHook";
import { ElMessageBox, ElMessage } from "element-plus";
import AppForm from "../../components/AppForm/index.vue";
import AppFormItem from "../../components/AppFormItem/index.vue";
import { reqPutUpdataPass } from "../../api/auth";

const router = useRouter();
const { userInfo } = useCustomStore();

const dialogVisible = ref(false);
const AppFormRef = ref();

const passwordModel = reactive({
  passWord: "",
  newPassWord: "",
  confirmNewPassWord: "",
});

const rules = reactive({
  passWord: [
    {
      required: true,
      min: 6,
      message: "请输入旧密码，旧密码不能为空，密码至少为6位数",
      trigger: ["change"],
    },
  ],
  newPassWord: [
    {
      required: true,
      min: 6,
      message: "请输入新密码，新密码不能为空，密码至少为6位数",
      trigger: ["change"],
    },
  ],
  confirmNewPassWord: [
    {
      required: true,
      message: "请确认密码，确认新密码不能为空",
      trigger: ["change"],
    },
    {
      validator: (_: any, value: any, callback: any) => {
        if (value !== passwordModel.newPassWord) {
          callback(new Error("新密码与确认密码不一致"));
        } else {
          callback();
        }
      },
      trigger: ["change"],
    },
  ],
});

// 修改密码的弹窗
const onVisible = (visible: boolean) => {
  dialogVisible.value = visible;
};

// 修改密码提交
const submitForm = () => {
  const formRef = AppFormRef?.value?.getAppFormRef()?.value;
  if (!formRef) return;

  formRef.validate(async (valid: Boolean) => {
    if (valid) {
      const data: any = await reqPutUpdataPass(passwordModel);
      const { code } = data;
      if (code == 0) {
        ElMessage.success("密码修改成功，请重新登录！");
        router.replace("/login");
        onVisible(false);
      }
    } else {
      ElMessage.info("请完善信息！");
      return false;
    }
  });
};

// 去账号设置
const onJump = () => {
  router.push("/config/userInfo");
};

// 退出登录
const onLogout = () => {
  ElMessageBox.confirm("确定要退出吗？", "退出", {
    type: "warning",
    confirmButtonText: "确定",
    cancelButtonText: "取消",
  }).then(async () => {
    ElMessage.success("退出成功！");
    router.replace("/login");
  });
};
</script>

<style lang="scss" scoped>
.header-container {
  color: $colfff;
  height: 80px;
  padding: 0 20px;
  .logo {
    img {
      width: 120px;
      height: auto;
    }
  }

  .dropdown {
    cursor: pointer;

    .user-name {
      color: $colfff;
      font-size: 16px;
    }
  }
}
</style>
