import { httpGet, httpPost, httpPut } from "./axios"

interface ReqLogin {
  phone?: string,
  passWord?: string,
  passWordMd5?: string
}

// 登录
export const reqPostLogin = (params: ReqLogin) => httpPost('/login', params);

// 获取个人信息
export const reqGetUserInfoDetail = () => httpGet('/userInfo')

// 修改个人信息
export const reqPutUserInfoUpdata = (params: any) => httpPut('/updata', params)

// 修改密码
export const reqPutUpdataPass = (params: any) => httpPut('/updata/pass', params)

// 退出
export default () => httpGet('/logout');



