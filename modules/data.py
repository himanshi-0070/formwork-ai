import pandas as pd
import numpy as np

def generate_dataset(n=2000):

    np.random.seed(42)

    materials_data = {
        "Steel": (20, 100),
        "Aluminium": (18, 90),
        "Plywood": (10, 60),
        "Plastic": (12, 50),
        "Timber": (8, 40),
        "FRP": (15, 85),
        "HDO": (9, 55),
        "Rubber": (14, 75),
        "Composite": (16, 95),
        "GI Sheet": (17, 80)
    }

    data = []

    for _ in range(n):
        height = np.random.randint(400, 1000)
        width = np.random.randint(400, 1000)
        material = np.random.choice(list(materials_data.keys()))
        reuse, cost = materials_data[material]

        data.append([height, width, material, reuse, cost])

    df = pd.DataFrame(data, columns=[
        "Height", "Width",
        "Material", "Reusability", "Cost_per_m2"
    ])

    return df, materials_data