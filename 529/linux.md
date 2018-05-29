# 查看一个进能够打开的最大文件数
` cat /proc/sys/fs/file-max`

# 关闭ip转发功能
`sysctl net.ipv4.ip_forward=0`
	或者修改/etc/sysctl.conf 文件

# 大多数发行版把内核的源代码放在/usr/src下

# uname -r 返回linux内核版本号

# lsmod 查看当前加载的模块

# ipv4.potaroo.net 查看ipv4何时终结

# 概念
- frame 帧 链路层
- packet 组 IP层
- segment 片段
- packet 包 通用术语
- unicast 单播 一台网络接口的地址
- multicast 组播 一组主机地址  有利于实现视频会议系统 IGMP 
- broadcast 广播 网络所有主机的地址
- anycast 一组主机中任意之一的地址
- ipv4 地址
	- 127第一个字节，loopback 环回网络 
	- A 类 1~126 N.H.H.H 早期网络，美国保留 (N net H host)
	- B 类 128~191 N.N.H.H 大型网络，通常要划分子网
	- C 类 192~223 N.N.N.H 
	- D 类 224~239 -       组播地址
	- E 类 240~255 -        试验地址
- 127个A类网络占用了多达一半的可用地址空间
- netmask 子网掩码 4字节 重新划分地址的主机部分和网络部分
	- 网络位设置 1，主机位设置0，从左到右，必须连续，网络位至少8位，主机至少2位，ipv4子网掩码只有22种可能
- ipcalc IP Calculator IP计算器
- 私用地址和NAT
	- 网络保留地址
		- A 10.0.0.0~10.255.255.255 10.0.0.0/8
		- B 172.16.0.0~172.31.255.255 172.16.0.0/12
		- C 192.168.0.0~192.168.255.255 192.168.0.0/16
- Network Address Translation 网络地址转换
	- 截获一个只在内部使用的地址的包，然后用一个真实的外部IP地址，或还有一个不同的源端口号来改写这些包的源地址。 NAT还维护一张内外地址/源端口对之间的映射表，应答包到达就可以反向转换
	-  多个回话复用一个IP地址，内部主机共享一个外部地址
- caida.org 统计和网络测量工具
- netstat -r 路由表 -rn 避免dns查询
- route add default gw 132.236.227.1 eth0 添加默认网关 静态路由
- IP转发 IP forwarding , 一台UNIX/linux主机启用IP转发，就成为了一台路由器
	- 它能够接受出现在一个网络接口上的第三方数据包，把它们按网关或者目标主机匹配到另一个接口上，再从那个接口重新发出这些数据包。 路由器
	- 建议关闭
- ppp 点对点协议
- ethtool 查询和设置一个网络接口上专门针对硬件介质的参数 链路速率和工作模式

# linux NAT 和包过滤
- 启动内核的ip转发功能
- modprobe iptable_nat
- modprobe ip_conntrack
- modprobe ip_conntract_ftp
- /proc/sys/net/ipv4/ip_forward 1

- iptables -t nat -A POSTROUTING -o eth1 -j SNAT --to 63.173.189.1
	- 