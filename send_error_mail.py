import datetime
import smtplib
from _datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import Functions.helper_functions as func


def send_error_msg(bramch):
    # if (to == ['nawajesh@skf.transcombd.com', '']):
    #     to = ['rejaul.islam@transcombd.com', '']
    #     cc = ['', '']
    #     bcc = ['', '']
    #     print('Report Sending to = ', to)

    to = ['', '']  # ['yakub@transcombd.com', 'tawhid@transcombd.com']
    cc = ['', '']
    bcc = ['rejaul.islam@transcombd.com', 'yakub@transcombd.com']  # ['aftab.uddin@transcombd.com', 'rejaul.islam@transcombd.com',
    # 'fazle.rabby@transcombd.com']

    msgRoot = MIMEMultipart('related')
    me = 'erp-bi.service@transcombd.com'
    # to = to
    # cc = ['biswascma@yahoo.com', 'yakub@transcombd.com', 'zubair.transcom@gmail.com']
    # bcc = ['rejaul.islam@transcombd.com', 'aftab.uddin@transcombd.com', 'fazle.rabby@transcombd.com']

    recipient = to + cc + bcc

    date = datetime.today()
    today = str(date.day) + '/' + str(date.month) + '/' + str(date.year) + ' ' + date.strftime("%I:%M %p")

    # # ------------ Group email --------------------
    subject = "Failed to Generate report" + today
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

    branchname_generator_df = pd.read_sql_query("""select branch,ndmname,branchname from ndm where branch like ? """,
                                                func.con, params={bramch})

    ndm_name = branchname_generator_df['ndmname']
    branch_name = branchname_generator_df['branchname']

    # # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText("""
                         <h2>Failed to Generate NDM [ """ + ndm_name[0] + """ ] : [""" + branch_name[0] + """] 
                         Report. 
                         </h2>
                                    """, 'html')
    msgAlternative.attach(msgText)

    # # ----------- Finally send mail and close server connection -----
    server = smtplib.SMTP(email_server_host, port)
    server.ehlo()
    print('\n-----------------')
    print('Sending Error Mail')
    server.sendmail(me, recipient, msgRoot.as_string())
    print('Mail Send')
    print('-------------------')
    server.close()
