
# This app is to calculate the expected number of renewals
* Xiaoyang Liu

# clone the repo
* git clone https://github.com/42195CA/nginx_uwsgi_flask_volterra_calculator.git

# build the docker image
* cd nginx_uwsgi_flask_volterra_calculator
* build the image: $bash build.sh

# if needed, to install docker engine
* sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# run the app
* run a container: $bash run.sh
* web page: localhost:8080
* restart if needed: $bash restart.sh

# modify code and push it to the github
* git status
* git add .
* git commit -m "log message"
* git push

# docker related command
ls all the running instances
* $sudo docker ps -a
* stop and remove one instance if needed
* $sudo docker stop flask_volterra
* $sudo docker remove flask_volterra
rm image
* docker image ls
* docker rmi imgName

