# create and python image file
FROM python:3.10-slim
# set the working directory
WORKDIR /app
# copy the requirements file
COPY requirements.txt .
# install the requirements
RUN pip install --no-cache-dir -r requirements.txt
# copy the rest of the application code
COPY . .
# expose the port the app runs on
EXPOSE 8000
# command to run the application
CMD ["streamlit","run","main.py"]