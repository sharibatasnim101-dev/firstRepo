# What is?
This is a minimal web server that uses the fastapi async library.

# How to set up?
**IMPORTANT**: Never run `pip install` outside the virtual environment.

Install a virtual environment, using vscode or the commands below:
```shell
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux
sudo apt update
sudo apt install python3-venv
python3 -m venv .venv
source venv/bin/activate
```
Install python requirements:
```shell
cd web-server
pip install -r requirements.txt
```

# How to run in local debug mode?
```shell
uvicorn main:app --reload
```
Changes made to the code will show up immediately thanks to `--reload`

# How to test?
http://127.0.0.1:8000