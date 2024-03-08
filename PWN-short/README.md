# short  签到

Title:
short

Intro:
简单题有手就行

Flag:
hsctf{pleasemakeshellcodeshortsh0rtsh0rt}

Hint:

1. 注意残余寄存器
2. one_gadget

Attachment:
./release/short
./release/libc-2.27.so

#!/bin/sh
cd ./ctf_xinetd
docker build -t "short" .
docker run -d -p <pub_port>:9999 -h "short" --name="short" short

