kamrul_branch = ['JESSKF', 'MIRSKF', 'KHLSKF', 'COMSKF', 'PATSKF', 'BSLSKF']
anwar_branch = ['MYMSKF', 'FRDSKF', 'TGLSKF', 'RAJSKF', 'SAVSK', 'BOGSKF']
atik_branch = ['HZJSKF', 'RNGSKF', 'KSGSKF', 'MOTSKF', 'DNJSKF', 'GZPSKF', 'KRNSKF']
nurul_branch = ['VRBSKF', 'NOKSKF', 'SYLSKF', 'MHKSKF', 'MLVSKF', 'FENSKF']
hafizur_branch = ['NAJSKF', 'CTGSKF', 'CTNSKF', 'KUSSKF', 'PBNSKF', 'COXSKF']


def find_to_email(branch_name):
    branch = branch_name
    for i in range(len(kamrul_branch)):
        if kamrul_branch[i]== branch:
            to = 'rejaul.islam@transcombd.com'
            return to

    for i in range(len(anwar_branch)):
        if anwar_branch[i]== branch:
            to = 'anwar_branch@transcombd.com'
            return to

    for i in range(len(atik_branch)):
        if atik_branch[i]== branch:
            to = 'atik_branch@transcombd.com'
            return to

    for i in range(len(nurul_branch)):
        if nurul_branch[i]== branch:
            to = 'nurul_branch@transcombd.com'
            return to

    for i in range(len(hafizur_branch)):
        if hafizur_branch[i]== branch:
            to = 'hafizur_branch@transcombd.com'
            return to

