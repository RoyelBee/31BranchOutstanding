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


def sector_wise_non_matured_credit(branch_name):
    sector_credit_df = pd.read_sql_query(""" Select case when MAINCUSTYPE='RETAIL' then 'Retail' else 'Institute' end  as CustType,Sum(OUT_NET) as Amount from
                        (select INVNUMBER,INVDATE,
                        CUSTOMER,TERMS,MAINCUSTYPE,
                        CustomerInformation.CREDIT_LIMIT_DAYS,
                        datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
                        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation
                        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                        where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash') as TblCredit
                        where Days_Diff<=0
                        group by case when MAINCUSTYPE='RETAIL' then 'Retail' else 'Institute' end""", func.con,
                                         params={branch_name})


    Institution = int(sector_credit_df.Amount.iloc[0])
    retail = int(sector_credit_df.Amount.iloc[1])

    values = [Institution, retail]

    colors = ['#e1052f', '#00cd6b']

    legend_element = [Patch(facecolor='#e1052f', label='Institution'),
                      Patch(facecolor='#00cd6b', label='Retail')]

    sector_total_credit = Institution + retail
    sector_total_credit = "Total \n" + func.joker(sector_total_credit)

    Institution = func.joker(Institution)
    retail = func.joker(retail)
    DataLabel = [Institution, retail]
    fig1, ax = plt.subplots()
    wedges, labels, autopct = ax.pie(values, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=120,
                                     pctdistance=.7)
    plt.setp(autopct, fontsize=14, color='black', fontweight='bold')
    plt.setp(labels, fontsize=14, fontweight='bold')
    ax.text(0, -.1, sector_total_credit, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#00daff')

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.50, fc='white')

    fig = plt.gcf()

    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('5. Non-Matured Credit', fontsize=16, fontweight='bold', color='#3e0a75')

    ax.axis('equal')
    plt.legend(handles=legend_element, loc='lower left', fontsize=11)
    plt.tight_layout()
    plt.savefig('./Images/regular_credit.png')
    plt.close()
    print('5. Sector wise Non Mature Credit- Regular Generated')
