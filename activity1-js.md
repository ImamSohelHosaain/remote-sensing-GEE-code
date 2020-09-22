# Javascript

The purpose of this lesson is to review the change from leaf-off imagery to leaf-on imagery for a study areas of interest.  

In this lesson, you will:

* Choose an area and Landsat collection of interest;
* Filter the Landsat collection to obtain leaf-off and leaf-on imagery; and,
* Display a single image from both leaf-off and leaf-on conditions.

## Data Acquisition & Pre-Processing
```{code-block} javascript
// Define boundary for Rocky Mountain National Park, Colorado
var rmnp_boundary = ee.FeatureCollection("users/calekochenour/Rocky_Mountain_National_Park__Boundary_Polygon");

// Define Landsat 8 collection
var landsat8_t1_sr = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR');

// Filter Landsat 8 Tier 1 SR to snow-on conditions near RMNP, 2018
var co_snow_on_2018 = landsat8_t1_sr
  .filterDate('2018-03-01', '2018-04-30')
  .filterBounds(rmnp_boundary)
  .sort('CLOUD_COVER')
  .first();

// Filter Landsat 8 Tier 1 SR to snow-off conditions near RMNP, 2018
var co_snow_off_2018 = landsat8_t1_sr
  .filterDate('2018-07-01', '2018-08-31')
  .filterBounds(rmnp_boundary)
  .sort('CLOUD_COVER')
  .first();
```

## Data Processing
```{code-block} javascript
// No data processsing in this lab.
```

## Data Visualization
```{code-block} javascript
// Define Landsat 8 RGB visualization parameters
var l8_vis_params_rgb = {
  'bands': ['B4', 'B3', 'B2'],
  'min': 0,
  'max': 3000
 };

// Define Landsat 8 CIR visualization parameters
var l8_vis_params_cir = {
  'bands': ['B5', 'B4', 'B3'],
  'min': 0,
  'max': 3000
 };

// Define RMNP boundary visualization parameters
var empty = ee.Image().byte();

var rmnp_boundary_vis = empty.paint({
  featureCollection: rmnp_boundary,
  color: 1,
  width: 3
});
```

```{code-block} javascript
// Center map to Rocky Mountain National Park, Colorado
Map.setCenter(-105.6836, 40.3428, 10);

// Add snow-on and snow-off images to map, RGB and CIR
Map.addLayer(
  rmnp_snow_on_2018,
  l8_vis_params_rgb,
  'Landsat 8 - RGB - 2018 - RMNP - Snow On');

Map.addLayer(
  rmnp_snow_on_2018,
  l8_vis_params_cir,
  'Landsat 8 - CIR - 2018 - RMNP - Snow On');

Map.addLayer(
  rmnp_snow_off_2018,
  l8_vis_params_rgb,
  'Landsat 8 - RGB - 2018 - RMNP - Snow Off');

Map.addLayer(
  rmnp_snow_off_2018,
  l8_vis_params_cir,
  'Landsat 8 - CIR - 2018 - RMNP - Snow Off');

// Add RMNP boundary to map
Map.addLayer(
  rmnp_boundary_vis,
  {'palette': 'FF0000'},
  'RMNP Boundary');
```

## Data Export
```{code-block} javascript
// No data export in this lab.
```
