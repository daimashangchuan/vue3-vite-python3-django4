/**
 * 公共
 */
import { defineStore } from 'pinia';
import { LocalUtil } from "../utils/caches";
import { initRouterList, initPermissionList } from "../utils"
import { AppPathList } from "../components/data"

interface UserInfo {
  name: string;
  phone: string;
  token: string;
  type: number;
  role: {
    permission: string
  }
}

interface AppItemList {
  path?: string;
  isPermission?: number;
  title?: string;
  name?: string;
  icon?: string;
  permissionPath?: string;
  component?: string;
  children?: AppItemList[] | null;
}


export default defineStore('AppModule', {
  state: () => ({
    // 登录信息
    userInfo: null as UserInfo | null,
    // 最全的数据
    AppList: AppPathList as AppItemList[] | null,
  }),


  actions: {
    setUserInfo(newState: UserInfo | null) {
      this.userInfo = newState;
    },

    setAppList(newState: any) {
      this.AppList = newState;
    },

    setAppClearCache() {
      this.userInfo = null;
      this.AppList = null;
      LocalUtil.del('AppModule')
    }
  },


  getters: {
    AppRouterList(state) {
      return initRouterList(state.AppList)
    },

    AppPermissionList(state) {
      return initPermissionList(state.AppList)
    }
  },

  // 将store的state中的全部数据进行缓存，直接在state同级下面添加persist对象
  persist: {
    key: "AppModule",
    paths: ['userInfo', 'AppList']
  }

})





