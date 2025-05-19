#### READ ME
Install python (includes pip)
```
brew install python3
```
Confirm python version
```
python3 --version
```

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
See detail in each sub-folder README
```

End session with virtual env
```
deactivate
```
