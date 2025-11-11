Classification & Regression Trees

9.1 Introduction

Trees
Decision trees can be used both for classification and regression, but mostly classification. 


Entropy & information gain --> Ace the Data Science Interview(pg 97 - pg 100)
if there is a lot of impurity in the data, then there will be less nformation gain
if it is pure data meaning less impurity, more info gain
- our root node in a decision tree is the one that has the most information gain
🔸 High entropy → more randomness, variety, or unpredictability
🔸 Low entropy → repetitive, predictable, or uniform

Ginni Index
<img width="687" height="462" alt="image" src="https://github.com/user-attachments/assets/13019197-1067-4902-b1ad-090d83f031b2" />

Add 2 imgs or notes:
- numerbs for entropy, how do I know I should use a specific variable or not
- numbers for gini index, how do I know I should use a specific variable or not


Cart Vs Random Forest
Think of it like this 👇

🧠 CART = one expert’s opinion
🌲 Random Forest = a panel of experts — each looks at slightly different data and features, then they vote or average their answers.



Bagging




All of these are strings you can pass to scoring= in GridSearchCV:

Scoring string	What it means	Notes
'r2'	R² (coefficient of determination)	Higher is better, range ~(-∞, 1]
'neg_mean_squared_error'	
−
MSE
−MSE	What you’re using now
'neg_root_mean_squared_error'	
−
RMSE
−RMSE	Easier to read than MSE (same units as target)
'neg_mean_absolute_error'	
−
MAE
−MAE	Robust to outliers
'neg_mean_absolute_percentage_error'	
−
MAPE
−MAPE	Error as a percentage (careful with values near 0)
'neg_median_absolute_error'



<img width="866" height="492" alt="image" src="https://github.com/user-attachments/assets/5c5e0f27-e485-44b7-854b-461bea971f36" />



                    🌳 Decision Tree Algorithms
─────────────────────────────────────────────
   ├── Single Tree Algorithms
   │     ├── ID3 → uses entropy
   │     ├── C4.5 → uses gain ratio
   │     └── CART → uses gini / MSE
   │
   ├── Ensemble (Multiple Trees)
   │     ├── Bagging → parallel independent trees
   │     │      └── Random Forest = Bagging + feature randomness
   │     │
   │     └── Boosting → sequential dependent trees
   │            ├── AdaBoost → reweight errors
   │            ├── Gradient Boosting → fit residuals
   │            ├── XGBoost → optimized gradient boosting
   │            ├── LightGBM → gradient boosting with leaf growth
   │            └── CatBoost → boosting for categorical data


🧩 Quick Analogy
Category	Analogy
CART / ID3 / C4.5	One decision tree (one student taking the exam)
Bagging / Random Forest	Many students take the exam separately → average their answers
Boosting (AdaBoost, XGBoost, etc.)	Students take the exam sequentially, each learning from the previous student’s mistakes


