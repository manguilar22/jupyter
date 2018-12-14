# Jupyter 

### Generate Password for Jupyter Notebook

**-$** jupyter notebook password 

*Copy and Paste your **sha:<_id>** within **~/.jupyter/jupyter_notebook_config.py** *

### Start Server (*HTTP*)

**-$** jupyter notebook 

### Generate Self-Signed Certificates (*SSL/TLS*)

**-$** openssl req -x509 -nodes -days 365 -newkey rsa:1028 -keyout private_key.key -keyout public_key.pem

### Start Jupyter Server (*HTTPS*)

**-$** jupyter notebook --keyfile=private_key.key --certfile=public_key.pem
