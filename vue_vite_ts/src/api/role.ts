import { httpDelete, httpGet, httpPost, httpPut } from "./axios"

// 创建角色
export const reqRoleInsert = (params = {}) => httpPost('/role/insert', params);

// 删除角色
export const reqDeleteRoleDelete = (params = {}) => httpDelete('/role/delete', params)

// 编辑角色
export const reqPutRoleUpdata = (params = {}) => httpPut('/role/updata', params)

// 查询角色
export const reqGetRoleList = (params = {}) => httpGet('/role/list', params);

// 角色详情
export const reqGetRoleDetail = (params = {}) => httpGet('/role/detail', params);



