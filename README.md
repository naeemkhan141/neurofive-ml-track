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

## Week 4: Ensemble Learning — Random Forest vs XGBoost
Trained Random Forest (79.21% accuracy) and XGBoost (79.84% accuracy) on the churn dataset, compared against Logistic Regression (82.19%) and Decision Tree (77%). Random Forest ranked numerical features (TotalCharges, tenure, MonthlyCharges) highest, while XGBoost prioritized categorical features (InternetService_Fiber optic, Contract_Month-to-month). Despite being more complex, both ensemble models underperformed the simpler Logistic Regression on this dataset — showing model complexity doesn't guarantee better results on smaller/simpler datasets.

| Model | Metric | Score |
|---|---|---|
| Logistic Regression | Accuracy | 82.19% |
| Decision Tree | Accuracy | 77% |
| Random Forest | Accuracy | 79.21% |
| XGBoost | Accuracy | 79.84% |

## Week 5: Handling Imbalanced & Messy Real-World Data
Churn dataset showed class imbalance (73.5% No Churn vs 26.5% Churn). Applied class_weight='balanced' in Logistic Regression to address it. Recall improved from 55.88% to 78.34% (catching far more actual churners), while accuracy dropped from 80.55% to 73.81% — showing accuracy alone was a misleading metric here, since a model that always predicts "No Churn" would score ~73% accuracy while being useless for identifying at-risk customers.

| Metric | Before (Baseline) | After (Balanced) |
|---|---|---|
| Accuracy | 80.55% | 73.81% |
| Precision | 65.72% | 50.43% |
| Recall | 55.88% | 78.34% |
| F1 Score | 60.40% | 61.36% |

## Week 5: Deploy Model as a Live Web App
Deployed the churn prediction model as an interactive Streamlit web app, where users input tenure, monthly charges, and total charges to get a live churn risk prediction.

**Live App:** https://naeem-churn-predictor.streamlit.app/

## Week 6 Capstone: Malicious URL Detector

### Problem Statement
Phishing and malicious URLs are one of the most common cyberattack vectors, tricking users into visiting harmful sites disguised as legitimate ones. This project builds a machine learning model that looks at a raw URL and predicts whether it's likely to be malicious (phishing/malware/defacement) or safe — without needing to actually visit the site.

### Approach
- Used a public dataset of 651,191 labeled URLs (benign, phishing, malware, defacement), sampled to a balanced 50,000 URLs
- Converted multi-class labels into a binary target: Benign vs Malicious
- Normalized all URLs (stripped protocol and "www.") before feature extraction to avoid data leakage
- Used a **TF-IDF character n-gram (2-5) representation** combined with **Logistic Regression**, allowing the model to learn actual character-level patterns in URLs (e.g. suspicious substrings, unusual structure) rather than relying on a handful of manually engineered features
- Augmented training data with well-known safe domains (Google, Facebook, Amazon, etc.) since bare/simple domains were underrepresented in the original dataset

### Key Lessons Learned
1. **Data leakage:** An early version of the model hit 94% accuracy by learning a shortcut — it flagged any URL containing "http://" or "https://" as suspicious, simply because malicious URLs in the dataset happened to include the protocol more often than benign ones. Removing the protocol before feature extraction fixed this, dropping accuracy to a more honest number but making the model actually useful.
2. **Distribution bias:** Even after fixing leakage, the model initially misclassified plain domains like "google.com" as malicious, because very short, path-less URLs were rare in the training data (most benign examples had a path, like "youtube.com/watch?v=..."). This was fixed by augmenting the training set with known-safe bare domains.
3. **Manual features vs. learned representations:** Hand-crafted features (URL length, number of dots, etc.) plateaued around 80-87% and were brittle to edge cases. Switching to a TF-IDF character n-gram representation let the model learn patterns directly from the text, which generalized better to real-world URLs.

### Results (Final Model)
| Metric | Score |
|---|---|
| Accuracy | 87.65% |
| Precision | 88.02% |
| Recall | 86.14% |
| F1 Score | 87.07% |

Real-world sanity check: correctly classified google.com, facebook.com, amazon.com, youtube.com, and wikipedia.org as safe, and correctly flagged an IP-based login URL, a shortened link, and a typosquatted domain (amaz0n-account-verify.tk) as malicious.

### Live App
Users can paste any URL into the app and instantly get a Malicious/Safe prediction with a risk score.
**Live App:** https://naeem-url-detector.streamlit.app/

### How to Run
1. Clone this repo
2. `cd url-detector`
3. `pip install -r requirements.txt`
4. `streamlit run app.py`

### Business Value
This tool could be integrated into browsers, email clients, or messaging apps to warn users in real-time before they click a suspicious link — helping prevent credential theft, malware infections, and financial fraud, especially for less tech-savvy users who can't easily spot phishing attempts themselves. Beyond the model itself, this project highlights a broader lesson for any ML practitioner: high accuracy on paper means nothing until the model is stress-tested against real, unseen, everyday inputs — that's where hidden shortcuts and biases actually surface.
