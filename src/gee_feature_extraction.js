// GEE Script: Sentinel-1 and Sentinel-2 Feature Extraction for Landslide Susceptibility
// Target Area: Arun Basin, Nepal
// Temporal Range: 2021-2026

var roi = ee.Geometry.Rectangle([86.8, 27.0, 87.5, 28.0]); // Approximate Arun Basin bounds
var startDate = '2021-01-01';
var endDate = '2026-01-01';

// 1. Digital Elevation Model (Topography)
var dem = ee.Image('JAXA/ALOS/AW3D30/V3_2').select('DSM').clip(roi);
var slope = ee.Terrain.slope(dem);
var aspect = ee.Terrain.aspect(dem);
var topoStack = dem.addBands([slope, aspect]).rename(['elevation', 'slope', 'aspect']);

// 2. Sentinel-2 (Optical) - Annual Median & NDVI
function maskS2clouds(image) {
  var qa = image.select('QA60');
  var cloudBitMask = 1 << 10;
  var cirrusBitMask = 1 << 11;
  var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
      .and(qa.bitwiseAnd(cirrusBitMask).eq(0));
  return image.updateMask(mask).divide(10000);
}

var s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(roi)
  .filterDate(startDate, endDate)
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
  .map(maskS2clouds);

var addNDVI = function(image) {
  var ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI');
  return image.addBands(ndvi);
};

var s2_ndvi = s2.map(addNDVI).select('NDVI').median().clip(roi);

// 3. Sentinel-1 (SAR) - Annual Median
var s1 = ee.ImageCollection('COPERNICUS/S1_GRD')
  .filterBounds(roi)
  .filterDate(startDate, endDate)
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
  .filter(ee.Filter.eq('instrumentMode', 'IW'));

var s1_vv = s1.select('VV').median().clip(roi);
var s1_vh = s1.select('VH').median().clip(roi);

// 4. CHIRPS (Rainfall) - Annual Mean
var precip = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY')
  .filterBounds(roi)
  .filterDate(startDate, endDate)
  .mean()
  .rename('mean_precip')
  .clip(roi);

// 5. Final Synergy Stack Export
var synergyStack = topoStack.addBands([s2_ndvi, s1_vv, s1_vh, precip]);

Export.image.toDrive({
  image: synergyStack,
  description: 'Synergy_Feature_Stack_Arun',
  scale: 30, // Resampled to DEM resolution
  region: roi,
  maxPixels: 1e13
});

print('Synergy Stack ready for export:', synergyStack);