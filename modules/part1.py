from sklearn.cluster import KMeans
from .data import generate_dataset

TOLERANCE = 15
CLUSTERS_PER_MATERIAL = 5

def find_existing_mould(user_height, user_width, selected_material):

    df, _ = generate_dataset()

    # 🔹 Get unique materials
    materials = df["Material"].unique()

    print("\n========== MATERIAL-WISE CLUSTER INFORMATION ==========\n")

    material_clusters = {}

    # 🔹 Create clusters separately for each material
    for material in materials:

        material_df = df[df["Material"] == material]

        X = material_df[["Height", "Width"]]

        kmeans = KMeans(n_clusters=CLUSTERS_PER_MATERIAL, random_state=42)
        kmeans.fit(X)

        centers = kmeans.cluster_centers_
        material_clusters[material] = centers

        print(f"Cluster Info for {material.upper()}:")
        for i, c in enumerate(centers):
            print(f"  Cluster-{i+1} → {int(c[0])} x {int(c[1])}")
        print()

    print("========================================================\n")

    # 🔹 Now match only within selected material
    selected_centers = material_clusters[selected_material]

    for center in selected_centers:
        std_h, std_w = int(center[0]), int(center[1])

        diff_h = user_height - std_h
        diff_w = user_width - std_w

        if abs(diff_h) <= TOLERANCE and abs(diff_w) <= TOLERANCE:
            return {
                "match": True,
                "standard_height": std_h,
                "standard_width": std_w,
                "diff_height": diff_h,
                "diff_width": diff_w
            }

    return {
        "match": False,
        "standard_height": user_height,
        "standard_width": user_width,
        "diff_height": 0,
        "diff_width": 0
    }