"""gunicorn configuration"""

bind = "0.0.0.0:5008"
workers = 2
accesslog = "-"
loglevel = "info"
capture_output = True
enable_stdio_inheritance = True
