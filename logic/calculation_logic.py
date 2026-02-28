import math
from logic.material_data import materials, AVAILABLE_HEIGHT, AVAILABLE_WIDTH, TOLERANCE


def check_dimension_match(input_h, input_w):
    if abs(input_h - AVAILABLE_HEIGHT) <= TOLERANCE and \
       abs(input_w - AVAILABLE_WIDTH) <= TOLERANCE:
        return True
    return False


def calculate_moulds(quantity, material):
    reuse = materials[material]["reusability"]
    return math.ceil(quantity / reuse)


def calculate_cost(height, width, moulds, material):
    area = (height / 1000) * (width / 1000)  # convert mm to meter
    cost_per_sqm = materials[material]["cost_per_sqm"]
    return area * cost_per_sqm * moulds