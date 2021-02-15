
from PIL import Image

def join_all_images():
    imp1 = Image.open("./Images/terms_wise_outstanding.png")
    widthx, heightx = imp1.size
    imp2 = Image.open("./Images/category_wise_credit.png")
    imageSize = Image.new('RGB', (1283, 481))
    imageSize.paste(imp1, (1, 0))
    imageSize.paste(imp2, (widthx + 2, 0))
    imageSize.save("./Images/all_credit.png")

    imp3 = Image.open("./Images/matured_credit.png")
    widthx, heightx = imp1.size
    imp4 = Image.open("./Images/aging_matured_credit.png")

    imageSize = Image.new('RGB', (1283, 481))
    imageSize.paste(imp3, (1, 0))
    imageSize.paste(imp4, (widthx + 2, 0))
    imageSize.save("./Images/all_Matured_credit.png")

    # ---------------------------------------------------------

    imp10 = Image.open("./Images/Category_wise_cash.png")
    widthx, heightx = imp1.size
    imp11 = Image.open("./Images/aging_cash_drop.png")

    imageSize = Image.new('RGB', (1283, 481))
    imageSize.paste(imp10, (1, 0))
    imageSize.paste(imp11, (widthx + 2, 0))
    imageSize.save("./Images/all_cash.png")

    # ------------- Closed to Matured, Matured Credit  ---------------------------

    imp5 = Image.open("./Images/regular_credit.png")
    widthx, heightx = imp1.size
    imp6 = Image.open("./Images/closed_to_matured_credit.png")

    imageSize = Image.new('RGB', (1283, 481))
    imageSize.paste(imp5, (1, 0))
    imageSize.paste(imp6, (widthx + 2, 0))
    imageSize.save("./Images/all_regular_credit.png")

    imp20 = Image.open("./Images/Cause_with_return.png")
    widthx, heightx = imp20.size
    imp21 = Image.open("./Images/LD_MTD_YTD_TARGET_vs_sales.png")
    imageSize = Image.new('RGB', (1283, 482))
    imageSize.paste(imp20, (1, 1))
    imageSize.paste(imp21, (widthx + 2, 1))
    imageSize.save("./Images/Cause_wise_delivery_man_wise_return.png")

    # ------------adding cause wise return and delivery man wise return----------

    imp22 = Image.open("./Images/Delivery_man_wise_return.png")
    widthx, heightx = imp22.size
    imageSize = Image.new('RGB', (1283, 482))
    imageSize.paste(imp22, (1, 1))
    imageSize.save("./Images/new_total_delivery_man_wise_return.png")

    # ------------adding cause wise return and delivery man wise return----------

    imp23 = Image.open("./Images/Day_Wise_Target_vs_Sales.png")
    widthx, heightx = imp23.size
    imageSize = Image.new('RGB', (1283, 482))
    imageSize.paste(imp23, (1, 1))
    imageSize.save("./Images//Day_wise_target_sales.png")

    imp24 = Image.open("./Images/Cumulative_Day_Wise_Target_vs_Sales.png")
    widthx, heightx = imp24.size
    imageSize = Image.new('RGB', (1283, 482))
    imageSize.paste(imp24, (1, 1))
    imageSize.save("./Images/Cumulative_Day_wise_target_sales.png")
    print('all image joined')
