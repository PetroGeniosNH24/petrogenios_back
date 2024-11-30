import sys
from waitress import serve
from hackaton_api import create_app

app, api = create_app()

if __name__ == "__main__":
    serve(app, listen='*:%s' % 80)

