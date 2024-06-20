import os
import uvicorn

os.environ['PYTHONPATH'] = 'D:\project\flutter_app'
uvicorn.run("main:app", reload=True)
