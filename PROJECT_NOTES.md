# Archive of Notes


### Late July (Finished EDA)

Key moments from EDA
- all 40 soil features have no predictive signal. these features were promptly removed
- dead-end finding feature signals that can discern between classes
    - Univariate Analysis
        - upon visually inspecting feature plots, there were no univariate signals that could discern a class from one another
    - Multivariate analysis
        - feature correlation pairs did not discern classes either
        - it seems sets of features can predict classes, HOWEVER, engineering these feature sets into the dataset isn't practical
            - there are too many unique combinations of feature sets among the 7 classes
            - a single feature set can be predictive of multiple classes -> while predictive, these sets can't discern between classes
                - even if a single feature set could discern multiple classes, it would need to have thresholds that serve as "boundaries" for a machine to classify a class. It isn't possible to manually create these "classification boundaries" 

Conclusion from EDA
- feature engineering isn't feasible because of the many complex, multivariate feature relationships across the 7 classes. These relationships are too difficult to manually engineer into dataset features, overlap between classes, and are unable to have manually created "classification boundaries"
- if we had to predict classes from a set of features, we can't manually assist the model in identifying discerning signals; the model ITSELF must capture complex feature relationships
- as a result, training Neural Networks and Tree-based methods are the most logical next stem

### Mid-Late August (Finished Notes)

Cleaned up project documentation

### Mid-Late August (Starting Model Training)

Current
