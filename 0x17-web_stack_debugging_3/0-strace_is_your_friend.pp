# Solve issue from wordpress-settings 

exec { 'fix-wp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
