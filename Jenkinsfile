pipeline {
    agent any

    environment {
        PYTHON_BIN = "C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest"
        FLASK_BIN = "C:\\Users\\danie\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\flask"
        WIREMOCK_JAR = "C:\\Tools\\wiremock-standalone-3.10.0.jar"
        FLASK_APP = "app\\api.py"
    }

    stages {
        stage('GetCode') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/wien996/CP1.A.DevopsCloudUnir.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                bat "dir"
            }
        }

        stage('Tests') {
            parallel {
                stage('Unit') {
                    steps {
                        echo 'Running Unit Tests...'
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            bat """
                                SET PYTHONPATH=%WORKSPACE%
                                ${PYTHON_BIN} --junitxml=result-unit.xml test\\unit
                            """
                        }
                    }
                }

                stage('Rest') {
                    steps {
                        echo 'Running Integration Tests...'
                        // Iniciar WireMock para pruebas simuladas
                        bat """
                            start /B java -jar ${WIREMOCK_JAR} --port 9090
                        """
                        
                        // Iniciar la aplicación Flask y ejecutar pruebas REST
                        catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                            bat """
                                set FLASK_APP=${FLASK_APP}
                                SET PYTHONPATH=%WORKSPACE%
                                start /B ${FLASK_BIN} run
                                ${PYTHON_BIN} --junitxml=result-rest.xml test\\rest
                            """
                        }
                    }
                }
            }
        }

        stage('Results') {
            steps {
                echo 'Collecting and displaying test results...'
                junit 'result*.xml'
                archiveArtifacts artifacts: 'result*.xml', allowEmptyArchive: true
            }
        }
    }
}
