from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from src import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5000)