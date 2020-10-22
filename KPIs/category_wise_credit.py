
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
import Functions.helper_functions as func


def category_wise_credit(branch_name):
    credit_category_df = pd.read_sql_query(""" Select case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' End as  'Category',Sum(OUT_NET) as Amount from
                            (select INVNUMBER,INVDATE,
                            CUSTOMER,TERMS,MAINCUSTYPE,
                            CustomerInformation.CREDIT_LIMIT_DAYS,
                            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
                            OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                            join ARCHIVESKF.dbo.CustomerInformation
                            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                            where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash') as TblCredit
                            group by case when Days_Diff>0 then 'Matured Credit' else 'Regular Credit' end
                                                                """, func.con, params={branch_name})


    matured = int(credit_category_df.Amount.iloc[0])
    not_mature = int(credit_category_df.Amount.iloc[1])

    values = [matured, not_mature]

    colors = ['#ffb667', '#b35e00']

    legend_element = [Patch(facecolor='#ffb667', label='Matured'),
                      Patch(facecolor='#b35e00', label='Not Mature')]

    total_credit = matured + not_mature

    total_credit = 'Total \n' + func.joker(total_credit)

    # ------------------new code--------------------
    matured = func.joker(matured)
    not_mature = func.joker(not_mature)

    DataLabel = [matured, not_mature]
    # -----------------------------------------------

    fig1, ax = plt.subplots()
    wedges, labels, autopct = ax.pie(values, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=120,
                                     pctdistance=.7)
    plt.setp(autopct, fontsize=14, color='black', fontweight='bold')
    plt.setp(labels, fontsize=14, fontweight='bold')
    ax.text(0, -.1, total_credit, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#00daff')

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.50, fc='white')

    fig = plt.gcf()

    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('2. Credit Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')

    ax.axis('equal')
    plt.legend(handles=legend_element, loc='lower left', fontsize=11)
    plt.tight_layout()
    plt.savefig('./Images/category_wise_credit.png')

    print('2. Category wise Credit Generated ')
    plt.close()
