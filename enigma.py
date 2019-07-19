clear
figlet WELLCOM | lolcat
echo
echo "[•]---------------------------------------[•]"  | lolcat
echo " |             ENIGMA SCRIPT               |"   | lolcat
echo " |-----------------------------------------|"   | lolcat
echo " | CODER     : NGURAH JORDI                |"   | lolcat
echo " | INSTAGRAM : ngurahjordi                 |"   | lolcat
echo " |                                ENJOY!!  |"   | lolcat
echo "[•]---------------------------------------[•]"  | lolcat
echo
echo "[•]---------------------------------------[•]"  | lolcat
echo " | 1. METASPLOIT                           |"   | lolcat
echo " | 2. FOLLOWER INSTAGRAM                   |"   | lolcat
echo " | 3. SPAM SMS                             |"   | lolcat
echo " | 4. LOCATOR                              |"   | lolcat
echo "[•]---------------------------------------[•]"  | lolcat
echo
echo "[•]---------------------------------------[•]"  | lolcat
echo " | I. INSTALL PACKAGE                      |"   | lolcat
echo " | E. EXIT                                 |"   | lolcat
echo "[•]---------------------------------------[•]"  | lolcat
echo "
echo "╭=>>[NUMBER]"                                   | lolcat
read -p "╰># " $                                      | lolcat

if [ $NUMBER = 1 ] || [ $NUMBER = 01 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 2
git clone https://github.com/4L13199/meTAInstall
cd meTAInstall
bash meTAInstall
fi

if [ $NUMBER = 2 ] || [ $NUMBER = 02]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 2
git clone https://github.com/ikiganteng/bot-igeh.git
cd bot-igeh
chmod +x *
unzip node_modules.zip
node index js
fi

if [ $NUMBER = 3 ] || [ $NUMBER = 03]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 2
git clone https://github.com/4L13199/LITESPAM.git
cd LITESPAM
chmod +x *
sh LITESPAM.sh
fi

if [ $NUMBER = 4 ] || [ $NUMBER = 04]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 2
git clone https://github.com/thelinuxchoice/locator.git
cd locator
chmod +x *
sh locator.sh
fi

if [ $ = I ] || [ $ = i ]
then
clear
pkg update && pkg upgrade
pkg install python2
pip2 install urllib3 chardet certifi idna requests
pkg install git
pkg install root-repo
pkg install unstable-repo
pkg install x11-repo
pip2 install mechanize
pkg install curl
pkg install ruby
pkg install gem
pkg install node.js
gem install lolcat
pkg install git
pkg install php
pkg install ruby cowsay toilet figlet
pkg install neofetch
pkg install nano
figlet -f slant " D O N E "|lolcat
fi

if [ $ = X ] || [ $ = x ]
then
clear
figlet -f slant "E X I T"|lolcat
sleep 2
echo $"THANK YOU WE HOPE YOU ENJOY"
sleep 2
exit
fi

#CTRL + C
trap ctrl_c INT
ctrl_c(){
clear
echo -e $"[#]>(Ctrl + C) Detected, Triying To Exit"
