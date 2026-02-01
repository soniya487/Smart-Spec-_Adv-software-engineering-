**SmartSpec – Intelligent Requirements Engineering System**


**Overview**

SmartSpec is an intelligent requirements engineering system designed to assist software analysts and developers in analyzing, validating, and improving software requirements during the early stages of the Software Development Life Cycle (SDLC).

In real-world software projects, requirements are often written in natural language by multiple stakeholders. This frequently leads to ambiguity, inconsistency, and low-quality specifications, which later cause rework, defects, and project delays.

SmartSpec addresses this problem by providing an automated, rule-driven, and NLP-assisted requirement analysis platform that evaluates functional and non-functional requirements before design and implementation begin.

The system is implemented as a FastAPI-based backend service with a lightweight frontend interface and interactive Swagger UI, enabling both technical and non-technical users to validate requirement quality efficiently.

**🎯 Problem Statement**

Traditional requirement analysis is:

  --Manual and time-consuming

  --Highly dependent on individual experience

  --Prone to missing ambiguity and quality issues

  --Difficult to trace across SDLC phases

As a result, poor-quality requirements often propagate into design and implementation, increasing cost and risk.

💡 Solution: SmartSpec

SmartSpec provides an automated requirements quality assessment pipeline that:

  --Accepts requirement statements as input
  
  --Classifies them as functional or non-functional

  --Detects ambiguity and weak wording
  
  --Evaluates requirement quality using predefined rules

 --Produces structured analysis outputs suitable for traceability

This allows teams to identify and correct requirement issues early, improving overall software quality.


 **System Architecture**

SmartSpec follows a layered architecture aligned with best software engineering practices:

1️⃣ Presentation Layer

Lightweight HTML frontend for requirement input

Swagger UI for API testing and demonstration

2️⃣ API Layer (FastAPI)

RESTful endpoints for requirement analysis

Input validation using Pydantic schemas

CORS enabled for frontend integration

3️⃣ Service Layer

NLP processing for textual analysis

Rule-based quality validation engine

Scoring and classification logic

4️⃣ Analysis Layer

Functional vs Non-Functional classification

Ambiguity detection

Requirement quality scoring

This architecture ensures modularity, scalability, and clear separation of concerns, making the system easy to extend in future phases.
<img width="2000" height="2000" alt="Untitled diagram _ Mermaid Chart-2026-02-01-153356" src="https://github.com/user-attachments/assets/0a51e9b2-a527-46b4-a207-e3977269dc00" />
-----------

**Key Features**

📄**Requirement Classification**

Identifies functional and non-functional requirements

⚠️**Ambiguity Detection**

Flags vague terms such as fast, user-friendly, efficient

📊**Quality Scoring**

Evaluates requirements based on clarity, testability, and structure

🔁 **Traceability Support**

Enables mapping of requirements to analysis outputs (RTM-ready)

🔍 **Interactive Swagger UI**

Simplifies testing and demonstration of backend services

**Technology Stack**
Layer                      Technology
Backend	                  Python, FastAPI
API Server	              Uvicorn
Validation               	Pydantic
Frontend                	HTML
Tooling	                  VS Code, Git, GitHub

**Practical Usage Scenario**

In real-world projects, requirements documents are written by multiple stakeholders and often contain ambiguity.
SmartSpec can be integrated into requirement review pipelines to automatically flag low-quality requirements before design and implementation begin.

**This reduces**:

  *Rework during later SDLC phases

  *Misinterpretation between stakeholders

  *Risk in compliance-heavy domains such as healthcare, finance, and enterprise software

  How to Run the Project Locally
Step 1: Clone the Repository
git clone https://github.com/soniya487/Smart-Spec-_Adv-software-engineering-.git
cd SmartSpec_ADVSE
**how to load and execute readme file is attached itself in the Repo please download it for reference **
**
Access the Application**

API Root: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Frontend UI: Open app/frontend/index.html in a browser **make sure you generate all the links after you load the application **


**Future Enhancements**


 * Integration with machine learning models

 * Advanced NLP techniques for semantic analysis

 * Persistent storage for requirement history

 * Full RTM generation across SDLC phases

 * Enhanced UI using React or Angular

  **Academic Context**

This project was developed as part of an Advanced Software Engineering course and demonstrates:

Requirements analysis concepts

Architectural design principles

SDLC alignment

Practical application of FastAPI in system design  

Overall this project helped me to standalone in the entire class and got me a good grade and reputation 

**Thankyou **
