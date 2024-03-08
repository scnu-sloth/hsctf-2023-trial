# Easyeasy

description：
F**k C++

flag:
HSCTF{C++_i5_a_much_t3rRible_l4nGuage}

release:
./release/*

Hint:
1. 简单的栈溢出，有些字符可能cin输入不了

shell:
```bash
docker build -t "easyeasy" .
docker run -d -p "0.0.0.0:9999:9999" -h "easyeasy" --name="easyeasy" easyeasy
```

