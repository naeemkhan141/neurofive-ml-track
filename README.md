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
