# excel的操作，读、写
# 导入包
import os
import xlrd     # 读
import xlwt     # 写
import xlutils.copy     # 读和写


class ExcelPrac(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.work_book = xlrd.open_workbook(self.file_path)  # 打开excel

    # 读取excel中信息
    def read_data(self, sheet_name):
        sheet = self.work_book.sheet_by_name(sheet_name)    # 按sheet名打开
        # sheet = self.work_book.sheet_by_index(0)       # 按索引打开sheet页
        sheet_names = self.work_book.sheet_names()         # 获取所有sheet页的名称列表
        row_nums = sheet.nrows      # 获取该sheet页的总行数
        col_num = sheet.ncols       # 获取该sheet页的总列数
        row_values = sheet.row_values(1)     # 获取整行数据
        col_values = sheet.col_values(1)     # 获取指定列数据的列表
        cell_value = sheet.cell_value(2, 1)              # 获取指定单元格的值
        cell_value1 = sheet.cell(2, 1).value             # 获取指定单元格的值
        print('行数：{}，列数：{}，行值：{}'.format(row_nums, col_num, row_values))
        print('所有sheet也名称为：{}'.format(sheet_names))
        print('指定单元格的值为：{} 和 {}'.format(cell_value, cell_value1))
        print('指定列值为：{}'.format(col_values))

    def write_data(self,):
        # read_book = xlrd.open_workbook(self.file_path)       # 读取excel中的所有数据
        write_book = xlutils.copy.copy(self.work_book)        # 赋值excel对象
        write_sheet = write_book.get_sheet(0)           # 获取复制对象的sheet页
        try:
            write_sheet.write(2, 4, '你猜')                # 在指定单元格写入内容
        except Exception as msg:
            print(msg)
        write_book.save(file_path)                         # 保存


if __name__ == '__main__':
    file_path = os.path.dirname(os.path.abspath(__file__)) + '\\' + 'data.xlsx'
    print(file_path)
    r = ExcelPrac(file_path)
    r.read_data('Sheet1')
    # w = ExcelPrac(file_path)
    # w.write_data()
