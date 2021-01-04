
import setup as action
import send_error_mail as error
import schedule

def dailyOutstandingJob():
    # # ------- kamrul Branches -----------------------------------------------(6)
    # # -----------------------------------------------------------------------

    # kamrul_branch = ['MIRSKF','KHLSKF','FENSKF','SAVSKF','RNGSKF','DNJSKF']
    #
    try:
        action.generate_kamrul_mail('MIRSKF', 'kamrul.ahsan@tdcl.transcombd.com')
    except:
        error.send_error_msg('MIRSKF')

    try:
        action.generate_kamrul_mail('KHLSKF', 'kamrul.ahsan@tdcl.transcombd.com')
    except:
        error.send_error_msg('KHLSKF')
    #
    try:
        action.generate_kamrul_mail('FENSKF', 'kamrul.ahsan@tdcl.transcombd.com')
    except:
        error.send_error_msg('FENSKF')

    try:
        action.generate_kamrul_mail('SAVSKF', 'kamrul.ahsan@tdcl.transcombd.com')
    except:
        error.send_error_msg('SAVSKF')

    try:
        action.generate_kamrul_mail('RNGSKF', 'kamrul.ahsan@tdcl.transcombd.com')
    except:
        error.send_error_msg('RNGSKF')

    try:
        action.generate_kamrul_mail('DNJSKF', 'kamrul.ahsan@tdcl.transcombd.com')
    except:
        error.send_error_msg('DNJSKF')

    # ------------- Anwar   ----------------------------------------------- (4)
    # ---------------------------------------------------------------------

    anwar_branch = ['KUSSKF','PBNSKF','SYLSKF','TGLSKF']

    try:
        action.generate_kamrul_mail('KUSSKF', 'anwar.hussain@tdcl.transcombd.com')
    except:
        error.send_error_msg('KUSSKF')

    try:
        action.generate_kamrul_mail('PBNSKF', 'anwar.hussain@tdcl.transcombd.com')
    except:
        error.send_error_msg('PBNSKF')

    try:
        action.generate_kamrul_mail('SYLSKF', 'anwar.hussain@tdcl.transcombd.com')
    except:
        error.send_error_msg('SYLSKF')

    try:
        action.generate_kamrul_mail('TGLSKF', 'anwar.hussain@tdcl.transcombd.com')
    except:
        error.send_error_msg('TGLSKF')


    # ---------------- Atik   ---------------------------------------------------- (5)
    # ----------------------------------------------------------------------------

    atik_branch = ['COXSKF', 'JESSKF', 'CTGSKF', 'CTNSKF', 'KRNSKF']
    try:
        action.generate_kamrul_mail('COXSKF', 'md.atikullaha@tdcl.transcombd.com')
    except:
        error.send_error_msg('COXSKF')

    try:
        action.generate_kamrul_mail('JESSKF', 'md.atikullaha@tdcl.transcombd.com')
    except:
        error.send_error_msg('JESSKF')

    try:
        action.generate_kamrul_mail('CTGSKF', 'md.atikullaha@tdcl.transcombd.com')
    except:
        error.send_error_msg('CTGSKF')

    try:
        action.generate_kamrul_mail('CTNSKF', 'md.atikullaha@tdcl.transcombd.com')
    except:
        error.send_error_msg('CTNSKF')

    try:
        action.generate_kamrul_mail('KRNSKF', 'md.atikullaha@tdcl.transcombd.com')
    except:
        error.send_error_msg('KRNSKF')


    # # ------------------- Nurul ---------------------------------------------- (6)
    ## -------------------------------------------------------------------------

    nurul_branch = ['MYMSKF','NAJSKF','KSGSKF','FRDSKF','GZPSKF']

    try:
        action.generate_kamrul_mail('MYMSKF', 'nurul.amin@tdcl.transcombd.com')
    except:
        error.send_error_msg('MYMSKF')

    try:
        action.generate_kamrul_mail('NAJSKF', 'nurul.amin@tdcl.transcombd.com')
    except:
        error.send_error_msg('NAJSKF')

    try:
        action.generate_kamrul_mail('KSGSKF', 'nurul.amin@tdcl.transcombd.com')
    except:
        error.send_error_msg('KSGSKF')

    try:
        action.generate_kamrul_mail('FRDSKF', 'nurul.amin@tdcl.transcombd.com')
    except:
        error.send_error_msg('FRDSKF')

    try:
        action.generate_kamrul_mail('GZPSKF', 'nurul.amin@tdcl.transcombd.com')
    except:
        error.send_error_msg('GZPSKF')

    try:
        action.generate_kamrul_mail('GPLSKF', 'nurul.amin@tdcl.transcombd.com')
    except:
        error.send_error_msg('GPLSKF')

    # ------------------- Hafizur  --------------------------------------------- (5)
    ## ------------------------------------------------------------------------
    hafizur_branch = ['BOGSKF', 'MLVSKF', 'MOTSKF', 'NOKSKF', 'RAJSKF' ]

    try:
        action.generate_kamrul_mail('BOGSKF', 'sheikh.hafizur@tdcl.transcombd.com')
    except:
        error.send_error_msg('BOGSKF')

    try:
        action.generate_kamrul_mail('MLVSKF', 'sheikh.hafizur@tdcl.transcombd.com')
    except:
        error.send_error_msg('MLVSKF')
    #
    try:
        action.generate_kamrul_mail('MOTSKF', 'sheikh.hafizur@tdcl.transcombd.com')
    except:
        error.send_error_msg('MOTSKF')

    try:
        action.generate_kamrul_mail('NOKSKF', 'sheikh.hafizur@tdcl.transcombd.com')
    except:
        error.send_error_msg('NOKSKF')

    try:
        action.generate_kamrul_mail('RAJSKF', 'sheikh.hafizur@tdcl.transcombd.com')
    except:
        error.send_error_msg('RAJSKF')

    # # -------------------- MR.Abdur Rab ------------------------------------ (5)
    arab = ['CNDSKF','COMSKF','PATSKF','BSLSKF','BBRSKF','TEJSKF']

    try:
        action.generate_kamrul_mail('CNDSKF', 'rab.abdur@tdcl.transcombd.com')
    except:
        error.send_error_msg('CNDSKF')

    try:
        action.generate_kamrul_mail('COMSKF', 'rab.abdur@tdcl.transcombd.com')
    except:
        error.send_error_msg('COMSKF')

    try:
        action.generate_kamrul_mail('PATSKF', 'rab.abdur@tdcl.transcombd.com')
    except:
        error.send_error_msg('PATSKF')

    try:
        action.generate_kamrul_mail('BSLSKF', 'rab.abdur@tdcl.transcombd.com')
    except:
        error.send_error_msg('BSLSKF')

    try:
        action.generate_kamrul_mail('BBRSKF', 'rab.abdur@tdcl.transcombd.com')
    except:
        error.send_error_msg('BBRSKF')

    try:
        action.generate_kamrul_mail('TEJSKF', 'rab.abdur@tdcl.transcombd.com')
    except:
        error.send_error_msg('TEJSKF')


schedule.every().day.at("15:20").do(dailyOutstandingJob)

while True:
    schedule.run_pending()


