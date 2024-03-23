#!/bin/bash

echo "Implemente aqui o script para executar a sua solução"
cd frontend
npm install
npm run dev &

cd ..

cd backend
python3 -m venv venv
. venv/bin/activate
pip install -r requirements
python app.py
