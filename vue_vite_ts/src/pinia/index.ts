/**
 * 状态主入口
 */

// 引入createPinia方法从pinia
import { createPinia } from 'pinia'
// 引入数据持久化插件
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
// 拿到pinia实例
const usePinia = createPinia()
// pinia使用数据持久化插件
usePinia.use(piniaPluginPersistedstate)

// 挂载 pinia
export const pinia = usePinia;

// pinia App模块
import useAppModule from "./useAppModule";
export const useAppPinia = useAppModule;

// pinia Ref模块
import useRefModule from "./useRefModule";
export const useRefPinia = useRefModule;

