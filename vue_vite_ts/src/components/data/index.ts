/**
 * 公共
 * 
 * AppRouterList
 *    path            路由
 *    isPermission    是否为权限侧边栏列表 1是 0否
 *    title           页面展示标题
 *    name            路由名称
 *    icon            权限侧边栏列表图表  可以为空
 *    permissionPath  拥有这个路由的权限（侧边栏的路由）
 *    component       组件存放路径文件
 */
export const AppPathList = [
  /**
   * 系统首页
   */
  {
    path: "/home",
    isPermission: 1,
    title: "系统首页",
    name: "Home",
    icon: "House",
    permissionPath: "/home",
    component: "../views/home/index.vue"
  },
  /**
   * 通知管理
   */
  {
    path: "/notices",
    isPermission: 1,
    title: "通知管理",
    name: "Notices",
    icon: "Notification",
    permissionPath: "/notices",
    component: "../views/notices/index.vue"
  },
  /**
   * 接种管理
   */
  {
    path: "/vaccinatelogs",
    isPermission: 1,
    title: "接种管理",
    name: "VaccinateLogs",
    icon: "MagicStick",
    permissionPath: "/vaccinatelogs",
    component: "../views/vaccinatelogs/index.vue"
  },
  /**
   * 统计信息
   */
  {
    path: "/statistics",
    isPermission: 1,
    title: "统计信息",
    name: "Statistics",
    icon: "DataAnalysis",
    permissionPath: "/statistics",
    component: "../views/statistics/index.vue"
  },
  /**
   * 检查管理
   */
  {
    path: "/checklogs",
    isPermission: 1,
    title: "检查管理",
    name: "Checklogs",
    icon: "FolderChecked",
    permissionPath: "/checklogs",
    component: "../views/checklogs/index.vue"
  },
  /**
   * 异常管理
   */
  {
    path: "/abnormitylogs",
    isPermission: 1,
    title: "异常管理",
    name: "Abnormitylogs",
    icon: "SetUp",
    permissionPath: "/abnormitylogs",
    component: "../views/abnormitylogs/index.vue"
  },
  /**
   * 系统管理
   */
  {
    path: "/config",
    isPermission: 1,
    title: "系统管理",
    name: "Setting",
    icon: "FolderChecked",
    permissionPath: "/config",
    component: "../views/config/index.vue",
    children: [
      /**
       * 账号管理
       */
      // 账号管理列表
      {
        path: "/config/users",
        isPermission: 1,
        title: "账号管理",
        name: "ConfigUsers",
        icon: "User",
        permissionPath: "/config/users",
        component: "../views/config/users/index.vue"
      },
      // 账号管理 添加
      {
        path: "/config/users/create",
        isPermission: 0,
        title: "添加账号",
        name: "ConfigUsersCreate",
        icon: "User",
        permissionPath: "/config/users",
        component: "../views/config/users/updata.vue"
      },
      // 账号管理 编辑
      {
        path: "/config/users/edit",
        isPermission: 0,
        title: "编辑账号",
        name: "ConfigUsersEdit",
        icon: "User",
        permissionPath: "/config/users",
        component: "../views/config/users/updata.vue"
      },
      /**
       * 角色管理
       */
      // 角色管理列表
      {
        path: "/config/roles",
        isPermission: 1,
        title: "角色管理",
        name: "ConfigRoles",
        icon: "Lock",
        permissionPath: "/config/roles",
        component: "../views/config/roles/index.vue"
      },
      // 角色管理 添加
      {
        path: "/config/roles/create",
        isPermission: 0,
        title: "添加角色",
        name: "ConfigRolesCreate",
        icon: "Lock",
        permissionPath: "/config/roles",
        component: "../views/config/roles/updata.vue"
      },
      // 角色管理 编辑
      {
        path: "/config/roles/edit",
        isPermission: 0,
        title: "编辑角色",
        name: "ConfigRolesEdit",
        icon: "Lock",
        permissionPath: "/config/roles",
        component: "../views/config/roles/updata.vue"
      },
      /**
       * 个人中心
       */
      {
        path: "/config/userInfo",
        isPermission: 1,
        title: "个人中心",
        name: "ConfigUserInfo",
        icon: "Avatar",
        permissionPath: "/config/userInfo",
        component: "../views/config/userInfo/index.vue",
        disabled: true
      }
    ]
  }
]


export const genderList = [
  { id: 1, name: '男' },
  { id: 2, name: '女' },
]