import Functions.helper_functions as func
import xlrd


def get_html_table():
    xl = xlrd.open_workbook('./Data/ClosedToMaturedTable.xlsx')
    sh = xl.sheet_by_name('Sheet1')

    th = ""
    td = ""
    for i in range(0, 1):
        th = th + "<tr>\n"
        th = th + "<th class=\"unit\">ID</th>"
        for j in range(1, sh.ncols):
            th = th + "<th class=\"unit\" >" + str(sh.cell_value(i, j)) + "</th>\n"
        th = th + "</tr>\n"

    for i in range(1, sh.nrows):
        td = td + "<tr>\n"
        td = td + "<td class=\"idcol\">" + str(i) + "</td>"
        for j in range(1, 2):
            td = td + "<td class=\"idcol\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(2, 7):
            td = td + "<td class=\"unit\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(7, sh.ncols):
            td = td + "<td class=\"idcol\">" + func.get_value(str(int(sh.cell_value(i, j)))) + "</td>\n"
        td = td + "</tr>\n"
    html = th + td
    return html
def get_html_table1():
    xl = xlrd.open_workbook('./Data/AgingMaturedTable.xlsx')
    sh = xl.sheet_by_name('Sheet1')

    th = ""
    td = ""
    for i in range(0, 1):
        th = th + "<tr>\n"
        th = th + "<th class=\"unit\">ID</th>"
        for j in range(1, sh.ncols):
            th = th + "<th class=\"unit\" >" + str(sh.cell_value(i, j)) + "</th>\n"
        th = th + "</tr>\n"

    for i in range(1, sh.nrows):
        td = td + "<tr>\n"
        td = td + "<td class=\"idcol\">" + str(i) + "</td>"
        for j in range(1, 2):
            td = td + "<td class=\"idcol\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(2, 7):
            td = td + "<td class=\"unit\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(7, sh.ncols):
            td = td + "<td class=\"idcol\">" + func.get_value(str(int(sh.cell_value(i, j)))) + "</td>\n"
        td = td + "</tr>\n"
    html = th + td
    return html
def get_html_table2():
    xl = xlrd.open_workbook('./Data/CashDropTable.xlsx')
    sh = xl.sheet_by_name('Sheet1')
    th = ""
    td = ""
    for i in range(0, 1):
        th = th + "<tr>\n"
        th = th + "<th class=\"unit\">ID</th>"
        for j in range(1, sh.ncols):
            th = th + "<th class=\"unit\" >" + str(sh.cell_value(i, j)) + "</th>\n"
        th = th + "</tr>\n"

    for i in range(1, sh.nrows):
        td = td + "<tr>\n"
        td = td + "<td class=\"idcol\">" + str(i) + "</td>"
        for j in range(1, 2):
            td = td + "<td class=\"idcol\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(2, 7):
            td = td + "<td class=\"unit\">" + str(sh.cell_value(i, j)) + "</td>\n"
        for j in range(7, sh.ncols):
            td = td + "<td class=\"idcol\">" + func.get_value(str(int(sh.cell_value(i, j)))) + "</td>\n"
        td = td + "</tr>\n"
    html = th + td
    return html


