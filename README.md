# FastAPI-Sample

## Create secret token
1. Open python console
2. To generate secret string use built in package `secrets` 
   ```
   import secrets
   secrets.token_hex(16)
   ```
    Where number 16, in this case, represents number of secret characters.
3. Paste your secret to .env file

## Launch API
Open terminal and type:
```
python -m uvicorn main:app 
```
or:
```
python -m uvicorn main:app --reload
```
if you want your API to automaticaly reload after every change
