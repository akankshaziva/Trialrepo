pipeline {
	
	agent any
	
	stages {
		
		stage("build") {
		
			steps {
				sh 'pwd'
			 
			}
		}
		
		stage("test") {
		
			steps {
				sh ' cd /var/lib/jenkins/workspace '
			 
			}
		}
		
		stage("deploy") {
		
			steps {
				sh '''
				pip3 install jenkinsapi
				python3 quickstart.py
				'''
			 
			}
		}
	}
}
