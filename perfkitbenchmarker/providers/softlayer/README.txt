
Notes on prereqs    :
PKB installation may require packages for Pandas and other components to install correctly.  
- On Ubuntu 14 the following prereqs were required:  apt-get install build-essential; apt-get install python-dev

1) Install PKB and SoftLayer requirements
	sudo pip install -r requirements.txt
	sudo pip install -r requirements-softlayer.txt
	
2) Run SoftLayer setup program
	slcli setup

3) To view system create options used below issue the following commands
   slcli vs  create-options
   
3) Run benchmarks

Examples:
NOTE: iperf currently needs to be run as root.  
>python pkb.py --cloud=SoftLayer --benchmarks=iperf --softlayer_user_name=root

Benchmark with 1Gib Nic card specified
>python pkb.py --cloud=SoftLayer --benchmarks=ping  --machine_type="{\"cpus\": 2, \"memory\": 4096, \"os\": \"UBUNTU_LATEST_64\", \"nic\": 1000 }" --softlayer_user_name=root

Benchmark with the Tokyo 4 datacenter specified and machine type 4 cpus, 4G memory,  1Gib NIC card
>python pkb.py --cloud=SoftLayer --benchmarks=iperf --zones=tok04 --machine_type="{\"cpus\": 4, \"memory\": 4096, \"os\": \"UBUNTU_LATEST_64\", \"nic\": 1000 }"  --softlayer_user_name=root

The Redis Benchmark with a Redis parameter and datacenter specified 
NOTE: currnently needs to be run as root
>python pkb.py --cloud=SoftLayer --benchmarks=redis --redis_clients=2  --zones=tok04 --softlayer_user_name=root

A private & public VLAN id specified to ensure VMs are located on the same vlan. 
VLAN ids can be queried with: slcli vlan list
The risk of specifing a VLAN is there is a chance no resources will be available for that VLAN 
>python pkb.py --cloud=SoftLayer --benchmarks=ping  --machine_type="{\"cpus\": 4, \"memory\": 4096, \"os\": \"UBUNTU_LATEST_64\", \"nic\": 1000, \"public_vlan_id\": 1205613, \"private_vlan_id\": 1205615}"  --softlayer_user_name=root

Storage benchmark with SAN attached and disk sizes specified
>python pkb.py --cloud=SoftLayer --benchmarks=fio  --machine_type="{\"cpus\": 4, \"memory\": 4096, \"os\": \"UBUNTU_LATEST_64\", \"nic\": 1000, \"san\": true, \"disk_size0\": 100, \"disk_size1\": 300 }"   --softlayer_user_name=root

Disk IO benchmark
>python pkb.py --cloud=SoftLayer --benchmarks=bonnie++ --zones=tok04 --machine_type="{\"cpus\": 4, \"memory\": 4096, \"os\": \"UBUNTU_LATEST_64\", \"nic\": 1000 }"  --softlayer_user_name=root


>python pkb.py --cloud=SoftLayer --benchmarks=unixbench --machine_type="{\"cpus\": 4, \"memory\": 4096, \"os\": \"UBUNTU_LATEST_64\", \"nic\": 1000 }"  --softlayer_user_name=root

