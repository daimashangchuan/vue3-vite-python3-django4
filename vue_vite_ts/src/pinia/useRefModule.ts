/**
 * 公共
 */
import { ref } from 'vue';
import { defineStore } from 'pinia';
import { getUpdataList } from "../utils"
import { LocalUtil } from "../utils/caches"
import zhCN from "../locale/zhCN";
import enGB from "../locale/enGB";
import jaJP from '../locale/jaJp';

interface TabList {
  label?: string;
  name?: string;
  key?: string;
}

export default defineStore('RefModule', () => {

  const AppTabList = ref([] as TabList[]);
  const setAppTabList = (newState: any) => {
    if (newState?.label && newState?.name) {
      // 存在 label 与 name，使用 key 做判断 有替换旧的，没有新增
      const list = getUpdataList((AppTabList.value || []), newState, 'key')
      AppTabList.value = list;
    } else {
      // newState   删除指定的 name
      const list = (AppTabList.value || []).filter((item: any) => item.name !== newState)
      AppTabList.value = list;
    }
  }


  // 语言文字     zh中文  en英文  ja日文
  const AppLocaleStatus = ref('ja');
  const AppLocale = ref(jaJP);
  const setAppLocaleStatus = (newState: any) => {
    AppLocaleStatus.value = newState
    AppLocale.value = newState === 'zh' ? zhCN : newState === 'en' ? enGB : jaJP
  }


  const setRefClearCache = () => {
    AppTabList.value = [];
    setTimeout(() => {
      LocalUtil.del('RefModule');
    }, 20)
  }

  return {
    AppTabList, setAppTabList, 
    AppLocaleStatus, AppLocale, setAppLocaleStatus,
    setRefClearCache
  }

}, {
  // 将store的state中的全部数据进行缓存，直接在state同级下面添加persist对象
  persist: {
    key: "RefModule",
    paths: ['AppTabList', 'AppLocaleStatus', 'AppLocale']
  }
})





