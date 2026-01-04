# Use a lightweight Python-Alpine image
FROM python:3.9-alpine

# Install build dependencies for psutil
RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /app

# Install Flask and psutil
RUN pip install --no-cache-dir flask psutil

# Copy app files
COPY . .

EXPOSE 80

CMD ["python", "app.py"]
