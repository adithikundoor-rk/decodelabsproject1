\# DecodeLabs Backend Task Engine (Project 1)



An industrial-grade, decoupled Command Line Interface (CLI) To-Do List application built with Python. This project serves as a foundational blueprint for backend architecture, focusing on the principles of \*\*Data Decoupling\*\*, \*\*In-Memory Storage\*\*, and \*\*Data Persistence\*\*.



\---



\## 🛠️ Architectural Blueprint



This application is built by splitting the system into distinct layers, mimicking production-ready backend systems:



\### 1. The Model (In-Memory Database \& Persistence)

\* \*\*Volatile Storage:\*\* Uses a structured Python dictionary (`todo\_database`) to serve as a high-speed, in-memory database lookup tool.

\* \*\*Disk Persistence:\*\* Mitigates the "Volatile Trap" (data loss upon process termination) by using the native `json` module to serialize and write data tracking logs safely to `todo\_data.json`.



\### 2. The View \& Controller (User Interface Logic)

\* \*\*Separation of Concerns:\*\* The interface loops, formatting, and input prompts are fully decoupled from core database operations. 

\* \*\*Pythonic Conventions:\*\* Utilizes clean `enumerate()` iteration blocks instead of manual indexing algorithms to keep code clear and efficient.



\### 3. The Gatekeeper

\* Controlled execution is guaranteed using the structural standard: `if \_\_name\_\_ == "\_\_main\_\_":` block.



\---



\## 🚀 Features



\* \*\*Create Tasks:\*\* Generate structural database models with unique numerical IDs automatically assigned.

\* \*\*Read Tasks:\*\* Real-time printing updates derived natively from the stored JSON registry layout.

\* \*\*Delete Tasks:\*\* Secure, selective removal of records from active system RAM and local disk storage.

\* \*\*JSON Backup:\*\* Persistent disk caching ensures zero data tracking loss between application launches.



\---



\## How to Run the System



\### Prerequisites

\* Ensure Python 3.x is installed on your operating system.



\### Deployment Instructions

1\. Clone this repository or download the source code files.

2\. Open your terminal or command prompt inside the project folder.

3\. Boot up the engine using the command:

&#x20;  ```bash

&#x20;  python todo\_list.py
---

## Step 3: Initialize Git and Publish to GitHub
Now that your codebase and documentation are ready, let's push them up to GitHub.

### 1. Create a GitHub Repository Online
1. Go to [GitHub](https://github.com/) and log into your account.
2. Click the **"+"** icon in the top-right corner and select **New repository**.
3. Name your repository: `decodelabs-todo-engine`.
4. Leave it as **Public**, and **DO NOT** check the boxes for "Add a README file" or "Add .gitignore" (since we already created them locally).
5. Click **Create repository**.

### 2. Connect Your Local Code to GitHub
Open your computer's terminal (or command prompt), navigate to your project folder using the `cd` command, and run these commands one by one:

```bash
# Initialize an empty local Git repository
git init

# Stage all your files (code and readme) to be tracked
git add .

# Commit your files into Git's history logs
git commit -m "Initial commit: Core engine logic and architectural README"

# Rename your primary branch to main
git branch -M main

# Link your local machine to your online GitHub repository
# (Copy the exact URL line displayed on your GitHub setup screen)
git remote add origin https://github.com/YOUR_USERNAME/decodelabs-todo-engine.git

# Push your code live to the internet!
git push -u origin main

