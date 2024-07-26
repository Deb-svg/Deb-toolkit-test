# scripts/deploy_to_server.py

import paramiko
import sys

def deploy_to_server(package_path, server_ip, username, password):
    try:
        # Set up the SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        # Upload the package
        sftp = ssh.open_sftp()
        sftp.put(package_path, '/remote/path/to/package.tar.gz')
        sftp.close()

        # Execute deployment commands on the remote server
        commands = [
            'tar -xzvf /remote/path/to/package.tar.gz -C /remote/deploy/directory',
            'cd /remote/deploy/directory && ./deploy_script.sh'  # Replace with actual deploy script or commands
        ]
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            print(stdout.read().decode())
            print(stderr.read().decode())

        ssh.close()
        print('Deployment completed successfully.')
    except Exception as e:
        print(f'Error during deployment: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: deploy_to_server.py <package_path> <server_ip> <username> <password>")
        sys.exit(1)

    deploy_to_server(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
