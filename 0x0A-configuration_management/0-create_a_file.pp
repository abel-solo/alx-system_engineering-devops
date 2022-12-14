# creating a file using puppet unsing below specification
file { '/tmp/school':
  path    => '/tmp/scchool',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
