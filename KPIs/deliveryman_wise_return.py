
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import Functions.helper_functions as func


def dp_man_wise_return(branch_name):
    try:
        delivery_man_wise_return_df = pd.read_sql_query("""select TWO.ShortName as DPNAME, SUM(Sales.ReturnAmount) as ReturnAmount from
            (select  DPID, AUDTORG,ISNULL(sum(case when TRANSTYPE<>1 then INVNETH *-1 end), 0) /ISNULL(sum(case when TRANSTYPE=1 then INVNETH end), 0)*100 as ReturnAmount from OESalesSummery
                    where AUDTORG like ? and 
                    left(TRANSDATE,6)=convert(varchar(6),getdate(),112)
                    group by DPID,AUDTORG) as Sales
            left join
            (select distinct AUDTORG,ShortName,DPID from DP_ShortName where AUDTORG like ?) as TWO
            on Sales.DPID = TWO.DPID
            and Sales.AUDTORG=TWO.AUDTORG
            where TWO.ShortName is not null
            and Sales.ReturnAmount>0
            group by TWO.ShortName
            order by ReturnAmount DESC""", func.con, params=(branch_name, branch_name))

        DPNAME = delivery_man_wise_return_df['DPNAME']
        y_pos = np.arange(len(DPNAME))
        ReturnAmount = abs(delivery_man_wise_return_df['ReturnAmount'])
        ReturnAmount = ReturnAmount.values.tolist()

        ran = max(ReturnAmount)
        color = '#418af2'
        fig, ax = plt.subplots(figsize=(12.81, 4.8))
        rects1 = plt.bar(y_pos, ReturnAmount, align='center', alpha=0.9, color=color)

        def autolabel(bars):
            loop = 0
            for bar in bars:
                show = ReturnAmount[loop]
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, (1.05 * height),
                        '%.2f' % (show) + '%', ha='center', va='bottom', fontsize=12, rotation=70, fontweight='bold')
                loop = loop + 1

        autolabel(rects1)

        plt.xticks(y_pos, DPNAME, rotation='vertical', fontsize='12')
        plt.yticks(np.arange(0, round(ran) + (.6 * round(ran))), fontsize='12')
        plt.xlabel('Delivery Person', fontsize='14', color='black', fontweight='bold')
        plt.ylabel('Return Percentage', fontsize='14', color='black', fontweight='bold')
        plt.title("9. Delivery Person's Return %", color='#3e0a75', fontsize='16', fontweight='bold')
        plt.tight_layout()

        plt.savefig('./Images/Delivery_man_wise_return.png')

        plt.close()
        print('9. Delivery man wise return generated')
    except:
        print("sorry! 9. Delivery man wise return cannot be generated")
        plt.figure(figsize=(12.81, 4.8))
        plt.text(0.5, 0.5, str('Sorry! Due to data unavailability, the graph cannot be generated'), fontsize=25,
                 color='red',
                 horizontalalignment='center', verticalalignment='center')
        plt.axis('off')
        # plt.show()
        plt.savefig('./Images/Delivery_man_wise_return.png')
        plt.close()
