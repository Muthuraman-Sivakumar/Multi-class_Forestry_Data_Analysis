# Data Dictionary

## About the Dataset

    ├── 581012 observations
    ├── 55 features    
        └── 54 input features                
            └── 10 numerical
            └── 44 binary
        └── 1 output feature
            └── 7 classes

## Numerical Features (10/54 input features)

| Feature Name | Units | What it Means |
|:-------------|:------|:--------------|
| Elevation | meters | at what height the forest area was found |
| Aspect | degrees azimuth | the direction of the terrain's slope (0 = N, 90 = W, etc.) |
| Slope | degrees | the slope of the terrain |
| Horizontal_Distance_To_Hydrology | meters | horiz. distance to nearest surface water source |
| Vertical_Distance_To_Hydrology | meters | vert. distance to nearest surface water source |
| Horizontal_Distance_To_Fire_Points | meters | horiz. distance to nearest wildfire ignition points |
| Horizontal_Distance_To_Roadways | meters | horiz. distance to nearest roadway |
| Hillshade_9am | sunlight index (0-255) | simulated amount of sunlight on the forest area @ 9am (0 = no light, 255 = max light). Please view [link](http://www.geography.hunter.cuny.edu/~jochen/GTECH361/lectures/lecture11/concepts/Hillshade.htm) for a visual explanation. NOTE: taken during Summer Solstice |
| Hillshade_Noon | sunlight index (0-255) | same as above but @ 12PM |
| Hillshade_3pm | sunlight index (0-255) | same as above but @ 3PM |

## Binary Features (44/54 input features)

| Feature Name | Units | What it Means |
|:-------------|:------|:--------------|
|Wilderness_Area1|0 - 1| 0 = absent, 1 = present|
|Wilderness_Area2|0 - 1| same as above|
|Wilderness_Area3|0 - 1| same as above|
|Wilderness_Area4|0 - 1| same as above|
|Soil_type1|0 - 1| same as above|
|Soil_type2|0 - 1| same as above |
|Soil_type3|0 - 1| same as above |
|...|
|Soil_type39|0 - 1| same as above |
## Target Feature (1/1 output features)

| Feature Name | Units | What it Means |
|:-------------|:------|:--------------|
| Covertype | 1-7 (whole numbers) | represents the type of forest associated with a given observation. Identified through: (1) Spruce/Fir (2) Lodgepole Pine(3) Ponderosa Pine (4) Cottonwood/Willow (5) Aspen (6) Douglas-fir (7) Krummholz|
