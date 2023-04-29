## Homework 19 - Jenkins  

#### Project Description  
Create a simple Jenkins pipeline for a private Github repo and Dockerhub to build an image for a GLTF viewer web app for animated 3D models.  

* Step 1: Generated access tokens from Github and Dockerhub and created credentials for the accounts in Jenkins settings
![Global credentials](./assets/jenkins_global_credentials.png)  

* Step 2: Installed Jenkins Docker plugins  

* Step 3: Initial Jenkins pipeline configuration  
![Jenkins initial pipeline](./assets/jenkins_pipeline_initial_setup.png)  

* Step 4: Pushed the code to github  
![Github repo](./assets/github_private_repo.png)  

  **Project structure:**  
  * Bundler: Webpack config for the dev and prod versions of the application. For the sake of simplicity in this exercise we are only building the dev version and pushing that to Docker.  
  ![bundler github folder](./assets/github_bundler.png)  

  * Src: Contains the application code 
  ![src github folder](./assets/github_src.png)  

  * Static: Contains the model, scene and textures  
  ![static github folder](./assets/github_static.png)  

  * Dockerfile

  * Jenkinsfile  
    ```Jenkinsfile
    pipeline {
      agent any
      options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
      }
      environment {
        registry = "neonhermit/gltf-anim"
        dockerImage = ''
        DOCKERHUB_CREDENTIALS = credentials('dockerhub_id')
      }
      stages {
        stage('Build image') {
          steps {
            script {
              dockerImage = docker.build("${registry}:${BUILD_NUMBER}")
            }
          }
        }
        stage('Push image') {
          steps {
            script {
              docker.withRegistry('https://registry-1.docker.io', 'dockerhub_id') {
                dockerImage.push()
              }
            }
          }
        }
      }
      post {
        always {
          sh 'docker logout'
        }
      }
    }
    ```

* Step 5: Build Now from Jenkins  
![Jenkins manual build](./assets/jenkins_manual_build.png)  

  After pressing the Build now button we can see that our project is built successfully.  
  * Since we specified in the Jenkinsfile to discard old builds if we go to the Jenkins pipeline configuration for the project we can see that the Discard old builds is now checked and we have a Strategy and number of builds to keep.
  ![jenkins discard old builds](./assets/jenkins_pipeline_setup_build_discard.png)   

  * Running the image  
  ![app build 1](./assets/app_build1.png)  

* Step 6: Install *ngrock*,  
in the Jenkins configuration for the pipeline we check BuildTriggers -> Github hook trigger  
![build trigger](./assets/jenkins_pipeline_settings_build_trigger.png)  

  and in the github repo we go to settings -> webhooks, adding a webhook to trigger only on push event.  
  ![github webhook](./assets/github_webhook_setup.png)

* Step 7: Modified the code to not have a scene background color, and pushed that to the github repo.  
![jenkins build](./assets/jenkins_build.png)  
![docker hub](./assets/dockerhub.png)  
![app build 2](./assets/app_build2.png)