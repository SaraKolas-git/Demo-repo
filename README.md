# Secure Git Push Validation using Jenkins & SonarQube

## Project Overview

This project implements a **DevSecOps pipeline** that validates Git commits before allowing code to pass the CI pipeline. The system enforces **commit identity validation** and **code security checks** using **Jenkins**, **Docker**, and **SonarQube**.

The goal is to ensure that only **authorized developers with valid identities** and **secure code** can pass the build process.

---

## Project Architecture

GitHub Repository
⬇

Jenkins CI Pipeline (Docker)
⬇

Commit Identity Validation
⬇

SonarQube Static Code Analysis
⬇

Quality Gate Enforcement

---

## Technologies Used

* Docker
* Jenkins
* SonarQube Community Edition
* GitHub
* Git
* Bash scripting
* DevSecOps CI practices

---

## System Components

### Jenkins

Runs the CI pipeline and performs:

* Repository polling
* Commit identity validation
* Triggering SonarQube scans
* Enforcing quality gates

### SonarQube

Performs **static code analysis** and detects:

* Security vulnerabilities
* Code smells
* Bugs

The pipeline fails if the **quality gate conditions are not met**.

### GitHub

Hosts the project repository and triggers Jenkins builds via **SCM polling**.

---

## Security Rules Implemented

The pipeline enforces the following rules:

### Commit Author Validation

1. Username must contain a **dot (`.`)**
   Example:

```
john.doe
```

2. Email must belong to the company domain

```
@optimumdataanalytics.com
```

If either rule fails, the Jenkins build will **fail immediately**.

---

### Code Security Validation

SonarQube Quality Gate enforces:

```
Vulnerabilities = 0
```

If vulnerabilities are detected, the build **fails**.

---

## Project Infrastructure

### Jenkins Container

```
Port: 9090
Image: jenkins/jenkins:lts
```

Persistent volume used for Jenkins data.

---

### SonarQube Container

```
Port: 9000
Image: sonarqube:community
```

Connected to the same Docker network as Jenkins.

---

## Implementation Phases

### Phase 1 – Docker Infrastructure Setup

* Clean Docker environment
* Create Docker network
* Run Jenkins container
* Run SonarQube container

---

### Phase 2 – GitHub Integration

* Generate GitHub Personal Access Token
* Configure Jenkins credentials
* Connect Jenkins to repository
* Enable **Poll SCM** trigger

---

### Phase 3 – Commit Identity Validation

Jenkins extracts commit metadata:

```
git log -1 --pretty=format:'%an <%ae>'
```

Validation rules:

* Username must contain `.`
* Email must match `@optimumdataanalytics.com`

Build fails if validation fails.

---

### Phase 4 – SonarQube Integration

* Install SonarQube Scanner
* Configure SonarQube server in Jenkins
* Generate authentication token
* Run static code analysis

---

### Phase 5 – Quality Gate Enforcement

Jenkins waits for the SonarQube Quality Gate result.

Build fails if:

```
Vulnerabilities > 0
```

---

### Phase 6 – Testing & Validation

Pipeline tested with the following scenarios:

| Test Case                    | Expected Result |
| ---------------------------- | --------------- |
| Valid username + valid email | Build passes    |
| Username without `.`         | Build fails     |
| Email outside company domain | Build fails     |
| Code with vulnerabilities    | Build fails     |

---

## Pipeline Workflow

1. Developer pushes code to GitHub
2. Jenkins polls the repository
3. Jenkins clones the repository
4. Commit identity validation runs
5. SonarQube analysis starts
6. Quality Gate validation runs
7. Build either **passes or fails**

---

## Expected Outcome

The pipeline ensures:

* Only **verified developers** can commit code
* Only **secure code** passes CI
* Security checks are automated

This approach follows **DevSecOps best practices** by integrating security directly into the CI pipeline.

---

## Author

Sara Kolas

DevSecOps CI Pipeline Implementation

Testing Jenkins identity validation
