
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


import Functions.helper_functions as func


def cumulative_sales_target(branch_name):
    ever_sale_df = pd.read_sql_query("""select right(formatdate,2) as days,isnull(amount,0) as Amount from (
       select formatdate from [Calendar] where left(formatdate,6)=convert(varchar(6), GETDATE(),112)) as cal
       left join (
       select cast(transdate as varchar(8)) as Transdate,sum(EXTINVMISC)/1000 as amount from OESalesDetails
       where left(transdate,6)=convert(varchar(6), GETDATE(),112) and AUDTORG like ?
       group by cast(transdate as varchar(8))) as sales
       on cal.formatdate=sales.Transdate
       order by formatdate""", func.con, params={branch_name})

    all_days_in_month = ever_sale_df['days'].tolist()
    day_to_day_sale = ever_sale_df['Amount'].tolist()
    # print(all_days_in_month)
    # print(day_to_day_sale)

    from datetime import date

    today = date.today()

    current_day = today.strftime("%d")
    current_day_in_int = int(current_day)
    # print(current_day_in_int)

    final_days_array = []
    final_sales_array = []
    for t_va in range(0, current_day_in_int):
        # print(t_va)
        final_days_array.append(all_days_in_month[t_va])
        final_sales_array.append(day_to_day_sale[t_va])

    # print(final_days_array)
    # print(final_sales_array)

    EveryD_Target2_df = pd.read_sql_query("""Declare @CurrentMonth NVARCHAR(MAX);
                       Declare @DaysInMonth NVARCHAR(MAX);
                       SET @CurrentMonth = convert(varchar(6), GETDATE(),112)
                       SET @DaysInMonth = DAY(EOMONTH(GETDATE())) 
                       select ISNULL(((Sum(TARGET)/@DaysInMonth)/1000), 0) as  YesterdayTarget from TDCL_BranchTarget  
                       where YEARMONTH = @CurrentMonth and AUDTORG like ?""",  func.con, params={branch_name})
    totarget = EveryD_Target2_df.values
    target_for_target = int(totarget[0, 0])
    # print(target_for_target)

    y_pos = np.arange(len(final_days_array))
    # print(y_pos)

    # --------------------------------------copy--------------------------------------

    n = 1
    Target = []
    labell = []
    for z in y_pos:
        labell.append(n)
        Target.append(int(target_for_target / 1000))
        n = n + 1

    # ----------------code for cumulitive sales------------
    import calendar
    import datetime

    now = datetime.datetime.now()
    total_days = calendar.monthrange(now.year, now.month)[1]
    # print(total_days)

    new_target = target_for_target
    # print(new_target)

    z = len(labell)
    # print(len(labell))
    fin_target = 0
    ttt = []
    for t_value in range(0, total_days + 1):
        # print(t_value)
        fin_target = new_target * t_value
        # print(fin_target)
        ttt.append(fin_target)
        fin_target = 0
    # print(ttt) #-------------------target data

    values = final_sales_array
    length = len(values)

    new = [0]
    final = 0
    for val in values:
        # print(val)
        get_in = values.index(val)
        # print(get_in)
        if get_in == 0:
            new.append(val)
        else:
            for i in range(0, get_in + 1):
                final = final + values[i]
            new.append(final)
            final = 0

    x = range(len(ttt))
    xx = range(len(new))

    list_index_for_target = len(ttt) - 1
    # print(list_index_for_target)

    list_index_for_sale = len(new) - 1
    # print(list_index_for_sale)
    # Change the color and its transparency
    fig, ax = plt.subplots(figsize=(12.81, 4.8))
    plt.fill_between(x, ttt, color="skyblue", alpha=1)
    plt.plot(xx, new, color="red", linewidth=5, linestyle="-")
    plt.xlabel('Days', fontsize='14', color='black', fontweight='bold')
    plt.ylabel('Amount', fontsize='14', color='black', fontweight='bold')
    # ax.set_ylabel('Amount', fontsize='14', color='black', fontweight='bold')
    # ax.set_xlabel('Day', fontsize='14', color='black', fontweight='bold')
    plt.title('13. MTD Target vs Sales - Cumulative', fontsize=16, fontweight='bold', color='#3e0a75')
    plt.xticks(np.arange(1, total_days + 1, 1))
    plt.legend(['sales', 'target'], loc='best', fontsize='14')
    plt.text(list_index_for_sale, ttt[list_index_for_sale],  func.get_value(str(int(ttt[list_index_for_sale]))) + 'K',
             color='black', fontsize=12, fontweight='bold')
    plt.text(list_index_for_sale, new[list_index_for_sale], func.get_value(str(int(new[list_index_for_sale]))) + 'K',
             color='black', fontsize=12, fontweight='bold')
    plt.text(list_index_for_target, ttt[list_index_for_target], func.get_value(str(int(ttt[list_index_for_target]))) + 'K',
             color='black', fontsize=12, fontweight='bold')

    plt.grid()
    plt.savefig("./Images/Cumulative_Day_Wise_Target_vs_Sales.png")
    # plt.show()
    plt.close()
    print('13. Cumulative day wise target sales')
