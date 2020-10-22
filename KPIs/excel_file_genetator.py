
import numpy as np
import pandas as pd

import Functions.helper_functions as func


def closed_to_matured_data(branch_name):
    ClosedToMaturedcredit_df = pd.read_sql_query("""select CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',
           CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',INVNUMBER as 'Inv Number',
           convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date', CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
           (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)*-1 as 'Matured In Days', OUT_NET as 'Credit Amount'
           from [ARCOUT].dbo.[CUST_OUT]
           join ARCHIVESKF.dbo.CustomerInformation
           on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST
    
           where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash'
            and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)  between -3 and 0
            order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)desc
               , OUT_NET desc
            """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/ClosedToMatured.xlsx', engine='xlsxwriter')
    ClosedToMaturedcredit_df.index = np.arange(1, len(ClosedToMaturedcredit_df) + 1)
    ClosedToMaturedcredit_df.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook = writer.book

    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)

    writer.save()
    print('Data 01: Closed to Matured')


def colsed_to_matured_mail_data(branch_name):
    ClosedToMaturedcredittable = pd.read_sql_query("""
              select top 20 CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',
            CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',INVNUMBER as 'Inv Number',
            convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date', CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
            (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)*-1 as 'Matured In Days', OUT_NET as 'Credit Amount'
            from [ARCOUT].dbo.[CUST_OUT]
            join ARCHIVESKF.dbo.CustomerInformation
            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

            where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash'
                and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)  between -3 and 0
                order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS)desc
                , OUT_NET desc
                           """, func.con, params={branch_name})
    writer = pd.ExcelWriter('./Data/ClosedToMaturedTable.xlsx', engine='xlsxwriter')
    ClosedToMaturedcredittable.index = np.arange(1, len(ClosedToMaturedcredittable) + 1)
    ClosedToMaturedcredittable.to_excel(writer, sheet_name='Sheet1', index=True)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)

    writer.save()
    print('Data 02: Closed to Matured Mail Table')




def aging_matured_data(branch_name):
    AgeingMaturedcredit_df = pd.read_sql_query("""
                           select CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',
                            INVNUMBER as 'Inv Number', convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date',
                             CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
                            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as 'Days Passed',OUT_NET as 'Credit Amount'

                            from [ARCOUT].dbo.[CUST_OUT]
                            join ARCHIVESKF.dbo.CustomerInformation
                            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

                            where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash' and OUT_NET>1
                            and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) >= 1
                            order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) desc
                                            , OUT_NET desc
                             """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/AgingMatured.xlsx', engine='xlsxwriter')
    AgeingMaturedcredit_df.index = np.arange(1, len(AgeingMaturedcredit_df) + 1)
    AgeingMaturedcredit_df.to_excel(writer, sheet_name='Sheet1', index=True)

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)
    writer.save()
    print('Data 03: Aging Matured')


def aging_matured_table(branch_name):
    AgeingMaturedcredittable = pd.read_sql_query("""
                           select top 20 CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',
                             INVNUMBER as 'Inv Number', convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date',
                             CustomerInformation.CREDIT_LIMIT_DAYS as 'Days Limit',
                            datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS as 'Days Passed'
                            ,OUT_NET as 'Credit Amount'
                            from [ARCOUT].dbo.[CUST_OUT]
                            join ARCHIVESKF.dbo.CustomerInformation
                            on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

                            where  [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS<>'Cash' and OUT_NET>1
                            and (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) >= 1
                            order by (datediff([dd] , CONVERT (DATETIME , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1-CREDIT_LIMIT_DAYS) desc
                             , OUT_NET desc
                            """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/AgingMaturedTable.xlsx', engine='xlsxwriter')
    AgeingMaturedcredittable.index = np.arange(1, len(AgeingMaturedcredittable) + 1)
    AgeingMaturedcredittable.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    writer.save()
    print('Data 04: Aging Matured Table ')

def cash_drop_data(branch_name):
    CashDrop_df = pd.read_sql_query("""
                         Select CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',
                         INVNUMBER as 'Inv Number',convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date',
                        datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as 'Days Over', OUT_NET as 'Credit Amount'
                        from [ARCOUT].dbo.[CUST_OUT]
                        join ARCHIVESKF.dbo.CustomerInformation
                        on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

                        where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS='Cash'  and OUT_NET>1
                        and (datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1) >=4
                        order by datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 desc
                          , OUT_NET desc
                         """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/CashDrop.xlsx', engine='xlsxwriter')
    CashDrop_df.index = np.arange(1, len(CashDrop_df) + 1)
    CashDrop_df.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.set_column('A:A', 4)
    worksheet.set_column('B:B', 12)
    worksheet.set_column('C:C', 25)
    worksheet.set_column('D:D', 30)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 17)
    worksheet.set_column('G:G', 14)
    worksheet.set_column('H:H', 18)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('J:J', 20)
    writer.save()
    print('Data 05: Cash Drop')


def cashdrop_table(branch_name):
    CashDroptable_df = pd.read_sql_query("""
                    Select top 20 CUSTOMER as 'Cust ID', CUSTNAME as 'Cust Name',CustomerInformation.TEXTSTRE1 as 'Address', CustomerInformation.MSOTR as 'Territory',
                     INVNUMBER as 'Inv Number',convert(varchar,convert(datetime,(convert(varchar(8),INVDATE,112))),106)  as 'Inv Date',
                    datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 as 'Days Over', OUT_NET as 'Credit Amount'
                    from [ARCOUT].dbo.[CUST_OUT]
                    join ARCHIVESKF.dbo.CustomerInformation
                    on [CUST_OUT].CUSTOMER = CustomerInformation.IDCUST

                    where [ARCOUT].dbo.[CUST_OUT].AUDTORG like ? and TERMS='Cash'  and OUT_NET>1
                    and (datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1) >=4
                    order by datediff([dd] , CONVERT (DATE , LTRIM(cust_out.INVDATE) , 102) , GETDATE())+1 desc
                     , OUT_NET desc
                    """, func.con, params={branch_name})

    writer = pd.ExcelWriter('./Data/CashDropTable.xlsx', engine='xlsxwriter')
    CashDroptable_df.index = np.arange(1, len(CashDroptable_df) + 1)
    CashDroptable_df.to_excel(writer, sheet_name='Sheet1', index=True)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    writer.save()
    print('Data 06: Cash Drop Table')


