## Create project and virtenv:
```
mkdir simple_todoapp
cd simple_todoapp
python -m venv ./.venv

# activate virtualenv:
source ./venv/bin/activate
```

## Dependancy installations:
```
# fastapi && uvicorn
pip install "fastapi[all]"

# for html responses and templates:
pip install python-multipart jinja2

# db packages:
pip install sqlalchemy
```

## Run the app:
`uvicorn app:app --reload`