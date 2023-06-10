# Here we deploy our flask app from init.py and run it with a local host
from webSite import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)