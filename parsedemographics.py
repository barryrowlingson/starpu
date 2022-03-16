import openpyxl as op

def get_demographics(path):
    wb = op.load_workbook(path)
    sheet = wb['Practice']
    demogs = {}
    for row in sheet.iter_rows(4):
        x = parse_row(row)
        if type(x) == type({}):
            demogs[row[0].value] = x
    return demogs
    
def parse_row(row):
    for item in row:
        if type(item.value) == type(None):
            return False
    demog = {'0-4':0,'5-14':0,'15-24':0,'25-34':0,'35-44':0,'45-54':0,'55-64':0,'65-74':0,'75+':0}
    demog['0-4'] = (row[2].value, row[21].value)
    demog['5-14'] = (row[3].value + row[4].value, row[22].value + row[23].value)
    demog['15-24'] = (row[5].value + row[6].value, row[24].value + row[25].value)
    demog['25-34'] = (row[7].value + row[8].value, row[26].value + row[27].value)    
    demog['35-44'] = (row[9].value + row[10].value, row[28].value + row[29].value)
    demog['45-54'] = (row[11].value + row[12].value, row[30].value + row[31].value)
    demog['55-64'] = (row[13].value + row[14].value, row[32].value + row[33].value)
    demog['65-74'] = (row[15].value + row[16].value, row[34].value + row[35].value)
    demog['75+'] = (row[17].value + row[18].value + row[19].value + row[20].value + row[21].value, row[36].value + row[37].value + row[38].value + row[39].value + row[40].value)
    return demog

def main():
    print(get_demographics('PublicHealthEngland-Data.xlsx'))
if __name__ == '__main__':
    main()
