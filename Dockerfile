# Dockerfile
# Basisimage für Python-Anwendungen herunterladen
FROM python:3.8-alpine
# Notwendige Bibliotheken installieren
RUN pip install flask
# Arbeitsverzeichnis im Container wechseln
WORKDIR /app
# Kopiere lokale Datei in das Container-Image
COPY Server.py /app
# Konfiguriere den Befehl, der im Container ausgeführt werden soll 
# (Anwendung Python + Skriptname als Parameter)
ENTRYPOINT [ "python" ]
CMD ["Server.py" ]