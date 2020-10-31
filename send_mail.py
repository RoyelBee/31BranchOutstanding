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

# # ------- kamrul Branches -----------------------------------------------
# # -----------------------------------------------------------------------

kamrul_branch = ['JESSKF', 'MIRSKF', 'KHLSKF', 'COMSKF', 'PATSKF', 'BSLSKF']

try:
    action.generate_kamrul_mail('JESSKF', 'kamrul.ahsan@tdcl.transcombd.com')
except:
    error.send_error_msg('JESSKF')

try:
    action.generate_kamrul_mail('MIRSKF', 'kamrul.ahsan@tdcl.transcombd.com')
except:
    error.send_error_msg('MIRSKF')

try:
    action.generate_kamrul_mail('KHLSKF', 'kamrul.ahsan@tdcl.transcombd.com')
except:
    error.send_error_msg('KHLSKF')

try:
    action.generate_kamrul_mail('COMSKF', 'kamrul.ahsan@tdcl.transcombd.com')
except:
    error.send_error_msg('COMSKF')

try:
    action.generate_kamrul_mail('PATSKF', 'kamrul.ahsan@tdcl.transcombd.com')
except:
    error.send_error_msg('PATSKF')

try:
    action.generate_kamrul_mail('BSLSKF', 'kamrul.ahsan@tdcl.transcombd.com')
except:
    error.send_error_msg('BSLSKF')

# # ------------- Anwar   -----------------------------------------------
# # ---------------------------------------------------------------------

# anwar_branch = ['MYMSKF', 'FRDSKF', 'TGLSKF', 'RAJSKF', 'SAVSK', 'BOGSKF']
# try:
#     action.generate_kamrul_mail('MYMSKF', 'anwar_branch@transcombd.com')
# except:
#     error.send_error_msg('MYMSKF')
#
# try:
#     action.generate_kamrul_mail('FRDSKF', 'anwar_branch@transcombd.com')
# except:
#     error.send_error_msg('FRDSKF')
#
# try:
#     action.generate_kamrul_mail('TGLSKF', 'anwar_branch@transcombd.com')
# except:
#     error.send_error_msg('TGLSKF')
#
# try:
#     action.generate_kamrul_mail('RAJSKF', 'anwar_branch@transcombd.com')
# except:
#     error.send_error_msg('RAJSKF')
#
# try:
#     action.generate_kamrul_mail('SAVSK', 'anwar_branch@transcombd.com')
# except:
#     error.send_error_msg('SAVSK')
#
# try:
#     action.generate_kamrul_mail('BOGSKF', 'anwar_branch@transcombd.com')
# except:
#     error.send_error_msg('BOGSKF')

# # ---------------- Atik   ----------------------------------------------------
# # ----------------------------------------------------------------------------
#
# atik_branch = ['HZJSKF', 'RNGSKF', 'KSGSKF', 'MOTSKF', 'DNJSKF', 'GZPSKF', 'KRNSKF']
#
# try:
#     action.generate_kamrul_mail('HZJSKF', 'md.atikullaha@tdcl.transcombd.com')
# except:
#     error.send_error_msg('HZJSKF')
#
# try:
#     action.generate_kamrul_mail('RNGSKF', 'md.atikullaha@tdcl.transcombd.com')
# except:
#     error.send_error_msg('RNGSKF')
#
# try:
#     action.generate_kamrul_mail('KSGSKF', 'md.atikullaha@tdcl.transcombd.com')
# except:
#     error.send_error_msg('KSGSKF')
#
# try:
#     action.generate_kamrul_mail('MOTSKF', 'md.atikullaha@tdcl.transcombd.com')
# except:
#     error.send_error_msg('MOTSKF')
#
# try:
#     action.generate_kamrul_mail('DNJSKF', 'md.atikullaha@tdcl.transcombd.com')
# except:
#     error.send_error_msg('DNJSKF')
#
# try:
#     action.generate_kamrul_mail('GZPSKF', 'md.atikullaha@tdcl.transcombd.com')
# except:
#     error.send_error_msg('GZPSKF')
#
# try:
#     action.generate_kamrul_mail('KRNSKF', 'md.atikullaha@tdcl.transcombd.com')
# except:
#     error.send_error_msg('KRNSKF')


# # # ------------------- Nurul ----------------------------------------------
# ## -------------------------------------------------------------------------

# nurul_branch = ['VRBSKF', 'NOKSKF', 'SYLSKF', 'MHKSKF', 'MLVSKF', 'FENSKF']
#
# try:
#     action.generate_kamrul_mail('VRBSKF', 'nurul.amin@tdcl.transcombd.com')
# except:
#     error.send_error_msg('VRBSKF')
#
# try:
#     action.generate_kamrul_mail('NOKSKF', 'nurul.amin@tdcl.transcombd.com')
# except:
#     error.send_error_msg('NOKSKF')
#
# try:
#     action.generate_kamrul_mail('SYLSKF', 'nurul.amin@tdcl.transcombd.com')
# except:
#     error.send_error_msg('SYLSKF')
#
# try:
#     action.generate_kamrul_mail('MHKSKF', 'nurul.amin@tdcl.transcombd.com')
# except:
#     error.send_error_msg('MHKSKF')
#
# try:
#     action.generate_kamrul_mail('MLVSKF', 'nurul.amin@tdcl.transcombd.com')
# except:
#     error.send_error_msg('MLVSKF')
#
# try:
#     action.generate_kamrul_mail('FENSKF', 'nurul.amin@tdcl.transcombd.com')
# except:
#     error.send_error_msg('FENSKF')

# # ------------------- Hafizur  ---------------------------------------------
# ## ------------------------------------------------------------------------
# hafizur_branch = ['NAJSKF', 'CTGSKF', 'CTNSKF', 'KUSSKF', 'PBNSKF', 'COXSKF']
#
# try:
#     action.generate_kamrul_mail('NAJSKF', 'sheikh.hafizur@tdcl.transcombd.com')
# except:
#     error.send_error_msg('NAJSKF')
#
# try:
#     action.generate_kamrul_mail('CTGSKF', 'sheikh.hafizur@tdcl.transcombd.com')
# except:
#     error.send_error_msg('CTGSKF')
#
# try:
#     action.generate_kamrul_mail('CTNSKF', 'sheikh.hafizur@tdcl.transcombd.com')
# except:
#     error.send_error_msg('CTNSKF')
#
# try:
#     action.generate_kamrul_mail('KUSSKF', 'sheikh.hafizur@tdcl.transcombd.com')
# except:
#     error.send_error_msg('KUSSKF')
#
# try:
#     action.generate_kamrul_mail('PBNSKF', 'sheikh.hafizur@tdcl.transcombd.com')
# except:
#     error.send_error_msg('PBNSKF')
#
# try:
#     action.generate_kamrul_mail('COXSKF', 'sheikh.hafizur@tdcl.transcombd.com')
# except:
#     error.send_error_msg('COXSKF')