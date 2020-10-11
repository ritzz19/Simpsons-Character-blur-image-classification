# Simpsons Character identification(end-to-end deployment)
In this project I have taken ten simpsons charcaters and have tried to make end to end image classification where it can detect character which are even blurred.

## Data generator:

1. I have taken complete dataset from kaggle (https://www.kaggle.com/alexattia/the-simpsons-characters-dataset) but have used just 1038 images in total for 10 different characters due to computational restriction.

2. Here I have blurred 30% of data in each category.

4. I have made skewed dataset where I have used one category which is just 3% of total dataset.

5. I have done data generator porcess in Data Genrator file.


## Training:

1. First Data augmentation was applied for the category which is less than 3% of total dataset.

2. To identify blur images better random blurr ranging from 1 to 50 have been used.

3. For training two transfer learning technique such as VGG16 and ResNet50 were used.

4. Got Better accuracy of in VGG16 as comapre to ResNet50.


## Deployment:

Flask and heroku is been used for the deployment. 

https://simpsons-character.herokuapp.com/

Detecting blur image:

![sim_blur (1)](https://user-images.githubusercontent.com/30840805/95685831-00f90400-0c18-11eb-8806-3159596d3805.png)

Detecting clear image :
![sim_blur (2)](https://user-images.githubusercontent.com/30840805/95685837-05bdb800-0c18-11eb-8d78-b7e25cf72b84.png)
