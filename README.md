# Analytics Pvt Ltd: DevOps Automation Project

## 📝 Project Overview

This project was developed for Analytics Pvt Ltd to address the growing demand for their product. It implements a comprehensive DevOps lifecycle to automate the deployment, scaling, and operation of their application containers. The solution replaces their previous monolithic architecture with a modern, containerized approach managed by Kubernetes, ensuring high availability and scalability.

---

## 🚀 DevOps Lifecycle & Workflow

The DevOps lifecycle is designed to be fully automated and integrated. The following steps outline the entire process:

1.  **Git Workflow**: The project uses a **Git workflow** to manage version control. The master branch is the source for all production releases, which are scheduled to occur on the 25th of every month.

2.  **Jenkins Pipeline**: A **Jenkins Pipeline script** is the core of this project, orchestrating the entire CI/CD process.

3.  **CodeBuild Trigger**: Any commit made to the master branch automatically triggers the Jenkins pipeline.

4.  **Containerization**:
    * The pipeline uses a **Dockerfile** to create a custom Docker image of the web application.
    * This Docker image is built and pushed to **Docker Hub** with every new commit.

5.  **Kubernetes Deployment**:
    * The pipeline deploys the containerized code to a **Kubernetes cluster**.
    * The application is configured to run with **2 replicas** to ensure high availability and load balancing.
    * A **NodePort service** is created and configured on port `30008` to expose the application to external traffic.

6.  **Infrastructure Management**:
    * **Terraform** is used to provision all the necessary infrastructure on **AWS**, ensuring a consistent and reproducible environment.
    * A **configuration management tool** is used to install and configure essential software on the servers.

---

## 🛠️ Infrastructure & Tools

| Tool/Technology | Role in Project |
| :--- | :--- |
| **AWS** | Cloud provider for hosting the entire infrastructure. |
| **Terraform** | Infrastructure as Code (IaC) tool for creating and managing AWS resources. |
| **Configuration Management** | Tool (e.g., Ansible, Chef) to automate software installation and configuration on servers. |
| **Git** | Version control system for the application code. |
| **Jenkins** | Automation server for orchestrating the CI/CD pipeline. |
| **Docker** | Containerization platform for packaging the application and its dependencies. |
| **Kubernetes** | Container orchestration platform for deploying, scaling, and managing the application containers. |

---

## ⚙️ Server Configuration

To support the pipeline, specific software is installed on each worker machine using a configuration management tool:

* **Worker1**: `Jenkins`, `Java`
* **Worker2**: `Docker`, `Kubernetes`
* **Worker3**: `Java`, `Docker`, `Kubernetes`
* **Worker4**: `Docker`, `Kubernetes`
