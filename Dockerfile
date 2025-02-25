FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install numpy pandas scikit-learn wandb opencv-python matplotlib
CMD ["python", "distance_classification.py"]
