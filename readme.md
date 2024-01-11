## Flask Python application

after cloning create venv with:
```
python3 -m venv venv
```

activate the venv:
```bash
source venv/bin/activate
```

install dependiencies from requirements.txt:
```
pip install -r requirements.txt
```

launch application with:
```
flask run
```

run emulated email server:
```
aiosmtpd -n -c aiosmtpd.handlers.Debugging -l localhost:8025
```

run test suite with:
```
python tests.py
```