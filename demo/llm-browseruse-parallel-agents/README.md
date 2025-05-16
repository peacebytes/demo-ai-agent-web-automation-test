#### READ ME
Install uv
```
pip install uv
```

Create & Activate virtual env
```
uv venv --python 3.13
source .venv/bin/activate
```

Install dependencies
```
uv pip install -r requirements.txt
```

Install Chromium (a lightweight version of Chrome)
```
playwright install --with-deps chromium
```

##### EXECUTE DEMO
```
python3 RunDemo.py
```

End session with virtual env
```
deactivate
```