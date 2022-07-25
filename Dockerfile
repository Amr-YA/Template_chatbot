FROM python:3.7
WORKDIR /app
ENV HOME=/app
COPY . .
RUN pip install -r requirements.txt 
RUN python -m spacy download xx_ent_wiki_sm
RUN python -m spacy download xx_sent_ud_sm
EXPOSE 5005 
USER 1001
CMD ["bash", "run.sh"]

