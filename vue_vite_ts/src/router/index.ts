/**
 * 路由主入口
 */
import { createRouter, createWebHashHistory } from "vue-router";
import { useCustomStore } from "../utils/customHook"

// 配置白名单 nextPath 可以不登录访问
const nextPath = ["/login"];

// 创建路由
const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/login',
      component: () => import('../views/login/index.vue'),
      meta: { title: "登录" }
    },
    {
      path: '/:pathMatch(.*)', // 匹配任何未被定义的路由
      name: '404',
      component: () => import('../views/notFound/404.vue'),
      meta: { title: "404" },
    }
  ]
})

// 路由跳转之前到钩子函数
router.beforeEach(async (to, _, next) => {

  const { userInfo, AppRouterList, setAppClearCache, setRefClearCache } = useCustomStore()

  // 判断是否去登录页 清除缓存信息
  if (to.path === '/login') {
    onRemoveRoute()
    setAppClearCache()
    setRefClearCache()
  }
  // 判断是否登录状态   配置白名单 nextPath 可以不登录访问
  if (!(userInfo || nextPath.includes(to.path))) {
    onRemoveRoute()
    next('/login');
    return undefined
  }

  // 动态添加路由
  if (AppRouterList && AppRouterList.length > 0) {
    // 避免重复添加
    if (!router.hasRoute('admin')) {
      router.addRoute({
        path: '/',
        name: "admin",
        redirect: { path: AppRouterList[0].path },
        component: () => import('../views/layout/index.vue'),
        children: AppRouterList
      });
      next(to.fullPath)
      return undefined
    }
  }

  next()
})

// 退出登录清除路由缓存
const onRemoveRoute = () => {
  if (router.hasRoute('admin')) {
    router.removeRoute('admin')
  }
}


export default router;


