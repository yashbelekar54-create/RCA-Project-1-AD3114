# Food Delivery Customer Spending Prediction Using Linear Regression

## 1. Project Overview

This project predicts the yearly spending of food-delivery customers using Machine Learning regression algorithms.

It uses the **Food Delivery Customers Dataset** to understand how customer behaviour and platform usage influence yearly spending.

Two regression techniques are explored and compared:

- Simple Linear Regression
- Multiple Linear Regression

## 2. Problem Statement

Food-delivery businesses need to understand customer behaviour to improve marketing and retention. This project predicts the yearly amount (INR) spent by customers from order frequency, time on the mobile app, time on the website and membership duration.

## 3. Project Objectives

- Understand and analyze the customer dataset.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Identify relationships between independent and dependent variables.
- Implement Simple Linear Regression.
- Implement Multiple Linear Regression.
- Evaluate model performance using regression metrics.
- Predict yearly customer spending for new customers.

## 4. Dataset Description

**Dataset Name:** `Food Delivery Customers.csv`

The dataset contains 500 customer records and 8 columns.

> ⚠️ The dataset is **synthetic**. It was generated with `generate_dataset.py` (seeded, fully reproducible). Emails use `example.com` and no real customers are included.

| Column | Description |
| --- | --- |
| Email | Customer email (placeholder) |
| City | Customer city |
| Avatar | Customer avatar colour label |
| Avg. Orders per Month | Average number of orders per month |
| Time on App | Minutes per session on the mobile app |
| Time on Website | Minutes per session on the website |
| Length of Membership | Years as a member |
| Yearly Amount Spent | Total yearly spending in INR (target) |

**Independent variables (X):** Avg. Orders per Month, Time on App, Time on Website, Length of Membership

**Dependent variable (Y):** Yearly Amount Spent

## 5. Machine Learning Algorithms

**Simple Linear Regression:** `Y = b0 + b1X` – uses the single feature most correlated with spending (Length of Membership).

**Multiple Linear Regression:** `Y = b0 + b1X1 + b2X2 + b3X3 + b4X4` – uses all four numeric features.

## 6. Technologies and Libraries Used

- Python, Jupyter Notebook / Google Colab / VS Code
- Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

## 7. Project Workflow

1. Import required Python libraries.
2. Load the dataset.
3. Explore the dataset using Pandas.
4. Check missing values and duplicate records.
5. Perform Exploratory Data Analysis.
6. Visualize relationships using scatter plots, a correlation heatmap and a pair plot.
7. Select independent and dependent variables.
8. Split the dataset into training and testing sets (70/30).
9. Build a Simple Linear Regression model.
10. Build a Multiple Linear Regression model.
11. Evaluate both models.
12. Visualize actual vs predicted values and residuals.
13. Predict spending for new customers.
14. Save the trained model.

## 8. Model Evaluation Metrics

| Metric | Purpose |
| --- | --- |
| MAE | Average absolute prediction error |
| MSE | Average squared prediction error |
| RMSE | Prediction error in the target's units (INR) |
| R² Score | Share of variance explained by the model |

## 9. Results (from the executed notebook)

Test set of 150 customers (`random_state=101`):

| Model | MAE (INR) | RMSE (INR) | R² |
| --- | --- | --- | --- |
| Simple LR (Length of Membership) | 5,707 | 7,093 | 0.337 |
| Multiple LR (4 features) | 3,001 | 3,762 | 0.814 |

Multiple LR coefficients (extra yearly spend per 1-unit increase): Length of Membership ≈ 6,785, Avg. Orders per Month ≈ 3,197, Time on App ≈ 2,088, Time on Website ≈ 79.

## 10. Installation and Setup

```bash
cd food-delivery-customer-spending-prediction
pip install -r requirements.txt
jupyter notebook
```

Open `Food_Delivery_Spending_Prediction_Linear_Regression.ipynb` and run the cells in order. The notebook is saved with its outputs, so results can be read without re-running. To regenerate the data: `python generate_dataset.py`.

## 11. Project Structure

```
food-delivery-customer-spending-prediction/
│
├── Food Delivery Customers.csv
├── Food_Delivery_Spending_Prediction_Linear_Regression.ipynb
├── generate_dataset.py
├── multiple_linear_regression_model.pkl
├── requirements.txt
└── README.md
```

## 12. Output Included in the Notebook

- Dataset information and statistical summary.
- Missing value and duplicate checks.
- Correlation heatmap, scatter plots and pair plot.
- Simple and Multiple Linear Regression models with coefficients.
- Metrics comparison table.
- Actual vs predicted plots and residual analysis.
- Predicted yearly spending for new customers.

## 13. Conclusion

Multiple Linear Regression (R² ≈ 0.81) predicts yearly spending far better than Simple Linear Regression (R² ≈ 0.34), showing the value of using several relevant features. Membership length, app time and order frequency drive spend; website time has almost no effect.

## 14. Future Improvements

- Ridge and Lasso Regression.
- Feature selection and hyperparameter tuning.
- Compare additional regression algorithms.
- Streamlit dashboard and web deployment.

---

Structure inspired by HardikRavriya/ecommerce-customer-spending-prediction.
