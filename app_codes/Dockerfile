FROM python:3.9
EXPOSE 8501
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run prod_recog2.py 
