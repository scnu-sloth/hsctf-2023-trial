# Thread Master

description：
已知源码的，多线程并发安全？

flag:
HSCTF{y0u_ar3_Uaf_anD_thr3ad_ma5ter}

release:
./release/*

Hint:
1. 你知道Linux存在8年的Dirty Cred漏洞吗？

shell:
docker build -t "thread" .
docker run -d -p "0.0.0.0:<port>:9999" -h "thread" --name="thread" thread

