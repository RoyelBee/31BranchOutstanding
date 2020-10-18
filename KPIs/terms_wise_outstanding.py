
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
import Functions.helper_functions as func

def create_terms_wise_outstanding(branc_names):
    outstanding_df = pd.read_sql_query(""" select
                    SUM(CASE WHEN TERMS='CASH' THEN OUT_NET END) AS TotalOutStandingOnCash,
                    SUM(CASE WHEN TERMS not like '%CASH%' THEN OUT_NET END) AS TotalOutStandingOnCredit
    
                    from  [ARCOUT].dbo.[CUST_OUT]
                    where AUDTORG like ? AND [INVDATE] <= convert(varchar(8),DATEADD(D,0,GETDATE()),112)
                                            """, func.con, params={branc_names})

    cash = int(outstanding_df['TotalOutStandingOnCash'])
    credit = int(outstanding_df['TotalOutStandingOnCredit'])

    data = [cash, credit]
    total = cash + credit
    total = 'Total \n' + func.joker(total)

    colors = ['#f9ff00', '#ff8600']

    legend_element = [Patch(facecolor='#f9ff00', label='Cash'),
                      Patch(facecolor='#ff8600', label='Credit')]

    # -------------------new code--------------------------

    ca = func.joker(cash)
    cre = func.joker(credit)

    DataLabel = [ca, cre]
    # -----------------------------------------------------

    fig1, ax = plt.subplots()
    wedges, labels, autopct = ax.pie(data, colors=colors, labels=DataLabel, autopct='%.1f%%', startangle=90,
                                     pctdistance=.7)
    plt.setp(autopct, fontsize=14, color='black', fontweight='bold')
    plt.setp(labels, fontsize=14, fontweight='bold')
    ax.text(0, -.1, total, ha='center', fontsize=14, fontweight='bold', backgroundcolor='#00daff')

    centre_circle = plt.Circle((0, 0), 0.50, fc='white')

    fig = plt.gcf()

    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('1. Total Outstanding', fontsize=16, fontweight='bold', color='#3e0a75')

    ax.axis('equal')
    plt.legend(handles=legend_element, loc='lower left',
               fontsize=11)
    plt.tight_layout()
    plt.savefig('./Images/terms_wise_outstanding.png')

    print('Fig 01: Terms wise Outstanding Generated')
    plt.close()