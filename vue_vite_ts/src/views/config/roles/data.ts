
import { tableColumnEmptyFormatter, tableColumnTimeFormatter } from "../../../utils"


export const columnList = [
  { label: "角色名称", prop: "name", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  { label: "角色说明", prop: "detail", formatter: (_: any, __: any, cellValue: any) => tableColumnEmptyFormatter(cellValue) },
  { label: "创建时间", prop: "createTime", formatter: (_: any, __: any, cellValue: any) => tableColumnTimeFormatter(cellValue) },
  { label: "最后修改时间", prop: "updataTime", formatter: (_: any, __: any, cellValue: any) => tableColumnTimeFormatter(cellValue) },
];


export const defaultTreeProps = {
  title: 'children',
  label: 'title',
  disabled: 'disabled',
}
