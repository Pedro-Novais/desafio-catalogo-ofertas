import sqlite3
import os
from typing import Optional

from sqlite3 import Connection

from django.http import JsonResponse
from django.views import View

from .utils import (
    format_value,
    get_price_float,
    get_porcentage_discount
)

class ProductApi(View):
    def get(self, request) -> JsonResponse:
        try:
            dir_script = os.path.dirname(os.path.abspath(__file__))
            dir_database = os.path.join(dir_script, '..', '..', 'database', 'data.db')

            conn = sqlite3.connect(dir_database)
            products = self.get_products(conn)
            
            return JsonResponse(products, safe=False)

        except Exception as e:
            return JsonResponse({}, safe=False)
    
    def get_products(self, conn: Connection) -> list[Optional[dict]]:
        try:
            list_products = []
            cursor = conn.cursor()

            msg_get_products = """
            SELECT * FROM products
            """

            cursor.execute(msg_get_products)
            products = cursor.fetchall()

            if not products:
                return []
            
            column_names = [desc[0] for desc in cursor.description]  

            for product in products:
                data = dict(zip(column_names, product))  
            
                price_full_formated = format_value(value=data.get("price_full"))
                price_with_discount_formated = format_value(value=data.get("price_final"))
                porcentage_formated = get_porcentage_discount(data.get("porcentage_discount"))
                price_float = get_price_float(data.get('price_full'))

                list_products.append({
                    "image": data.get("image"), 
                    "name": data.get("name"),
                    "price_full": price_full_formated,
                    "instalments": data.get("installments"), 
                    "link": data.get("link"),
                    "price_with_discount": price_with_discount_formated,
                    "porcentage_discount": data.get("porcentage_discount"), 
                    "type_ship_full": int(data.get("type_ship")),
                    "ship_free": data.get("ship_free"),
                    "price": price_float,
                    "porcentage": porcentage_formated
                })

            cursor.fetchall()
            cursor.close()

            return list_products
        
        except Exception as e:
            print("Erro ao resgatar dados do banco: {}".format(e))