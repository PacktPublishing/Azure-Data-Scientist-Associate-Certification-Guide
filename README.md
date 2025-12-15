


# Azure Data Scientist Associate Certification Guide	

<a href="https://www.packtpub.com/product/azure-data-scientist-associate-certification-guide/9781800565005"><img src="https://static.packt-cdn.com/products/9781800565005/cover/smaller" alt="Azure Data Scientist Associate Certification Guide" height="256px" align="right"></a>

This is the code repository for [Azure Data Scientist Associate Certification Guide](https://www.packtpub.com/product/azure-data-scientist-associate-certification-guide/9781800565005), published by Packt.

**A hands-on guide to machine learning in Azure and passing the Microsoft Certified DP-100 exam**

## What is this book about?
The Azure Data Scientist Associate Certification Guide helps you acquire practical knowledge for machine learning experimentation on Azure. It covers everything you need to pass the DP-100 exam and become a certified Azure Data Scientist Associate.

This book covers the following exciting features: 
* Create a working environment for data science workloads on Azure
* Run data experiments using Azure Machine Learning services
* Create training and inference pipelines using the designer or code
* Discover the best model for your dataset using Automated ML
* Use hyperparameter tuning to optimize trained models

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1800565003) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

> For content updates and additional content have a look in the "[Updates and additional topics](./Updates-and-additions.md)" page.

> You can find the answers to the book's questions in the "[Knowledge check answers](./Knowledge-check-answers.md)" page.

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
from azureml.train.hyperdrive import GridParameterSampling
from azureml.train.hyperdrive import choice
param_sampling = GridParameterSampling( {
	"a": choice(0.01, 0.5),
	"b": choice(10, 100)
     }
)
```

**Following is what you need for this book:**
This book is for developers who want to infuse their applications with AI capabilities and data scientists looking to scale their machine learning experiments in the Azure cloud. Basic knowledge of Python is needed to follow the code samples used in the book. Some experience in training machine learning models in Python using common frameworks like scikit-learn will help you understand the content more easily.

With the following software and hardware list you can run all code files present in the book (Chapter 1-12).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1        | Azure portal                    | Windows, Mac OS X, and Linux (Any) |
| 2        | Azure Machine Learning Studio            | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800565005_ColorImages.pdf).

### Related products
* Cloud Analytics with Microsoft Azure [[Packt]](https://www.packtpub.com/product/cloud-analytics-with-microsoft-azure/9781839216404) [[Amazon]](https://www.amazon.com/dp/1839216409)

* Cloud Scale Analytics with Azure Data Services [[Packt]](https://www.packtpub.com/product/cloud-scale-analytics-with-azure-data-services/9781800562936) [[Amazon]](https://www.amazon.com/dp/1800562934)

## Get to Know the Authors
**Andreas Botsikas**
is an experienced advisor working in the software industry. He has worked in the finance sector, leading highly efficient DevOps teams, and architecting and building high-volume transactional systems. He then traveled the world, building AI-infused solutions with a group of engineers and data scientists. Currently, he works as a trusted advisor for customers onboarding into Azure, de-risking and accelerating their cloud journey. He is a strong engineering professional with a Doctor of Philosophy (Ph.D.) in resource optimization with artificial intelligence from the National Technical University of Athens.

**Michael Hlobil**
is an experienced architect focused on quickly understanding customers' business needs, with over 25 years of experience in IT pitfalls and successful projects, and is dedicated to creating solutions based on the Microsoft Platform. He has an MBA in Computer Science and Economics (from the Technical University and the University of Vienna) and an MSc (from the ESBA) in Systemic Coaching. He was working on advanced analytics projects in the last decade, including massive parallel systems and Machine Learning systems. He enjoys working with customers and supporting the journey to the cloud.


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781800565005">https://packt.link/free-ebook/9781800565005 </a> </p>