import re
from typing import Literal

def formate_value(value: str | None) -> float | Literal[None]:
    if not value:
        return None
    
    return "R$ {}".format(value)