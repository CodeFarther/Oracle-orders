product = {
    'Product': 'Cod Fillet',
    'Order Value': 345,
    'Running Total': 0,
    'Pallets': [],
    'Chasers': 0,
    'OutSt Total': 0
}

product['Pallets'].append(120)


def get_total(numbers):
    return sum(numbers)


def get_remainder(running_tot, order_num):
    return order_num - running_tot


product['Running Total'] = get_total(product['Pallets'])
product['OutSt Total'] = get_remainder(product['Running Total'], product['Order Value'])

print product['Product'],
print '\t', product['Order Value'],
print '\t', product['Running Total'],
print '\t', product['OutSt Total']
