# py_finance_scripts
py_finance_scripts

### Useful commands
Install pyenv on mac
```commandline
brew install pyenv
```

Install pyenv on Ubunutu
```commandline
curl https://pyenv.run | bash
```

### How to setup pyenv and use
`https://realpython.com/intro-to-pyenv`

Create a virtual environment for a project
```commandline
pyenv virtualenv 3.7.10 py_finance_scripts
```

To begin using the virtual environment, it needs to be activated 
```commandline
pyenv local py_finance_scripts
```

Install packages using the pip command  
```commandline
pip install requests
```

If you are done working in the virtual environment for the moment, you can deactivate it.  
```commandline
pyenv deactivate
```

In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages. To do this, run  
```commandline
pip freeze > requirements.txt
```

Install all dependencies  
```commandline
pip install -r requirements.txt
```

---
Useful Links
1. https://realpython.com/intro-to-pyenv/
2. https://docs.python-guide.org/dev/virtualenvs