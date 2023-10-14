import { httpDelete, httpGet, httpPost, httpPut } from "./axios"

// 创建通知
export const reqNoticeInsert = (params = {}) => httpPost('/notice/insert', params);

// 删除通知
export const reqDeleteNoticeDelete = (params = {}) => httpDelete('/notice/delete', params)

// 编辑通知
export const reqPutNoticeUpdata = (params = {}) => httpPut('/notice/updata', params)

// 查询通知
export const reqGetNoticeList = (params = {}) => httpGet('/notice/list', params);



