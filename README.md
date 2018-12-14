# Jupyter 

### Generate Password for Jupyter Notebook

**-$** jupyter notebook password 

Copy and Paste your **sha:<_id>** within **~/.jupyter/jupyter_notebook_config.py** 

### Start Server (*HTTP*)

**-$** jupyter notebook 

### Generate Self-Signed Certificates (*SSL/TLS*)

**-$** openssl req -x509 -nodes -days 365 -newkey rsa:1028 -keyout <span style="color:orange">private_key.key</span> -keyout <span style="color:blue">public_key.pem</span> 

### Start Jupyter Server (*HTTPS*)

**-$** jupyter notebook --keyfile=<span style="color:orange">private_key.key</span> --certfile=<span style="color:blue">public_key.pem</span>
