# Colorectal Cancer Prediction Pipeline

## 📌 Project Overview
This project focuses on building an **end-to-end machine learning pipeline** for predicting **5-year survival outcomes** in colorectal cancer patients.  
The pipeline covers **data preprocessing, feature selection, model training, deployment via Flask, containerization with Docker, and orchestration using Kubeflow Pipelines**.

Colorectal cancer remains one of the leading causes of cancer-related deaths worldwide. Early detection and risk assessment can significantly improve patient survival rates and treatment outcomes.  
This project leverages real-world patient data to develop a predictive model that can assist healthcare professionals in making informed decisions.

---

## 📊 Dataset
The dataset contains detailed clinical, demographic, and lifestyle factors for colorectal cancer patients.

**Example (first 2 rows)**:

| Patient_ID | Country | Age | Gender | Cancer_Stage | Tumor_Size_mm | Family_History | Smoking_History | Alcohol_Consumption | Obesity_BMI | Diet_Risk | Physical_Activity | Diabetes | Inflammatory_Bowel_Disease | Genetic_Mutation | Screening_History | Early_Detection | Treatment_Type | Survival_5_years | Mortality | Healthcare_Costs | Incidence_Rate_per_100K | Mortality_Rate_per_100K | Urban_or_Rural | Economic_Classification | Healthcare_Access | Insurance_Status | Survival_Prediction |
|------------|---------|-----|--------|--------------|---------------|----------------|-----------------|---------------------|-------------|-----------|-------------------|----------|----------------------------|------------------|-------------------|-----------------|----------------|------------------|----------|------------------|-------------------------|-------------------------|----------------|------------------------|-------------------|-----------------|---------------------|
| 1          | UK      | 77  | M      | Localized    | 69            | No             | No              | Yes                 | Overweight  | Low       | Low               | No       | No                         | No               | Regular           | Yes             | Combination    | Yes              | No       | 54413            | 50                      | 5                       | Urban          | Developed              | Moderate          | Insured         | Yes                 |
| 2          | UK      | 59  | M      | Localized    | 33            | No             | No              | No                  | Overweight  | Moderate  | Low               | No       | No                         | No               | Regular           | No              | Chemotherapy   | Yes              | No       | 76553            | 37                      | 25                      | Urban          | Developing             | High              | Uninsured       | Yes                 |

---

## 🧪 Workflow

### 1. **Data Preprocessing**
- Cleaned and handled missing values.
- Encoded categorical features.
- Scaled numerical features for model consistency.

### 2. **Feature Selection**
- Applied **Chi-Square test** to select the **top 5 most influential features** impacting survival outcomes.

### 3. **Model Training**
- Used supervised learning models to predict **5-year survival**.
- Evaluated performance using accuracy, precision, recall, and F1-score.

### 4. **Flask Web UI**
- Built an interactive web application for predictions.
- Users can input patient details and receive survival probability.

### 5. **Containerization with Docker**
- Packaged the Flask application into a **Docker image** for easy deployment.

### 6. **Pipeline Orchestration with Kubeflow**
- Created a **Kubeflow pipeline** to automate:
  - Data preprocessing
  - Model training
  - Model deployment
- Ensured reproducibility and scalability.

---

## 🛠 Tech Stack
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Web Framework:** Flask
- **Containerization:** Docker
- **Pipeline Orchestration:** Kubeflow Pipelines
- **Data Handling:** Pandas, NumPy
- **Feature Selection:** Chi-Square Test
- **Scaling:** StandardScaler / MinMaxScaler

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/colorectal-cancer-pipeline.git
cd colorectal-cancer-pipeline
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3. Run Flask App
```bash
python app.py
```

### 4. Build Docker Image
```bash
docker build -t colorectal-cancer-prediction .
docker run -p 5000:5000 colorectal-cancer-prediction
```

### 5. Deploy with Kubeflow
- Upload the pipeline file (`cancerpred_pipeline.py`) to your Kubeflow instance.
- Run the pipeline from the Kubeflow UI.

---

## 📈 Results & Insights
- **Top 5 features** identified as most impactful in survival prediction.
- Flask UI enables quick survival probability checks for given patient data.
- Docker + Kubeflow ensures the solution is **scalable, portable, and reproducible**.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Acknowledgments
- Inspiration from colorectal cancer research literature.
- Kubeflow and Scikit-learn open-source communities.
