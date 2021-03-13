# ECE143_Drug_Analysis
This repository contains the project that was done for ECE143 (Programming for Data Analysis) at UCSD. It contains all the data, code and approaches used in the project. 

The data folders(Data,webmd,ExData) contain all data required to complete the project. The analysis notebook contains the recommender system and data visualization graphs. 

## Project Description
Diseases are one of the biggest problems people face and there's multiple drugs for each symptom people experience. People don't know the appropriate drug to choose from based on their symptoms. Therefore, we will build a recommender system based on collaborative filtering and latent factor models. Visualizations of certain data such as ratings on different drugs for a certain condition can also help patients make decisions. The proposed solution will effectively save time spent at the doctors with finding a nearby drug store with the recommended drug. 

## Datasets Used:
1) UCI ML Drug Review (https://www.kaggle.com/jessicali9530/kuc-hackathon-winter-2018)
2) WebMD Drug Reviews (https://www.kaggle.com/rohanharode07/webmd-drug-reviews-dataset)

## Flow:
To run the project, everything you need will be in the Analysis.ipynb notebook. However, you first need to create and activate the conda environment.
Create conda:
```
conda-env create -f environment.yml
```

Activate environment:
```
conda activate 143_v3
```

Once you've run this, jupyter should use this environment to run the notebook. The notebook will contain everything else you need, from an introduction to the data, to the visualisation, to the Recommender System.

## Group Members:
1) Kevin Liang
2) Rushil Roy
3) Xiaoqian Liu
4) Zhiyuan Hu
5) Zonglin Di
