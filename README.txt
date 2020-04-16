 1. The python program "AccessAPI.py" tries to acccess the https://macaddress.io/ api and retrieve the information pertaining to that address.
 2. The API key is unique to each user singed up to the API and hence, security is handled by the API Key. The API is usable only with a valid API key.
 3. The program takes the input MAC address in the format of command-line.
 4. The script has been dockerized using the "Dockerfile" file, that does the following steps:
	a. This line is used to specify the docker OS and we have used ubuntu as the OS.
	b. The next line mentions the file that needs to be added to the docker image.
	c. Since we are using python and the "requests" library, we have it preinstalled in the next line.
	d. We speicify the python command that needs to happen to run our script.
5. The docker image was created using the command "docker build --tag python-accessapi-app ." , which creats the image python-accessapi-app.
6. Since we are passing command-line arugments to our python script, the following line was used to run the build "docker run python-accessapi-app python AccessAPI.py 44:38:39:ff:ef:57"