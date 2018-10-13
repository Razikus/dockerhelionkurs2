FROM python:3
RUN pip3 install flask
COPY main.py /main.py
HEALTHCHECK --start-period=10s --interval=3s --timeout=3s --retries=1 \
	CMD curl -f http://localhost:5000 || exit 1
ENTRYPOINT ["python", "/main.py"]
