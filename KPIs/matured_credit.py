
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
import Functions.helper_functions as func


def matured_credit(branch_name):
    mature_credit_df = pd.read_sql_query("""
                        Select case when MAINCUSTYPE='RETAIL' then 'Retail' else 'Institute' end  as CustType,Sum(OUT_NET) as Amount from
                        (select INVNUMBER,INVDATE,
                        CUSTOMER,TERMS,MAINCUSTYPE,
                        CustomerInformation.CREDIT_LIMIT_DAYS,
                        datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as Days_Diff,
                        OUT_NET from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation
                        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
                        where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash') as TblCredit
                        where Days_Diff>0
                        group by case when MAINCUSTYPE='RETAIL' then 'Retail' else 'Institute' end
                        """, func.con, params={branch_name})


    Institution = int(mature_credit_df.Amount.iloc[0])
    retail = int(mature_credit_df.Amount.iloc[1])

    values = [Institution, retail]

    colors = ['#f213e5', '#bcf303']

    legend_element = [Patch(facecolor='#f213e5', label='Institution'),
                      Patch(facecolor='#bcf303', label='Retail')]

    Sector_total_matured = Institution + retail

    Sector_total_matured = 'Total \n' + func.joker(Sector_total_matured)

    Institution = func.joker(Institution)
    retail = func.joker(retail)
    DataLabel = [Institution, retail]
    fig1, ax = plt.subplots()
    wedges, labels, autopct = ax.pie(values, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=130,
                                     pctdistance=.7)
    plt.setp(autopct, fontsize=14, color='black', fontweight='bold')
    plt.setp(labels, fontsize=14, fontweight='bold')
    ax.text(0, -.1, Sector_total_matured, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#00daff')

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.50, fc='white')

    fig = plt.gcf()

    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('3. Matured Credit', fontsize=16, fontweight='bold', color='#3e0a75')

    ax.axis('equal')
    plt.legend(handles=legend_element, loc='lower left', fontsize=11)
    plt.tight_layout()
    plt.savefig('./Images/matured_credit.png')
    plt.close()
    print('3. Sector wise Credit- Matured Generated')
