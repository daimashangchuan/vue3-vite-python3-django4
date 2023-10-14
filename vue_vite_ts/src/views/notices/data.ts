
import { tableColumnEmptyFormatter, tableColumnTimeFormatter } from "../../utils"

// 账号列表标题
export const columnList = [
  { label: "通知标题", prop: "title", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  { label: "通知详情", prop: "detail", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  { label: "创建时间", prop: "createTime", formatter: (_: any, __: any, cellValue: any) => tableColumnTimeFormatter(cellValue) },
  { label: "最后修改时间", prop: "updataTime", formatter: (_: any, __: any, cellValue: any) => tableColumnTimeFormatter(cellValue) },
];



