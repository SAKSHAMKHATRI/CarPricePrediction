# 🚗 Used Car Price Prediction

A Machine Learning web application that predicts the selling price of a used car based on its specifications. The application is built using **Python, Scikit-learn, Streamlit, and Random Forest Regressor**.

Live Demo: https://carpriceprediction-djvpnrrmb9mkcsc49ru8on.streamlit.app/
---

## 📌 Features

- Predicts the selling price of a used car.
- Dynamic Brand and Model selection.
- User-friendly Streamlit interface.
- Machine Learning pipeline with preprocessing.
- Random Forest Regressor for accurate predictions.
- Cross-validation for model evaluation.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib

---

## 📂 Dataset

**Dataset:** CarDekho Used Car Dataset

The dataset contains information such as:

- Brand
- Model
- Vehicle Age
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission Type
- Mileage
- Engine
- Max Power
- Seats
- Selling Price

---

## 🤖 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Selection
4. Train-Test Split
5. Data Preprocessing
6. Model Training (Random Forest Regressor)
7. Model Evaluation
8. Cross Validation
9. Save Model using Joblib
10. Deploy using Streamlit

---

## 📊 Model Performance

| Metric | Score |
|--------|-------:|
| R² Score | **0.9331** |
| MAE | **₹100,000 (approx.)** |
| RMSE | **₹224,000 (approx.)** |
| 5-Fold Cross Validation | **0.8769** |

---

## 📁 Project Structure

```
CarPricePrediction/
│
├── app.py
├── train.ipynb
├── README.md
├── requirements.txt
│
├── data/
│   └── cardekho_dataset.csv
│
├── model/
│   └── car_price_model.joblib
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-link>
```

Move to the project folder:

```bash
cd CarPricePrediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Better UI Design
- Deployment on Streamlit Cloud
- Price Range Visualization
- Car Image Support
- More ML Models for Comparison

---

## 👨‍💻 Author

**Saksham Khatri**

Computer Science Engineering (AI & ML)

Chitkara University
