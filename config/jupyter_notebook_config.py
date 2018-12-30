# Set options for certfile, ip, password, and toggle off
# browser auto-opening
#c.NotebookApp.certfile = u'/absolute/path/to/your/certificate/mycert.pem'
#c.NotebookApp.keyfile = u'/absolute/path/to/your/certificate/mykey.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server

c.NotebookApp.allow_root = False 

c.NotebookApp.ip = '*'

c.NotebookApp.password = u'sha1:f71d43ef14ea:35d9e0dce987ac937a85f9111bdbf0933ab24d72'

c.NotebookApp.allow_password_change = False

c.NotebookApp.password_required = True

c.NotebookApp.open_browser = False

c.NotebookApp.base_url = '/test/'

# THIS IS THE LINE TO TEST , scalability 
c.NotebookApp.iopub_data_rate_limit = 10e6

# It is a good idea to set a known, fixed port for server access
c.NotebookApp.port = 4000
