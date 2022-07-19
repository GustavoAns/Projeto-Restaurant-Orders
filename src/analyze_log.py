from csv import DictReader
from collections import Counter

def read_csv(path):
    with open(path, encoding="utf-8") as file:
        fieldnames = ['cliente', 'pedido', 'dia']
        salesList = DictReader(file, fieldnames=fieldnames)
        return [row for row in salesList]

def best_seller(allSales, name = "maria"):
    bestSeller = []
    for sale in allSales:
        if sale['cliente'] == name:
            bestSeller.append(sale['pedido'])
    return Counter(bestSeller).most_common(1)[0][0]

def how_many_request(allSales, name = "arnaldo", pedido = "hamburguer"):
    request_quant = 0
    for sale in allSales:
        if sale['cliente'] == name and sale['pedido'] == pedido:
            request_quant += 1
    return request_quant

def never_requested(allSales, name = "joao"):
    menu = set()
    requested = set()
    for sale in allSales:
        menu.add(sale['pedido'])
        if sale['cliente'] == name:
            requested.add(sale['pedido'])
    return menu.difference(requested)

def day_never_used(allSales, name = "joao"):
    menu = set()
    visited = set()
    for sale in allSales:
        menu.add(sale['dia'])
        if sale['cliente'] == name:
            visited.add(sale['dia'])
    return menu.difference(visited)

def write_txt_w(path, data):
    with open(path, 'w') as file:
        for line in data:
            file.write(str(line) + '\n')
        
def analyze_log(path_to_file):
    file_type = path_to_file.split(".")[-1]
    if file_type != "csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        data = []
        allSales = read_csv(path_to_file)
        data.append(best_seller(allSales))
        data.append(how_many_request(allSales))
        data.append(never_requested(allSales))
        data.append(day_never_used(allSales))
        write_txt_w('data/mkt_campaign.txt', data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
