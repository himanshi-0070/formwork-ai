import json

def generate_erp_output(material, moulds_required, total_cost):

    data = {
        "Material": material,
        "Moulds_to_Procure": moulds_required,
        "Total_Cost": total_cost
    }

    return json.dumps(data, indent=4)
