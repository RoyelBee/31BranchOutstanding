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


def generate_all_return_info(branch_name):
    left, width = 0.0, .19
    bottom, height = .5, 1
    right = left + width
    top = 1
    fig = plt.figure(figsize=(16, 4))
    ax = fig.add_axes([0, 0, 1, 1])
    # ---------- Remove border from the figures  ------------------
    for item in [fig, ax]:
        item.patch.set_visible(False)
    fig.patch.set_visible(False)
    ax.axis('off')
    # -------------------------------------------------------------
    p = patches.Rectangle(
        (left, bottom), width, height,
        color='#fcea17'
    )
    ax.add_patch(p)

    # -------- Last Day Return  ----------------------------------------------
    lastDaySales = pd.read_sql_query("""
                            select  isnull(Sum(EXTINVMISC),0) as  LastDaySales from OESalesDetails
                            where TRANSDATE = convert(varchar(8),DATEADD(D,0,GETDATE()-1),112)
                            and AUDTORG like ?
                                            """, func.con, params={branch_name})

    LastDayReturn = pd.read_sql_query("""
                            select ISNULL(sum(EXTINVMISC), 0) as ReturnAmount from OESalesDetails
                            where AUDTORG like ? and transtype<>1 and PRICELIST <> 0 and
                            (TRANSDATE = convert(varchar(8),DATEADD(D,0,GETDATE()-1),112))
                             """, func.con, params={branch_name})

    ld_sales = int(lastDaySales['LastDaySales'])
    ld_return = float(LastDayReturn['ReturnAmount'])
    l_retn = abs(ld_return)
    ret1 = float((l_retn / ld_sales) * 100)
    return_p = '%.2f' % (ret1)
    return_p = str(return_p) + '%'
    kpi_label = 'LD' + "\n"
    ax.text(.5 * (left + right), .5 * (bottom + top), kpi_label,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=24, color='black',
            transform=ax.transAxes)

    ax.text(.5 * (left + right), .4 * (bottom + top), return_p,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=34, color='red',
            transform=ax.transAxes)
    # print('Last Day Return Added')
    # --------------------  Monthly  Return  Box --------------------------------
    left, width = .20, .19
    bottom, height = .5, .5
    right = left + width
    top = 1
    p = patches.Rectangle(
        (left, bottom), width, height,
        color='#fcea17'
    )
    ax.add_patch(p)
    monthly_sales = pd.read_sql_query(""" Declare @monthStartDay NVARCHAR(MAX);
                            Declare @monthCurrentDay NVARCHAR(MAX);
                            SET @monthStartDay = convert(varchar(8),DATEADD(month, DATEDIFF(month, 0,  GETDATE()), 0),112)
                            set @monthCurrentDay = convert(varchar(8),DATEADD(D,0,GETDATE()),112);
                            select  isnull(Sum(EXTINVMISC),0) as  MTDSales from OESalesDetails
                            where TRANSDATE between  @monthStartDay and @monthCurrentDay
                            and AUDTORG like ?
                            """, func.con, params={branch_name})

    monthly_return_df = pd.read_sql_query("""select ISNULL(sum(EXTINVMISC), 0) as ReturnAmount from OESalesDetails
                    where AUDTORG like ? and transtype<>1 and PRICELIST <> 0 and
                    (TRANSDATE between
                    (convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112))
                    and (convert(varchar(8),DATEADD(D,0,GETDATE()),112)))
                                """, func.con, params={branch_name})

    monthly_return = float(monthly_return_df['ReturnAmount'])
    m_sales = int(monthly_sales['MTDSales'])
    retn = abs(monthly_return)
    ret1 = float((retn / m_sales) * 100)
    return_p = '%.2f' % (ret1)
    return_p = str(return_p) + '%'
    kpi_label = 'MTD' + "\n"

    ax.text(.5 * (left + right), .5 * (bottom + top), kpi_label,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=24, color='black',
            transform=ax.transAxes)

    ax.text(.5 * (left + right), .4 * (bottom + top), return_p,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=34, color='red',
            transform=ax.transAxes)

    # print('MTD Return Added')
    # # ---------- Yearly return Box ------------------------
    yearly_sales = pd.read_sql_query("""
                        select  isnull(Sum(EXTINVMISC),0) as  YTDSales from OESalesDetails
                        where AUDTORG like ? AND TRANSDATE>= (convert(varchar(8),DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0),112))
                        """, func.con, params={branch_name})

    yearly_return = pd.read_sql_query("""
                              select isnull(sum(EXTINVMISC),0) as ReturnAmount from OESalesDetails where
                            AUDTORG like ? and
                            transtype<>1 and PRICELIST <> 0 and
                            (TRANSDATE between (convert(varchar(8),DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0),112))
                            and (convert(varchar(8),DATEADD(D,0,GETDATE()),112)))
             """, func.con, params={branch_name})

    left, width = .40, .19
    bottom, height = .5, .5
    right = left + width
    top = 1
    y_sales = int(yearly_sales['YTDSales'])
    yearly_return_amount = int(yearly_return['ReturnAmount'])
    return_amount = abs(yearly_return_amount)
    return_p = float((return_amount / y_sales) * 100)
    return_p = '%.2f' % (return_p)
    return_p = str(return_p) + '%'

    p = patches.Rectangle(
        (left, bottom), width, height,
        color='#fcea17'
    )
    ax.add_patch(p)
    kpi_label = 'YTD' + "\n"

    ax.text(.5 * (left + right), .5 * (bottom + top), kpi_label,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=24, color='black',
            transform=ax.transAxes)

    ax.text(.5 * (left + right), .4 * (bottom + top), return_p,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=34, color='red',
            transform=ax.transAxes)
    # print('YTD Return Added')

    # # ---------- YAGO MTD  Return Box ------------------------
    yago_monthly_sales = pd.read_sql_query("""Declare @YagoMonthStartDay NVARCHAR(MAX);
                            Declare @YagomonthCurrentDay NVARCHAR(MAX);
                            SET @YagoMonthStartDay = convert(varchar(6), DATEFROMPARTS ( DATEPART(yyyy, GETDATE()) - 1, 1, 1 ), 112)
                            set @YagomonthCurrentDay = convert(varchar(8), DATEADD(year, -1, GETDATE()), 112)
                            select  Sum(EXTINVMISC) as  MTDSales from OESalesDetails
                            where TRANSDATE between  @YagoMonthStartDay and @YagomonthCurrentDay
                            and AUDTORG like ?
                             """, func.con, params={branch_name})

    yago_monthly_return_df = pd.read_sql_query("""select ISNULL(sum(EXTINVMISC), 0) as ReturnAmount from OESalesDetails
            where AUDTORG like ? and transtype<>1 and PRICELIST <> 0 and
            transdate between (convert(varchar(6), DATEFROMPARTS ( DATEPART(yyyy, GETDATE()) - 1, 1, 1 ), 112))
            and (convert(varchar(8), DATEADD(year, -1, GETDATE()), 112))
                                """, func.con, params={branch_name})

    monthly_return = float(yago_monthly_return_df['ReturnAmount'])
    m_sales = int(yago_monthly_sales['MTDSales'])
    left, width = .60, .19
    bottom, height = .5, .5
    right = left + width
    top = 1
    p = patches.Rectangle(
        (left, bottom), width, height,
        color='#fc8b17'
    )
    ax.add_patch(p)
    retn = abs(monthly_return)
    ret1 = float((retn / m_sales) * 100)
    return_p = '%.2f' % (ret1)
    return_p = str(return_p) + '%'
    kpi_label = 'YAGO MTD' + "\n"

    ax.text(.5 * (left + right), .5 * (bottom + top), kpi_label,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=24, color='black',
            transform=ax.transAxes)

    ax.text(.5 * (left + right), .4 * (bottom + top), return_p,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=34, color='black',
            transform=ax.transAxes)

    # print('YAGO MTD Return Added')
    # # # ---------- YAGO YTD Return  Box ------------------------
    yago_yearly_sales = pd.read_sql_query("""
                            select  isnull(Sum(EXTINVMISC),0) as  YTDSales from OESalesDetails
                            where AUDTORG like ? AND TRANSDATE between (convert(varchar(8), DATEFROMPARTS ( DATEPART(yyyy, GETDATE()) - 1, 1, 1 ), 112))
                            and (convert(varchar(8), DATEADD(year, -1, GETDATE()), 112))
                            """, func.con, params={branch_name})

    yago_yearly_return = pd.read_sql_query("""
                            select isnull(sum(EXTINVMISC),0) as ReturnAmount from OESalesDetails where
                            AUDTORG like ? and
                            transtype<>1 and PRICELIST <> 0 and
                            (TRANSDATE between (convert(varchar(8), DATEFROMPARTS ( DATEPART(yyyy, GETDATE()) - 1, 1, 1 ), 112))
                            and (convert(varchar(8), DATEADD(year, -1, GETDATE()), 112)))
                            """, func.con, params={branch_name})

    left, width = .80, .20
    bottom, height = .5, .5
    right = left + width
    top = 1
    y_sales = int(yago_yearly_sales['YTDSales'])
    yearly_return_amount = int(yago_yearly_return['ReturnAmount'])
    return_amount = abs(yearly_return_amount)
    return_p = float((return_amount / y_sales) * 100)
    return_p = '%.2f' % (return_p)
    return_p = str(return_p) + '%'

    p = patches.Rectangle(
        (left, bottom), width, height,
        color='#fc8b17'
    )
    ax.add_patch(p)
    kpi_label = 'YAGO YTD' + "\n"

    ax.text(.5 * (left + right), .5 * (bottom + top), kpi_label,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=24, color='black',
            transform=ax.transAxes)

    ax.text(.5 * (left + right), .4 * (bottom + top), return_p,
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=34, color='black',
            transform=ax.transAxes)

    # plt.tight_layout()
    plt.savefig('./Images/return.png')
    dirpath = os.path.dirname(os.path.realpath(__file__))
    im = Image.open('./Images/return.png')
    left = 0
    top = 0
    right = 1600
    bottom = 200
    im1 = im.crop((left, top, right, bottom))
    im1.save('./Images/return.png')
    # print('Return Generated ')

    # # Join Title and Results
    title_img = Image.open("./Images/return_text.png")
    return_img = Image.open("./Images/return.png")
    dst = Image.new('RGB', (1602, 301))
    dst.paste(title_img, (0, 0))
    dst.paste(return_img, (1, title_img.height))
    dst.save('./Images/main_return.png')
    print('All Return KPI generated')
