node{

    stage('SCM checkout'){
        git url: 'https://github.com/mukeshreddy02/Log_Reg_CI-CD.git',branch: 'master'
    }


    stage('Build Docker Image'){
        sh 'docker build -t mukeshreddy02/python_flask_log_reg .'
    }

    stage('Push Docker Image'){
        withCredentials([string(credentialsId: 'Docker_Hub_Pwd', variable: 'Docker_Hub_Pwd')]) {
          sh "docker login -u mukeshreddy02 -p ${Docker_Hub_Pwd}"
        }
        sh 'docker push mukeshreddy02/python_flask_log_reg'
     }

    stage('Run Docker Image In Dev Server'){

        def dockerRun = ' docker run  -d -p 5000:5000 --name python_flask_log_reg mukeshreddy02/python_flask_log_reg'
          
          sshagent(['DOCKER_SERVER']) {
          sh 'ssh -o StrictHostKeyChecking=no ubuntu@13.232.172.99 docker stop python_flask_log_reg || true'
          sh 'ssh  ubuntu@13.232.172.99 docker rm python_flask_log_reg || true'
          sh 'ssh  ubuntu@13.232.172.99 docker rmi -f  $(docker images -q) || true'
          sh "ssh  ubuntu@13.232.172.99 ${dockerRun}"
       }
       
    }
   
     stage('SendEmailNotification'){
         emailext body: '''Build is Over

         Regards,
         Mukesh reddy,

         ''', subject: 'Build is Over', to: 'mukeshram1995@gmail.com'
      }
} 
