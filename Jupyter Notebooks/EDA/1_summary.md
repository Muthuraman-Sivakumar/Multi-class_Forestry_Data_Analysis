# EDA Summary Note

    ===========================================================================================================
    |                                                                                                         |
    |       The original dataset was split 70:10:20 into training, validation, and testing respectively       |
    |                                                                                                         |
    |                         All EDA and preprocessing is done on the training data                          |
    |                                                                                                         |
    ===========================================================================================================

# Summaries
### (b) Class Distributions

    Histogram visual shows a clear class imbalance. Here are the results
            
        Class Distribution Summary:
        ========================================
        Cover Type 1: 148,288 samples (36.46%)
        Cover Type 2: 198,310 samples (48.76%)
        Cover Type 3: 25,028 samples (6.15%)
        Cover Type 4: 1,923 samples (0.47%)
        Cover Type 5: 6,645 samples (1.63%)
        Cover Type 6: 12,157 samples (2.99%)
        Cover Type 7: 14,357 samples (3.53%)

        Total Samples: 406,708
        Number of Classes: 7

    
    We will address this issue last during the Preprocessing stage. In other words, only AFTER all EDA and preprocessing has taken place

    This ensures that class balancing techniques are done on clean data. This way class balancing won't blur EDA or preprocessing


### (c) Multivariate Feature Visualizations

    =======================================================================================================================================
    |                                                                                                                                     |
    |       To reduce noise, the training dataset was cut to 1.5 Standard Deviations. This was done by separating the training data       |
    |                               into each class, then trimming each feature to 1.5 Standard Deviations.                               |
    |                                                                                                                                     |
    |                                  This step was taken to remove outliers and identify core signals                                   |
    |                                                                                                                                     |
    =======================================================================================================================================

    Univariate patterns are the simplest signal to find, therefore discovering them should be the first approach in EDA

    Strong, clear univariate patterns also eliminate the need for complex modeling


    Summary:
        
    Key Sunlight Feature Insights
    
        Histogram:

            Aspect: 
                    
                    All classes have a bimodal distribution (deviations are explained by a
                    lack of samples)

                    Can feature engineer bimodal data at valley for deeper exploration

                    Where to split: C1-3 and C7 @ 250, C4-6 @ 200

            Hillshade:

                    Can feature engineer how much a hillshade changed between times

                    3 new features: changes @ (9AM-12PM), (12PM - 3PM), (9AM, 3PM)

            Overall:

                    Some combination of these 5 metrics can represent a class. by themselves, they aren't useful

        Scaterplot:

                These depict the physical relationship between variables

                What physical laws I gleaned:
                        - aspect is analgous to x-coordinates for rotation
                        - slope is analgous to y-coordinates for rotation

                        - slope can either minimize or maximize sunlight
                        - aspect and slope are independent with one another
                        - there are key aspect ranges that can predict hillshade values (local min/max)


    Key Distance Feature Insights
    
        Histogram:

            Elevation: 

                    Clear elevation trends, high predictive weight
            
            Overall:

                    Some combination of these 5 metrics can represent
                    a class. by themselves, they aren't useful



    Sunlight + Distance Feature Associations:

        Summary: 

            Each set of 5 scatterplots show class distinction across all feature relationships

            Gives an idea to what features need to be grouped to engineer discerning, predictive features


    Wilderness Area:

        Summary:

            Each class has predictive Wilderness Area patterns, however these patterns overlap between classes.
            
            Therefor univariate analysis is not enough - features representing multiple variable must be engineered to capture discerning signals

    Soil Type:

        Summary:

            A quick glance at visualizations show almost 0 soil types were present among each class. As a result, there is no predictive signal from soil types. If anything, it will create noise and increase computation time

            As a result all 40 soil features will be removed from the dataset

### (d) Pearson Correlation Analysis

    
