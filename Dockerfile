FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:9a7d-main

# Install pip
RUN apt-get install -y python3-pip

#install required packages
RUN python3 -m pip install -U scvelo
RUN python3 -c "import scvelo"

RUN python3 -m pip install -U jupyter notebook
RUN jupyter notebook --version

RUN python3 -m pip install -U papermill
RUN python3 -c "import papermill"

RUN python3 -m pip install -U black
RUN python3 -c "import black"

# You can use local data to construct your workflow image.  Here we copy a

COPY runScVelo.ipynb /root/runScVelo.ipynb
COPY runScVelo.sh /root/runScVelo.sh


# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
COPY wf /root/wf
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
RUN python3 -m pip install --upgrade latch
WORKDIR /root
