/**
 *  封装请求的方法
 */
import axios from "axios";
import router from '../router/index'
import { ElMessage } from "element-plus"
import { useCustomStore } from "../utils/customHook";

const errorMsg = '服务器异常，请联系系统管理员！'

axios.defaults.baseURL = '/api';
axios.defaults.timeout = 5000;
// 发送请求时携带 CSRF 令牌
axios.defaults.withCredentials = true;

// const headers = {
//   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
//   'Content-Type': 'application/json; charset=utf-8',
//   'Content-Type':'multipart/form-data'
// }

const axiosInstance = axios.create();

// 请求 request 拦截器，在这里，我们给每个请求都加 sessionId
axiosInstance.interceptors.request.use(request => {

  const { userInfo } = useCustomStore();
  request.headers["autn-sjw-token"] = `${userInfo?.token || ''}`;
  return request;

}, error => Promise.reject(error));


// 响应 response 拦截器
axiosInstance.interceptors.response.use(response => {

  if (response.status === 200) {

    const { code = 9686, msg = "接口返回空白" } = response.data || {};

    if (code === 9686 || code !== 0) {
      ElMessage({ showClose: true, message: msg, type: 'error' });
      // 登录失效/鉴权失败
      if (code === 1600) router.replace('/login');
      return false
    }

    return response.data;

  } else {

    ElMessage({ showClose: true, message: errorMsg, type: 'error' });
    return false

  }

}, error => Promise.reject(error));


export const httpGet = async (url: string, params = {}, headers?: object) => await axiosInstance.get(url, { params, headers });
export const httpPost = async (url: string, data = {}, headers?: object) => await axiosInstance.post(url, data, { headers });
export const httpPut = async (url: string, data = {}, headers?: object) => await axiosInstance.put(url, data, { headers });
export const httpDelete = async (url: string, params = {}, headers?: object) => await axiosInstance.delete(url, { params, headers });






