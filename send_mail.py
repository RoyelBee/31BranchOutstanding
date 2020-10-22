import setup as action
import send_error_mail as error
import smtplib
import traceback
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

import setup as action
import send_error_mail as error

# # ------- kamrul Branches ------------------------------
kamrul_branch = ['JESSKF', 'MIRSKF', 'KHLSKF', 'COMSKF', 'PATSKF', 'BSLSKF']

try:
    action.generate_kamrul_mail('JESSKF', 'rejaul.islam@transcombd.com')
except:
    error.send_error_msg('JESSKF')

try:
    action.generate_kamrul_mail('MIRSKF', 'rejaul.islam@transcombd.com')
except:
    error.send_error_msg('MIRSKF')

try:
    action.generate_kamrul_mail('KHLSKF', 'rejaul.islam@transcombd.com')
except:
    error.send_error_msg('KHLSKF')

try:
    action.generate_kamrul_mail('COMSKF', 'rejaul.islam@transcombd.com')
except:
    error.send_error_msg('COMSKF')

try:
    action.generate_kamrul_mail('PATSKF', 'rejaul.islam@transcombd.com')
except:
    error.send_error_msg('PATSKF')

try:
    action.generate_kamrul_mail('BSLSKF', 'rejaul.islam@transcombd.com')
except:
    error.send_error_msg('BSLSKF')
