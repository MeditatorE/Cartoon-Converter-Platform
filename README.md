# Cartoon-Converter-Platform
This Project for CS252 Final Project @Macau university of Science and Technology.

Please click here for our [**personal homepage**](https://github.com/MeditatorE/Cartoon-Converter-Platform/tree/main/homepage) to contact us.

# What is the "Cartoon Converter Platform"? 
This project is mainly divided into two parts, namely cartoon converter and image resource sharing platform. You can access our platform through cartoon converter.
## Cartoon Converter
Cartoon Converter is an image processing tool that runs locally. It can convert any style of pictures into cartoon style. We now provide four styles for you to choose from. If you want to know more about it, [**please click here**](https://github.com/MeditatorE/Cartoon-Converter-Platform/tree/main/pretrained_model).
### How to use The Converter?
We provide a Demo here:

![](https://github.com/MeditatorE/Cartoon-Converter-Platform/blob/main/Demo/Convert.gif)

If you want to see the detailed user manual, [**please click here**](https://github.com/MeditatorE/Cartoon-Converter-Platform/tree/main/homepage).
## Picture Resource Sharing Platform
The picture resource sharing platform is another part of this project. 

This platform is used in conjunction with the converter. Its function is to provide a resource sharing platform for artists to download and upload pictures, and to provide creative inspiration and picture resources for art practitioners. 

Anyone can upload or download pictures from this platform. Of course, we also provide an interface on the converter to help users easily upload their converted cartoon-style pictures.
### How to visit the platform?

We have provided an interface for entering the platform on the converter and uploading pictures to the platform.

![](https://github.com/MeditatorE/Cartoon-Converter-Platform/blob/main/Demo/platform.gif)
## How to start?
### 1. Clone this repo

```
https://github.com/MeditatorE/Cartoon-Converter-Platform.git
```
### 2. Install required modules

```
pip install -r requirements.txt
```
### 3. Run main.py
```
python main.py
```
# How did we develop this project?
We uploaded our development plan on Jira. In general, our development process is divided into three stages: 

**Sprint I** mainly develops local cartoon converters, 

**Sprint II** mainly develops online resource sharing platforms and 

**Sprint III** mainly responsible for integrating the online and offline parts and optimizing the entire project.

You can go to our [**development page on Jira**](https://zyp-001.atlassian.net/jira/software/c/projects/CCP/issues) to learn more.

## Sprint I
At this stage we mainly need to train the model and implement a GUI as an interface to help users access the model. 
We use a model called Cartoon GAN, which was presented in a paper at the 2018 CVPR conference called [***CartoonGAN: Generative Adversarial Networks for Photo Cartoonization***](https://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf). Its specific structure is shown below.
<img width="831" alt="截屏2022-05-17 下午8 25 08" src="https://user-images.githubusercontent.com/90904086/168810282-25bbabf4-8d82-4f10-b2f0-d7e1d6a85442.png">


