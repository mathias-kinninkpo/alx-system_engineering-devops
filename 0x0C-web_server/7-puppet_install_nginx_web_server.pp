# Install Nginx web server
# Configure Nginx server

# Update the existing packages
exec { 'sudo apt-get update':
  path    => ['/usr/bin', '/usr/sbin'],
  command => 'apt-get update'
}

# Install nginx
package { 'nginx':
  ensure   => installed,
  provider => apt,
  require  => Exec['sudo apt-get update']
}

# Install ufw to allow the firewall to accept HTTP request
package { 'ufw':
  ensure   => installed,
  provider => apt,
  require  => Exec['sudo apt-get update']
}

# Configure the firewall
exec { 'sudo ufw allow \'Nginx HTTP\'':
  path    => ['/usr/bin', '/usr/sbin'],
  command => 'ufw allow \'Nginx HTTP\'',
  require => Package['ufw']
}

# Create the index.html file when querying Nginx at its root /
file { 'Hello World!':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Hello World!\n'
}

exec { '/etc/nginx/sites-available/default':
  path    => ['/usr/bin', '/usr/sbin'],
  command => 'sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default'
}

exec { 'service nginx start':
  path    => ['/usr/bin', '/usr/sbin'],
  command => 'service nginx start'
}
