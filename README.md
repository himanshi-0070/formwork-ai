# 🏗 AI-Based Formwork Optimization System

An AI-powered system that optimizes construction mould (formwork) usage 
using Machine Learning and reusability logic to reduce cost and improve efficiency.

---

## 🚀 Project Overview

In construction projects, moulds (formwork panels) are often purchased repeatedly 
without considering standard dimensions and material reusability.

This system solves that problem by:

- Standardizing mould dimensions using KMeans Clustering
- Creating separate clusters for each construction material
- Checking if an existing mould can be reused (±15mm tolerance)
- Calculating required moulds based on reusability
- Comparing Traditional Cost vs AI Optimized Cost
- Showing total savings

---

## 🧠 Core Architecture

### 🔹 Part 1 – Material-wise Dimension Clustering

- 2000 synthetic dataset generated
- 10 construction materials included
- Each material has independent clusters
- KMeans clustering used for dimension grouping
- Tolerance rule: ±15mm

Example:

Manual Input: 490 x 510  
Standard Cluster: 500 x 500  

Result:
- Height Difference: -10 mm
- Width Difference: +10 mm
- Existing mould can be reused ✅

---

### 🔹 Part 2 – Reusability Optimization

Instead of buying moulds for every usage cycle:

Moulds Required = ceil(Usage Required / Reusability)

Example:

Reusability = 20  
Usage Required = 40  

Moulds Needed = 2 (NOT 40)

This significantly reduces unnecessary purchases.

---

### 🔹 Part 3 – Cost Comparison

Traditional Cost:
Cost per mould × Total Usage

Optimized Model Cost:
Cost per mould × Moulds Required

Savings:
Traditional Cost − Model Cost

Example:

If cost per mould = ₹100  
Usage = 40  

Traditional Cost = ₹4000  
Optimized Cost = ₹200  
Savings = ₹3800  

---

## 🏗 Materials Included

- Steel  
- Aluminium  
- Plywood  
- Plastic  
- Timber  
- FRP  
- HDO  
- Rubber  
- Composite  
- GI Sheet  

Each material has:
- Defined reusability factor
- Defined cost per square meter

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Scikit-learn (KMeans)  
- NumPy  
- Pandas  

---

## 📂 Project Structure

formwork_ai_project/

│── app.py  
│  
├── modules/  
│     ├── __init__.py  
│     ├── data.py  
│     ├── part1.py  
│     ├── part2.py  
│     ├── part3.py  

---

## ▶ How to Run the Project

### 1️⃣ Create Virtual Environment

python -m venv venv

### 2️⃣ Activate Environment

Windows:
venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install streamlit scikit-learn pandas numpy

### 4️⃣ Run Application

python -m streamlit run app.py

---

## 📊 System Workflow

User Input  
↓  
Material-wise Clustering  
↓  
Existing Mould Detection  
↓  
Reusability Calculation  
↓  
Cost Comparison  
↓  
Savings Output  

---

## 💰 Business Impact

- Reduces unnecessary mould purchases  
- Optimizes material utilization  
- Minimizes construction cost  
- Promotes sustainable construction practices  

---

## 📌 Future Enhancements

- Cluster visualization graphs  
- Real construction dataset integration  
- Adjustable tolerance level  
- Cloud deployment  

---

## 👩‍💻 Developed For

AI-Based Construction Optimization Project  
Academic & Industrial Research Purpose
