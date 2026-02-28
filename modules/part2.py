import math
from .data import generate_dataset

def calculate_moulds_required(material, usage_required):

    _, materials_data = generate_dataset()

    reusability = materials_data[material][0]

    moulds_needed = math.ceil(usage_required / reusability)

    return moulds_needed, reusability