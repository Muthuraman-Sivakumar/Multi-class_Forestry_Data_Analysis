# EDA Summary

### 1 - Class Distribution

    (1) strong class imbalance present.

        imbalance will affect feature visualizations.
        
        will address during Preprocessing, not EDA

### 2 - Feature Visualizations

    (1) trimmed dataset to 1.5 SD to remove outliers and
        more easily identify core insights

    (2) no features was predictive alone. however, "sets"
        of features amongs classes show predictive promise.

        I will engineer feature "sets" in Step 5

    (3) all 40 soil features have been removed (no predictive
        value as all classes have near 0% soil type presence)


### 3 - Pearson Correlation Analysis

    (1) no single predictive correlations between pairs
        of features.

        again points to engineering feature "sets"


# Detailed Description
Round 1 - Class Distributions


        Goal:

                Discover if there are imbalanced classes that 
                will affect EDA and model training

        Findings:        
        
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

                
                We will address this issue only after all EDA and preprocessing steps have been taken

                This ensures that any over/under sampling and synthetic data generation is done on clean data


Round 2 - Univariate Analysis


        Goal:

                Univariate patterns are the simplest signal to find, therefore
                discovering them should be the first approach in EDA

                Strong, clear univariate patterns also eliminate the need for complex modeling


        Findings:
        
                I will list only patterns which correlate to a specific 
                class or signal underlying patterns for further exploration.

                Anything not inherently interesting will not be listed. 



        Trimmed Dataset to 1.5 SD to remove outliers and identify core signals

        
    Sunlight Features
    
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

                    Some combination of these 5 metrics can represent
                    a class. by themselves, they aren't useful

        Scaterplot:

                These depict the physical relationship between variables

                What physical laws I gleaned:
                        - aspect is analgous to x-coordinates for rotation
                        - slope is analgous to y-coordinates for rotation

                        - slope can either minimize or maximize sunlight
                        - aspect and slope are independent with one another
                        - there are key aspect ranges that can predict hillshade values (local min/max)


    Distance Features
    
        Histogram:

            Elevation: 

                    Clear elevation trends, high predictive weight 
            
            Overall:

                    Some combination of these 5 metrics can represent
                    a class. by themselves, they aren't useful



Sunlight and Distance Features:

    Scatterplot: 

        aech set of 5 scatterplots together show 
        class distinction across all feature relationships

        can create feaetures to describe this

Overall:

    To capture sets of features together, I can engineer features
    to numerically represent their "set" distribution/average


Wilderness Area:

    there are patterns for classes, however other classes share this.
    
    for this reason, univariate analysis is not enough unless paired with a class' "set" distribution

    Summary:

        Area 0 corresponds with 1, 2, 7
        Area 1 corresponds with none
        Area 2 corresponds with 1, 2, 3, 5, 6, 7
        Area 3 corresponds with 3, 4, 6


        Class 1 and 2 ONLY match to Areas 0 and 1
        Class 3 ONLY matches to Area 2 and 3
        Class 4 ONLY matches to Area 3
        Class 5 ONLY matches to Area 2
        Class 6 ONLY matches to Areas 2 and 3
        Class 7 ONLY matches to areas 0 and 2

Soil Type:

    not enough "yes" for any class to have any predictive value.

    will remove these 40 features

Future Directions:

        The preprocessing step is the step where the dataset itself will change.

        This step works in parallel to the modeling step. Model selection dictates the necessary preprocessing
        
        For this dataset that means removing/creating features + balancing classes.

        Perhaps each model requires a slightly different dataset. This step will take care of that
