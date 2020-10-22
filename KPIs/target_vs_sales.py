import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import Functions.helper_functions as func


def target_sales(branch_name):
    try:
        LD_Target_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
                        Declare @DaysInMonth NVARCHAR(MAX);
                        SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                        SET @DaysInMonth = DAY(EOMONTH(GETDATE())) 
                        select ISNULL((Sum(TARGET)/@DaysInMonth), 0) as  YesterdayTarget from TDCL_BranchTarget  
                        where YEARMONTH = @CurrentMonth and AUDTORG like ?""", func.con, params={branch_name})
        toto = LD_Target_df.values
        ld_target = int(toto[0, 0])

        MTD_Target_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
    
                        SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
    
                        select ISNULL((Sum(TARGET)), 0) as  MTDTarget from TDCL_BranchTarget  
                        where YEARMONTH = @CurrentMonth and AUDTORG like ? """, func.con, params={branch_name})

        momo = MTD_Target_df.values
        Mtd_target = int(momo[0, 0])

        from datetime import date
        from datetime import datetime

        given_date = datetime.today().date()

        toto = datetime.today().date()
        first = given_date.replace(day=1)
        day1 = date(toto.year, toto.month, toto.day)
        day2 = date(first.year, first.month, first.day)
        no_of_days = (day1 - day2).days

        import calendar
        import datetime

        now = datetime.datetime.now()
        total_days = calendar.monthrange(now.year, now.month)[1]

        final_mtd_target = int((Mtd_target / total_days) * no_of_days)

        YTD_Target_df = pd.read_sql_query(""" select ISNULL((Sum(TARGET)), 0) as  YTDTarget from TDCL_BranchTarget  
                        where convert(varchar(4), YEARMONTH,112) = convert(varchar(4), GETDATE(),112)
                          and AUDTORG like ?""", func.con, params={branch_name})

        yoyo = YTD_Target_df.values
        Ytd_target = int(yoyo[0, 0])
        final_ytd_target = int(Ytd_target - ((Mtd_target / total_days) * (total_days - no_of_days)))
        LD_Sales_df = pd.read_sql_query("""Declare @Currentday NVARCHAR(MAX);
                        SET @Currentday = convert(varchar(8), GETDATE()-1,112);
                        select  isnull(Sum(EXTINVMISC),0) as  YesterdaySales from OESalesDetails  
                        where LEFT(TRANSDATE,8) = @Currentday and AUDTORG like ? """, func.con, params={branch_name})

        Ld_toto = LD_Sales_df.values
        MTD_Sales_df = pd.read_sql_query(""" Declare @Currentmonth NVARCHAR(MAX);
                        SET @Currentmonth = convert(varchar(6), GETDATE(),112);
                        select  isnull(Sum(EXTINVMISC),0) as  MTDSales from OESalesDetails  
                        where LEFT(TRANSDATE,6) = @Currentmonth and AUDTORG like ?""", func.con, params={branch_name})

        MTD_momo = MTD_Sales_df.values
        YTD_Sales_df = pd.read_sql_query("""Declare @Currentyear NVARCHAR(MAX);
                        SET @Currentyear = convert(varchar(4), GETDATE(),112);
                        select  isnull(Sum(EXTINVMISC),0) as  YTDSales from OESalesDetails  
                        where LEFT(TRANSDATE,4) = @Currentyear and AUDTORG like ? """, func.con, params={branch_name})

        YTD_yoyo = YTD_Sales_df.values
        labels = ['LD', 'MTD', 'YTD']
        aa = int(final_mtd_target / 1000)
        bb = int(final_ytd_target / 1000)
        cc = int(ld_target / 1000)
        Targets = [cc, aa, bb]

        Sales = [int(Ld_toto[0, 0] / 1000), int(MTD_momo[0, 0] / 1000), int(YTD_yoyo[0, 0] / 1000)]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, Targets, width, label='Target')
        rects2 = ax.bar(x + width / 2, Sales, width, label='Sales')

        maf_kor5 = max(Sales)
        # Add some text for labels, title and custom x-axis tick labels, etc.
        plt.yticks(np.arange(0, maf_kor5 + (.8 * maf_kor5), maf_kor5 / 5), fontsize=12)
        ax.set_ylabel('Amount', fontsize='14', color='black', fontweight='bold')
        ax.set_xlabel('Group Wise Sales', fontsize='14', color='black', fontweight='bold')
        ax.set_title('11. Target vs Sales', fontsize=16, fontweight='bold', color='#3e0a75')

        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()


        def autolabel(bars):
            for bar in bars:
                height = int(bar.get_height())
                ax.text(bar.get_x() + bar.get_width() / 2., .995 * height,
                        func.get_value(str(height)) + "K",
                        ha='center', va='bottom', fontsize=12, rotation=45, fontweight='bold')


        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()

        # plt.show()
        plt.savefig('./Images/LD_MTD_YTD_TARGET_vs_sales.png')
        print('11. Target vs Sales ')

        plt.close()
    except:
        print("sorry! 11. Target vs Sales cannot be generated")
        plt.figure(figsize=(6.4, 4.8))
        plt.text(0.5, 0.5, str('Sorry! Due to data unavailability, the graph cannot be generated'), fontsize=25,
                 color='red',
                 horizontalalignment='center', verticalalignment='center')
        plt.axis('off')
        # plt.show()
        plt.savefig('./Images/LD_MTD_YTD_TARGET_vs_sales.png')