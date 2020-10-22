
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import Functions.helper_functions as func


def closed_matured_credit(branch_name):
    CloseTo_mature_df = pd.read_sql_query("""
                            SELECT  AgingDays, sum(CreditAmount)/1000 as Amount FROM
                            (Select CUSTOMER, CUSTNAME, INVDATE,   Sum(OUT_NET) as CreditAmount ,
                            case
                             when TblCredit.Days_Diff between '-3' and '0'  THEN '0 - 3 days'
                            when TblCredit.Days_Diff between '-10' and '-4'  THEN '4 - 10 days'
                            when TblCredit.Days_Diff between '-15' and '-11'  THEN '11 - 15 days'
                            else '16+ Days' end  as AgingDays,
    
                            CASE
                            when TblCredit.Days_Diff between '-3' and '0' then 1
                            when TblCredit.Days_Diff between '-10' and '-4' then 2
                            when TblCredit.Days_Diff between '-15' and '-11'  then 3
                            ELSE  4
                            END AS SERIAL
                            from
                                (select CUSTNAME, INVNUMBER,INVDATE,
                        CUSTOMER,TERMS,MAINCUSTYPE,
                        CustomerInformation.CREDIT_LIMIT_DAYS,
                        (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) as Days_Diff,
                        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation
                        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                        where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash' and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)<=0
                        ) as TblCredit
                       -- where Days_Diff<=0
    
                                group by CUSTOMER, CUSTNAME, INVDATE,
                                    case
                             when TblCredit.Days_Diff between '-3' and '0'  THEN '0 - 3 days'
                            when TblCredit.Days_Diff between '-10' and '-4'  THEN '4 - 10 days'
                            when TblCredit.Days_Diff between '-15' and '-11'  THEN '11 - 15 days'
                                         else '16+ Days' end
    
                            ,CASE
                            when TblCredit.Days_Diff between '-3' and '0' then 1
                            when TblCredit.Days_Diff between '-10' and '-4' then 2
                            when TblCredit.Days_Diff between '-15' and '-11'  then 3
                            ELSE  4
                            END ) AS T1
                            group by T1.AgingDays, SERIAL
                            order by SERIAL
    
                                            """, func.con, params={branch_name})

    width = 0.75
    AgingDays = CloseTo_mature_df['AgingDays']
    y_pos = np.arange(len(AgingDays))
    performance = CloseTo_mature_df['Amount']
    tovalue = sum(performance)
    maf_kor = max(performance)
    fig, ax = plt.subplots()
    colors = ['#f00228', '#ff6500', '#deff00', '#2c8e14']
    bars = plt.bar(y_pos, performance, width, color=colors, align='center', alpha=1)

    def autolabel(bars):
        for bar in bars:
            height = int(bar.get_height())
            ax.text(bar.get_x() + bar.get_width() / 2., .995 * height,
                    func.for_bar(height),
                    ha='center', va='bottom', fontsize=12, rotation=45, fontweight='bold')

    autolabel(bars)

    def autolabel2(bars):
        for bar in bars:
            height = int(bar.get_height())
            ax.text(bar.get_x() + bar.get_width() / 2., .5 * height,
                    str(round(((height / tovalue) * 100), 1)) + "%",
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

    autolabel2(bars)

    plt.xticks(y_pos, AgingDays, fontsize=12)
    plt.yticks(np.arange(0, maf_kor + (.6 * maf_kor), maf_kor / 5), fontsize=12)
    plt.xlabel('Aging Days', color='black', fontsize=14, fontweight='bold')
    # plt.yticks(np.arange(0, round(ran) + (.6 * round(ran))), fontsize='12')
    plt.ylabel('Amount', color='black', fontsize=14, fontweight='bold')
    plt.title('6. Non-Matured Credit Age', color='#3e0a75', fontweight='bold', fontsize=16)
    plt.tight_layout()
    plt.savefig('./Images/closed_to_matured_credit.png')
    plt.close()
    print('6. Closed to mature Credit Generated')
