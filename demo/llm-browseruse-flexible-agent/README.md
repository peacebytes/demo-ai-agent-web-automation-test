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
python3 RunDemo.py 'go to https://www.saucedemo.com/, then try to login with a prohibited account, verify that user should not be logged in, close browser in the end'
```

End session with virtual env
```
deactivate
```
