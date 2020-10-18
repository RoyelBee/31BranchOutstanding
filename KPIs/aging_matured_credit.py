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


def aging_matured_credit(branch_name):
    aging_mature_df = pd.read_sql_query("""
                             SELECT  AgingDays, sum(Amount)/1000 as Amount FROM
                            (Select
                            case
                             when TblCredit.Days_Diff between '1' and '3'  THEN '1 - 3 days'
                            when TblCredit.Days_Diff between '4' and '10'  THEN '4 - 10 days'
                            when TblCredit.Days_Diff between '11' and '15'  THEN '11 - 15 days'
                            else '16+ Days' end  as AgingDays,
                            --OUT_NET
                            Sum(OUT_NET) as Amount,
    
                            CASE
                            when TblCredit.Days_Diff between '1' and '3'  THEN 1
                            when TblCredit.Days_Diff between '4' and '10'  THEN 2
                            when TblCredit.Days_Diff between '11' and '15'  THEN 3
                            ELSE  4
                            END AS SERIAL
                            from
                                (select INVNUMBER,INVDATE,
                        CUSTOMER,TERMS,MAINCUSTYPE,
                        CustomerInformation.CREDIT_LIMIT_DAYS,
                        (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
                        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation
                        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                        where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash' ) as TblCredit
                        where Days_Diff>0
    
                                group by
                                    case
                             when TblCredit.Days_Diff between '1' and '3'  THEN '1 - 3 days'
                            when TblCredit.Days_Diff between '4' and '10'  THEN '4 - 10 days'
                            when TblCredit.Days_Diff between '11' and '15'  THEN '11 - 15 days'
                                         else '16+ Days' end,
                                    CASE
                            when TblCredit.Days_Diff between '1' and '3'  THEN 1
                            when TblCredit.Days_Diff between '4' and '10'  THEN 2
                            when TblCredit.Days_Diff between '11' and '15'  THEN 3
                            ELSE  4 END ) AS T1
                            group by T1.AgingDays, SERIAL
                            order by SERIAL
                                                """, func.con, params={branch_name})

    width = 0.75
    AgingDays = aging_mature_df['AgingDays']
    y_pos = np.arange(len(AgingDays))
    performance = aging_mature_df['Amount']
    aging_total = sum(performance)
    fig, ax = plt.subplots()
    colors = ['#2c8e14', '#deff00', '#ff6500', '#f00228']
    bars = plt.bar(y_pos, performance, width, align='center', alpha=1, color=colors)
    maf_kor2 = max(performance)

    def autolabel(bars):
        # attach some text labels
        for rect in bars:
            height = int(rect.get_height())
            ax.text(rect.get_x() + rect.get_width() / 2., .995 * height,
                    func.for_bar(height), ha='center', va='bottom', fontsize=12, rotation=45, fontweight='bold')

    autolabel(bars)

    def autolabel3(bars):
        for bar in bars:
            height = int(bar.get_height())
            ax.text(bar.get_x() + bar.get_width() / 2., .5 * height,
                    str(round(((height / aging_total) * 100), 1)) + "%",
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

    autolabel3(bars)

    plt.xticks(y_pos, AgingDays, fontsize=12)
    # plt.yticks(fontsize=12)
    plt.yticks(np.arange(0, maf_kor2 + (.6 * maf_kor2), maf_kor2 / 5), fontsize=12)
    plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
    plt.ylabel('Amount', color='black', fontsize=14, fontweight='bold')
    plt.title('4. Matured Credit Age', color='#3e0a75', fontweight='bold', fontsize=16)
    plt.tight_layout()
    plt.savefig('./Images/aging_matured_credit.png')
    plt.close()
    print('4. Aging Mature Credit Generated')
