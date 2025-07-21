# Real-world Forest Covertypes Classification Project

        project goal: create a mutli-class classification model that can accurately predict forest covers (tree types) given real-world data


## Overview of Dataset and its Source

        The project uses the real-world "Forest Covertypes" dataset taken from the UC Irvine Machine Learning Repository. The Dataset was downloaded via the Scikit-learn library

                UC Irvine link: https://archive.ics.uci.edu/dataset/31/


        Dataset Overview

                581012 observations
                54 features
                7  classes

                Each observation represents a 30m x 30m forest area

                The target feature is the forest covertype
                There are 7 unique covertypes -> 7 classes in dataset

                Features are numerical or binary
                        
                        numerical data is raw (not scaled)
                        discrete data is binary (0's or 1's).
        
        
        ***More details regarding the dataset and its features are found on UC Irvine's website***



        Citation:

                Blackard, Jock. "Covertype." UCI Machine Learning Repository, 1998, https://doi.org/10.24432/C50K5N.

        Copyright:

                Copyright Jock A. Blackard and Colorado State University


## File Structure

        

## Project Workflow
        
        Used a modified CRISP-DM workflow to outline project
        
        Replaced "Deployment" step with "Report" summarizing the project's work and outcomes


### 1. Project Understanding

        Task
                
                - build a multiclass classification model to accurately predict forest covers

        Success Criteria
                
                - model accuracy between 80-90% on stratified test datasets

        Considerations

                - preprocessing methods should properly handle size and dimensionality to both strip noise AND identify relevant signals
                - select a model relative to the postprocessed dataset's characteristics
                - emphasize research on robust, validated test metrics to ensure model strength

        Assumptions
                
                - not all features of the dataset are useful for classification
                - continuous features will need to be normalized

        Contingency Plan (if model poorly performs on test metrics)
                
                1. verify whether testing/validation was correctly executed
                2. double-check preprocessing step for issues
                3. double-check training + validation steps for issues
                4. reconsider model choice



        Project Tools:

                ML

                        - scikit-learn (easy to use, tabular data, fast prototyping, includes relevant processing, testing, and validation steps)
                
                Data Manipulation
                
                        - *pandas (general data manipulation)
                        - *NumPy (useful, efficient arrays + statistics + math functions)
                        imbalanced-learn (imbalanced classes)
                
                Visualization
                
                        - *matplotlib (complete customization for edge uses, matematics, physicss, engineering, etc)
                        - *seaborn (explicitly informative statistical visuals, highly useful plots - pair + corr)

                EDA extension

                        - Data Wrangler (makes EDA tasks simpler with an interactive UI)


### 2. Data Understanding

        Data Collection

                - collected dataset from scikit-learn's dataset import
                - converted the dataset from a "Bunch" type to "DataFrame"
                        - features and target variables were separate
                        - had to merge both together into a single DataFrame for EDA

        Data Description
                
                - 581012 samples (medium-to-large size)
                - 54 features (medium-to-high dimensionality)
                        - 10 numerical features
                                - Elevation
                                        meters
                                - Aspect
                                        degrees azimuth
                                        the direction of the terrain's slope (0 = N, 90 = W, etc.)
                                - Horizontal_Distance_To_Hydrology
                                        meters
                                        horiz. distance to nearest surface water source
                                - Vertical_Distance_To_Hydrology
                                        meters
                                        vert. distance to nearest surface water source
                                - Horizontal_Distance_To_Roadways 
                                        meters
                                        horiz. distance to nearest roadway
                                - Hillshade (9am, Noon, 3pm)
                                        0-255 index (0 = no light, 255 = full light)
                                        SIMULATED amount of sunlight/shadows (calculated from aspect, elevation, and the Sun's angle)
                                        taken during summer solstice
                                - Horizontal_Distance_To_Fire_Points 
                                        meters
                                        horiz. distance to nearest wildfire ignition points
                        - 44 binary features (0 = absent, 1 = present)
                                - 4 unqiue wilderness areas
                                - 40 unique soil types
                        - 7 classes
                                - represented as whole values between 1-7
                                        (1) Spruce/Fir
                                        (2) Lodgepole Pine
                                        (3) Ponderosa Pine
                                        (4) Cottonwood/Willow
                                        (5) Aspen
                                        (6) Douglas-fir
                                        (7) Krummholz

        Features of Interest
                
                some features like hillshade, elevation, and aspect may have complex correlations that can't be captured with a single correlation matrix.

                        hillshade metrics are calculated by finding the angle between Aspect and Sun. this is a non-linear correlation as a higher angle may mean the sun won't cast light on the slope anymore

                - hillshade (SIMULATED amount of sunlight/shadows) during summer solstice (strongest sunlight of yr)
                - aspect (where a slope faces)
                
                - wilderness areas

                - soil types
        
        Data Exploration

                1st Round - Using Data Wrangler for Simple Exploration

                        - Enormous class imbalance
                                (1)

                

        Verify Data Quality

### 3. Data Preparation


### 4. Data Modeling


### 5. Model Validation


### 6. Report
"# Personal-ML-Project" 
