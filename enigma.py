clear
bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning
echo
echo
echo
echo $i"["$bi"•"$i"]"$me"───────────────────────────────────────────"$i"["$bi"•"$i"]"
echo $i" |"$cy"     WELCOME"$i"         |"
echo $i" |"$me"─────────────────────────────────────────────"$i"|"
echo $i" |"$pu" Creating by :"$ku" Ngurah Jordi"$i"          |"
echo $i" |"$pu" THANKS TO :"$cy"~ BLEATING ENIGMA"$i"  |"
echo $i" |"$pu" Contack Gmail :"$ku" ngurahjordi31@gmail.com"$i"      |"
echo $i"["$bi"•"$i"]"$me"───────────────────────────────────────────"$i"["$bi"•"$i"]"
echo
echo $i"────────────────────────────────"$i"
echo $i"|"$me" 1"$i" |"$cy" METASPLOIT        "$i"|"$i"
echo $i"|"$me" 2"$i" |"$cy" FOLLOWER INSTAGRAM      "$i"|"$i"
echo $i"|"$me" 3"$i" |"$cy" SPAM SMS          "$i"|"$i"
echo $i"|"$me" 4"$i" |"$cy" LOCATOR           "$i"|"$i"
echo $i"────────────────────────────────"$i"
echo $i"|"$me"I"$i" |"$cy" INSTALL PACKAGE  "$i"|"$i"
echo $i"|"$me"E"$i" |"$cy" EXIT             "$i"|"$i"
echo $i"────────────────────────────────"$i"
echo
echo $me"["$i""SELECT""$bi"]"
echo $me"¦"
read -p"└=> " pil

if [ $pil = 1 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 1
git clone https://github.com/4L13199/meTAInstall
cd meTAInstall
bash meTAInstall
fi

if [ $pil = 2 ]
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

if [ $pil = 3 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 1
git clone https://github.com/4L13199/LITESPAM.git
cd LITESPAM
chmod +x *
sh LITESPAM.sh
fi

if [ $pil = 4 ]
then
clear
figlet -f slant "S E C. . ."|lolcat
sleep 1
git clone https://github.com/thelinuxchoice/locator.git
cd locator
chmod +x *
sh locator.sh
fi

if [ $pil = I ]
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

if [ $pil = X ]
then
clear
figlet -f slant "E X I T"|lolcat
sleep 2
echo $cy"THANK YOU WE HOPE YOU ENJOY"
sleep 2
echo $i"Bila Ada Kesalahan Kamu Bisa Nanya Kepada Saya"
sleep 2
echo $ku"WhatsApp :"$i" 085835787069"
echo $ku"Facebook :"$i" Riski Darmawan"
sleep 2
echo $pur">> Thanks Yang Sudah Support Saya <<"
exit
fi