FROM python:3.10-slim-bullseye
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install pipenv
RUN useradd --create-home --shell /bin/bash/ anon
USER anon
ENV PATH=/home/anon/.local/bin:$PATH WORKON_HOME=/home/anon/.local/share/virtualenvs
RUN mkdir --parents /home/anon/.local/share/virtualenvs/
RUN chmod 777 /home/anon/.local/share/virtualenvs/
WORKDIR /home/anon/src
CMD ["bash"]
