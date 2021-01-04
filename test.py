# import KPIs.cumulative_sales_target as cm
# cm.cumulative_sales_target('FENSKF')
import setup as action
import send_error_mail as error
try:
    action.generate_kamrul_mail('BSLSKF', 'rab.abdur@tdcl.transcombd.com')
except:
    error.send_error_msg('BSLSKF')