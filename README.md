# smartqqbot project

使用smartqq API接口，可以实现自动回复和获取聊天记录

使用前首先添加外部依赖：

apt-get install libzbar-dev

然后添加库：

pip install -r requirements.txt

支持绑定登录，一般一次扫码以后可以维持两天左右的登录状态，

使用-help在聊天窗口中获取命令

当前无法获得用户好友，群，讨论组等的唯一信息，使用昵称来区别，

数据库储存内容为：

表名：normal/group/discuss + z + 昵称的每个unicode字符对应数字以z分隔

MsgOrder integer primary key,
Time text,
FromNick text,
ToNick text,
content text

登录后的机器人不需要其他用户端同时在线，可以接受到他人发出的消息，

但是无法接收到自己通过其他客户端发出的信息

（群和讨论组可以收到，但是无法识别，因为uin不是自己的qq号，每次登录都会改变，也无法获取到昵称信息）

注意：

对于输出的csv文件均为对应表名称

讨论组中#开头的消息不记录

所有聊天中命令均不记录

好友聊天中对非命令信息使用图灵机器人自动回复

讨论组聊天中，对@消息进行自动回复


