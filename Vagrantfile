Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty32"

  config.vm.network :forwarded_port, host: 8000, guest: 8000
  config.vm.network :forwarded_port, host: 8080, guest: 8080

end
