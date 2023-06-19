pipeline {
  agent any

  stages {
    stage('Build Docker Image') {
      steps {
        // Build the Docker image
        script {
          docker.build("behave-selenium")
        }
      }
    }

    stage('Run Tests in Docker') {
      steps {
        // Run the Behave tests using the Docker image
        script {
          docker.image("behave-selenium").run()
        }
      }
    }
  }
}
