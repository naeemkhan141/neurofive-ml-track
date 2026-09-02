# neurofive-ml-track
Titanic Exploratory Data Analysis using Python and Pandas
## Week 2: Titanic Survival Prediction

Trained a Logistic Regression model using scikit-learn to predict passenger survival.

**Features used:** pclass, age, sibsp, parch, fare, sex

**Approach:**
- Encoded categorical columns (sex, embarked) using pd.get_dummies()
- Split data into 80% training / 20% testing
- Trained a Logistic Regression model
- Evaluated using accuracy score and confusion matrix

**Result:** Achieved 81% accuracy on the test set.

## Week 3: Model Evaluation & Tuning

Added precision, recall, and F1-score evaluation using classification_report.
Used GridSearchCV to tune hyperparameters (C, max_iter).

**Best Parameters:** C=0.1, max_iter=500
**Original Accuracy:** 0.81
**Tuned Accuracy:** 0.8212

## Week 3: Customer Churn Prediction — Working with a Business Problem
Analyzed telecom customer data to predict churn. Top factors: tenure, MonthlyCharges, TotalCharges. Compared Logistic Regression (82% accuracy) vs Decision Tree (77% accuracy). Business use: identify high-risk customers early for retention offers.

Tuning gave a small (~1%) accuracy improvement, showing the default settings were already reasonably good.

## Week 4: Build a Proper ML Pipeline with Feature Engineering
Built a scikit-learn Pipeline using ColumnTransformer (StandardScaler for numerical, OneHotEncoder for categorical) chained with Logistic Regression — achieved 82.19% accuracy, matching the manual approach. Tested 2 new engineered features (AvgMonthlySpend, IsNewCustomer) but they slightly reduced accuracy (81.48%), showing existing features already captured that signal. Final pipeline saved with joblib for reuse.
