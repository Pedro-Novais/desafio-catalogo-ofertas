from typing import Literal

def formate_value(value: str | None) -> float | Literal[None]:
    if not value:
        return None
    
    return "R$ {}".format(value)

def get_porcentage_discount(porcentage):
        if not porcentage:
            return 0
        if porcentage[1] == "%":
             return int(porcentage[0])
        
        new_porcentage = "{}{}".format(porcentage[0], porcentage[1])
        print(new_porcentage)
        try:
            porcenatge_formated = int(new_porcentage)
            return porcenatge_formated
        except Exception as e:
            return 0
        
def get_price_float(price):
    try:
        price = float(price)
        return price
    except Exception as e:
        return 0