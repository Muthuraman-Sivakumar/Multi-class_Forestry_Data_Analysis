# Archive of Notes


### Late July (Finished EDA)

Key moments from EDA
- all 40 soil features have no predictive signal. these features were promptly removed
- dead-end finding feature signals that can discern between classes
    - Univariate Analysis
        - visually inspecting feature plots, there was so univariate signal that can discern a class
    - Multivariate analysis
        - feature correlation pairs did not strongly discern classes
        - sets of features did predict classes, HOWEVER, engineering these sets into features isn't practical
            - there are many unique feature sets for the 7 classes
            - multiple classes can "map" to a feature set -> identifying threshold across multiple features for a single class isn't feasible

Conclusion from EDA
- feature engineering isn't feasible because of the complex, multivariate feature relationships across the 7 classes. These relationships are too labor-intensive to engineer into features and overlap between classes
- if we had to predict classes from a set of features, we can't assist the model in identifying discerning signals; the model ITSELF must capture complex feature relationships
- Training Neural Networks and Tree-based methods are the most logical next stem

### Mid-Late August (Finished Notes)

Cleaned up project documentation

### Mid-Late August (Starting Model Training)

Current
