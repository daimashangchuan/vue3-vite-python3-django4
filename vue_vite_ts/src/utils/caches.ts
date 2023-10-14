/**
 *  公用的工具方法
 */
import Cookies from 'js-cookie';

/**
 *  cookie  添加   获取    删除
 */
export const CookieUtil = {
  //  options   expires有效时间   path 对path路径有效
  set(key: string, value: any, options?: any) {
    return Cookies.set(key, value, options);
  },
  // key 为空 获取全部的 cookie
  get(key: string) {
    return Cookies.get(key) ? Cookies.get(key) : null;
  },
  //  options   expires有效时间   path 对path路径无效
  del(key: string, options?: any) {

    return Cookies.remove(key, options);
  }
};

/**
 * localStorage  添加   获取    删除
 */
export const LocalUtil = {
  set(key: string, value?: any) {
    return localStorage.setItem(key, JSON.stringify(value || ""));
  },
  get(key: string) {
    const StorageValue = localStorage.getItem(key);
    return StorageValue !== null ? JSON.parse(StorageValue) : '';
  },
  del(key: string) {
    return localStorage.removeItem(key);
  }
};

