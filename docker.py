import streamlit as st

## List of docker commands
#1. docker –version,
#2. docker pull,
#3. docker run,
#4. docker ps,
#5. docker ps -a,
#6. docker exec,
#7. docker stop,
#8. docker kill,
#9. docker commit,
#10. docker login,
#11. docker push,
#12. docker images,
#13. docker rm,
#14. docker rmi,
#15. docker build


a = """
<style>
#MainMenu {visibility : hidden; }
footer {visibility : hidden; }
</style>
"""
st.markdown(a, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #0E8500;'>DOCKER COMMANDS</h1>", unsafe_allow_html=True)

commands = ['About/Select','docker –version', 'docker pull', 'docker run', 'docker ps', 'docker ps -a', 'docker exec', 'docker stop', 'docker kill',
            'docker commit', 'docker login', 'docker push', 'docker images', 'docker rm', 'docker rmi', 'docker build'
            ]
select = st.selectbox('', commands)

if select == 'docker –version':
    cmd = ('docker –version')
    st.write('This command is used to get the currently installed version of docker')
    st.code(cmd)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/Docker_Version-Docker-Commands-Edureka-3-e1510653973130.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/version/"><i>&#9654;  Version Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)


elif select == 'docker pull':
    st.write('This command is used to pull images from the docker repository(hub.docker.com)')
    cmd1 = ('docker pull <image name>')
    st.code(cmd1)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/Docker_Pull-Docker-Commands-Edureka-2-e1510653950923.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/pull/"><i>&#9654;  Pull Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker run':
    st.write('This command is used to create a container from an image')
    cmd2 = ('docker run -it -d <image name>')
    st.code(cmd2)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_run-Docker-Commands-Edureka-e1510653910376.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/run/"><i>&#9654;  Run Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker ps':
    st.write('This command is used to list the running containers')
    cmd3 = ('docker ps')
    st.code(cmd3)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_ps-Docker-Commands-Edureka-e1510653881541.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/ps/"><i>&#9654;  PS Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker ps -a':
    st.write('This command is used to show all the running and exited containers')
    cmd4 = ('docker ps -a')
    st.code(cmd4)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_psa-Docker-Commands-Edureka-e1510653854892.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/ps/"><i>&#9654;  PS Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker exec':
    st.write('This command is used to access the running container')
    cmd5 = ('docker exec -it <container id> bash')
    st.code(cmd5)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_exec-Docker-Commands-Edureka-e1510653829237.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/exec/"><i>&#9654;  EXEC Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker stop':
    st.write('This command stops a running container')
    cmd6 = ('docker stop <container id>')
    st.code(cmd6)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_stop-Docker-Commands-Edureka-e1510653793521.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/stop/"><i>&#9654;  Pull Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker kill':
    st.write('This command kills the container by stopping its execution immediately. The difference between ‘docker kill’ and ‘docker stop’ is that ‘docker stop’ gives the container time to shutdown gracefully, in situations when it is taking too much time for getting the container to stop, one can opt to kill it')
    cmd7 = ('docker kill <container id>')
    st.code(cmd7)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_kill-Docker-Commands-Edureka-e1510653772661.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/kill/"><i>&#9654;  Kill Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker commit':
    st.write('This command creates a new image of an edited container on the local system')
    cmd8 = ('docker kill <conatainer id> <username/imagename>')
    st.code(cmd8)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_commit-Docker-Commands-Edureka-e1510653734760.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/commit/"><i>&#9654;  Commit Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker login':
    st.write('This command is used to login to the docker hub repository')
    cmd9 = ('docker login')
    st.code(cmd9)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_login-Docker-Commands-Edureka-1-e1510653706645.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/login/"><i>&#9654;  Login Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker push':
    st.write('This command is used to push an image to the docker hub repository')
    cmd10 = ('docker push <username/image name>')
    st.code(cmd10)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_push-Docker-Commands-Edureka-e1510653678749.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/push/"><i>&#9654;  Push Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker images':
    st.write('This command lists all the locally stored docker images')
    cmd11 = ('docker images')
    st.code(cmd11)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_images-Docker-Commands-Edureka-e1510653647888.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/images/"><i>&#9654;  Images Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker rm':
    st.write('This command is used to delete a stopped container')
    cmd12 = ('docker rm <container id>')
    st.code(cmd12)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_rm-Docker-Commands-Edureka-e1510653622699.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/rm/"><i>&#9654;  rm Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker rmi':
    st.write('This command is used to delete an image from local storage')
    cmd13 = ('docker rmi <image-id>')
    st.code(cmd13)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_rmi-Docker-Commands-Edureka-e1510653592230.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/rmi/"><i>&#9654;  rmi Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'docker build':
    st.write('This command is used to build an image from a specified docker file')
    cmd14 = ('docker build <path to docker file>')
    st.code(cmd14)
    st.image('https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/docker_built-Docker-Commands-Edureka-e1510653559161.png')
    st.markdown('<strong>'
                '<a href = "https://docs.docker.com/engine/reference/commandline/build/"><i>&#9654;  Build Command Official Documentation</i></a>'
                '</strong>', unsafe_allow_html=True)

elif select == 'About/Select':
    st.markdown("<br></br>"
                "<p style='text-align:center;font-size:20px'>Docker helps developers bring their ideas to life by conquering the complexity of app development. We simplify and accelerate development workflows with an integrated dev pipeline and through the consolidation of application components. Actively used by millions of developers around the world, Docker Desktop and Docker Hub provide unmatched simplicity, agility and choice.</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size:35px;text-align:center'>"
                "<b><strong>DOCKER ARCHITECTURE EXPLANATION</strong>"
                "</b>"
                "<p style = 'font-size:15px;text-align:center;font-family:Comic Sans MS'>Docker uses a client-server architecture.</p>"
                "</p>", unsafe_allow_html=True)
    st.image('https://csharpcorner-mindcrackerinc.netdna-ssl.com/article/docker-architecture-environtment-advantages/Images/Docker%20Architecture.png')

    st.markdown("<h2 style='text-align:center;color:white;'>" 
                "<p style='font-size:25px;text-align:left;font-family: Roboto'>"
                "<b>&#9673; BUILD</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; The docker <a href = 'https://docs.docker.com/engine/reference/commandline/build/'>build command</a> builds Docker images from a Dockerfile and a “context”. A build’s context is the set of files located in the specified PATH or URL. "
                "</p>"
                "</p>"
    
                "<p style='font-size:25px;text-align:left;font-family: Roboto'>"
                "<b>&#9673; PULL</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; The docker <a href = 'https://docs.docker.com/engine/reference/commandline/pull/'>build command</a> builds Docker images from a Dockerfile and a “context”. A build’s context is the set of files located in the specified PATH or URL.</p>"
                "</p>"
    
                "<p style='font-size:25px;text-align:left;font-family: Roboto'>"
                "<b>&#9673; RUN</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; The docker <a href = 'https://docs.docker.com/engine/reference/commandline/run/'>run command</a> first creates a writeable container layer over the specified image, and then starts it using the specified command.</p>"
                
                "<br></br>"
    
                "<p style='font-size:25px;text-align:left;font-family: Sitka Text'>"
                "<b>&#9634; Docker Client</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out.</p>"
                "</p>"
                
                "<p style='font-size:25px;text-align:left;font-family: Sitka Text'>"
                "<b>&#9634; Docker Daemon</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.</p>"
                "</p>"

                "<p style='font-size:25px;text-align:left;font-family: Sitka Text'>"
                "<b>&#9634; Docker Images</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization.</p>"
                "</p>"

                "<p style='font-size:25px;text-align:left;font-family: Sitka Text'>"
                "<b>&#9634; Docker Containers</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; A container is a runnable instance of an image. You can create, start, stop, move, or delete a container using the Docker API or CLI. You can connect a container to one or more networks, attach storage to it, or even create a new image based on its current state.</p>"
                "</p>"
                
                "<p style='font-size:25px;text-align:left;font-family: Sitka Text'>"
                "<b>&#9634; Docker Registry</b>"
                "<p style='font-size:15px;text-align:left;font-family: Comic Sans MS'>&#9644; A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default. You can even run your own private registry.</p>"
                "</h2>", unsafe_allow_html=True)

    st.markdown("<h5 style = 'text-align : left; text-color : white>"
                "<p style='font-size:1px'>"
                "<u>Youtube Videos link</u>"
                "<br></br>"
                "<a href = 'https://youtu.be/Gw2Jrid4SaQ'>CodeWithHarry</a>"
                "<br></br>"
                "<a href = 'https://youtu.be/pTFZFxd4hOI'>Programming with Mosh</a>"
                "<br></br>"
                "<a href = 'https://youtu.be/GGaDSAMeopo'>Telusko</a>"
                "<br></br>"
                "<a href = 'https://youtu.be/3c-iBn73dDE'>TechWorld with Nana</a>"
                "</p>"
                "</h3>", unsafe_allow_html=True)


    st.markdown("</p><br>Official Documentation <a href = 'https://docs.docker.com/get-started/overview/'>link</a></p>"
                "</p>Play with <a href = 'https://labs.play-with-docker.com/'>Docker</a></br></p>"
                , unsafe_allow_html=True)