# Options
# https://jupyter-notebook.readthedocs.io/en/stable/config.html

# Set options for certfile, ip, password, and toggle off
# browser auto-opening
#c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'
#c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mykey.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server

c.NotebookApp.allow_root = False 

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8000
c.NotebookApp.allow_remote_access = True
c.NotebookApp.allow_origin = '*' #allow all origins

## Hashed password to use for web authentication.
#  
#  To generate, type in a python/IPython shell:
#  
#    from notebook.auth import passwd; passwd()
#  
#  The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = u''

c.NotebookApp.allow_password_change = False

c.NotebookApp.password_required = True 

c.NotebookApp.open_browser = False

c.NotebookApp.base_url = '/'

################
# Scalability 
###############

# Maximum rate at which stream output can be sent on iopub before they are limited.
c.NotebookApp.iopub_data_rate_limit = 10e6

# Maximum rate at which messages can be sent on iopub before they are limited.
c.NotebookApp.iopub_msg_rate_limit = 10e6 

# Gets or sets the maximum amount of memory, in bytes, that is allocated for use by the buffer manager. (Default: 536870912)
c.NotebookApp.max_buffer_size=536000000 #536e6
