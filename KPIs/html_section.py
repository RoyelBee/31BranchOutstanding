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

all_table = """ <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <style>
                                            table
                                            {   
                                                width: 796px;
                                                border-collapse: collapse;
                                                border: 1px solid gray;
                                                padding: 5px;
                                            }
                                            td{
                                                padding-top: 5px;
                                                border-bottom: 1px solid #ddd;
                                                text-align: left;
                                                white-space: nowrap;
                                                border: 1px solid gray;
                                                text-align: justify;
                                                text-justify: inter-word;

                                            }
                                            th{
                                                padding: 2px;
                                                border: 1px solid gray;
                                                font-size: 10px !important;
                                                text-align:left;
                                                white-space: nowrap;
                                                text-align: justify;
                                                text-justify: inter-word;

                                            }
                                            th.table30tr{
                                                font-size:15px !important;
                                                height: 24px !important;
                                                background-color: brown;
                                                color: white;
                                                text-align: left;
                                                white-space: nowrap;
                                            }

                                            th.unit{

                                                background-color: #5ef28d;
                                                width:22px;
                                                font-size: 10px;
                                                white-space: nowrap;
                                                text-align: justify;
                                                text-justify: inter-word;

                                            }
                                            td.idcol{
                                                text-align: right;
                                                background-color: #efedf2;
                                                white-space: nowrap;
                                                font-size: 9px;
                                                text-justify: inter-word;
                                            }
                                            td.unit{
                                                background-color: #efedf2;
                                                white-space: nowrap;
                                                font-size: 9px;
                                                text-align: justify;
                                                text-justify: inter-word;

                                            }
                                            tr:hover {
                                                background-color:#f5f5f5;
                                            }
                                        </style>
                                    <title>Mail</title>
                                </head>
                                <body>
                                <h3 style='text-align:left'> Top 20 Closed to Mature Credit</h3>
                                <table>
                                    <p style="text-align:left"> """ + get_html_table() + """</p>
                                </table>

                                <h3 style='text-align:left'> Top 20 Aging Mature Credit</h3>
                                <table>
                                    <p style="text-align:left"> """ + get_html_table1() + """</p>
                                </table>

                                 <h3 style='text-align:left'> Top 20 Cash Drop Credit</h3>
                                <table>
                                    <p style="text-align:left"> """ + get_html_table2() + """</p>
                                </table>
                                </body>
                                </html>
                                """
