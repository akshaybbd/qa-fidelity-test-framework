# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install project dependencies
RUN pip install -r requirements.txt

# Copy the test files
COPY . .

# Set environment variables (if needed)
# ENV VARIABLE_NAME=value

# Run the Behave tests
CMD ["behave"]
