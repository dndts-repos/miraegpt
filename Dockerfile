FROM python:3.11-slim
WORKDIR /app
RUN pip install mkdocs mkdocs-material
COPY mkdocs.yml .
COPY docs/ docs/
EXPOSE 8000
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]