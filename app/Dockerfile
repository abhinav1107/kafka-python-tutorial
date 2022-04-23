FROM confluentinc/cp-kafka:7.0.1
USER root
RUN pip install --no-cache-dir confluent-kafka
COPY --chown=appuser:appuser app.py /home/appuser/app.py
WORKDIR /home/appuser
USER appuser
