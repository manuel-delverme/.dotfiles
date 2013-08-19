# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto -h'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    #alias grep='grep --color=auto'
    #alias fgrep='fgrep --color=auto'
    #alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ..='cd ..'
alias cd..='cd ..'
alias ...='cd ../..'
alias ll='ls -l'
alias la='ls -A'
alias l='ls' #  -CF'
alias vi='vim'
alias radio_trance_128='mplayer http://listen.trancebase.fm/tunein-mp3-pls'
alias radio_hardcore_128='mplayer http://listen.hardbase.fm/tunein-mp3-pls'
alias radio_hardcore_80='mplayer http://listen.hardbase.fm/tunein-aacplus-pls'
alias vps='ssh root@41.215.240.102'
alias raspy='ssh root@10.5.5.99'
alias icd='cd ~/isaac/'
alias bcd='cd ~/isaac/Manhattan/A_CoDe/'
alias wcd='cd /var/www/'
alias radio_techno_80='mplayer http://listen.technobase.fm/tunein-aacplus-pls'
alias radio_happycore='mplayer http://u3.happyhardcore.com'
alias todo='~/scripts/todo.sh'
alias update='~/scripts/update.sh'
alias download='axel -a -n 15'
alias scanlan='nmap -sP $(ip -o addr show | grep inet\  | egrep "wlan|grep" | cut -d\  -f 7)'
alias adt='~/adt-bundle/eclipse/eclipse' #  -CF'
alias l='ls' #  -CF'
alias ts='bash ~/Downloads/TeamSpeak3-Client-linux_amd64/ts3client_runscript.sh'
alias pastebin="curl -F 'sprunge=<-' http://sprunge.us"
# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

#source ~/ros/setup.sh
#source ~/ros/setup.bash

#export ROS_PACKAGE_PATH=/home/user/ros/navigation:/home/user/ros/diagnostics:/home/user/ros/common:/home/user/ros/robot_model_tutorials:/home/user/ros/laser_pipeline:/home/user/ros/simulator_gazebo:/home/user/ros/visualization_tutorials:/home/user/ros/geometry:/home/user/ros/pluginlib:/home/user/ros/bullet:/home/user/ros/robot_model:/home/user/ros/xacro:/home/user/ros/image_transport_plugins:/home/user/ros/dynamic_reconfigure:/home/user/ros/stage:/home/user/ros/executive_smach:/home/user/ros/driver_common:/home/user/ros/physics_ode:/home/user/ros/visualization_common:/home/user/ros/python_qt_binding:/home/user/ros/bond_core:/home/user/ros/image_common:/home/user/ros/geometry_visualization:/home/user/ros/common_rosdeps:/home/user/ros/diagnostics_monitors:/home/user/ros/bfl:/home/user/ros/image_pipeline:/home/user/ros/common_tutorials:/home/user/ros/robot_model_visualization:/home/user/ros/geometry_experimental:/home/user/ros/perception_pcl:/home/user/ros/vision_opencv:/home/user/ros/visualization:/home/user/ros/executive_smach_visualization:/home/user/ros/slam_gmapping:/home/user/ros/filters:/home/user/ros/orocos_kinematics_dynamics:/home/user/ros/geometry_tutorials:/home/user/ros/nodelet_core:/opt/ros/fuerte/stacks:/opt/ros/fuerte/share:/opt/ros/fuerte/share/ros:/home/user/isaac/Manhattan/Simone.Baratta/ros_workspace/
#export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:~/ros/beginner_tutorials
#export ROS_HOSTNAME=localhost ##ROS SINGLE MACHINE SETTINGS
#export ROS_MASTER_URI=http://localhost:11311 ## SAME AS ABOVE
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/user/sheep/wxWidgets-2.9.4/lib
export PATH=$PATH:/home/user/android-sdk-linux/tools
export PATH=$PATH:/home/user/android-sdk-linux/platform-tools

~/scripts/todo.sh
alias tvps='torify ssh root@41.215.240.102 -p 443'
alias connections="netstat -tuanpl"
