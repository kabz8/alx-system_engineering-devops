package { 'php5-mbstring':
  ensure => installed,
}

service { 'apache2':
  ensure => running,
  enable => true,
  require => Package['php5-mbstring'],
}

exec { 'enable-mbstring':
  command => '/usr/sbin/php5enmod mbstring',
  unless  => '/usr/sbin/php5query -s -d mbstring',
  require => Package['php5-mbstring'],
  notify  => Service['apache2'],
}
