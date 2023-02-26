#!/bin/sh
cat workers | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        ssh root@$line -n "rm -rf /Lab1_BD2/ && mkdir /Lab1_BD2/"
        echo "Copy data to $line"
        scp  /Lab1_BD2/setup.py root@$line:/Lab1_BD2/ && scp /Lab1_BD2/manager root@$line:/Lab1_BD2/ && scp /Lab1_BD2/workers root@$line:/Lab1_BD2/
        echo "Setup $line"
        ssh root@$line -n "cd /Lab1_BD2/ && python3 setup.py && ntpdate time.nist.gov"
        echo "Finished config node $line"
    fi
done
