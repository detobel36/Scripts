# CONFIG
PING_LIMIT=50 # In milisecond
REFRESH=2     # In second


# FUNCTION
function pingUrl {
    ping -c 1 $1 | grep -oP 'time=\K\d+\.\d*'
}

function colorNumber {
    result=$1
    if (( $(echo "$result > $PING_LIMIT" | bc -l) )); then
      result="\e[91m\e[1m$result\e[0m"
    fi
    echo $result
}


# MAIN RUN

for (( ; ; ))
do
  resultGoogle=$(colorNumber $(pingUrl "google.be"))
  resultGithub=$(colorNumber $(pingUrl "github.com"))

  clear
  echo -e -n "Google.be: $resultGoogle ms | "
  echo -e -n "Github: $resultGithub ms"
  echo ""
  nmcli -p -f ACTIVE,SSID,SSID-HEX,CHAN,RATE,SIGNAL,BARS,SECURITY dev wifi
  sleep $REFRESH
done

