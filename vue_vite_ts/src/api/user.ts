import { httpDelete, httpGet, httpPost, httpPut } from "./axios"

// 创建用户
export const reqUserInsert = (params = {}) => httpPost('/user/insert', params);

// 删除用户
export const reqDeleteUserDelete = (params = {}) => httpDelete('/user/delete', params)

// 编辑用户
export const reqPutUserUpdata = (params = {}) => httpPut('/user/updata', params)

// 查询用户
export const reqGetUserList = (params = {}) => httpGet('/user/list', params);

// 用户详情
export const reqGetUserDetail = (params = {}) => httpGet('/user/detail', params);



