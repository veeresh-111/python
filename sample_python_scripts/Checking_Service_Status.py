import subprocess

service_name = 'httpd'
status = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE)
print(f'Status of {service_name}:', status.stdout.decode().strip())
