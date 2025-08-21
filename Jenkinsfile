pipeline {
  agent any

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '20'))
    disableConcurrentBuilds()
  }

  environment {
    PY = 'python3'
    VENV = '.venv'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'python3 --version || true'
        sh 'pip3 --version || true'
      }
    }

    stage('Prepare Python') {
      steps {
        sh '''
          set -eu
          # Ensure venv module exists (Ubuntu/Debian)
          command -v python3 >/dev/null
          if ! python3 -m venv --help >/dev/null 2>&1; then
            echo "Python venv module missing. Install: sudo apt-get update && sudo apt-get install -y python3-venv"
            exit 1
          fi
          # Create venv in workspace (owned by jenkins user)
          if [ ! -d "${VENV}" ]; then
            ${PY} -m venv "${VENV}"
          fi
          . "${VENV}/bin/activate"
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Lint') {
      steps {
        sh '''
          set -e
          . "${VENV}/bin/activate"
          flake8 src tests
        '''
      }
    }

    stage('Test') {
      steps {
        sh '''
          set -e
          . "${VENV}/bin/activate"
          mkdir -p reports
          pytest -q --junitxml=reports/junit.xml
        '''
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
