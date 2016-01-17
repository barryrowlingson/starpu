import openpyxl as op
import re

def get_weights(path):
    f = op.load_workbook(path)
    sheet = f['STAR-PUs']
    idxs = get_sect_cells('D6') # First cell containing section code is D6
    ranges = []
    for ix in idxs:
        ranges.append(get_cells_range(ix))
    weights = {}
    for idx, cell_range in ranges:
        for section in re.findall(r'(\d[\.\d]+)', str(sheet[idx].value)):
            weights[section] =  parse_weight(sheet, cell_range)
    return weights

def get_sect_cells(first):
    """There are 25 different weights, calcs the 'key' cell index"""
    sectionlist = []
    res = re.fullmatch(r"([A-Z])([0-9]+)", first)
    for i in range(25):
        sectionlist.append(res.group(1) + str(int(res.group(2)) + 15 * i))
    return sectionlist
    
     
def get_cells_range(idx):
    res = re.fullmatch(r"([A-Z])([0-9]+)", idx)
    first = chr(ord(res.group(1)) - 1) + str(int(res.group(2)) + 3)
    last = chr(ord(res.group(1)) + 1) + str(int(res.group(2)) + 11)
    return (idx, first + ':' + last)

def parse_weight(sheet, cell_range):
    weight = {}
    for age, m, f in sheet.iter_rows(cell_range):
        weight[age.value] = (m.value, f.value)
    return weight
    
if __name__ == '__main__':
    get_weights('PrescribingUnits2013.xlsx')