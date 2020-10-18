

import KPIs.banner as banner
import KPIs.terms_wise_outstanding as trems_outs
import KPIs.category_wise_credit as cat_credit
import KPIs.matured_credit as m_credit
import KPIs.closed_to_matured_credit as c_m_credit
import KPIs.aging_matured_credit as aging_m_credit
import KPIs.sector_wise_non_mature_credit as sec_non_mature_credit
import KPIs.category_wise_cash_outstanding as cash
import KPIs.aging_cash_drop as cash_drop
import KPIs.join_all_images as fig_join
# import KPIs.return_info as return_info
# import KPIs.cause_wise_return as cause_return
import KPIs.deliveryman_wise_return as dp_return
import KPIs.day_wise_target_vs_sales as day_target_sales
import KPIs.target_vs_sales as target_sales
import KPIs.cumulative_sales_target as cm_target_sales
import KPIs.excel_file_genetator as data_generator

# banner.create_banner('VRBSKF')
# trems_outs.create_terms_wise_outstanding('VRBSKF')
# cat_credit.category_wise_credit('VRBSKF')
# m_credit.matured_credit('VRBSKF')
# c_m_credit.closed_matured_credit('VRBSKF')
# aging_m_credit.aging_matured_credit('VRBSKF')
# sec_non_mature_credit.sector_wise_non_matured_credit('VRBSKF')
# cash.cash_outstanding('VRBSKF')
# cash_drop.aging_cash_drop('VRBSKF')
# fig_join.join_all_images()
# return_info.generate_all_return_info('VRBSKF')
# dp_return.dp_man_wise_return('VRBSKF')
# cause_return.cause_wise_teturn('VRBSKF')
# target_sales.target_sales('VRBSKF')
# day_target_sales.day_wise_target_sales('VRBSKF')
# cm_target_sales.cumulative_sales_target('VRBSKF')

data_generator.closed_to_matured_data('VRBSKF')