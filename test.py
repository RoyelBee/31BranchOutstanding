import KPIs.banner as b
import os

b_list =  ['JESSKF', 'MIRSKF', 'KHLSKF']


for i in range(len(b_list)):
    try:
        if os.path.exists("./Images/banner_ai.png"):
            os.remove("./Images/banner_ai.png")
            print('banner removed')

            b.create_banner_fig(b_list[i])
            print('new banner created')
        else:

            b.create_banner_fig(b_list[i])
            print('new banner created')
    except:
        print('hi')