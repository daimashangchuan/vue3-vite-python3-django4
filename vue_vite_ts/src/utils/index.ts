import { codeToText } from "element-china-area-data";
import { genderList } from "../components/data"
import dayjs from "dayjs";
const modules = import.meta.glob("../views/**/**.vue")

// 初始化路由
export const initRouterList = (data: any) => {
  const list = Array.isArray(data) ? JSON.parse(JSON.stringify(data)) : [];
  return (list || []).map((item: any) => {

    const meta = { title: item.title, permissionPath: item.permissionPath };
    const component = modules[`${item.component}`];

    if (item.children && item.children.length > 0) {
      return { ...item, meta, children: initRouterList(item.children), component }
    }

    return { ...item, meta, component }
  });
};


// 初始化权限列表
export const initPermissionList = (data: any) => {
  const list = Array.isArray(data) ? JSON.parse(JSON.stringify(data)) : [];
  return (list || []).reduce((pre: any, item: any) => {
    if (item.isPermission === 1) {
      const newItem = { ...item };
      if (newItem.children) {
        newItem.children = initPermissionList(newItem.children);
      }
      pre.push(newItem);
    }
    return pre;
  }, []);
};


// 获取包含权限的所有路由
export const getPathList = (data: any, paths: any, includeChildren = true) => {
  const list = JSON.parse(JSON.stringify(data))
  return list.reduce((result: any, item: any) => {
    if (paths.includes(item.permissionPath)) {
      if (includeChildren && item.children) {
        const filteredChildren = getPathList(item.children, paths, includeChildren);
        if (filteredChildren.length > 0) {
          const newItem = { ...item, children: filteredChildren };
          result.push(newItem);
        } else {
          result.push(item);
        }
      } else {
        result.push(item);
      }
    } else if (includeChildren && item.children) {
      const filteredChildren = getPathList(item.children, paths, includeChildren);
      if (filteredChildren.length > 0) {
        const newItem = { ...item, children: filteredChildren };
        result.push(newItem);
      }
    }

    return result;
  }, []);
}

// 修改list数组，存在修改  不存在新增
export const getUpdataList = (list: any, data: any, contrast = 'id') => {
  list = JSON.parse(JSON.stringify(list))
  const existingIndex = list.findIndex((item: any) => item[contrast] === data[contrast]);
  if (existingIndex !== -1) {
    list[existingIndex] = data;
  } else {
    list.push(data);
  }
  return list
}


// table的column 为空 格式化
export const tableColumnEmptyFormatter = (cellValue: any) => {
  return cellValue || '--';
}

// 获取省市区 状态转文字
export const tableColumnRegionFormatter = (cellValue: any) => {
  const region: any[] = cellValue ? cellValue.split(',') : null;
  return region ? `${codeToText[region[0]]}/${codeToText[region[1]]}/${codeToText[region[2]]}` : '--';
}

// table的column的状态 格式化  gender性别
export const tableColumnStatusFormatter = (type = 'status', cellValue: any) => {
  const list = type === 'gender' ? genderList : []
  const data = list.find(item => item.id === cellValue)
  return data?.name || '--'
}

// table的column 时间 格式化
export const tableColumnTimeFormatter = (cellValue: any) => {
  return cellValue ? dayjs(cellValue).format('YYYY-MM-DD HH:mm:ss') : '--'
}



















