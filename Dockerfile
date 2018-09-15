FROM python

RUN apt-get update && apt-get install -y mplayer && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/*
RUN pip install Flask
ADD ./ palacsinta
WORKDIR /palacsinta

ENTRYPOINT ["python"]
CMD ["palacsinta.py"]