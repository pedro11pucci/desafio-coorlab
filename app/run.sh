#!/bin/bash

cd frontend
npm install
npm run dev &

cd ..

cd backend
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python app.py
