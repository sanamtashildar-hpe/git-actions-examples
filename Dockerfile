FROM alpine:3.19

# Simple demo image that prints repository details
RUN adduser -S appuser
USER appuser
WORKDIR /app
COPY README.md /app/README.md

CMD ["sh", "-c", "echo 'Docker build successful' && cat /app/README.md"]
