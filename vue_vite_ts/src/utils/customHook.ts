/**
 * 自定义 Hook
 */
import { storeToRefs } from "pinia";
import { useAppPinia,  useRefPinia } from '../pinia';

// 获取 Store 动态
export const useCustomStore = () => {
  const RefStore = useRefPinia();
  const AppStore = useAppPinia();
  const { AppLocale, AppLocaleStatus, AppTabList } = storeToRefs(RefStore);
  return {
    ...AppStore,
    ...RefStore, 
    AppLocale, 
    AppLocaleStatus, 
    AppTabList
  }
}

