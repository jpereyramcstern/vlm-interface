import csv
# import fanuc.constant as CONSTANT
import constant.picking_demand as picking
import constant.storage_request as storage
import constant.item_master as create_item
import constant.stock_request as stock
import constant.inventory_demand as inventory
import time
from datetime import datetime

def dict_to_csv(path, list_dict):
    with open(path, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for row in list_dict:
            spamwriter.writerow(row)

def make_picking_template(pickind_demand_id, item_number, ordered_quantity, count):
    today = datetime.today()
    item1 = picking.picking_demand_dict1
    item1['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item1['picking_demand_id'] = pickind_demand_id
    item1['serial_number'] = count

    item2 = picking.picking_demand_dict2
    item2['picking_demand_id'] = pickind_demand_id
    item2['item_number'] = item_number
    item2['ordered_quantity'] = ordered_quantity
    item2['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item2['serial_number'] = count + 1
    for x in range(2,21):
        item2[f'csia_{x}'] = ''

    return ([item1.values(), item2.values()])


def make_storage_template(storage_demand_id, item_number, ordered_quantity, count):
    today = datetime.today()
    item1 = storage.storage_request_dict
    item1['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item1['storage_demand_id'] = storage_demand_id
    item1['serial_number'] = count
    
    item2 = storage.storage_request_dict2
    item2['storage_demand_id'] = storage_demand_id
    item2['item_number'] = item_number
    item2['ordered_quantity'] = ordered_quantity
    item2['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item2['serial_number'] = count + 1

    for x in range(2,21):
        item2[f'csia_{x}'] = ''


    return ([item1.values(), item2.values()])


def make_master_item(item_number, quantity_unit, abc_value, desc, count):
    today = datetime.today()
    item1 = create_item.item_dict1
    item1['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item1['serial_number'] = count
    item1['item_number'] = item_number
    item1['quantity_unit'] = quantity_unit
    item1['abc_value'] = abc_value

    item2 = create_item.item_dict2
    item2['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item2['item_number'] = item_number
    item2['serial_number'] = count + 1
    item2['item_description'] = desc

    return ([item1.values(), item2.values()])


def make_stock_template(stock_id, item_number, count):
    today = datetime.today()
    item1 = stock.stock_request_dict
    item1['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item1['serial_number'] = count
    item1['stock_id'] = stock_id
    item1['item_number'] = item_number

    return ([item1.values()])

def make_inventory_template(demandNo, item_number, count):
    today = datetime.today()
    item1 = inventory.inventory_demand_dict
    item1['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item1['serial_number'] = count
    item1['demandNo'] = demandNo

    item2 = inventory.inventory_demand_dict2
    item2['creation_time'] = today.strftime("%y%m%d%H%M%S")
    item2['item_number'] = item_number
    item2['serial_number'] = count + 1
    item2['demandNo'] = demandNo
    for x in range(2,21):
        item2[f'csia_{x}'] = ''

    return ([item1.values(), item2.values()])


picking_template = make_picking_template('picking_demand02', 'HER1', 20, 3)
storage_template = make_storage_template('storage02', 'HER1', 20, 1)
item_template = make_master_item("HER2", 'PCS', '1', 'MILK HERSHEY', 1)
stock_template = make_stock_template('stock02','HER2', 1)
inventory_template = make_inventory_template('storage_demand02','HER2', 1)

vlm_dict = dict_to_csv('./test2.csv', picking_template)
vlm_dict = dict_to_csv('./test3.csv', storage_template)
vlm_dict = dict_to_csv('./test4.csv', item_template)
vlm_dict = dict_to_csv('./test5.csv', stock_template)
vlm_dict = dict_to_csv('./test6.csv', inventory_template)
