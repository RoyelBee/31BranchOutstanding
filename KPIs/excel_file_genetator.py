
import matplotlib.pyplot as plt
import pandas as pd
import os

dirpath = os.path.dirname(os.path.realpath(__file__))

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from math import log, floor
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc as db
import xlrd
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime as dd
from PIL import Image
from datetime import datetime

import Functions.helper_functions as func


def closed_to_matured_data(branch_name):
    ClosedToMaturedcredit_df = pd.read_sql_query("""select CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',
           CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',INVNUMBER as 'Inv Number',
           convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date', CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
           (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)*-1 as 'Matured In Days', OUT_NET as 'Credit Amount'
           from [ARCOUT].dbo.[CUST_OUT]
           join ARCHIVESKF.dbo.CustomerInformation
           on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
    
           where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash'
               and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)  between -3 and 0
               order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)desc
               , OUT_NET desc
    
            """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/ClosedToMatured.xlsx', engine='xlsxwriter')
    ClosedToMaturedcredit_df.index = np.arange(1, len(ClosedToMaturedcredit_df) + 1)
    ClosedToMaturedcredit_df.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook = writer.book

    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)

    writer.save()
    print('Closed to Matured : Excel Created')


def colsed_to_matured_mail_data(branch_name):
    ClosedToMaturedcredittable = pd.read_sql_query("""
              select top 20 CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',
            CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',INVNUMBER as 'Inv Number',
            convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date', CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)*-1 as 'Matured In Days', OUT_NET as 'Credit Amount'
            from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

            where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash'
                and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)  between -3 and 0
                order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)desc
                , OUT_NET desc
                           """, func.con, params={branch_name})
    writer = pd.ExcelWriter('./Data/ClosedToMaturedTable.xlsx', engine='xlsxwriter')
    ClosedToMaturedcredittable.index = np.arange(1, len(ClosedToMaturedcredittable) + 1)
    ClosedToMaturedcredittable.to_excel(writer, sheet_name='Sheet1', index=True)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)

    writer.save()
    print('Closed to Matured Mail Table  : Excel Created')

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

def aging_matured_data(branch_name):
    AgeingMaturedcredit_df = pd.read_sql_query("""
                           select CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',
                            INVNUMBER as 'Inv Number', convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date',
                             CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
                            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as 'Days Passed',OUT_NET as 'Credit Amount'

                            from [ARCOUT].dbo.[CUST_OUT]
                            join ARCHIVESKF.dbo.CustomerInformation
                            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

                            where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash' and OUT_NET>1
                            and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) >= 1
                            order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) desc
                                            , OUT_NET desc
                             """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/AgingMatured.xlsx', engine='xlsxwriter')
    AgeingMaturedcredit_df.index = np.arange(1, len(AgeingMaturedcredit_df) + 1)
    AgeingMaturedcredit_df.to_excel(writer, sheet_name='Sheet1', index=True)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)
    writer.save()
    print('Aging Matured : Excel Created')

def aging_matured_table(branch_name):
    AgeingMaturedcredittable = pd.read_sql_query("""
                           select top 20 CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',
                             INVNUMBER as 'Inv Number', convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date',
                             CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
                            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as 'Days Passed'
                            ,OUT_NET as 'Credit Amount'
                            from [ARCOUT].dbo.[CUST_OUT]
                            join ARCHIVESKF.dbo.CustomerInformation
                            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

                            where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash' and OUT_NET>1
                            and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) >= 1
                            order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) desc
                             , OUT_NET desc
                            """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/AgingMaturedTable.xlsx', engine='xlsxwriter')
    AgeingMaturedcredittable.index = np.arange(1, len(AgeingMaturedcredittable) + 1)
    AgeingMaturedcredittable.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    writer.save()

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

def cash_drop_data(branch_name):
    CashDrop_df = pd.read_sql_query("""
                         Select CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',
                         INVNUMBER as 'Inv Number',convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date',
                        datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as 'Days Over', OUT_NET as 'Credit Amount'
                        from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation
                        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

                        where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS='Cash'  and OUT_NET>1
                        and (datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1) >=4
                        order by datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 desc
                          , OUT_NET desc
                         """, func.con, params={branch_name})

    writer = pd.ExcelWriter('CashDrop.xlsx', engine='xlsxwriter')
    CashDrop_df.index = np.arange(1, len(CashDrop_df) + 1)
    CashDrop_df.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)
    writer.save()
    print('Cash Drop : Excel Created')