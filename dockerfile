FROM python:slim
ENV TOKEN='6357806497:AAGyUiGX_CSCWnIUM2WKsQMbn2Uytujkd5Y'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py