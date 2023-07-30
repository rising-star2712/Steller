# Steller
## Notion For Presentation

To utilize our repository you first need to clone it using the following command :
```git clone https://github.com/rising-star2712/Steller.git```

Then navigate to project directoy using cd command :
```cd deck-generator```

After that setup a virtual environment :
```
python -m venv env
env\Scripts\activate
```

Install required requirements using pip :
```
pip install -r requirements.txt
```

There might be conflicts with your Python version so make sure version of Python is greater than 3.7 

If few requirements are not installed which can be case if there are some conflicts then 
we need to seperately install the requirements or libraries using the command
```pip install library-name```

You need to specify your own Open AI Key in the file hmtl_gen.py file in variable OPEN_API_KEY

Once all libraries are installed according to the process try running app.py file which uses Flask 
```python app.py```
