
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
import Functions.helper_functions as func

def cash_outstanding(branch_name):
    try:
        sector_wise_cash_df = pd.read_sql_query(""" Select case when MAINCUSTYPE='RETAIL' then 'Retail' else 'Institute' end  as CustType,Sum(OUT_NET) as Amount from
                               (select INVNUMBER,INVDATE,
                               CUSTOMER,TERMS,MAINCUSTYPE,
                               CustomerInformation.CREDIT_LIMIT_DAYS,
                               datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
                               OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                               join ARCHIVESKF.dbo.CustomerInformation
                               on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                               where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS='Cash') as TblCredit
        
                               group by case when MAINCUSTYPE='RETAIL' then 'Retail' else 'Institute' end """, func.con,
                                                params={branch_name})
        Institution = int(sector_wise_cash_df.Amount.iloc[0])
        retail = int(sector_wise_cash_df.Amount.iloc[1])

        values = [Institution, retail]
        colors = ['#a9e11a', '#1798ca']
        legend_element = [Patch(facecolor='#a9e11a', label='Institution'),
                          Patch(facecolor='#1798ca', label='Retail')]

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
        ax.text(0, -.1, sector_total_credit, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#b1bec1')
        # draw circle
        centre_circle = plt.Circle((0, 0), 0.50, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        # Equal aspect ratio ensures that pie is drawn as a circle
        plt.title('7. Cash Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')
        ax.axis('equal')
        plt.legend(handles=legend_element, loc='lower left', fontsize=11)
        plt.tight_layout()
        plt.savefig('./Images/Category_wise_cash.png')
        plt.close()
        print('7. Category wise Cash Generated')
    except:

        plt.figure(figsize=(12.81, 4.8))

        plt.title('7. Cash Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')

        plt.text(0.5, 0.5, str('Sorry! this figure cannot be generated'), fontsize=25,
                 color='red',
                 horizontalalignment='center', verticalalignment='center')
        plt.axis('off')
        # plt.show()
        plt.savefig('./Images/Category_wise_cash.png')
        plt.close()

        print('No data')
