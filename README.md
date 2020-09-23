# Simpsons Character identification(end-to-end deployment)
In this project I have taken ten simpsons charcaters and have tried to make end to end image classification.

## Data generator:

1. I have taken complete dataset from kaggle (https://www.kaggle.com/alexattia/the-simpsons-characters-dataset) but have used just 1038 images in total for 10 different characters due to computational restriction.

2. Here I have blurred 30% of data in each category.

4. I have made skewed dataset where I have used one category which is just 3% of total dataset.

5. I have done data generator porcess in Data Genrator file.


## Training:

1. First Data augmentation was applied for the category which is less than 3% of total dataset.

2. To identify blurr images better random blurr ranging from 1 to 50 have been used.

3. For training two transfer learning technique such as VGG16 and ResNet50 were used.

4. Got Better accuracy of in VGG16 as comapre to ResNet50.


## Deployment:

Flask and heroku is been used for the deployment. 

https://simpson-classification.herokuapp.com/

![2020-09-23_13-35-21](https://user-images.githubusercontent.com/30840805/93985494-cb909180-fda2-11ea-8229-dd17333c9903.png)
