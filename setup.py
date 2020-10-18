import smtplib
import traceback
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
import os
import KPIs.terms_wise_outstanding as trems_outs
import KPIs.category_wise_credit as cat_credit
import KPIs.matured_credit as m_credit
import KPIs.closed_to_matured_credit as c_m_credit
import KPIs.aging_matured_credit as aging_m_credit
import KPIs.sector_wise_non_mature_credit as sec_non_mature_credit
import KPIs.category_wise_cash_outstanding as cash
import KPIs.aging_cash_drop as cash_drop
import KPIs.join_all_images as fig_join
import KPIs.return_info as return_info
import KPIs.cause_wise_return as cause_return
import KPIs.deliveryman_wise_return as dp_return
import KPIs.day_wise_target_vs_sales as day_target_sales
import KPIs.target_vs_sales as target_sales
import KPIs.cumulative_sales_target as cm_target_sales
import KPIs.excel_file_genetator as data_generator
import Functions.email_finder as email
import KPIs.html_section as html_sec

b_list = ['MIRSKF', 'KHLSKF', 'JESSKF']

for i in range(len(b_list)):

    try:

        import KPIs.banner as banner
        banner.create_banner_fig(b_list[i])
        trems_outs.create_terms_wise_outstanding(b_list[i])  # 1

        cat_credit.category_wise_credit(b_list[i])  # 2
        m_credit.matured_credit(b_list[i])  # 3
        aging_m_credit.aging_matured_credit(b_list[i])  # 4

        sec_non_mature_credit.sector_wise_non_matured_credit(b_list[i])  # 5
        c_m_credit.closed_matured_credit(b_list[i])  # 6
        cash.cash_outstanding(b_list[i])  # 7

        cash_drop.aging_cash_drop(b_list[i])  # 8
        dp_return.dp_man_wise_return(b_list[i])  # 9zss
        cause_return.cause_wise_teturn(b_list[i])  # 10

        target_sales.target_sales(b_list[i])  # 11
        day_target_sales.day_wise_target_sales(b_list[i])  # 11
        cm_target_sales.cumulative_sales_target(b_list[i])  # 12
        fig_join.join_all_images()

        return_info.generate_all_return_info(b_list[i])

        data_generator.closed_to_matured_data(b_list[i])
        data_generator.colsed_to_matured_mail_data(b_list[i])
        data_generator.aging_matured_data(b_list[i])

        data_generator.aging_matured_table(b_list[i])
        data_generator.cash_drop_data(b_list[i])
        data_generator.cashdrop_table(b_list[i])


        html_sec.get_html_table()
        html_sec.get_html_table2()
        html_sec.get_html_table2()
        all_table = html_sec.all_table


        msgRoot = MIMEMultipart('related')
        me = 'erp-bi.service@transcombd.com'

        mail = email.find_to_email(b_list[i])
        to = [mail, '']
        cc = ['', '']
        bcc = ['', '']
        recipient = to + cc + bcc

        # # ------------ Group email --------------------
        subject = "SK+F Formulation Reports - "
        email_server_host = 'mail.transcombd.com'
        port = 25

        msgRoot['From'] = me
        msgRoot['To'] = ', '.join(to)
        msgRoot['Cc'] = ', '.join(cc)
        msgRoot['Bcc'] = ', '.join(bcc)
        msgRoot['Subject'] = subject

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        msgText = MIMEText("""
                <img src="cid:banner" height='230' width='796'> <br>
               <img src="cid:all_credit"  width='796'><br>
               <img src="cid:all_Matured_credit"  width='796'> <br>
               <img src="cid:all_regular_credit"  width='796'> <br>
               <img src="cid:all_cash"  width='796'> <br>
               <img src="cid:main_return" width='796'> <br>

               <img src="cid:delivery_mans_return_with_cause"  width='796'><br>
                <img src="cid:return_with_cause"  width='796'><br>
               <img src="cid:day_wise_sales_target"  width='796'><br>
               <img src="cid:cumulative_day_wise_sales_target"  width='796'><br>

               """ + all_table + """

                <br>
                <img src="cid:logoo" height='70' width='150'> <br>
               <i><font color="blue">****This is a system generated report ****</i></font>""",
                           'html')

        msgAlternative.attach(msgText)

        # --------- Set Credit image in mail   -----------------------
        fp = open('./Images/banner_ai.png', 'rb')
        banner = MIMEImage(fp.read())
        fp.close()

        banner.add_header('Content-ID', '<banner>')
        msgRoot.attach(banner)

        # --------- Set Credit image in mail   -------------------------
        fp = open('./Images/all_credit.png', 'rb')
        credit = MIMEImage(fp.read())
        fp.close()

        credit.add_header('Content-ID', '<all_credit>')
        msgRoot.attach(credit)

        # --------- Set Matured Credit image in mail   -------------------------
        fp = open('./Images/all_Matured_credit.png', 'rb')
        all_Matured_credit = MIMEImage(fp.read())
        fp.close()

        all_Matured_credit.add_header('Content-ID', '<all_Matured_credit>')
        msgRoot.attach(all_Matured_credit)

        # --------- Set Matured Credit image in mail   -------------------------
        fp = open('./Images/all_regular_credit.png', 'rb')
        all_regular_credit = MIMEImage(fp.read())
        fp.close()

        all_regular_credit.add_header('Content-ID', '<all_regular_credit>')
        msgRoot.attach(all_regular_credit)

        # --------- Set Cash Drop image in mail   -------------------------
        fp = open('./Images/all_cash.png', 'rb')
        all_cash = MIMEImage(fp.read())
        fp.close()

        all_cash.add_header('Content-ID', '<all_cash>')
        msgRoot.attach(all_cash)

        # --------- Set Return image in mail   -------------------------
        fp = open('./Images/main_return.png', 'rb')
        main_return = MIMEImage(fp.read())
        fp.close()

        main_return.add_header('Content-ID', '<main_return>')
        msgRoot.attach(main_return)

        # --------set Cause_wise_delivery_man_wise_return in mail-----------

        fp = open('./Images/Cause_wise_delivery_man_wise_return.png', 'rb')
        return_with_cause = MIMEImage(fp.read())
        fp.close()

        return_with_cause.add_header('Content-ID', '<return_with_cause>')
        msgRoot.attach(return_with_cause)

        # ---------------------------------------------------------------------

        fp = open('./Images/new_total_delivery_man_wise_return.png', 'rb')
        return_with_cause = MIMEImage(fp.read())
        fp.close()

        return_with_cause.add_header('Content-ID', '<delivery_mans_return_with_cause>')
        msgRoot.attach(return_with_cause)

        # ---------------------------------------------------------------------

        fp = open('./Images/Day_wise_target_sales.png', 'rb')
        return_with_cause = MIMEImage(fp.read())
        fp.close()

        return_with_cause.add_header('Content-ID', '<day_wise_sales_target>')
        msgRoot.attach(return_with_cause)

        # ---------------------------------------------------------------------------
        fp = open('./Images/Cumulative_Day_wise_target_sales.png', 'rb')
        return_with_cause = MIMEImage(fp.read())
        fp.close()

        return_with_cause.add_header('Content-ID', '<cumulative_day_wise_sales_target>')
        msgRoot.attach(return_with_cause)

        # --------- team logo in mail   -----------------------
        fp2 = open('./Images/ai_group_image.jpeg', 'rb')
        team_logoo = MIMEImage(fp2.read())
        fp2.close()

        team_logoo.add_header('Content-ID', '<logoo>')
        msgRoot.attach(team_logoo)

        # Closed to matured Excel attachment
        part = MIMEBase('application', "octet-stream")
        file_location = './Data/ClosedToMatured.xlsx'

        # Create the attachment file (only do it once)
        import os

        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msgRoot.attach(part)

        # Aging matured Excel attachment--------------
        part = MIMEBase('application', "octet-stream")
        file_location = './Data/AgingMatured.xlsx'
        # Create the attachment file (only do it once)
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msgRoot.attach(part)

        # Cash Drop  Excel attachment--------------
        part = MIMEBase('application', "octet-stream")
        file_location = './Data/CashDrop.xlsx'
        # Create the attachment file (only do it once)
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msgRoot.attach(part)

        # ----------- Finally send mail and close server connection ---
        server = smtplib.SMTP(email_server_host, port)
        server.ehlo()
        print('\n-----------------')
        print('Sending Mail')
        server.sendmail(me, recipient, msgRoot.as_string())
        print('Mail Send')
        print('-------------------')
        # server.close()

        # from datetime import datetime
        # import pytz
        #
        # tz_NY = pytz.timezone('Asia/Dhaka')
        # datetime_BD = datetime.now(tz_NY)
        # print("Execution time:", datetime_BD.strftime("%I:%M %p"))
        # import winsound
        #
        # winsound.Beep(1000, 500)
        import time
        time.sleep(5)

    except Exception as e:
        error_title = str(e)
        error_details = traceback.format_exc()

        print(error_title)

        msgRoot = MIMEMultipart('related')
        me = 'erp-bi.service@transcombd.com'

        to = ['fazle.rabby@transcombd.com', '']
        cc = ['', '']
        bcc = ['', '']
        recipient = to + cc + bcc

        # # ------------ Group email --------------------
        subject = "SK+F Formulation Reports - "
        email_server_host = 'mail.transcombd.com'
        port = 25

        msgRoot['From'] = me
        msgRoot['To'] = ', '.join(to)
        msgRoot['Cc'] = ', '.join(cc)
        msgRoot['Bcc'] = ', '.join(bcc)
        msgRoot['Subject'] = subject

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        msgText = MIMEText("""
                <img src="cid:banner" height='230' width='796'> <br>
               <h3 style="color:#FF0000";> The mail did not get generated for some issues.</h3>
                <br> <img src="cid:logoo" height='100' width='250'> <br>
               <i><font color="blue">****This is a system generated report ****</i></font>""",

                       'html')

        msgAlternative.attach(msgText)

        # --------- Set Credit image in mail   -----------------------
        fp = open('./Images/banner_ai.png', 'rb')
        banner = MIMEImage(fp.read())
        fp.close()

        banner.add_header('Content-ID', '<banner>')
        msgRoot.attach(banner)

        # --------- team logo in mail   -----------------------
        fp2 = open('./Images/ai_group_image.jpeg', 'rb')
        team_logoo = MIMEImage(fp2.read())
        fp2.close()

        team_logoo.add_header('Content-ID', '<logoo>')
        msgRoot.attach(team_logoo)

        # ----------- Finally send mail and close server connection ---
        server = smtplib.SMTP(email_server_host, port)
        server.ehlo()
        print('\n-----------------')
        print('Sending Mail')
        server.sendmail(me, recipient, msgRoot.as_string())
        print('Mail Send')
        print('-------------------')
        server.close()

        from datetime import datetime
        import pytz

        tz_NY = pytz.timezone('Asia/Dhaka')
        datetime_BD = datetime.now(tz_NY)
        print("Execution time:", datetime_BD.strftime("%I:%M %p"))
        import winsound

        winsound.Beep(1000, 500)

