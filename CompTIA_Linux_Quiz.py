#!/usr/bin/env python3

# CompTIA Linux+ XKO-004 Test

#QUESTION 1
Which of the following would be the BEST solution for a systems administrator to access the graphical user environment of a Linux machine remotely?
    A. VNC
    B. KDE
    C. X11
    D. RPC

Correct Answer: A

#Explanation/Reference:
# Reference: https://www.sfu.ca/computing/about/support/tips/remote-to-linux-with-gui.html

#QUESTION 2
A technical support engineer receives a ticket from a user who is trying to create a 1KB file in the /tmp directory and is getting the following error: No space left on device. The support engineer checks the / tmp directory, and it has 20GB of free space.
Which of the following BEST describes a possible cause for this error?
    A. The /tmp directory is not mounted.
    B. The filesystem is formatted with a 4MB block size.
    C. the filesystem ran out of inodes.
    D. The /tmp directory has been set with an immutable attribute.

Correct Answer: C

#Explanation/Reference:
#Reference: https://www.maketecheasier.com/fix-linux-no-space-left-on-device-error/

#QUESTION 3
Which of the following is the BEST reason for not storing database files in the /var directory?
    A. The /var filesystem is not fast enough for database files.
    B. The number of files in /var is limited by the available inodes.
    C. Files in /var do not have strict file permissions.
    D. If log files fill up /var, it might corrupt the database.

Correct Answer: D



#QUESTION 4
SIMULATION
A junior system administrator had trouble installing and running an Apache web server on a Linux server. You have been tasked with installing the Apache web server on the Linux server and resolving the issue that prevented the junior administrator from running Apache.
INSTRUCTIONS
Install Apache and start the service. Verify that the Apache service is running with the defaults.
Typing “help” in the terminal will show a list of relevant commands.
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.
CentOS Command Prompt

Correct Answer:


QUESTION 5 DRAG DROP
The lead Linux has added a disk, /dev/sdd, to a VM that is running out of disk space. Place the following steps in the correct order from first (1) to last (4) to add the disk to the existing LVM.
Select and Place:

Correct Answer: 

Section: (none) Explanation
Explanation/Reference:
Reference: https://www.rootusers.com/how-to-increase-the-size-of-a-linux-lvm-by-expanding-the-virtualmachine-disk/

#QUESTION 6
An administrator receives a warning about a file system filling up, and then identifies a large file located at / tmp/largelogfile. The administrator deletes the file, but no space is recovered on the file system.
Which of the following commands would BEST assists the administrator in identifying the problem?
    A. lsof  | grep largelogfile
    B. pkill /tmp/largelogfile
    C. pgrep largelogfile
    D. ps –ef  | grep largelogfile
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/solutions/2316
QUESTION 7
Which of the following can be used to boot a DVD from a remote device to initialize a Linux system setup on bare metal hardware as if it is a local DVD?
    A. UEFI
    B. PXE
    C. NFS
    D. GRUB
Correct Answer: A or B
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/installation_guide/ ch-boot-x86
QUESTION 8
After starting a long-running script, a systems administrator needs to verify the frequency of what is filling up the /var partition and kill it because it is consuming too much space.
Which of the following is the correct sequence given only a terminal is available?
A. 1. CTRL-C
    2. bg
    3. watch df  /var
    4. CTRL-C
    5. fg
    6. CTRL-ZB. 1. CTRL-C
    2. fg
    3. watch df  /var
    4. CTRL-Z
    5. bg
    6. CTRL-ZC. 1. CTRL-Z
    2. bg
    3. watch df  /var
    4. CTRL-C
    5. fg
    6. CTRL-CD. 1. CTRL-Z
    2. bg
    3. watch df  /var
    4. CTRL-Z
    5. fg
    6. CTRL-C
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 9
A Linux administrator must identify a user with high disk usage. The administrator runs the # du –s /home/ * command and gets the following output:

Based on the output, User3 has the largest amount of disk space used. To clean up the file space, the administrator needs to find out more information about the specific files that are using the most disk space.
Which of the following commands will accomplish this task?
    A. df –k /home/User3/files.txt
    B. du –a /home/User3/*
    C. du –sh /home/User/
    D. find . –name /home/User3 -print
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://unix.stackexchange.com/questions/37221/finding-files-that-use-the-most-disk-space
QUESTION 10
A Linux server has multiple IPs. A Linux administrator needs to verify if the HTTP server port is bound to the correct IP. 
Which of the following commands would BEST accomplish this task?
    A. route
    B. host
    C. nslookup
    D. netstat
    E. ip
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.tecmint.com/find-listening-ports-linux/
QUESTION 11
A systems administrator needs to append output of ls –lha /opt command to the contents of a test.txt file. Which of the following commands will accomplish this?
    A. ls –lha /opt > test.txt
    B. ls –lha /opt < test.txt
    C. ls –lha /opt >> test.txt
    D. ls –lha /opt << test.txt
Correct Answer: C
Section: (none)
Explanation
Explanation/Reference:
Reference: https://www.cyberciti.biz/faq/linux-append-text-to-end-of-file/
QUESTION 12 A Linux administrator needs to remotely update the contents of the www.comptia.org/contacts URL.
Which of the following commands would allow the administrator to download the current contents of the URL before updating?
    A. curl www.comptia.org/contacts
    B. dig www.comptia.org/contacts
    C. apt-get www.comptia.org/contacts
    D. yum list www.comptia.org/contacts
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.thegeekstuff.com/2012/04/curl-examples/
QUESTION 13 Which of the following BEST describes containers running on a Linux system?
    A. Containers only need the namespaces functionality to run on a Linux system available since kernel 2.6.
    B. Containers need a hypervisor to run on a Linux system. Cgroups namespaces are functionalities used forthe kernel but not for running containers.
    C. Containers only need the cgroups functionality for running on a Linux system. Namespaces is not a Linuxkernel functionality needed for creating and managing containers.
    D. Containers use the cgroups and namespaces functionalities to isolate processes and assign hardwareresources to each of those isolated processes.
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.linuxjournal.com/content/everything-you-need-know-about-linux-containers-part-iiworking-linux-containers-lxc
QUESTION 14
A networked has been crashing intermittently. A Linux administrator would like to write a shell script that will attempt to ping the server and email an alert if the server fails to respond. The script will later be scheduled via cron job.
Which of the following scripts would BEST accomplish this task?
A
B
C

Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 15
A Linux administrator is testing connectivity to a remote host on a shared terminal. The administrator wants to allow other users to access the terminal while the command is executing. 
Which of the following commands should the administrator use?
    A. bg ping remotehost
    B. fg ping remotehost
    C. ping remotehost < results
    D. ping remotehost &
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 16
A Linux administrator needs to switch from text mode to GUI. Which of the following runlevels will start the GUI by default?
A. Runlevel 3 B. Runlevel 4 C. Runlevel 5
D. Runlevel 6
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: http://www.linfo.org/runlevel_def.html
QUESTION 17
A junior systems administrator is configuring localization option environment variables. The administrator is given a checklist of tasks with the following requirements:
 View current settings of the LC_ALL environment variable only.  Modify the LANG environment variable to US English Unicode.
Given this scenario, which of the following should be performed to meet these requirements? (Choose two.)
    A. echo $LC_ALL
    B. locale
    C. cat $LC_ALL
    D. export LANG = en_US.UTF-8
    E. export $LANG = en_US.UTF
    F. stty
Correct Answer: BD
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.tecmint.com/set-system-locales-in-linux/
QUESTION 18
An administrator needs to change the IP address on a server remotely. After updating the configuration files, a network restart is needed. However, the administrator fears that when the network connection drops, the network restart script will be killed before the new IP address has been set. 
Which of the following commands would prevent the script from being killed?
    A. nohup service network restart
    B. service network restart &
    C. echo “service network restart” | at now
    D. bg service network restart
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 19
A Linux administrator is testing a new web application on a local laptop and consistently shows the following 403 errors in the laptop’s logs:

The web server starts properly, but an error is generated in the audit log. Which of the following settings should be enabled to prevent this audit message?
    A. httpd_can_network_connect = 1
    B. httpd_enable_scripting = 1
    C. httpd_enable_homedirs = 1
    D. httpd_enable_cgi = 1
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 20 Which of the following BEST describes the purpose of the X11 system?
    A. X11 provides graphical display capabilities
    B. X11 provides command line capabilitiesC. X11 provides networking capabilities
D. X11 provides telephony capabilities.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://en.wikipedia.org/wiki/X_Window_System
QUESTION 21 An administrator is analyzing a Linux server which was recently hacked.
Which of the following will the administrator use to find all unsuccessful login attempts?
    A. nsswitch
    B. faillock
    C. pam_tally2
    D. passwd
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
QUESTION 22 A junior administrator needs to unload an older video kernel module.
Which of the following commands would BEST accomplish this task?
    A. modprobe
    B. insmod
    C. rmmod
    D. chmod
    E. depmod
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/ Kernel_Administration_Guide/sec-Unloading_a_Module.html
QUESTION 23
An administrator is attempting to block SSH connections to 192.168.10.24 using the Linux firewall. After implementing a rule, a connection refused error is displayed when attempting to SSH to 192.168.10.24.
Which of the following rules was MOST likely implemented?
    A. iptables –A –p tcp –d 192.168.10.24 –dropt 22 –j REJECT
    B. iptables –A –p tcp –d 192.168.10.24 –dropt 22 –j DROP
    C. iptables –A –p tcp –d 192.168.10.24 –dropt 22 –j FORWARD
    D. iptables –A –p tcp –d 192.168.10.24 –dropt 22 –j REFUSE
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.golinuxhub.com/2014/03/how-to-allowblock-ssh-connection-from.html
QUESTION 24
A junior Linux administrator is setting up system-wide configuration settings. The goal is to ensure the PATH environment variable includes the following locations for all users who log into a Linux system:

The administrator issues the following commands at the terminal:

Respectively, the output of these commands is as follows:

Given this output, which of the following would be the BEST action for the administrator to perform to address this issue?
    A. Update the /etc/profile.d file using a text editor, navigate to the PATH element, add the missing locations, and run the bash_completion.sh script to update the changes.
    B. Update the /etc/profile file using a text editor, navigate to the PATH element, add the missing locations and run the . /etc/profile command to update the changes.
    C. Update the /etc/profile.d file using a text editor, navigate to the PATH element, add the missing locations, and reboot to update the changes.
    D. Update the /etc/profile file using a text editor navigate to the PATH element, add the missing locations, and restart the bash process to update the changes.
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 25
A Linux systems administrator needs to provision multiple web servers into separate regional datacenters. The systems architect has instructed the administrator to define the server infrastructure using a specific tool that consumes a text-based file.
Which of the following is the BEST reason to do this?
    A. To document the infrastructure so it can be included in the system security plan
    B. To ensure the administrator follows the planning phase of the systems development life cycle
    C. To define the infrastructure so it can be provisioned consistently with minimal manual tasks
    D. To validate user requirements have been met within each regional datacenter for compliance
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 26 A Linux administrator needs to set permissions on an application with the following parameters:
 The owner of the application should be able to read, write, and execute the application.
 Members of the group should be able to read and execute the application.  Everyone else should not have access to the application.
Which of the following commands would BEST accomplish these tasks?
A. chmod 710 <application name> B. chmod 730 <application name> C. chmod 750 <application name>
D. chmod 760 <application name>
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
QUESTION 27
A junior Linux administrator is trying to verify connectivity to the remote host host1 and display round-trip statistics for ten ICMP requests.
Which of the following commands should the administrator execute?
    A. ping –c 10 host1
    B. traceroute –c 10 host1
    C. netstat host1
    D. pathping –c 10 host1
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://shapeshed.com/unix-ping/
QUESTION 28
A junior Linux administrator is updating local name resolution to support IPv6. The administrator issues the command cat /etc/hosts and receives the following output: 127.0.0.1      localhost
Which of the following actions should the administrator perform to accomplish this task?
    A. Modify the /etc/hosts file, and add the ipv6 localhost entry to the file.
    B. Modify the /etc/hosts file, and add the ::1 localhost entry to the file.
    C. Modify the /etc/hosts file, and add the ipv4 localhost entry to the file.
    D. Modify the /etc/hosts file, and add the 0.0.0.0 localhost entry to the file.
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 29
A Linux systems administrator needs to copy the contents of a directory named “working” on the local working system to a folder /var/www/html on a server named “corporate-web”.
Which of the following commands will allow the administrator to copy all the contents to the web server?
    A. scp –r working/* webuser@corporate-web:/var/www/html
    B. tar working/* webuser@corporate-web:/var/www/html
    C. cp –r working/* webuser@corporate-web:/var/www/html
    D. mv working webuser@corporate-web:/var/www/html
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://unix.stackexchange.com/questions/232946/how-to-copy-all-files-from-a-directory-to-aremote-directory-using-scp
QUESTION 30
A systems administrator has received reports of intermittent network connectivity to a particular website. Which of the following is the BEST command to use to characterize the location and type of failure over the course of several minutes?
    A. mtr www.comptia.org
    B. tracert www.comptia.org
    C. ping www.comptia.org
    D. netstat www.comptia.org
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.lifewire.com/traceroute-linux-command-4092586
QUESTION 31
A Linux administrator has configured a Linux system to be used as a router. The administrator confirms that two network adapters are properly installed and functioning correctly. In addition, the output of the iptables –L command appears to contain a complete firewall configuration. 
Which of the following commands does the administrator need to issue for the router to be fully functional?
    A. echo “1” > /proc/sys/net/ipv4/ip_forward 
    B. echo “0” > /proc/sys/net/ipv4/tcp_abort_on_overflow
    C. echo “0” > /proc/sys/net/ipv4/max_connections
    D. echo “1” > /proc/sys/net/ipv4/ip_default_ttl
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 32
A systems administration team has decided to their systems as immutable instances. They keep the desired state of each of their systems in version control and apply automation whenever they provision a new instance. If there is an issue with one of their servers, instead of troubleshooting the issue they terminate the instance and rebuild it using automation. 
Which of the following is this an example of?
    A. Inventory
    B. Orchestration
    C. Infrastructure as code
    D. Agentless deployment
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
QUESTION 33
A systems administrator wants to deploy several applications to the same server quickly. Each application should be abstracted from the host with its own dependencies and libraries and utilize a minimal footprint.
Which of the following would be BEST in this scenario?
    A. Virtual machines
    B. Type 2 hypervisor
    C. Chroot jails
    D. Containers
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 34 An operator finds a user is having issues with opening certain files.
Which of the following commands would allow the security administrator to list and check the SELinux context?
A. ls –D B. ls –a C. ls –Z
D. ls -1
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/securityenhanced_linux/sect-security-enhanced_linux-working_with_selinux-selinux_contexts_labeling_files
QUESTION 35
A new corporate policy states that Bluetooth should be disabled on all company laptops. Which of the following commands would disable the use of Bluetooth?
    A. echo “blacklist bluetooth” > /etc/modprobe.d/blacklist-bluetooth
    B. echo “kill bluetooth” > /etc/modprobe.d/kill-bluetooth
    C. echo “modprobe bluetooth” > /etc/modprobe.d/modporbe-bluetooth
    D. echo “rmmod bluetooth” > /etc/modprobe.d/rmmod-bluetooth
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 36
A junior Linux administrator is installing a new application with CPU architecture requirements that have the following specifications:
 x64 bit
 3.0GHz speed
 Minimum quad core
The administrator wants to leverage existing equipment but is unsure whether the requirements of these systems are adequate. The administrator issues the following command cat  /proc/cpuinfo. The output of the command is as follows:

Which of the following is the recommended course of action the administrator should take based on this output?
A. Install the application, as the system meets the application requirements B. Procure new equipment that matches the recommended specifications
    C. Recompile the Linux kernel to support the installation.
    D. Reconfigure lib modules to support the new application.
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 37
A Linux systems administrator wants the ability to access systems remotely over SSH using RSA authentication. To which of the following files should the RSA token be added to allow this access?
    A. authorized_keys
    B. ~/.ssh/ssh_config
    C. id_rsa.pub
    D. known_hosts
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authenticationon-a-linux-server
QUESTION 38 A Linux server needs to be accessed, but the root password is not available.
Which of the following would BEST allow an administrator to regain access and set a new known password at the same time?
    A. Boot into single-user mode and reset the password via the passwd command.
    B. Boot into single-user mode and reset the password by editing the /etc/passwd file.
    C. Boot into single-user mode and reset the password by editing the /etc/shadow file.
    D. Boot into single-user mode and reset the password via the chage command.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://phoenixnap.com/kb/how-to-change-root-password-linux
QUESTION 39 A Linux administrator wants to fetch a Git repository from a remote Git server. 
Which of the following is the BEST command to perform this task?
    A. git checkout
    B. git clone
    C. git merge
    D. git config
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
QUESTION 40
An administrator needs to create a shared directory in which all users are able to read, write, and execute its content but none of the regular users are able to delete any content.
Which of the following permissions should be applied to this shared directory?
A. rwxrwxrwt B. rwxrwxrws C. rwxrwxrwx
D. rwxrwxrw*
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 41
A systems administrator has finished building a new feature for the monitoring software in a separate Git branch.
Which of the following is the BEST method for adding the new feature to the software’s master branch?
    A. Merge the changes from the feature branch to the master branch.
    B. Save the changes to the master branch automatically with each Git commit.
    C. Clone the feature branch into the master branch.
    D. Pull the changes from the feature branch into the master branch.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
QUESTION 42 Which of the following will provide a list of all flash, external, internal, and SSD drives?
A. lspci B. lsmod C. lsblk
D. lsusb
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.linux.com/learn/intro-to-linux/2017/3/how-format-storage-devices-linux
QUESTION 43 Which of the following configuration management tools is considered agentless?
    A. Puppet
    B. Salt
    C. Ansible
    D. Chef
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.intigua.com/blog/puppet-vs.-chef-vs.-ansible-vs.-saltstack
QUESTION 44
An administrator reviews the following configuration file provided by a DevOps engineer:

Which of the following would the application parsing this file MOST likely have to support?
    A. YAML
    B. AJAX
    C. JSON
    D. SOAP
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 45 Which of the following is a difference between YAML and JSON?
    A. Users can comment in YAML but not in JSON
    B. JSON only uses curly brackets, while YAML only uses square brackets
    C. JSON is used in web development, while YAML is used solely in back-end systems.
    D. YAML has been deprecated for JSON.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.json2yaml.com/yaml-vs-json
QUESTION 46
A junior administrator of a physical server receives log messages indicating the out-of-memory killer has been active. All memory slots are in use on the motherboard, but additional disk space is available. Space has been allocated for a swap file. 
Which of the following should the administrator use to reduce the output of memory messages?
    A. free : swapoff / swapfile ; swapon -a
    B. mkswap /swapfile; swapon –a
    C. fallocate –l 2G /swapfile && swapon –a
    D. echo “1” > /proc/meninfo ; swapon / swapfile
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 47
A junior Linux administrator is optimizing a system in which an application needs to take priority 0 when running the process. The administrator runs the ps command and receives the following output:

Given this scenario, which of the following steps will address this issue?
    A. Issue the command renice –n 0 –p 8481
    B. Issue the command renice –p 8481
    C. Issue the command renice –p 0 -n 8481
    D. Issue the command renice –n 8481
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 48
An administrator needs to mount the shared NFS file system testhost:/testvolume to mount point /mnt/ testvol and make the mount persistent after reboot. 
Which of the following BEST demonstrates the commands necessary to accomplish this task? A.
B.
C.
D.
Correct Answer: A
Section: (none)
Explanation
Explanation/Reference:
QUESTION 49
A systems administrator has deployed a Linux server based on an Anaconda process with all packages and custom configurations necessary to install a web server role.
Which of the following could be used to install more Linux servers with the same characteristics?
    A. /etc/sysconfig/anaconda.cfg
    B. /root/anaconda.auto
    C. /root/anaconda-ks.cfg
    D. /etc/sysconfig/installation.cfg
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/installation_guide/ sn-automating-installation
QUESTION 50
A Linux administrator is using a Linux system as a router. During the tests, the administrator discovers that IP packets are not being sent between the configured interfaces. 
Which of the following commands enables this feature for IPv4 networks?
    A. cat /proc/sys/net/ipv4/ip_route > 1
    B. echo “1” > /proc/sys/net/ipv4/ip_forward
    C. echo “1” > /proc/sys/net/ipv4/ip_route
    D. echo “1” > /proc/sys/net/ipv4/ip_net
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 51
A systems administrator wants to know the current status of a series of dd jobs that were started in the background three hours ago. 
Which of the following commands will achieve this task?
    A. sudo killall –HUP dd
    B. sudo killall dd
    C. sudo killall –TERM dd
    D. sudo killall -USR1 dd
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://askubuntu.com/questions/215505/how-do-you-monitor-the-progress-of-dd
QUESTION 52 A Linux administrator needs the “tech” account to have the option to run elevated commands as root.
Which of the following commands would BEST meet this goal?
    A. $ su – tech –c “/bin/bash”
    B. # usermod –aG wheel tech
    C. # sudo –i tech
    D. # groupadd –u tech –g root
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 53 Which of the following is the purpose of the vmlinux file on a Linux system?
    A. To prevent a Linux kernel panic
    B. To start a Linux virtual machine
    C. To provide the executable kernel for the system
    D. To enable resource access to the network
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://en.wikipedia.org/wiki/Vmlinux
QUESTION 54
Ann, a junior systems administrator, is required to add a line to the /etc/yum.conf file. However, she receives the following error message when she tries to add the line: 

Ann performs some diagnostics to attempt to find the root cause:

Which of the following commands should Ann execute to write content to /etc/yum?
    A. chmod 755 /etc/yum.conf
    B. setfacl –m m:rw /etc/yum.conf
    C. chattr –I /etc/yum.conf
    D. setenforce 0
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 55 A Linux administrator needs to take stock of USB devices attached to the system.
Which of the following commands would be BEST to complete this task?
    A. lspci
    B. lsusb
    C. cat /proc/USB
    D. modprobe -–usb
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://linuxhint.com/list-usb-devices-linux/
QUESTION 56
Given the output below:

Which of the following commands can be used to remove MyPhoto.jpg from the current directory?
    A. unlink ./MyPhoto.jpg
    B. del Pictures/photo.jpg
    C. rm –rf ./Pictures
    D. rm –f MyPhoto.jpg
    E. ln –rm ./Pictures/photo.jpg
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 57 Which of the following server roles would assign a host IP address?
    A. DHCP
    B. NTP
    C. DNS
    D. SSH
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 58 Which of the following commands would show the default printer on a Linux system?
    A. lpr
    B. lpq
    C. lpstat
    D. lspci
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://superuser.com/questions/123576/show-default-linux-printer
QUESTION 59
A systems administrator has set up third-party log aggregation agents across several cloud instances. The systems administrator wants to create a dashboard of failed SSH attempts and the usernames used.
Which of the following files should be watched by the agents?
    A. /var/log/audit/audit.log
    B. /var/log/kern.log C. /var/log/monitor
D. /etc/rsyslog.conf
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 60
A systems administrator must clean up all application files in the directory /var/log/app. However, the company’s security policy requires the files to be kept on the backup server for one year. The Linux server has only the tar and bzip2 packages installed.
Which of the following commands will package and compress the files?
    A. tar –zcvf applicationfiles.tar.bz2 /var/log/app/*
    B. tar –jcvf applicationfiles.tar.bz2 /var/log/app/*
    C. tar –cvf applicationfiles.tar.bz2 /var/log/app/*
    D. tar –xvf applicationfiles.tar.bz2 /var/log/app/*
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 61
In order to comply with new security policies, an administrator needs to prevent the SSH server from using insecure algorithms.
Which of the following files should be edited to accomplish this?
    A. /etc/ssh/sshd_config
    B. /etc/ssh/ssh_config
    C. ~/.ssh/ssh_config
    D. /etc/ssh/known_hosts
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 62 Which of the following configuration files should be modified to disable Ctrl+Alt+Del in Linux?
    A. /etc/inittab
    B. ~/.bash_profile
    C. /etc/securetty
    D. /etc/security/limits.conf
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.linuxtechi.com/disable-reboot-using-ctrl-alt-del-keys/
QUESTION 63
Joe, a user, is unable to log in to the server and contracts the systems administrator to look into the issue. The administrator examines the /etc/passwd file and discovers the following entry:
joe:x:505:505::/home/joe:/bin/false
Which of the following commands should the administrator execute to resolve the problem?
    A. usermod –s /bin/bash joe
    B. passwd –u joe
    C. useradd –s /bin/bash joe
    D. chage –E -1 joe
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://doc.lagout.org/security/McGraw-Hill%20-%20Hacking%20Exposed%2C%203rd%20Ed%20%20Hacking%20Exposed%20Win2.pdf (303)
QUESTION 64
A server is almost out of free memory and is becoming unresponsive. Which of the following sets of commands will BEST mitigate the issue?
    A. free, fack, partprobe
    B. lsof, lvcreate, mdadm
    C. df, du, rmmod
    D. fdisk, mkswap, swapon -a
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://vitux.com/7-commands-to-check-swap-space-in-debian-10/
QUESTION 65
A Linux administrator is using a public cloud provider to host servers for a company’s website. Using the provider’s tools, the administrator wrote a JSON file to define how to deploy the servers. Which of the following techniques did the administrator use?
    A. Infrastructure as code
    B. Build automation
    C. Platform as a service
    D. Automated configuration
Correct Answer: B or C
Section: (none) Explanation
Explanation/Reference:
Reference: https://cloud.google.com/cloud-build/docs/build-config
QUESTION 66
A Linux system is running normally when the systems administrator receives an alert that one application spawned many processes. The application is consuming a lot of memory, and it will soon cause the machine to become unresponsive. Which of the following commands will stop each application process?
    A. kill ‘pidof application’
    B. killall application
    C. kill -9 ‘ps –aux | grep application’
    D. pkill -9 application
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.tecmint.com/how-to-kill-a-process-in-linux/
QUESTION 67
A systems administrator configured a new kernel module, but it stopped working after reboot. Which of the following will allow the systems administrator to check for module problems during server startup?
    A. lsmod
    B. modprobe
    C. modinfo
    D. dmesg
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/ deployment_guide/sec-displaying_information_about_a_module
QUESTION 68
A junior Linux administrator is installing patches using YUM. The administrator issues the following command:
yum list installed
The output of the command is as follows:

Given this scenario and the output, which of the following should the administrator do to address this issue?
    A. renice –n 9 –p 5180
    B. killall yum
    C. ps –ef | grep yum
    D. top | grep yum
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.thegeekdiary.com/yum-command-fails-with-another-app-is-currently-holding-the-yumlock-in-centos-rhel-7/
QUESTION 69
A systems administrator needs to retrieve specific fields from a csv file. Which of the following tools would accomplish this task?
    A. awk
    B. sort
    C. print
    D. echo
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://stackoverflow.com/questions/19602181/how-to-extract-one-column-of-a-csv-file
QUESTION 70
Two specific users need access to a directory owned by root where backups are located. Which of the following commands would BEST ensure the specified users can access the backup files?
A. umask B. chcon
    C. chmod
    D. setfacl
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 71 Which of the following is the purpose of the monitoring server role?
    A. To aggregate web traffic to watch which websites employees are visiting
    B. To collect status and performance information about the servers in an environment
    C. To provide user authentication services to a network
    D. To provide real-time analysis of potential threats to the organization
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 72
A junior administrator is migrating a virtual machine from a Type 1 hypervisor to a Type 2 hypervisor. To ensure portability, which of the following formats should the administrator export from the Type 1 hypervisor to ensure compatibility?
    A. OWASP
    B. VDI
    C. VMDK
    D. OVA
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://docs.vmware.com/en/VMware-Fusion/11/com.vmware.fusion.using.doc/GUID-16E390B1829D-4289-8442-270A474C106A.html
QUESTION 73
A junior systems administrator is upgrading a package that was installed on a Red Hat-based system. The administrator is tasked with the following:
 Update and install the new package.
 Verify the new package version is installed.
Which of the following should be done to BEST accomplish these task? (Choose two.)
    A. yum install <package name>
    B. yum upgrade
    C. rpm –e <package name>
    D. rpm –qa
    E. apt-get <package name>
    F. apt-get upgrade
Correct Answer: AD
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/ deployment_guide/ch-yum
QUESTION 74 Which of the following is the template for the grub.cfg file?
    A. /etc/default/grub
    B. /etc/grub2.cfg
    C. /etc/sysct1.conf
    D. /boot/efi
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://geek-university.com/linux/grub-version-2/
QUESTION 75
A Linux administrator implemented a new HTTP server using the default configuration. None of the users on the network can access the server. If there is no problem on the network or with the users’ workstations, which of the following steps will BEST analyze and resolve the issue?
    A. Run netstat to ensure the port is correctly bound, and configure the firewall to allow access on ports 80 and 443
    B. Run route to ensure the port is correctly bound, and configure the firewall to allow access on ports 80 and 443
    C. Run netcat to ensure the port is correctly bound, and configure a static route to the web to allow access on ports 80 and 443
    D. Run route to ensure the port is correctly bound, and configure SELinux to allow access on ports 80 and
443
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.varonis.com/blog/netcat-commands/
QUESTION 76
A Linux storage administrator wants to create a logical volume group. Which of the following commands is required to start the process?
A. pvcreate B. vgcreate C. lvcreate
D. mkfs.xfs
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.thegeekstuff.com/2010/08/how-to-create-lvm/
QUESTION 77
A Linux administrator built a GitLab server. Later that day, a software engineer tried to access the server to upload the repository during the final step of installation. The software engineer could not access the website. Which of the following firewall rules would allow access to this site?
    A. iptables –A INPUT –p tcp –m multiport --dports 80,443 –m conntrack –cstate NEW, ESTABLISHED –j ACCEPT
    B. iptables –A INPUT –p tcp –m multiport --dports 80,443 –m conntrack –cstate ESTABLISHED –j ACCEPT
    C. iptables –A INPUT –p tcp –m multiport --dports 80,443 –m conntrack –cstate RELATED, ESTABLISHED –j ACCEPT
    D. iptables –A INPUT –p tcp –m multiport --dports 80,443 –m conntrack –cstate NEW,
ESTABLISHED –j REJECT
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://serverfault.com/questions/578730/when-using-iptables-firewall-rules-why-assert-new-stateon-all-allowed-ports
QUESTION 78
While creating a file on a volume, the Linux administrator receives the following message: No space left on device. Running the df –m command, the administrator notes there is still 50% of usage left. Which of the following is the NEXT step the administrator should take to analyze the issue without losing data?
    A. Run the df –i command and notice the inode exhaustion
    B. Run the df –h command and notice the space exhaustion
    C. Run the df –B command and notice the block size
    D. Run the df –k command and notice the storage exhaustion
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.tecmint.com/how-to-check-disk-space-in-linux/
QUESTION 79 A user attempts to use the mount -a command but gets the following error:
mount: mount point /mnt/test does not exist
Which of the following commands best describes the action the Linux administrator should take NEXT?
A. mount –a /mnt/test B. mkdir –p /mnt/test
    C. mdadm –p /mnt/test
    D. mkfs /mnt/test
    E. touch /mnt/test
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://serverfault.com/questions/751113/mount-point-does-not-exist-despite-creating-it
QUESTION 80 Which of the following is modified to reconfigure the boot environment?
    A. grub-mkconfig
    B. grub.cfg
    C. update-grub
    D. grub2-mkconfig
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
Reference: https://tipsonubuntu.com/2016/07/20/grub2-boot-order-ubuntu-16-04/
QUESTION 81
A company wants to ensure that all newly created files can be modified only by their owners and that all new directory content can be changed only by the creator of the directory. Which of the following commands will help achieve this task?
    A. umask 0022
    B. umask 0012
    C. chmod –R 0644 /
    D. chmod –R 0755 /
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.computerhope.com/unix/uumask.htm
QUESTION 82
A Linux administrator needs to back up the folder /usr/domain, and the output must be a gzip compressed tar. Which of the following commands should be used?
    A. tar –cv domain.tar.gz /usr/domain
    B. tar –cvf /usr/domain domain.tar.gz
    C. tar –czvf domain.tar.gz /usr/domain
    D. tar –cxzv /usr/domain domain.tar.gz
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://help.ubuntu.com/community/BackupYourSystem/TAR
QUESTION 83
A Linux administrator needs every new file created on a directory to maintain the group permissions of the same directory. Which of the following commands would satisfy this requirement?
    A. chmod o+s <directory>
    B. chmod u+s <directory> C. chmod +s <directory>
D. chmod g+s <directory>
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://unix.stackexchange.com/questions/115631/getting-new-files-to-inherit-group-permissionson-linux
QUESTION 84 Which of the following statements BEST represents what the term “agentless” means regarding orchestration?
    A. Installation of a tool is not required on the remote system to perform orchestration tasks
    B. It facilitates version control when using infrastructure as code during orchestration
    C. It automatically removes malware from the remote system during orchestration
    D. A tool can only be accessed remotely to perform orchestration tasks
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://whatis.techtarget.com/definition/agentless
QUESTION 85
Given that a company’s policy states that users cannot install third-party tools on Window servers, which of the following protocols will allow a Linux GUI to connect to a Windows server?
A. VNC B. NX
    C. RDP
    D. X11
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows
QUESTION 86
Ann, a junior Linux administrator, needs to copy software from her local machine to assist in developing a software application on a remote machine with the IP address 192.168.3.22. The file needs to be placed on the /tmp directory. After downloading the RPM to the local machine, which of the following commands would be BEST to use to copy the software?
    A. scp ~/software.rpm USER@192.168.3.22:/tmp
    B. scp ~/software.rpm USER@192.168.3.22:  /tmp
    C. wget USER@192.168.3.22:/tmp -f ~/software.rpm
    D. scp USER@192.168.3.22 ~/software.rpm :/tmp
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://linuxize.com/post/wget-command-examples/
QUESTION 87
An administrator is tasked with increasing the size of the volume /dev/vg/lv to 20GB. Which of the following BEST illustrates the steps the administrator should take?
    A. vgextend –L20G /dev/vg/lv; resizelv /dev/vg/lv
    B. parted –L20G /dev/vg/lv; remount /dev/vg/lv
    C. mkfs –L20G /dev/vg/lv; tune2fs /dev/vg/lv
    D. lvextend –L20G /dev/vg/lv; resize2fs /dev/vg/lv
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 88
A systems administrator observes high latency values when reaching a remote web server. Which of the following commands will help determine and isolate issues on the network side?
    A. mtr
    B. dig
    C. netstat
    D. route
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.keycdn.com/support/what-is-latency
QUESTION 89
A Linux administrator wants to obtain a list of files and subdirectories in the /etc directory that contain the word “services”. Once the files and subdirectories are discovered, they should be listed alphabetically in the / var/tmp/foundservices file. Which of the following shell scripts will accomplish this task?
A. #/bin/bash find /etc –name services | sort > /var/tmp/foundservices B. #/bin/bash locate /etc –sort –name services > /var/tmp/foundservices C. #/bin/bash find –name services –sort </var/tmp/foundservices D. #/bin/bash find /etc –name services –sort > /var/tmp/foundservices
Correct Answer: A
Section: (none)
Explanation
Explanation/Reference:
QUESTION 90
A systems administrator is enabling quotas on the /home directory of a Linux server. The administrator makes the appropriate edits to the /etc/fstab file and attempts to issue the commands to enable quotas on the desired directory. However, the administrator receives an error message stating the filesystem does not support quotas. Which of the following commands should the administrator perform to proceed?
    A. mount –o remount /home
    B. quotacheck -cg
    C. edquota /home
    D. quotaon /home
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.tecmint.com/set-filesystem-disk-quotas-on-ubuntu/
QUESTION 91
A systems administrator needs to install a new piece of hardware that requires a new driver. The driver should be manually installed. Which of the following describes the order of commands required to obtain module information, install the module, and check the log for any errors during module installation?
    A. lsmod, modprobe, modinfo
    B. modinfo, insmod, modprobe
    C. modinfo, insmod, dmesg
    D. lsmod, insmod, dmesg
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
QUESTION 92
A new HTTPS web service is being deployed on a server. Which of the following commands should the Linux administrator use to ensure traffic is able to flow through the system firewall to the new service?
    A. iptables –I OUTPUT –p tcp --sport 443 –j ACCEPT
    B. iptables –A INPUT –p tcp --dport 443 –j ACCEPT
    C. iptables –I INPUT --dport 443 –j ACCEPT
    D. iptables –A OUTPUT –p tcp --dport 443 –j ACCEPT
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.linode.com/docs/security/firewalls/control-network-traffic-with-iptables/
QUESTION 93
An administrator has modified the configuration file for a service. The service is still running but is not using the new configured values. Which of the following will BEST remediate this issue?
    A. kill -HUP
    B. init 0
    C. service start
    D. renice -10
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 94
An administrator needs to see a list of the system user’s encrypted passwords. Which of the following Linux files does the administrator need to read?
    A. /etc/shadow
    B. /etc/skel
    C. /etc/passwd
    D. /etc/pw
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.cyberciti.biz/faq/where-are-the-passwords-of-the-users-located-in-linux/
QUESTION 95
A Linux administrator is setting up a testing environment and needs to connect to a separate testing server using the production server name. The administrator needs to override the hostname that the DNS is returning in order to use the test environment. Which of the following commands should be run on each of the testing systems to BEST meet this goal?
    A. # hostnamectl set-hostname “192.168.1.100 production.company.com”
    B. # grep –i IP “${ip addr show} production.company.com” > /etc/resolv.conf
    C. # ip addr add 192.168.1.100/24 dev eth0 && rndc reload production.company.com
    D. # echo “192.168.1.100 production.company.com” >> /etc/hosts
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/ sec_configuring_host_names_using_hostnamectl
QUESTION 96
A Linux administrator opens a ticket to have an external hard drive mounted. As a security policy, external storage kernel modules are disabled.
Which of the following is the BEST command for adding the proper kernel module to enable external storage modules?
A. rmmod /lib/modules/3.6.12-100-generic/kernel/drivers/usb/storage/usb-storage.ko B. modinfo /lib/modules/3.6.12-100-generic/kernel/drivers/usb/storage/usbstorage.ko
    C. depmod /lib/modules/3.6.12-100-generic/kernel/drivers/usb/storage/usbstorage.ko
    D. insmod /lib/modules/3.6.12-100-generic/kernel/drivers/usb/storage/usbstorage.ko
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.cyberciti.biz/faq/linux-how-to-load-a-kernel-module-automatically-at-boot-time/
QUESTION 97 Which of the following are Linux desktop managers? (Choose two.)
    A. KDE
    B. GNOME
    C. GUI
    D. VNC
    E. X11
    F. SPICE
Correct Answer: AB
Section: (none) Explanation
Explanation/Reference:
QUESTION 98
A systems administrator is configuring options on a newly installed Linux VM that will be deployed to the Pacific time zone. Which of the following sets of commands should the administrator execute to accurately configure the correct time settings?
A. cd /etc ln –s /usr/share/zoneinfo/US/Pacific localtime B. cd /usr/local ln –s /usr/share/zoneinfo/US/Pacific zoneinfo C. cd /etc/local ln –s /usr/share/zoneinfo/US/Pacific localtime D. cd /usr/share/local ln –s /usr/share/zoneinfo/US/Pacific localectl
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 99
A user has connected a Bluetooth mouse to a computer, but it is not working properly. Which of the following commands should the systems administrator use to fix the issue?
    A. lsmod –i bluetooth
    B. insmod bluetooth
    C. modprobe –r bluetooth
    D. depmod –i bluetooth
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
QUESTION 100
An administrator notices that a long-running script, /home/user/script.sh, is taking up a large number of system resources. The administrator does not know the script’s function. Which of the following commands should the administrator use to minimize the script’s impact on system resources?
    A. renice
    B. kill
    C. bg
    D. nohup
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 101
An administrator needs to deploy 100 identical CentOS workstations via PXE boot. Which of the following should the administrator use to minimize the amount of interaction with the consoles needed?
    A. Kickstart script
    B. Ghost image on a distribution server
    C. Hard disk duplicator
    D. Hard disk duplicator
    E. Ubiquity script
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 102
A user, jsmith, needs access to database files located on a server. Which of the following will add jsmith to the “dba” group and preserve existing group memberships?
    A. usermod –a –G dba jsmith
    B. usermod –g dba jsmith
    C. useradd –g dba jsmith
    D. groupmod dba –u jsmith
Correct Answer: AC
Section: (none) Explanation
Explanation/Reference:
Explanation:
According to the reference given below. Both AC is correct.
Reference:
https://www.cyberciti.biz/faq/howto-linux-add-user-to-group/
QUESTION 103
A Linux administrator installed a new network adapter and temporarily disabled the network service from starting on boot. The partial output of chkconfig is as follows:

Which of the following commands BEST describes how the administrator should re-enable the network service?
    A. chkconfig --level 0 network on
    B. chkconfig --level 0-6 network on
    C. chkconfig --level 6 network on
    D. chkconfig --level 12 network on
    E. chkconfig --level 345 network on
Correct Answer: E
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.thegeekdiary.com/how-to-enable-or-disable-service-on-boot-with-chkconfig/
QUESTION 104
An engineer is working on a production application deployment that requires changing a web application property file called server.property that is managed by the Git version control system. A cloned copy of the remote repository in which the server.property file exists is on the local desktop computer. The engineer makes appropriate changes to the files, saves it as server.property, and executes git commit –m “changed the property file” server.property. Which of the following commands did the engineer fail to perform?
    A. git init server.property
    B. git merge server.property
    C. git add server.property
    D. git push server.property
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.earthdatascience.org/workshops/intro-version-control-git/basic-git-commands/
QUESTION 105
A Linux administrator retrieved a repository of files from a Git server using git clone. The administrator wants to see if a configuration file was added to the repository. Which of the following Git arguments should be used to see the recent modifications?
    A. fetch
    B. log
    C. init
    D. pull
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 106
A systems administrator is unable to reach other devices on the network and the Internet. The server is configured with the IP address 192.169.1.50/24 on eth0. The server’s router is 192.168.1.1. The administrator reviews the output of route –n:

Which of the following commands should the administrator run to correct the issue?
    A. route del default gw 192.168.2.1 eth0; route add default gw 192.168.1.1 eth0
    B. route add –net 192.168.10.0 netmask 255.255.255.0 gw 192.168.2.1 eth0
    C. route add 192.168.1.1 default 192.168.1.50 eth0
    D. route host gw 192.168.1.1 eth0
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 107
A junior Linux administrator needs to access production servers using a secure SSH protocol. Which of the following files should contain the public key to gain remote access to the server?
    A. ~/ssh/authorized-keys
    B. /etc/authorized_keys
    C. /etc/sshd/ssh.conf
    D. ~/.ssh/authorized_keys
Correct Answer: D
Section: (none)
Explanation
Explanation/Reference:
Reference: https://www.linode.com/docs/security/securing-your-server/
QUESTION 108
An administrator needs to see the type of CPU that a server is running. Which of the following files contains this information?
    A. /proc/cpuinfo
    B. /etc/devices/info.conf
    C. /dev/proc/cpu
    D. /sys/dev/cpuinfo
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.binarytides.com/linux-cpu-information/
QUESTION 109
A junior systems administrator is creating a cron job. The cron job requirements are as follows:  Run the hello.sh script every hour (24 times in one day).  Run it on Monday only.
Given this scenario, which of the following crontab options should be configured to meet these requirements?
    A. 0 *** 1 hello.sh
    B. 0 24 ** Monday hello.sh
    C. 24 *** Monday hello.sh
    D. 1 *** 0 hello.sh
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html
QUESTION 110
A Linux systems administrator is setting up SSH access with PKI for several using their newly created RSA keys. Which of the following MOST securely achieves this task?
    A. Use curl to copy each user’s public key file to the respective system
    B. Use cp to copy each user’s public key file to the respective system
    C. Use ssh-copy-id to copy each user’s public key file to the respective system
    D. Use ssh-copy-id to copy each user’s private key file to the respective system
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
Reference: https://www.linode.com/docs/security/authentication/use-public-key-authentication-with-ssh/ QUESTION 111
The development team has automated their software build process so each time a change is submitted to the source code repository, a new software build is compiled. They are requesting that the Linux operations team look into automating the deployment of the software build into the test environment. Which of the following is the benefit to the development team for implementing deployment automation?
    A. To ensure the build commits are also deployed to the test environment
    B. To enable notifications when builds are deployed to the test environment
    C. To ensure software builds in test are not accidentally deployed to production
    D. To streamline the deployment process for deploying builds into test environments
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 112
A Linux administrator needs to schedule a cron job to run at 1:15 p.m. every Friday to report the amount of free disk space on the system and to send the output to a file named “freespace”. Which of the following would meet this requirement?
    A. 13 15 * * 5 df > /freespace
    B. 15 13 * * 5 df > /freespace C. 15 1 * * 6 df > /freespace
D. 15 13 6 * * df > /freespace
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 113
A technician wants to secure a sensitive workstation by ensuring network traffic is kept within the local subnet.
To accomplish this task, the technician executes the following command:
echo 0 > /proc/sys/net/ipv4/ip_default_ttl
Which of the following commands can the technician use to confirm the expected results? (Choose two.)
    A. tcpdump
    B. traceroute
    C. route
    D. iperf
    E. ip
    F. arp
Correct Answer: A and F
Section: (none) Explanation
Explanation/Reference:
QUESTION 114
A junior Linux administrator needs to ensure a service will start on system boot. Which of the following commands should be used to accomplish this task?
    A. chkconfig <service> on
    B. systemctl <service> bootup
    C. service <service> enable
    D. crontab install <service>
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
Reference: https://geekflare.com/how-to-auto-start-services-on-boot-in-linux/
QUESTION 115 SIMULATION
Find the file named core and remove it from the system.
INSTRUCTIONS
Type “help” to display a list of available commands.
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.
Linux Shell

Correct Answer: Example 1
Section: (none)
Explanation
Explanation/Reference: Explanation:

Reference: https://www.cyberciti.biz/faq/linux-unix-how-to-find-and-remove-files/
QUESTION 116
DRAG DROP
As a Systems Administrator, to reduce disk space, you were tasked to create a shell script that does the following:
Add relevant content to /tmp/script.sh, so that it finds and compresses rotated files in /var/log without recursion.
INSTRUCTIONS
Fill the blanks to build a script that performs the actual compression of rotated log files.
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.
Select and Place:

Correct Answer: 

Section: (none) Explanation
Explanation/Reference:
QUESTION 117 HOTSPOT
After installing a new web server, you are unable to browse to the default web page.
INSTRUCTIONS
Review all the command output and select the command needed to remediate the issue.
If at any time you would like to bring back the initial state of the simulation, please click the Reset All button.
Hot Area:

Correct Answer: 

Section: (none) Explanation
Explanation/Reference:
QUESTION 118
A Linux administrator has installed a web application firewall in front of a web server running on HTTP port 8080 and successfully started the HTTP server. However, after opening the application URL in an Internet browser, the administrator discovered that the application does not work. The administrator performed the following diagnostic steps:
Output of sysctl -a command:

Output of iptables -L command:

Output of netstat –nltop | grep "8080":

Which of the following is the NEXT step the administrator should perform to permanently fix the issue at the kernel level?
    A. sysctl -w net.ipv4.ip_forward=1 then run sysctl -w /etc/sysctl.conf to enable the change
    B. Edit /etc/sysctl.conf file and add net.ipv4.ip_forward = 1 then run sysctl -p /etc/ sysctl.conf to enable the change
    C. Add iptables rule iptables -A INPUT -m state --state NEW -p tcp --dport 8080 -j then restart httpd daemon
    D. Add iptables rule iptables -A FORWARD-m state --state NEW -p tcp --dport 8080 –j
ACCEPT then restart httpd daemon
Correct Answer: D
Section: (none)
Explanation
Explanation/Reference:
QUESTION 119 A member of the production group issues the following command:
echo "Monday through Friday" > /production_docs/days
The command fails to execute, so the user obtains the following output:
drwxr--r-- root production 0 Jun 16 2018 production -rw-r--r-- production production 4096 Jun 14 2018 days
Which of the following commands should the user execute to BEST fix the issue?
    A. chmod g+w production to change the permissions of the days file
    B. chgrp root production_docs/days to change the group ownership of the production_docs/ days file
    C. chmod g+S production to set the GUID on the production_docs directory
    D. chown production to change the ownership of the production_docs directory
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 120
A junior systems administrator created a new filesystem /dev/sda1 with mountpoint /data and added it to the /etc/fstab for auto-mounting.
When the systems administrator tries to mount the file system, the system refuses. Given the output below:

Which of the following steps is necessary?
    A. Change the filesystem from /dev/sda1 to /dev/sda2 and reboot.
    B. Change the options to auto,dev,sync,rw,nosuid and run the mount -a command.
    C. Change the mount point to data and reboot.
    D. Change the dump column to 1 and run the mount -a command.
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 121
A user wants to list the lines of a log, adding a correlative number at the beginning of each line separated by a set of dashes from the actual message. Which of the following scripts will complete this task? A.
B.
C.
D.
Correct Answer: D
Section: (none) Explanation
Explanation/Reference:
QUESTION 122
An analyst is trying to determine which public IP addresses are managed by Company A, but the script is not working correctly.

Which of the following explains what is wrong with the script?
    A. $(cat ip-list.txt) should be changed to `cat ip-list.txt` in the for statement.
    B. The for should be changed to while in the loop.
    C. The > should be changed to 2> in the do statement.
    D. The -ne flag should be changed to -eq in the if statement.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 123
All users are reporting that they cannot connect to the SFTP server. The administrator runs a scan:

Which of the following would allow the administrator to fix the problem?
    A. Allow SFTP connections on port 22 using /etc/sysconfig/iptables.
    B. Allow SFTP connections on port 20 and 21 using /etc/sysconfig/iptables.
    C. Allow SFTP connections on port 25 using /etc/sysconfig/iptables.
    D. Allow SFTP connections on port 1456 using /etc/sysconfig/iptables.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 124
A Linux systems administrator installed a new web server, which failed while attempting to start. The administrator suspects that SELinux is causing an issue and wants to temporarily put the system into permissive mode. Which of the following would allow the administrator to accomplish this?
    A. echo SELINUX=PERMISSIVE >> /etc/sysconfig/selinux
    B. setenforce 0
    C. sestatus 0
    D. chcon httpd_sys_content_t /var/
Correct Answer: B
Section: (none) Explanation
Explanation/Reference:
QUESTION 125
A configuration management tool running every minute is enforcing the service HTTPd to be started. To perform maintenance, which of the following series of commands can be used to prevent the service from being started?
    A. systemctl stop httpd && systemctl mask httpd
    B. systemctl disable httpd && systemctl mask httpd C. systemctl stop httpd && systemctl hide httpd
D. systemctl disable httpd && systemctl hide httpd
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 126
An administrator has written the following Bash script:

All necessary files exist in the correct locations. However, when the administrator executes /home/user/ test.sh the following error is received:
No such file or directory
Which of the following is the MOST likely cause of the error?
    A. The shebang points to the wrong path.
    B. The script is not executable.
    C. The formatting of the file is incorrect.
    D. Nslookup is not installed.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 127
An administrator is troubleshooting an application that has failed to start after the server was rebooted.
Noticing the data volume is not mounted, the administrator attempts to mount it and receives this error:

Upon checking the logical volume status, the administrator receives this information:

Which of the following can be said about the data logical volume, and how can this problem be resolved?
    A. The logical volume is not active. The administrator should make it active with lvchange -ay /dev/ datavg/datalv and then mount it.
    B. The logical volume file system has become corrupted. The administrator should repair it with xfs_repair /dev/datavg/datalv and then mount it.
    C. The logical volume is OK but the /dev special files are missing. The administrator should recreate them by running /dev/MAKEDEV.
    D. The file system is read-only. The administrator should remount it as read-write with the command mount o remount.rw /data.
Correct Answer: A
Section: (none) Explanation
Explanation/Reference:
QUESTION 128
A four-drive Linux NAS has been improperly configured. Each drive has a capacity of 6TB, for a total storage capacity of 24TB. To reconfigure this unit to be not pluggable for drive replacement and provide total storage of 11TB to 12TB, which of the following would be the correct RAID configuration?
A. RAID 01 B. RAID 03 C. RAID 10
D. RAID 50
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
QUESTION 129
A systems administrator suspects a process with a PID of 2864 is consuming resources at an alarming rate. The administrator uses the command renice -n -5 -p2864, but it does not solve the issue. Which of the following commands should the administrator execute to correct the issue?
    A. nice -n 5 -p 2864
    B. nice -n -5 -p 2864
    C. renice -n 10 -p 2864
    D. renice -n -10 -p 2864
Correct Answer: C
Section: (none) Explanation
Explanation/Reference:
