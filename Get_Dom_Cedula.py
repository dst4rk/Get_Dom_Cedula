import requests
import json
from bs4 import BeautifulSoup
import argparse

def id_numer(url,cedula_num):
    cedula = str(cedula_num)
    results(url,cedula)

def range_id(url,start,end):
    for i in range(start,end+1):
        numero = str(i)
        cedula = numero.zfill(10)
        results(url,cedula)

def get_url(url): 
    cedula = "00000000000"
    while cedula != "99999999999":
        for i in range(40238000000, 40299999999):
            numero = str(i)
            cedula = numero.zfill(10)
            results(url,cedula)

def results(url,cedula):
    response = requests.get(url + cedula)
    soup = BeautifulSoup(response.content, "html.parser")
    soup = str(soup)
    if soup != '{"ok":false}':
        json_string = soup 
        data = json.loads(json_string)
        cedula1 = data['Cedula']
        nombres = data['Nombres']
        apellido1 = data['Apellido1']
        apellido2 = data['Apellido2']
        fecha_nacimiento = data['FechaNacimiento']
        lugar_nacimiento = data['LugarNacimiento']
        foto = data['foto']
        print("")
        print('Cedula:', cedula1)
        print('Nombre:', nombres, apellido1, apellido2)
        print('Fecha de Nacimiento:', fecha_nacimiento)
        print('Lugar de Nacimiento:', lugar_nacimiento)
        print('Foto:', foto)

def options():
    parser = argparse.ArgumentParser(description="Herramienta para realizar diferentes opciones con una cadena")
    parser.add_argument("--iterate", action="store_true", help="Itera a través de todos los 0 hasta llegar a 1000000000")
    parser.add_argument("--range", type=int, nargs=2, help="Define un rango entre 000000000 y 1000000000")
    parser.add_argument("--number", type=int, help="Reemplaza 000000000 por la entrada del usuario")
    args = parser.parse_args()
    if args.iterate:
        get_url("http://api.adamix.net/apec/cedula/")
    elif args.range:
        start,end = args.range
        range_id("http://api.adamix.net/apec/cedula/",start,end)
    elif args.number:
        id_numer("http://api.adamix.net/apec/cedula/",args.number) 

def run():
    options()


if __name__ == '__main__':
    run()