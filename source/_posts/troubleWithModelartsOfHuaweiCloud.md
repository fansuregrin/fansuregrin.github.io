---
title: Visual Studio Code连接华为云ModelArts问题总结
date: '2022-10-14 21:01:00'
categories:
  - - linux
---
近日，Machine Learning的实验需要在华为云的ModelArts平台上开展。我在ModelArts上创建了Notebook并添加密钥后，一直不能在本地用vscode连接远程的开发环境。具体错误信息如下：

```
Connection permission denied (publickey). Please make sure the key file is correctly selected and [the file permission is correct](https://code.visualstudio.com/docs/remote/troubleshooting#_local-ssh-file-and-folder-permissions). You can view the instance keypair information on ModelArts console.
```

我查看了下我的密钥文件的权限，明显有权限访问。然后，我从Linux系统换到Windows系统，依然是权限错误！搁置了一个晚上后，我尝试从终端连接远程开发环境，发现它提示我`Permissions for "/path/to/pem/file" are too open. It is required that your private key files are Not accessible by others`。原来不是权限没给够，是权限给的过大了。。。

将密钥文件只给自己可读可写权限，其他用户和组都不给任何权限后，就能正常连接了！

这里贴出一些可能出现的错误的解决方法的链接，以供后续参考！

- [报错“Permissions for 'x:/xxx.pem' are too open”如何解决？](https://support.huaweicloud.com/modelarts_faq/modelarts_05_3120.html)
- [VS Code连接开发环境失败常见问题](https://support.huaweicloud.com/modelarts_faq/modelarts_05_0513.html)
- [Local ssh file and folder permissions with vscode](https://code.visualstudio.com/docs/remote/troubleshooting#_local-ssh-file-and-folder-permissions)

