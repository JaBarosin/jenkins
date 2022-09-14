# Jenkins Docker server setup
These instructions will help you setup, build and run your container with docker.sock mounted as volume so jenkins server can also run docker in the container.

**Setup and Build**

- Prior to building your jenkins container:
  - Clone this repository
  - Add cbctl binary to your app folder

- Build image  - ```sudo docker build . -t <image-name>```

- Confirm docker engine is installed and up to date - ```docker --version```

**Option 1 - Quick start run with docker:**

NOTE: replace <image/name> with your <you-repository/jenkins-container>

```
docker run \
  --name jenkins-server \
  --publish 8080:8080 \
  --publish 50000:50000 \
  --volume /var/jenkins:/var/jenkins_home \
	--volume /var/run/docker.sock:/var/run/docker.sock \
  <image/name>
```

- Once your jenkins server is up and running, the homepage will require an initial login password which can be found by running ```docker exec jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword```

Update the cbctl creds:
- Copy the commands provided in the CLI config setup guide.
- attach to your jenkins-server - ```docker exec -it jenkins-server /bin/bash```
- paste in cli config details and press enter.  Confirm that they are stored on your jenkins-server by running - ```cat ~/.cbctl/.cbctl.yaml```


**Option 2 - Setup Jenkins-server to run as Service**

Setup jenkins user:
  - sudo groupadd --system jenkins
  - sudo useradd -s /sbin/nologin --system -g jenkins jenkins
  - sudo mkdir /var/jenkins
  - sudo chown -R 1000:1000 /var/jenkins
Create service for systemd:
  - sudo vi /etc/systemd/system/jenkins-docker.service
  - copy in jenkins-docker.service and update image name
Start jenkins-docker as service:
  - sudo systemctl daemon-reload
  - sudo systemctl start jenkins-docker


**Jenkins Plugins**

Once logged in, go to [Managed Jenkins] > [Manage Plugins] to add additional plugins after initial setup.

If integrating with Slack add:
- Slack Notification
- Global Slack Notification

**Credentials**

If using the Jenkinsfile in [JaBarosin/NodeApp](https://github.com/JaBarosin/NodeApp) demo, you will need to add creds for a few tools.
 
- For Docker needs a username/password credential (can do this via the Jenkins UI at *your-jenkins-docker-server IP/credentials/store/system/domain/_/*
- For [Slack secret text credential](https://plugins.jenkins.io/slack/) 

Source of setup steps:
https://computingforgeeks.com/running-jenkins-server-in-docker-container-systemd/
