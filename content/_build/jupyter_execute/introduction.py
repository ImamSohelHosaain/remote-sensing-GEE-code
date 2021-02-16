# Introduction

Imagery is arguably one of the most important and useful geospatial data layers available today; however, it is still one of the most difficult to deploy effectively over the myriad of computing platforms available to geographic information system (GIS) users. The public now takes for granted their ability to see current aerial views of any location on the plant. There are many, many web services and applications that make use of imagery as an interactive backdrop for both the casual and expert user.

Geospatial professionals also want to make use of imagery and other very large raster datasets in an analysis framework. They want to do more than simply view, zoom, pan, and rotate into 3D views. They want to run image processing and analysis algorithms to extract information and features to be used in scientific research, modeling, and decision support systems.

Google Earth Engine (GEE) is an example of a cloud-based image service that combines an extensive archive of satellite imagery, historical and current, with application programming interfaces (APIs) that allow analysis to be performed on this imagery without having to move it to the user's desktop. Noel Gorelick {cite}`gorelick2017google` has written a very nice review of the GEE program and its goals.

Our goal with this online "textbook" resource is to provide example workflows, in both `Javascript` and `Python` that will enable the "student" of GEE to rapidly get up to speed and produce results. We follow a generalized workflow for most image processing tasks that includes the following steps:

* Acquisition and Preprocessing;
* Processing;
* Postprocessing;
* Visualization; and,
* Export.

## Content

This textbook is organized into five parts, with each part containing chapters.

### Part 1: Data Catalog

Part 1 introduces the datasets in the [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets). Earth Engine organizes data into the following categories:

* Climate and Weather;
* Imagery; and,
* Geophysical.

The chapters in Part 1 explore these categories and subsequent data collections in-depth to provide information necessary for using the data in Earth Engine.

### Part 2: Beginner Workflows

Part 2 provides introductory workflows to introduce Earth Engine functionality. Each chapter shows a few tasks and processes to familiarize the reader with the Earth Engine platform and syntax. Part 2 contains Chapters 1-7.

{doc}`Chapter 1 <./02-beginner/chapter01-qualitative-change-detection>` provides a workflow to observe qualitative change from snow-on to snow-off conditions in Rocky Mountain National Park, Colorado, United States. 

{doc}`Chapter 2 <./02-beginner/chapter02-normalized-difference-vegetation-index>` provides a workflow to demonstrate the Normalized Difference Vegetation Index (NDVI) for snow-on and snow-off conditions in Rocky Mountain National Park, Colorado, United States.

{doc}`Chapter 3 <./02-beginner/chapter03-image-composites>` provides a workflow to create composite images from a collection of Summer imagery in Rocky Mountain National Park, Colorado, United States.

{doc}`Chapter 4 <./02-beginner/chapter04-image-mosaics>` provides a workflow to create a mosaic image from water features and imagery in Vermont, United States.

{doc}`Chapter 5 <./02-beginner/chapter05-image-collection-iteration>` provides a workflow to iterate through an image collection and calculate the cumulative NDVI difference for imagery in Rocky Mountain National Park, Colorado, United States. 

{doc}`Chapter 6 <./02-beginner/chapter06-cloud-masking>` provides a workflow to mask clouds and cloud shadows within imagery for Rocky Mountain National Park, Colorado, United States.

{doc}`Chapter 7 <./02-beginner/chapter07-data-quality-bitmasks>` provides a workflow to explore quality flag bitmasks for imagery in Rocky Mountain National Park, Colorado, United States.

Chapter quick reference:

* {doc}`./02-beginner/chapter01-qualitative-change-detection`
* {doc}`./02-beginner/chapter02-normalized-difference-vegetation-index`
* {doc}`./02-beginner/chapter03-image-composites`
* {doc}`./02-beginner/chapter04-image-mosaics`
* {doc}`./02-beginner/chapter05-image-collection-iteration`
* {doc}`./02-beginner/chapter06-cloud-masking`
* {doc}`./02-beginner/chapter07-data-quality-bitmasks`

### Part 3: Intermediate Workflows 

Part 3 provides workflows that piece together tasks and processes from Part 2 in order to create more complex and meaningful workflows, and introduces more complex tasks and processes.

### Part 4: Advanced Workflows

Part 4 provides full scientific workflows in Earth Engine that have been re-created from existing, peer-reviewed papers and/or ongoing remote sensing projects. One of the goals of this book is to promote and provide open and reproducible science workflows, and this chapter is dedicated to creating this type of workflow within the Earth Engine platform.

### Part 5: Appendices

Part 5 provides supplemental information in the form of appendices. Current appendices include:

* Acronym List; and,
* Bibliography.

## Prerequisites

In order to reproduce the computational workflows in this book, you must have an active [Google Earth Engine account](https://earthengine.google.com/).


```{toctree}
:hidden:
:titlesonly:
:caption: Data Catalog

01-catalog/chapter01-landsat
01-catalog/chapter02-sentinel
01-catalog/chapter03-modis
01-catalog/chapter04-high-resolution
```


```{toctree}
:hidden:
:titlesonly:
:caption: Beginner Workflows

02-beginner/chapter01-qualitative-change-detection
02-beginner/chapter02-normalized-difference-vegetation-index
02-beginner/chapter03-image-composites
02-beginner/chapter04-image-mosaics
02-beginner/chapter05-image-collection-iteration
02-beginner/chapter06-cloud-masking
02-beginner/chapter07-data-quality-bitmasks
```


```{toctree}
:hidden:
:titlesonly:
:caption: Intermediate Workflows

03-intermediate/chapter08-raster-reprojection-resampling
03-intermediate/chapter09-raster-reduce-resolution
03-intermediate/chapter10-spectral-indices-math
03-intermediate/chapter11-image-region-statistics
03-intermediate/chapter12-image-statistics-module
03-intermediate/chapter13-data-correlation
03-intermediate/chapter14-arrays-tasseled-cap
03-intermediate/chapter15-data-conversion-export
```


```{toctree}
:hidden:
:titlesonly:
:caption: Advanced Workflows

04-advanced/chapter16-agriculture-boundaries-vaalharts
04-advanced/chapter17-rice-fields-columbia
04-advanced/chapter18-alpine-treeline-colorado
```


```{toctree}
:hidden:
:titlesonly:
:caption: Appendices

05-appendices/appendix-a-acronym-list
05-appendices/appendix-b-bibliography
```
