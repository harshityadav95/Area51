## Setting up Virtual Environment


### Settin up Python pyenv Linux
```
# Install Pyenv Dependency
$sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

$ curl https://pyenv.run | bash

# For Bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

# Refreshing the Shell
$ exec "$SHELL"

# Check pyenv version
$ pyenv --version

# View available python version
$ pyenv install --list

# Install python version
$ pyenv install 3.12.0

# Setpyenv version
$ pyenv global 3.12.0
$ pyenv local 3.12.0
$ pyenv shell 3.12.0

# Install  pip
$ python -m pip install --upgrade pip

# Install virtualenv
$ pip install virtualenv
$ python -m venv venv
```
### Activate virtualenv
```
#Windows
$ env/Scripts/activate

#Linux/Unix
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

```

## Running Streamlit Application

```
$ streamlit run main.py

# Run Streamlit Application on Different port

$ streamlit run main.py --port 8501

```

## Docker Build Locally

```
docker build -t streamlitstarter:v1 .

docker images

docker run -p 8501:8501 streamlitstarter:v1

```
To view your app, users can browse to http://0.0.0.0:8501 or http://localhost:8501

## Build Using Poadman Locally
```
podman build -t streamlit starter -f Dockerfile .
```



## Reference 
- https://medium.com/@aashari/easy-to-follow-guide-of-how-to-install-pyenv-on-ubuntu-a3730af8d7f0
- https://docs.streamlit.io/deploy/tutorials/docker
- https://hackmd.io/@maelvls/fixing-403-forbidden-ghcr
- https://www.propelauth.com/post/streamlit-authentication






