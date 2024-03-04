from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# Generate a synthetic dataset
X, y = make_classification(n_samples=10000, n_features=20, n_classes=3, n_informative=15, random_state=42)

# Simulate categorical feature with 3 categories encoded as 0, 1, 2
cat_feature = np.random.choice([0, 1, 2], size=X.shape[0])

# Scenario 1: Original encoding
X1 = np.column_stack((X, cat_feature))

# Scenario 2: Shuffled encoding
# Create a mapping for shuffled encoding
shuffled_encoding = {0: 2, 1: 0, 2: 1}
shuffled_feature = np.vectorize(shuffled_encoding.get)(cat_feature)
X2 = np.column_stack((X, shuffled_feature))

# Split the dataset into training and testing sets
X1_train, X1_test, y_train, y_test = train_test_split(X1, y, test_size=0.3, random_state=42)
# X2_train, X2_test = train_test_split(X2, test_size=0.3, random_state=42)[0::2]

# Correcting the data splitting and retraining in one execution
X2_train, X2_test, _, _ = train_test_split(X2, y, test_size=0.3, random_state=42)

# Reinitialize classifiers
clf1 = RandomForestClassifier(n_estimators=100, random_state=42)
clf2 = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit models
clf1.fit(X1_train, y_train)
clf2.fit(X2_train, y_train)

# Predict
y_pred1 = clf1.predict(X1_test)
y_pred2 = clf2.predict(X2_test)

# Calculate accuracies
accuracy1 = accuracy_score(y_test, y_pred1)
accuracy2_corrected = accuracy_score(y_test, y_pred2)

accuracy1, accuracy2_corrected
