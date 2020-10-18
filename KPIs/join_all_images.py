import matplotlib.pyplot as plt
import pandas as pd
import os

dirpath = os.path.dirname(os.path.realpath(__file__))

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from math import log, floor
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc as db
import xlrd
from matplotlib.patches import Patch
from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime as dd
from PIL import Image
from datetime import datetime

import Functions.helper_functions as func


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
