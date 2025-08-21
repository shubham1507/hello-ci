pipeline {
  agent {
    docker {
      image 'python:3.12-slim'
      args '-u'
    }
  }

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '20'))
    disableConcurrentBuilds()
  }

  environment {
    PIP_DISABLE_PIP_VERSION_CHECK = '1'
    PYTHONDONTWRITEBYTECODE = '1'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'python --version && pip --version'
      }
    }
    stage('Install Deps') {
      steps {
        sh 'pip install --no-cache-dir -r requirements.txt'
      }
    }
    stage('Lint') {
      steps {
        sh 'flake8 src tests'
      }
    }
    stage('Test') {
      steps {
        sh 'mkdir -p reports && pytest -q --junitxml=reports/junit.xml'
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/junit.xml'
          archiveArtifacts artifacts: 'reports/**', onlyIfSuccessful: false
        }
      }
    }
  }

  post {
    success { echo '✅ Build passed!' }
    failure { echo '❌ Build failed. Check stages above.' }
  }
}
