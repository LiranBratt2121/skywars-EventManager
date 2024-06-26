# SkyWars Event Manager

SkyWars Event Manager is a project designed to manage SkyWars events on the FRC IL discord server.
## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine using:

```bash
git clone https://github.com/<your-username>/skywars-EventManager.git
cd skywars-EventManager
```

### 2. Create a Virtual Environment
Create a virtual environment to manage your project's dependencies:
```bash
python -m venv env
```

### 3. Activate the Virtual Environment
Activate the virtual environment.
```bash
.\env\bin\activate
```

### 4. Install Requirements
Install the project dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 5. Add HYPIXEL_API_KEY
Create a .env file inside the api folder and add your Hypixel API key. The .env file should look like this:
```env
HYPIXEL_API_KEY=your_hypixel_api_key
```

### Running the Project
After completing the setup steps, you can run the project using:
```bash
python main.py
```
