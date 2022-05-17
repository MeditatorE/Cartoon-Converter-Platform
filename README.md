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
We use a model called Cartoon GAN, which was presented in a paper at the 2018 CVPR conference called [***CartoonGAN: Generative Adversarial Networks for Photo Cartoonization***](https://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf). Its specific structure is shown below:

<img width="831" alt="截屏2022-05-17 下午8 25 08" src="https://user-images.githubusercontent.com/90904086/168810282-25bbabf4-8d82-4f10-b2f0-d7e1d6a85442.png">

### What is Cartoon GAN? And Why Cartoon GAN?
CartoonGAN is a Generative Adversarial Network (GAN) framework specialized for cartoon stylization. 

Actually, existing methods are not satisfied with the cartoonization effect, because 

**(1)** cartoon style has unique characteristics, is highly simplified and abstract, and 

**(2)** cartoon images tend to have sharp edges, smooth color shading and relatively simple textures. 

However, this model proposes two new losses suitable for cartoonization: 

**(1)** the semantic content loss, which is formulated as sparse regularization in the high-level feature maps of the VGG network to cope with the large stylistic variation between photos and cartoons, and 

**(2)** Edge-promoting adversarial loss for preserving sharp edges. We further introduce an initialization phase to improve the convergence of the network to the target manifold. 

The result is that the model is able to generate high-quality cartoon images from real-world photos.

![0](https://user-images.githubusercontent.com/90904086/168812044-3b8bbbd5-8067-4699-b541-e65bab341480.png)
![0_Hosoda](https://user-images.githubusercontent.com/90904086/168812106-4fe2d135-68e8-4e15-9a60-1c577180abd5.png)
![0_Shinkai](https://user-images.githubusercontent.com/90904086/168812154-f17d3f8e-f9b4-417f-89c7-beb719e75dba.png)
![0_Paprika](https://user-images.githubusercontent.com/90904086/168812185-bd3806a1-24d6-4420-93cf-b8839aa4b650.png)
![0_Hayao](https://user-images.githubusercontent.com/90904086/168812215-f3f99993-e3a1-4254-9cfe-95e487b450f4.png)

### About code implementation
In the implementation part, in order to avoid the high cost of collecting different styles of datasets, we finally decided to download the model pre-training model and related code implementation from a [**GitHub project**](https://github.com/MeditatorE/CartoonGAN-Test-Pytorch-Torch).

For GUI, we use Tkinter to implement, we embed all APIs for accessing models or web pages into the GUI, and the GUI looks as shown in the following figure:

![WechatIMG43](https://user-images.githubusercontent.com/90904086/168814637-aabc9cec-6622-48e7-8545-9f1124150962.jpeg)

# Sprint II
In the second stage, we mainly develop an online resource sharing platform. 
In this part, we mainly use the [**Chevereto**](https://github.com/MeditatorE/Cartoon-Converter-Platform/tree/main/Chevereto-free) framework to build our [**web page**](http://jellyfin.orangetien.icu:1500/). Our web page is built on a server. Unfortunately, our link is temporary, so we provide A [**tutorial**](https://github.com/MeditatorE/Cartoon-Converter-Platform/blob/main/Chevereto-free/cheverto.pdf) to help you quickly rebuild this page.

Anyone can upload and download images from our database on our resource sharing platform, we provide a Demo here:

![](https://github.com/MeditatorE/Cartoon-Converter-Platform/blob/main/Demo/webpage.gif)

# Sprint III
In this part, we need to integrate the online and offline parts and optimize the function of our converter. We also developed our [**personal web page and online user manual**](https://github.com/MeditatorE/Cartoon-Converter-Platform/tree/main/homepage) at this stage to help users quickly understand how to use our project.

Here is the Demo:

![](https://github.com/MeditatorE/Cartoon-Converter-Platform/blob/main/Demo/homepage.gif)

## Evluate
For the quality of the output picture, we use two indicators for evaluation, **PSNR and SSIM**.

**PSNR** is the abbreviation of "Peak Signal to Noise Ratio", that is, the peak signal-to-noise ratio, which is an objective standard for evaluating images, which has limitations, Generally used for an engineering project between maximum signal and background noise. It is the logarithm of the mean square error between the original image and the processed image relative to **(2^n-1)^2** (the square of the maximum value of the signal, n is the number of bits per sample value), and its unit is dB.

<img width="313" alt="截屏2022-05-17 下午9 36 10" src="https://user-images.githubusercontent.com/90904086/168823961-1513b654-e6a2-4100-8afe-0c45cece82b9.png">

**SSIM** (Structural Similarity), structural similarity, is an indicator to measure the similarity of two images. Structural similarity index defines structural information as independent of brightness and contrast from the perspective of image composition, reflecting the properties of object structure in the scene, and models distortion as a combination of three different factors of brightness, contrast and structure. The mean is used as an estimate of brightness, the standard deviation is used as an estimate of contrast, and the covariance is used as a measure of structural similarity.

<img width="460" alt="截屏2022-05-17 下午9 36 36" src="https://user-images.githubusercontent.com/90904086/168823988-3101c1d7-d97e-4d0d-8fa7-079d3deb05e4.png">

<img width="423" alt="截屏2022-05-17 下午9 36 50" src="https://user-images.githubusercontent.com/90904086/168823999-a7e27f65-6a7f-4848-ad86-7781291c7abf.png">

<img width="439" alt="截屏2022-05-17 下午9 36 56" src="https://user-images.githubusercontent.com/90904086/168824010-8a9608f7-410b-446f-b463-a27813d6927e.png">

We randomly select 20 images to calculate these two indicators, and then calculate the average, the results are shown below:

| Indicators/Style | Hayao  | Hosoda | Paprika | Shinkai |
| :--------------: | :----: | :----: | :-----: | :-----: |
|     **SSIM**     | 0.649  | 0.692  |  0.632  |  0.743  |
|     **PSNR**     | 28.139 | 28.288 | 28.078  | 28.431  |

Through the analysis of SSIM and PSNR, we can confirm that our generated images are of good quality without distortion and structural confusion, and our image processing tools have new performance.


