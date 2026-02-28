from .data import generate_dataset

def cost_comparison(material, usage_required, moulds_required, height, width):

    _, materials_data = generate_dataset()

    cost_per_m2 = materials_data[material][1]

    area_m2 = (height * width) / 1_000_000

    cost_per_mould = cost_per_m2 * area_m2

    traditional_cost = cost_per_mould * usage_required

    model_cost = cost_per_mould * moulds_required

    savings = traditional_cost - model_cost

    return round(cost_per_mould,2), round(traditional_cost,2), round(model_cost,2), round(savings,2)