# Chapter 12 - Operationalizing models with code

In this chapter you are going to operationalize the machine learning models you have been training so far in this book. You are going to explore two approaches:

- Exposing a real time endpoint which will be exposing a REST API you can use to make inferences and
- You are going to expand your pipeline authoring knowledge to efficiently make inferences on top of big data in parallel. 

You will start by registering a model in the workspace, to keep track of the artifact. Then you will publish a REST API, something that will allow your model to integrate with third party applications like [PowerBI](https://docs.microsoft.com/en-us/power-bi/connect-data/service-aml-integrate). 
Then you will author a pipeline to process half a million of records within a couple of minutes, in a very cost-effective manner.

This folder contains all code snippets found within the book's chapter.
