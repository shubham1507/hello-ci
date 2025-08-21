pipeline {
    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PYTHONDONTWRITEBYTECODE       = '1'
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

        stage('Package (optional)') {
            when {
                expression { return fileExists('pyproject.toml') || fileExists('setup.cfg') }
            }
            steps {
                sh 'python -m pip install build && python -m build'
                archiveArtifacts artifacts: 'dist/**', fingerprint: true
            }
        }
    }

    post {
        success {
            echo '✅ Build passed!'
        }
        failure {
            echo '❌ Build failed. Check stages above.'
        }
    }
}
