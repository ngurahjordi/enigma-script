python2
clear
b='\033[1m'
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
echo -n $green"DATE AND TIME NOW "; date +"%d %B %Y"|lolcat
echo
echo "___________________________________________" | lolcat
echo "\033[32;1m|  NGURAH JORDI " |lolcat
echo "\033[32;1m| Enjoy, A little but useful "|lolcat
echo "\033[32;1m___________________________________________" | lolcat
echo
echo "\033[32;1m────────────────────────────────" | lolcat
echo $b"1. METASPLOIT"|lolcat
echo $b"2. FOLLOWER INSTAGRAM"|lolcat
echo $b"3. SPAM SMS"|lolcat
echo $b"4. LOCATOR"|lolcat 
echo "\033[32;1m"────────────────────────────────" | lolcat
echo $b"I. NSTALL PACKAGE"|lolcat
echo $b"E. EXIT"| lolcat
echo "\033[32;1m"────────────────────────────────" | lolcat
echo
echo "\033[32;1m╭──=>>[SELECT NUMBER]"
read -p "╰──────────────────────────> : " b

if [ $b = 1 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 1
git clone https://github.com/4L13199/meTAInstall
cd meTAInstall
bash meTAInstall
fi

if [ $b = 2 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 1
git clone https://github.com/ikiganteng/bot-igeh.git
cd bot-igeh
chmod +x *
unzip node_modules.zip
node index js
fi

if [ $b = 3 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 1
git clone https://github.com/4L13199/LITESPAM.git
cd LITESPAM
chmod +x *
sh LITESPAM.sh
fi

if [ $b = 4 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 1
git clone https://github.com/thelinuxchoice/locator.git
cd locator
chmod +x *
sh locator.sh
fi

if [ $b = I ]
then
clear
pkg update && pkg pgrade
apt install python2
pip2 install urllib3 chardet certifi idna requests
pkg install git
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

if [ $b = X ]
then
clear
figlet -f slant "E X I T"|lolcat
sleep 2
echo $cy"THANK YOU WE HOPE YOU ENJOY"
sleep 2
exit
fi
