# ETL-SQLServer
ETL process and SQLServer connection.

## 🌎 Repository Structure 
```
ETL-SQLServer/
├── main.py
├── .gitignore
├── env/                # Virtual enviroment
└── requirements.txt
└── pkg                 # Contains all needed files
    └── __init__.py     # Specifies that folder 'pkg' is a Python package
    └── config.py       # Contains all configuration params
    └── modules.py      # Contains all functions
    └── settings.py     # Contains all global variables
    └── .env            # Contains all secret parameters (not provided)
```

## ✨ Details
**main.py:** 

## 🚀 How to run locally
1. Clone this repository:
```
git clone https://github.com/departamentoIA/ETL-SQLServer.git
```
2. Set virtual environment and install dependencies.

For Windows:
```
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
```
For Linux:
```
python -m venv env && source env/bin/activate && pip install -r requirements.txt
```
3. Create '.env' file with your secret data. An example of its structure is shown in "config.py".

4. Run "main.py".

## 📦 Portability
To make this project executable, run (Windows):
```
pyinstaller --onefile --add-data "pkg/.env;." main.py
```