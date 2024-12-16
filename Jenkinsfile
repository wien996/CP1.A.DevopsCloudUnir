pipeline {
    agent any
    environment {
        PYTHON = "C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python313\\Scripts"
        FLASK_APP = "app\\api.py"
        PYTHONPATH = "%WORKSPACE%"
    }
    stages {
        stage('GetCode') {
            steps {
                git 'https://github.com/wien996/CP1.A.DevopsCloudUnir.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Starting build process for branch develop.'
                bat "dir"
            }
        }
        stage('Tests') {
            parallel {			
		stage('Unit'){
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            bat '''
                                SET PYTHONPATH=%WORKSPACE%
                                C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest --junitxml=result-unit.xml test\\unit
                            '''
                        }
                    }
                }
			
                stage('Rest') {
                    steps {
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            bat '''
                                SET FLASK_APP=${FLASK_APP}
                                SET PYTHONPATH=%WORKSPACE%
                                start /B C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\flask run
                                ${PYTHON_BIN}\\pytest --junitxml=result-rest.xml test\\rest
                            '''
                        }
                    }
                }
            }
        }
        stage('Results') {
            steps {
                junit 'result*.xml'
            }
        }
    }
}
