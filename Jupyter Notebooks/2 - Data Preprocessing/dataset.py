from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_covtype

data_bunch = fetch_covtype(as_frame=True)

df = data_bunch.data  # Extract the actual DataFrame
target = data_bunch.target  # Extract the target variable

df['Cover_Type'] = target  # Add the target variable to the DataFrame
df = df.rename(columns={
        "Horizontal_Distance_To_Fire_Points": "H_Dist_Fire_Points",
        "Horizontal_Distance_To_Roadways": "H_Dist_Roadways", 
        "Vertical_Distance_To_Hydrology": "V_Dist_Hydrology",
        "Horizontal_Distance_To_Hydrology": "H_Dist_Hydrology"
})

# Split data into training, validation, and testing sets (70:10:20 split)
X = df.drop('Cover_Type', axis=1)
y = df['Cover_Type']

# 70% train, 30% temp
X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, random_state=0, stratify=y
)

# 30% temp -> 10% validation + 20% testing
X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=2/3, random_state=0, stratify=y_temp
)

# Create DataFrames for each split
training = X_train.copy()
training['Cover_Type'] = y_train

validation = X_val.copy()
validation['Cover_Type'] = y_val

testing = X_test.copy()
testing['Cover_Type'] = y_test

print(f"Training set size: {len(training)} ({len(training)/len(df)*100:.1f}%)")
print(f"Validation set size: {len(validation)} ({len(validation)/len(df)*100:.1f}%)")
print(f"Testing set size: {len(testing)} ({len(testing)/len(df)*100:.1f}%)")



class dataset:
        def __init__(self):
                self.training = training
                self.validation = validation
                self.testing = testing
        
        def get_training(self):
                return self.training
        
        def get_validation(self):
                return self.validation
        
        def get_testing(self):
                return self.testing


class helper:

        def __init__(self):
                pass

        @staticmethod
        def get_correlation(plt, df, feature_list, sns, np, corr_type, title_add_on):

                # Create subplots for correlation matrices
                fig, axes = plt.subplots(3, 3, figsize=(12, 12))  # 3 rows, 3 columns
                fig.suptitle(f'{title_add_on} Features - Absolute {corr_type.capitalize()} Correlations', fontsize=20, fontweight='bold', y=0.98)

                # Flatten axes for easier indexing
                axes_flat = axes.flatten()

                # Create correlation plot for each cover type
                for cover_type in range(7):
                        # Filter data for this cover type
                        type_data = df[df['Cover_Type'] == cover_type + 1]
                        
                        # Calculate correlation matrix for this cover type
                        corr_matrix = type_data[feature_list].corr(method=corr_type)

                        # Convert to absolute values
                        abs_corr_matrix = corr_matrix.abs()
                        
                        # Create mask for upper triangle
                        mask = np.triu(np.ones_like(abs_corr_matrix, dtype=bool))
                        
                        # Create heatmap
                        sns.heatmap(abs_corr_matrix, 
                                annot=True,           # Show correlation values
                                cmap='Blues',          # Red color scheme for absolute values
                                vmin=0,               # Set minimum value to 0
                                vmax=1,               # Set maximum value to 1
                                square=True,          # Make cells square-shaped
                                fmt='.2f',            # 2 decimal places
                                cbar=False,           # No individual colorbars (saves space)
                                linewidths=0.5,       # Slightly thicker lines for clarity
                                annot_kws={'size': 9}, # Optimized text size
                                mask=mask,            # Hide upper triangle
                                ax=axes_flat[cover_type])   # Use flattened axes
                        
                        # Customize subplot
                        axes_flat[cover_type].set_title(f'Cover Type {cover_type + 1}', 
                                                        fontsize=13, fontweight='bold', pad=10)
                        axes_flat[cover_type].set_xlabel('')
                        axes_flat[cover_type].set_ylabel('')
                        
                        # Rotate labels for better fit with optimized sizing
                        axes_flat[cover_type].tick_params(axis='x', labelsize=8, rotation=45)
                        axes_flat[cover_type].tick_params(axis='y', labelsize=8, rotation=0)

                # Hide the unused 8th and 9th subplots (since we only have 7 cover types)
                axes_flat[7].set_visible(False)
                axes_flat[8].set_visible(False)

                # Add a single colorbar for all plots with better positioning
                cbar = fig.colorbar(axes_flat[0].collections[0], 
                                        ax=axes, 
                                        orientation='horizontal', 
                                        fraction=0.08, 
                                        pad=0.08, 
                                        shrink=0.6,
                                        aspect=30)
                cbar.set_label('Absolute Correlation Coefficient', fontsize=12, labelpad=10)

                # Adjust layout with proper spacing
                plt.subplots_adjust(left=0.08, right=0.88, top=0.88, bottom=0.30, 
                                        wspace=.5, hspace=0.9)
                plt.show()

        @staticmethod
        def get_cross_correlation(plt, df, feature_list_1, feature_list_2, sns, corr_type, title_1, title_2):

                # Create subplots for cross-correlation matrices (sunlight vs distance)
                fig, axes = plt.subplots(3, 3, figsize=(18, 15))
                fig.suptitle(f'{title_1} vs {title_2} Features - Absolute {corr_type.capitalize()} Correlation', fontsize=20, fontweight='bold', y=0.98)

                # Flatten axes for easier indexing
                axes_flat = axes.flatten()

                # Create cross-correlation plot for each cover type
                for cover_type in range(7):
                        # Filter data for this cover type
                        type_data = df[df['Cover_Type'] == cover_type + 1]
                        
                        # Calculate full correlation matrix
                        all_features = feature_list_1 + feature_list_2
                        full_corr_matrix = type_data[all_features].corr(method=corr_type)
                        
                        # Extract cross-correlation between sunlight and distance features
                        cross_corr_matrix = full_corr_matrix.loc[feature_list_1, feature_list_2]

                        # Convert to absolute values for 0-1 range
                        abs_cross_corr_matrix = cross_corr_matrix.abs()
                        
                        # Create heatmap with improved formatting
                        sns.heatmap(abs_cross_corr_matrix, 
                                annot=True,           # Show correlation values
                                cmap='Blues',         # Blue color scheme for absolute values
                                vmin=0,               # Set minimum value to 0
                                vmax=1,               # Set maximum value to 1
                                fmt='.2f',            # 2 decimal places instead of scientific notation
                                cbar=False,           # No individual colorbars
                                linewidths=0.5,       # Grid lines
                                annot_kws={'size': 9}, # Text size for values
                                ax=axes_flat[cover_type])
                        
                        # Customize subplot
                        axes_flat[cover_type].set_title(f'Cover Type {cover_type + 1}', 
                                                        fontsize=14, fontweight='bold', pad=10)
                        axes_flat[cover_type].set_xlabel('Distance Features', fontsize=10)
                        axes_flat[cover_type].set_ylabel('Sunlight Features', fontsize=10)
                        
                        # Rotate and size labels for better readability
                        axes_flat[cover_type].tick_params(axis='x', labelsize=8, rotation=45)
                        axes_flat[cover_type].tick_params(axis='y', labelsize=8, rotation=0)

                # Hide the unused 8th and 9th subplots
                axes_flat[7].set_visible(False)
                axes_flat[8].set_visible(False)

                # Add a single colorbar for all plots
                cbar = fig.colorbar(axes_flat[0].collections[0], 
                                        ax=axes, 
                                        orientation='horizontal', 
                                        fraction=0.08, 
                                        pad=0.12, 
                                        shrink=0.8,
                                        aspect=40)
                cbar.set_label('Absolute Correlation Coefficient (0-1)', fontsize=12, labelpad=10)

                # Adjust layout with proper spacing
                plt.subplots_adjust(left=0.08, right=0.92, top=0.90, bottom=0.25, 
                                        wspace=0.4, hspace=0.9)
                plt.show()
