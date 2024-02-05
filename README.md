# Flask Azure Email Service

This project is a Flask-based backend server deployed on Microsoft Azure, designed to listen for webhook notifications and trigger an Azure Communication Services workflow to send emails.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the App](#running-the-app)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Flask Azure Email Service is a backend server that integrates with Microsoft Azure Communication Services. It listens for webhook notifications from a third-party platform and triggers an Azure Communication Services workflow to send emails to specified entities.

## Features

- Webhook listener for third-party notifications
- Integration with Azure Communication Services for email sending

## Prerequisites

- Python
- Azure Communication Services account
- Azure App Service (for deployment)

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

- Set up your environment variables, including Azure Communication Services connection details 

```
export FLASK_APP=__init__.py
export FLASK_ENV=development
```

## Running the App

- Run the flask app locally for development

```
flask run
```

## Deployment

- Deploy the flask app on Azure App Service following Azure portal instructions

## Usage

- Configure third-party platforms to send webhook notifications to the deployed Azure App Service URL

## Contributing

- Feel free to contribute by submitting bug reports, feature requests, or code contributions

## License

- This project is licensed under the MIT License
