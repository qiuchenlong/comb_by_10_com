# coding=utf-8
# {
# Title = COMB
# Level = 1
# Owner = Irisa
# Partner = qiuchenlong
# Create = 2017/3/8 
# Update = 2017/3/8 
# }

#obj 机器管理

    #i 单个主机单管理

    #p 地址 = 服务器地址，包括云服务器和企业内部的服务器

    #p 配置 = 机器初始配置，加入管理那一刻的配置情况

    #m 获取应用 = 获取该机器上运行的应用

    #m 系统情况 = 机器系统运行情况，包括网络、cpu、内存、磁盘等

    #m 关机 = 注意数据的保存

    #m 开机 =

    #m 迁移 = 将机器上的环境配置、应用搬到另一台机器
       #f 1、备份机器数据 2、验证目标机器系统兼容情况 3、迁移
       
    #m 重启
        #i 重启时注意把加入事件的任务启动