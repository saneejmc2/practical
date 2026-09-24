🚀 1. Prerequisites
Make sure you have:

Docker installed (docker --version)
Port 8080 free (Jenkins UI)

📦 2. Pull Jenkins Image
Use the official image:

docker pull jenkins/jenkins:lts

▶️ 3. Run Jenkins Container
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

🔹 What this does:
-p 8080:8080 → Jenkins web UI
-p 50000:50000 → agent communication
-v jenkins_home:/var/jenkins_home → persistent data

🌐 4. Access Jenkins
Open browser:

http://localhost:8081

🔑 5. Get Initial Admin Password
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword