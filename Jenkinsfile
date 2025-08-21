pipeline {
  agent any
  options {
    ansiColor('xterm'); timestamps(); buildDiscarder(logRotator(numToKeepStr: '20')); disableConcurrentBuilds()
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Install Deps') {
      steps {
        sh '''
          set -e
          PY=${PYTHON:-python3}
          $PY -m pip install --user --upgrade pip
          $PY -m pip install --user -r requirements.txt
          echo "PATH update hint: ~/.local/bin should be on PATH"
        '''
      }
    }
    stage('Lint') {
      steps { sh '~/.local/bin/flake8 src tests || flake8 src tests' }
    }
    stage('Test') {
      steps {
        sh 'mkdir -p reports && (~/.local/bin/pytest -q --junitxml=reports/junit.xml || pytest -q --junitxml=reports/junit.xml)'
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/junit.xml'
          archiveArtifacts artifacts: 'reports/**', onlyIfSuccessful: false
        }
      }
    }
  }
}
