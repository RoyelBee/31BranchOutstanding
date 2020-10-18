import traceback2

try:
    print("all ok"+66)
except Exception as e:
    error_title = str(e)
    error_details = traceback2.format_exc()
    print(error_title, error_details)
    # mail_sender(error_title, error_details)
