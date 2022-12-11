# use puppet to make changes to configuration file
# set up your client SSH configuration file to connect to a server without password

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
        path    => '/bin/'
}
