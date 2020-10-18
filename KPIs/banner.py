
import pandas as pd

from PIL import Image, ImageDraw, ImageFont
import pytz
import datetime as dd
from PIL import Image
from datetime import datetime

import Functions.helper_functions as func

def create_banner(branch_name):
    date = datetime.today()
    day = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
    tz_NY = pytz.timezone('Asia/Dhaka')
    datetime_BD = datetime.now(tz_NY)
    time = datetime_BD.strftime("%I:%M %p")
    date = datetime.today()
    x = dd.datetime.now()
    day = str(date.day) + '-' + str(x.strftime("%b")) + '-' + str(date.year)
    tz_NY = pytz.timezone('Asia/Dhaka')
    datetime_BD = datetime.now(tz_NY)
    time = datetime_BD.strftime("%I:%M %p")
    img = Image.open("./Images/new_ai.png")
    title = ImageDraw.Draw(img)
    timestore = ImageDraw.Draw(img)
    tag = ImageDraw.Draw(img)
    branch_name_holder = ImageDraw.Draw(img)

    font = ImageFont.truetype("./Images/Stencil_Regular.ttf", 60, encoding="unic")
    font1 = ImageFont.truetype("./Images/ROCK.ttf", 50, encoding="unic")
    font2 = ImageFont.truetype("./Images/ROCK.ttf", 35, encoding="unic")
    branch = branch_name
    branchname_generator_df = pd.read_sql_query("""select branch,ndmname,branchname from ndm where branch like ? """,
                                                func.con, params={branch})

    ndmname_generator = branchname_generator_df['ndmname']
    branch_name = branchname_generator_df['branchname']

    tag.text((25, 8), 'SK+F', (255, 255, 255), font=font)
    branch_name_holder.text((25, 270),'BRANCH: ' + branch_name[0], (255, 209, 0), font=font1)
    timestore.text((25, 435), time + "\n" + day, (255, 255, 255), font=font2)
    timestore.text((27, 380), 'NDM : ' + ndmname_generator[0], (255, 165, 0), font=font2)
    img.save('./Images/banner_ai.png')
    print('Fig 01: Banner Created')