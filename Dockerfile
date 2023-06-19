FROM python:3.9

WORKDIR /app

# Install Chrome browser and dependencies
RUN apt-get update && apt-get install -yq \
    wget \
    gnupg \
    ca-certificates \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -yq \
    google-chrome-stable


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["behave"]
