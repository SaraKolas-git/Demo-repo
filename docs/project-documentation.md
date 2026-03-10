# Secure Git Push Validation System

This project implements a DevSecOps pipeline using Jenkins, Docker, GitHub, and SonarQube.

## Pipeline Flow

Developer → GitHub → Jenkins → Identity Validation → SonarQube Scan → Quality Gate

## Security Rules

1. Username must contain "."
2. Email must belong to @optimumdataanalytics.com
3. SonarQube vulnerabilities must be 0

## Tools Used

- Docker
- Jenkins
- SonarQube
- GitHub
- Shell scripting
