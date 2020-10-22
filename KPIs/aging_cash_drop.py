

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import Functions.helper_functions as func


def aging_cash_drop(branch_name):
    cash_drop_df = pd.read_sql_query(""" SELECT  AgingDays, sum(Amount)/1000 as Amount FROM (  Select
                case
                    when Days_Diff between 0 and 3  THEN '0 - 3 days'
                    when Days_Diff between 4 and 10  THEN '4 - 10 days'
                    when Days_Diff between 11 and 15  THEN '11 - 15 days'
                    else '16+ Days' end  as AgingDays,
                --OUT_NET
                Sum(OUT_NET) as Amount,
    
                CASE
                    when TblCredit.Days_Diff between '0' and '3'  THEN 1
                    when TblCredit.Days_Diff between '4' and '10'  THEN 2
                    when TblCredit.Days_Diff between '11' and '15'  THEN 3
                    ELSE  4
                    END AS SERIAL
                from
                    (select INVNUMBER,INVDATE,
                    CUSTOMER,TERMS,MAINCUSTYPE,
                    datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as Days_Diff,
                    OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                    where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS='Cash') as TblCredit
                    group by
    
                    case
                        when Days_Diff between 0 and 3 THEN '0 - 3 days'
                        when Days_Diff between 4 and 10  THEN '4 - 10 days'
                        when Days_Diff between 11 and 15  THEN '11 - 15 days'
                            else '16+ Days' end
                    ,CASE
                    when TblCredit.Days_Diff between '0' and '3'  THEN 1
                    when TblCredit.Days_Diff between '4' and '10'  THEN 2
                    when TblCredit.Days_Diff between '11' and '15'  THEN 3
                    ELSE  4 end ) as T1
                    group by T1.AgingDays, SERIAL
                order by SERIAL """, func.con, params={branch_name})

    width = 0.75
    AgingDays = cash_drop_df['AgingDays']
    y_pos = np.arange(len(AgingDays))
    performance = cash_drop_df['Amount']
    new_totall = sum(performance)
    fig, ax = plt.subplots()
    colors = ['#f00228', '#ff6500', '#deff00', '#2c8e14']

    bars = plt.bar(y_pos, performance, width, align='center', alpha=0.9, color=colors)
    maf_kor3 = max(performance)

    def autolabel(bars):
        for bar in bars:
            height = int(bar.get_height())
            ax.text(bar.get_x() + bar.get_width() / 2., .995 * height,
                    func.for_bar(height),
                    ha='center', va='bottom', fontweight='bold', rotation=45, fontsize=12)

    autolabel(bars)

    def autolabel4(bars):
        for bar in bars:
            height = int(bar.get_height())
            ax.text(bar.get_x() + bar.get_width() / 2., .5 * height,
                    str(round(((height / new_totall) * 100), 1)) + "%",
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

    autolabel4(bars)

    plt.xticks(y_pos, AgingDays, fontsize=12)
    # plt.yticks(fontsize=12)
    plt.yticks(np.arange(0, maf_kor3 + (.6 * maf_kor3), maf_kor3 / 5), fontsize=12)
    plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
    plt.ylabel('Amount', color='black', fontsize=14, fontweight='bold')
    plt.title('8. Aging of Cash Drop', color='#3e0a75', fontweight='bold', fontsize=16)
    plt.tight_layout()
    plt.savefig('./Images/aging_cash_drop.png')
    plt.close()
    # # plt.show()
    print('8. Aging Days - Cash Drop Generated')
