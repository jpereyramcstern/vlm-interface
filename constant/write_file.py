import csv
import fanuc.constant as CONSTANT

## Read File


# columns = columns.split(',')

# print(columns)

# ETL
## Extract information
def csv_to_dict(path):
    vlm_dict = {}
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in (spamreader):
            for i, col in enumerate(row):
                vlm_dict[CONSTANT.COLUMNS_CVS_VLM[i]] = col
    return vlm_dict

# print(vlm_dict)

## Parse File

# Program number
# item number
# Quantity
# tray height
# X coordinate (half x1, x2)
# Y corodinate (half y1, y2)

# Transform
def output(vlm_dict):
    output = {}
    output['program_number'] = 0
    output['item_number'] = vlm_dict['ITEMNO']
    output['qty'] = vlm_dict['QTY']
    output['tray_height'] = vlm_dict['TRAYHEIGHT']
    output['x'] = (float(vlm_dict['X1VALUE']) + float(vlm_dict['X2VALUE'])) / 2
    output['y'] = (float(vlm_dict['Y1VALUE']) + float(vlm_dict['Y2VALUE'])) / 2
    return output


# Load
def send_to_fanuc(payload):


def main(path = '../vlm/documents/BoxPosition.csv'):
    # Start Robot

    # Send Program ID

    # Send Instructions



vlm_dict = csv_to_dict('../vlm/documents/BoxPosition.csv')
output_dict = output(vlm_dict)

# Inventory Demand
inventory_demand_dict = dict({
    server: 'HOST',
    program: 'WAMAS',
    serial_number: 1,
    creation_time: '20201024193053',
    record_type: 'LOGIMATINVD00005'
    demandNo: '',
    clientId: '',
    invetory_demand: '',
    priority: '',
    noteNo: '',
    info: '',
    info2: ''
})

# Inventory Demand
inventory_demand_dict = dict({
    host: 'HOST',
    program: 'WAMAS',
    serial_number: 1,
    creation_time: '20201024193053',
    record_type: 'LOGIMATINVD00005'
    demandNo: '',
    clientId: '',
    invetory_demand: '',
    priority: '',
    noteNo: '',
    info: '',
    info2: ''
})

print(output_dict)