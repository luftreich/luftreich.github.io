# XEL 测试节点搭建简易教程
 * 参考来源: https://github.com/OrdinaryDude/elastic-core-maven/blob/master/UPD1.md
 * 本地或者远程Linux主机均可

## 1. 安装docker
 * ` curl -fsSL get.docker.com -o- | sh -`
## 2. 安装节点
 * `git clone https://github.com/OrdinaryDude/xel-core-docker.git ; cd cd xel-docker && ./build.sh; `
 * `./run_foreground.sh # 运行`
## 3. 建立测试账户,二选一
 * 本地: http://localhost:16876 # 
 * 远程: http://远程IP:16876 
  * 获取测试代币，可直接找开发人员索取，具体详见Slack
## 4. 提交任务到测试网络
 * `git clone https://github.com/OrdinaryDude/xel-demos.git`
 * `cd xel-demos/simple-job-xel`
 * 填入账户密码到`secret.txt`文件
 * `python creatework.py`
## 5. 挖矿做任务
 * `git clone https://github.com/OrdinaryDude/xel_miner.git`
 * `cd xel_miner && cmake . ; make`
 * 以下方式二选一， 视具体操作环境而定
  * 本地: ./xel_miner -P "账户密码" -o "127.0.0.1:16876" --delaysleep 1 -t 1
  * 远程: ./xel_miner -P "账户密码" -o "远程IP:16876" --delaysleep 1 -t 1

## 完
<p>
<a href="https://github.com/OrdinaryDude/elastic-core-maven/blob/master/UPD1.md"><img src="http://www.dirk-loss.de/ssh-port-forwarding.png" alt="XEL"></a>
</p>

 
