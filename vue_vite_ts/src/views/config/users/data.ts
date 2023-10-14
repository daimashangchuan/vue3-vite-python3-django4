
import {
  tableColumnEmptyFormatter,
  tableColumnTimeFormatter,
  tableColumnRegionFormatter,
  tableColumnStatusFormatter
} from "../../../utils"


// 账号列表标题
export const columnList = [
  { label: "账号", prop: "phone", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  { label: "姓名", prop: "name", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  { label: "性别", prop: "gender", formatter: (_: any, __: any, cellValue: any) => tableColumnStatusFormatter('gender', cellValue) },
  { label: "年龄", prop: "age", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  { label: "省市区", prop: "region", formatter: (_: any, __: any, cellValue: any) => tableColumnRegionFormatter(cellValue) },
  { label: "详细地址", prop: "address", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  {
    label: "角色名称",
    prop: "role",
    formatter: (_: any, __: any, cellValue: any) => cellValue && cellValue.name ? cellValue.name : '--',
  },
  { label: "创建时间", prop: "createTime", formatter: (_: any, __: any, cellValue: any) => tableColumnTimeFormatter(cellValue) },
  { label: "最后修改时间", prop: "updataTime", formatter: (_: any, __: any, cellValue: any) => tableColumnTimeFormatter(cellValue) },
];



