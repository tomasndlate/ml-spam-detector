<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://tomasndlate.github.io/ml-spam-detector/">
    <img src="client/public/ml-spam-detector.ico" alt="Logo" width="80" height="80">
  </a>

  <h1 align="center">ML Spam Detector</h1>

  <p align="center">
     A machine learning-based spam detection system with a web client, an API, and a trained ML model
    <br />
    <br />
    <a href="https://tomasndlate.github.io/ml-spam-detector/"><strong>Explore ML Spam Detector live »</strong></a>
    <br />
  </p>
</div>

<img width="1647" alt="ML Spam Detector website photo" src="https://github.com/user-attachments/assets/8ed216b0-e78e-445d-965f-00c3140e59bb" />


## Overview

This project implements a spam detector using a machine learning model deployed as an AWS Lambda function. The system consists of:

**Client**: A React-based frontend hosted on GitHub Pages.

**API**: A serverless API built with AWS Lambda (using a Docker image) and exposed via AWS API Gateway.

**Model**: A scikit-learn model.

## Features

**Spam classification**: Users can input text to classify whether it is spam or not.

**Serverless deployment**: The backend runs on AWS Lambda for cost efficiency and scalability.

**Infrastructure as Code**: Terraform is used to manage AWS infrastructure.

## Technologies Used

#### Frontend (Client)

- React
- Tailwind CSS
- GitHub Pages for hosting

#### Backend (API)

- AWS Lambda (Docker-based)
- AWS API Gateway
- Terraform for infrastructure management

#### Machine Learning (Model)

- Scikit-learn for training and inference
- Pickle for model serialization
  

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. You are free to use, modify, and distribute this software under the terms of the MIT License.

## Contact

For any inquiries, suggestions, or feedback, feel free to reach out:

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tomasndlate/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https:/github.com/tomasndlate)
