pipeline {
    agent any

    stages {
        stage('GetCode') {
            steps {
                git 'https://github.com/wien996/CP1.A.DevopsCloudUnir.git'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Reto 3'
                bat "dir"
            }
        }
        
		stage('Tests') {
			parallel {	
				stage('Unit') {
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
					        // Start WireMock
					        bat '''
					            start /B java -jar C:\\Tools\\wiremock-standalone-3.10.0.jar --port 9090
					        '''
					        
					        // Start Flask app and execute REST tests
					        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
					            bat '''
					                set FLASK_APP=app\\api.py
					                SET PYTHONPATH=%WORKSPACE%
					                start /B C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\flask run
					                C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest --junitxml=result-rest.xml test\\rest
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
