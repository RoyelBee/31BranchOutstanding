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

def cause_wise_teturn(branch_name):
    try:
        cause_wise_return_df = pd.read_sql_query("""select case
                            when Cause_Of_Return_ID = '000'  THEN 'Not Mentioned'
                            when Cause_Of_Return_ID = '005'  THEN 'Product Short'
                            when Cause_Of_Return_ID = '010'  THEN 'Shop Closed'
                            when Cause_Of_Return_ID = '015'  THEN 'Canceled/Cash Short'
                            when Cause_Of_Return_ID = '020'  THEN 'Computer Mistake'
                            when Cause_Of_Return_ID = '025'  THEN 'Next Day Delivery'
                            when Cause_Of_Return_ID = '030'  THEN 'Part Sale'
                            when Cause_Of_Return_ID = '035'  THEN 'Not Ordered'
                            when Cause_Of_Return_ID = '040'  THEN 'Not Delivered'
                            when Cause_Of_Return_ID = '050'  THEN 'Approved Return'
                            when Cause_Of_Return_ID = '065'  THEN 'MSO Mistake'
                            End AS Cause
                            , ISNULL(sum(EXTINVMISC), 0) as ReturnAmount from OESalesDetails
                            where AUDTORG like ? and transtype<>1 and PRICELIST <> 0 and
                            TRANSDATE between
                            (convert(varchar(8),DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0),112))
                            and (convert(varchar(8),DATEADD(D,0,GETDATE()),112))
                            group by Cause_Of_Return_ID""", func.con, params={branch_name})

        Cause_name = cause_wise_return_df['Cause']
        y_pos = np.arange(len(Cause_name))
        Return_amount = abs(cause_wise_return_df['ReturnAmount'])
        Return_amount = Return_amount.values.tolist()

        total = sum(Return_amount)

        for_looping = 0
        new_return_amount = []
        for some_value in Return_amount:
            changed_values = (Return_amount[for_looping] / total) * 100
            new_return_amount.insert(for_looping, changed_values)
            for_looping = for_looping + 1

        color = ['#1ff015', '#418af2', '#f037d9', '#ecc13f', '#e2360a', '#1ff015', '#418af2', '#f037d9', '#ecc13f',
                 '#e2360a']
        width = 0.75

        plt.figure(figsize=(2, 1))
        fig, ax = plt.subplots()
        rects1 = plt.bar(y_pos, new_return_amount, width, align='center', alpha=0.9, color=color)

        def autolabel(bars):
            loop = 0
            for bar in bars:
                show = float((Return_amount[loop] / total) * 100)
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1 * height,
                        '%.2f' % (show) + '%',
                        ha='center', va='bottom', fontsize=12, rotation=45, fontweight='bold')
                loop = loop + 1

        autolabel(rects1)
        plt.xticks(y_pos, Cause_name, fontsize='12', color='black')
        plt.yticks(np.arange(0, 101, 10), color='black', fontsize='12')
        plt.xlabel('Return Cause', fontsize='14', color='black', fontweight='bold')
        plt.ylabel('Return Percentage', fontsize='14', color='black', fontweight='bold')
        plt.title('10. Cause wise Return', color='#3e0a75', fontsize='16', fontweight='bold')
        plt.tight_layout()
        plt.savefig('./Images/Cause_with_return.png')
        plt.close()
        print('10. cause wise return generated')
    except:
        print("sorry! 10. cause wise return cannot be generated")
        plt.figure(figsize=(6.4, 4.8))
        plt.text(0.5, 0.5, str('Sorry! Due to data unavailability, the graph cannot be generated'), fontsize=25,
                 color='red',
                 horizontalalignment='center', verticalalignment='center')
        plt.axis('off')
        # plt.show()
        plt.savefig('./Images/Cause_with_return.png')
        plt.close()
