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


def day_wise_target_sales(branch_name):
    try:
        daily_sales_df = pd.read_sql_query("""select Right(transdate,2) as [day], isnull(Sum(EXTINVMISC),0)/1000 as  EverydaySales from OESalesDetails  
                        where LEFT(TRANSDATE,6) =convert(varchar(6), GETDATE(),112)  and AUDTORG like ?
                        group by transdate
                        order by transdate""", func.con, params={branch_name})

        EveryD_Target_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
                        Declare @DaysInMonth NVARCHAR(MAX);
                        SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                        SET @DaysInMonth = DAY(EOMONTH(GETDATE())) 
                        select ISNULL((Sum(TARGET)/@DaysInMonth), 0) as  YesterdayTarget from TDCL_BranchTarget  
                        where YEARMONTH = @CurrentMonth and AUDTORG like ?""", func.con, params={branch_name})
        totarget = EveryD_Target_df.values
        target_for_target = int(totarget[0, 0])

        Every_day = daily_sales_df['day'].tolist()

        y_pos = np.arange(len(Every_day))

        every_day_sale = daily_sales_df['EverydaySales'].tolist()

        n = 1
        Target = []
        labell = []
        for z in y_pos:
            labell.append(n)
            Target.append(int(target_for_target / 1000))
            n = n + 1

        fig, ax = plt.subplots(figsize=(12.81, 4.8))
        labels = labell

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        rects2 = ax.bar(y_pos, every_day_sale, width, label='Sales')
        maf_kor4 = max(every_day_sale)
        # Add some text for labels, title and custom x-axis tick labels, etc.
        line = ax.plot(Target, color='orange', label='Target')
        plt.yticks(np.arange(0, maf_kor4 + (.8 * maf_kor4), maf_kor4 / 5), fontsize=12)
        ax.set_ylabel('Amount', fontsize='14', color='black', fontweight='bold')
        ax.set_xlabel('Day', fontsize='14', color='black', fontweight='bold')
        ax.set_title('12. MTD Target vs Sales', fontsize=16, fontweight='bold', color='#3e0a75')

        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()


        def autolabel(bars):
            for bar in bars:
                height = int(bar.get_height())
                ax.text(bar.get_x() + bar.get_width() / 2., .995 * height,
                        func.get_value(str(height)) + "K",
                        ha='center', va='bottom', fontsize=12, rotation=45, fontweight='bold')


        autolabel(rects2)

        fig.tight_layout()

        plt.savefig("./Images/Day_Wise_Target_vs_Sales.png")
        print('12. Day Wise Target vs Sales')
        plt.close()
    except:
        print("sorry! 12. Day Wise Target vs Sales cannot be generated")
        plt.figure(figsize=(12.81, 4.8))
        plt.text(0.5, 0.5, str('Sorry! Due to data unavailability, the graph cannot be generated'), fontsize=25,
                 color='red',
                 horizontalalignment='center', verticalalignment='center')
        plt.axis('off')
        plt.savefig("./Images/Day_Wise_Target_vs_Sales.png")
        plt.close()
