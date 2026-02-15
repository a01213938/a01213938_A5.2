# pylint: disable=invalid-name
"""
Módulo para calcular el total de ventas a partir de archivos JSON.
Nombre: Jorge Muñoz Estrada
Matrícula: A01213938
"""

import sys
import json
import time


def load_json_file(file_path):
    """Carga un archivo JSON y maneja errores de lectura."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error al cargar {file_path}: {error}")
        return None


def main():
    """Función principal para el cálculo de ventas."""
    start_time = time.time()

    if len(sys.argv) != 3:
        print("computeSales.py priceCatalogue.json salesRecord.json")
        return

    prices_data = load_json_file(sys.argv[1])
    sales_data = load_json_file(sys.argv[2])

    if prices_data is None or sales_data is None:
        return

    # Crear diccionario de precios para búsqueda rápida O(1)
    price_map = {item['title']: item['price'] for item in prices_data}
    total_sales = 0.0
    errors = []

    for record in sales_data:
        product = record.get('Product')
        quantity = record.get('Quantity')
        if product in price_map:
            total_sales += price_map[product] * quantity
        else:
            errors.append(f"Producto no encontrado: {product}")

    elapsed_time = time.time() - start_time
    # Formatear resultados
    output = [
        "--- TOTAL SALES REPORT ---",
        f"Total Cost: ${total_sales:,.2f}",
        f"Execution Time: {elapsed_time:.4f} seconds",
        "---------------------------"
    ]
    if errors:
        print("\n".join(errors))

    result_text = "\n".join(output)
    print(result_text)

    with open("SalesResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write(result_text)


if __name__ == "__main__":
    main()
