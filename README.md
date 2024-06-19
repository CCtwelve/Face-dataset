# Face-dataset
Our database has been authorized by the volunteers for public use for scientific research purposes.

## Introduction

In this repository, we provide a simple dataset example which consists of three males and three females, each exhibiting 8 different expressions. These expressions include: neutral, angry, smiling, surprised, pouting, eyes closed, left eye closed, and right eye closed. For each expression, we provide information such as the frontal view, left view, right view, UV map, 3D mesh, 3D point cloud, and landmark coordinates. Additionally, our images are all high-resolution (4000x6000), with original point cloud densities ranging from 200,000 to 300,000, and facial point cloud densities ranging from 100,000 to 200,000. We have enlisted several experts to mark the landmarks in our database and through multiple rounds of confirmation and cross-checking, to ensure the accuracy of the landmarks. If our paper is accepted, the complete dataset will be made publicly available on Google Drive, and the code will be made public on GitHub.

## Dataset Construction
Our dataset includes the following sections:
![图片加载失败](https://github.com/CCtwelve/Face-dataset/blob/main/display/structure.jpg)
Among them, the jpg files under the "obj" directory are 2D UV maps, and the mtl is the file that links UV maps with obj, while stl represents 3D mesh information. Under the "points" directory, the cie file is our custom data format. We provide Python version data reading code, so people can read the desired data from the cie file according to their needs. This code can obtain the original facial point cloud and landmark coordinates from the cie file. It's worth mentioning that the asc file is the preprocessed point cloud of a face, serving as input data for the GPS, while the txt file contains the three-dimensional coordinates of landmarks. The preprocessing methods include segmentation, smoothing, outlier filtering, etc., to make the face smoother and more regular. The preprocessing methods include segmentation, smoothing, outlier filtering,  etc., to make the face smoother and more regular.

## Display
We will display the data styles of for sections.

### Obj
![图片加载失败](https://github.com/CCtwelve/Face-dataset/blob/main/display/obj.gif)

### Texture
![图片加载失败](https://github.com/CCtwelve/Face-dataset/blob/main/display/texture.jpg)

### Point And Landmark

This section displays the post-processed facial point cloud and the landmark coordinates annotated by experts.

![图片加载失败](https://github.com/CCtwelve/Face-dataset/blob/main/display/points_and_landmark.gif)

### Point cloud denoising process result
This section displays the results before and after the noise reduction process of the point cloud, with the processed results serving as the input data for the  Geometric point sampling (GPS).
<center>

| ![Before noise reduction](https://github.com/CCtwelve/Face-dataset/blob/main/display/befor.gif) | ![After noise reduction](https://github.com/CCtwelve/Face-dataset/blob/main/display/after.gif) |
|:---:|:---:|
| Before noise reduction processing. | After noise reduction processing. |
</center>
 
