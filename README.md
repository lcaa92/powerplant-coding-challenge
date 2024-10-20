# Python version

- Python 3.11

# Requirements

To run the app, it is necessary to install dependencies:

```
python -m pip install -r requirements.txt
```

Plus: for dev packages, it is necessary to install dev packages

```
python -m pip install -r requirements_dev.txt
```

# How to run

Fast API DEV mode
```
fastapi dev main.py --port 8888
```

Fast API Production mode
```
fastapi run main.py --port 8888
```

Starting app manually
```
python main.py
```