FROM jupyter/pyspark-notebook:414b5d749704

LABEL maintainer="Jupyter Project"

USER $NB_UID

# Apache Toree kernel
RUN pip install toree==0.3.0 && \
    jupyter toree install --sys-prefix && \
    rm -rf /home/"$NB_USER"/.local && \
    fix-permissions "$CONDA_DIR" && \
    fix-permissions /home/"$NB_USER"

# Spylon-kernel
RUN conda install --quiet --yes 'spylon-kernel=0.4*' && \
    conda clean --all -f -y && \
    python -m spylon_kernel install --sys-prefix && \
    rm -rf /home/"$NB_USER"/.local && \
    fix-permissions "$CONDA_DIR" && \
    fix-permissions /home/"$NB_USER"

# Copy python requirements
COPY requirements.txt requirements.txt

# Install python requirements
RUN pip install -r requirements.txt

# Plotly set up
RUN export NODE_OPTIONS=--max-old-space-size=4096
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build
RUN jupyter labextension install jupyterlab-plotly@1.4.0 --no-build
RUN jupyter labextension install plotlywidget@1.4.0 --no-build
RUN jupyter lab build
RUN unset NODE_OPTIONS
