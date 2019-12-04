import xlrd
import xlsxwriter

source_file = []
for i in range(1, 208): # 确定文件名规则
    file_name = "F:/xls/948d817b6ecfa0f2016ecfa0f2fb0000/" + str(i) + "_body.xls"
    source_file.append(file_name)
    # print(file_name)
    # print(source_file)
target_file = "F:/xls/test1.xls"

data = []
for i in source_file:
    wb = xlrd.open_workbook(i, formatting_info=True)  # 保留原格式
    for sheet in wb.sheets():
        for rownum in range(sheet.nrows):
            data.append(sheet.row_values(rownum))
print(data)

workbook = xlsxwriter.Workbook(target_file)
worksheet = workbook.add_worksheet()
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.write(i, j, data[i][j])

workbook.close()
