FROM gavin17423/forbigquery
WORKDIR /app
ADD . /app
RUN ["pip3","install","BeautifulSoup4"]
RUN ["pip3","install","selenium"]
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/HowDress-3b7e9bc86e83.json"

CMD ["python3","/app/connectBigquery.py"]
CMD ["/bin/bash"]

