
mbox数据导入导出工具
====

简介
-------

本工具用来对mbox文件进行导入和导出，导入或导出的文件为eml格式。
前段时间准备把邮件客户端从Outlook迁入Thunderbird中，在邮件的格式转中
出现了难题。

于是在网上搜了一个发现一个可行的方案是先安装Foxmail然后把Outlook的PST
文件转换为eml格式文件，然后再安装ImportExportTools扩展进行导入。

Foxmail 转换的效果非常不错，可以正常将PST转换为eml文件，但ImportExportTools
扩展就不太好用了。

于是在使用python编写了这个小工具，可以将eml文件批量转换为mbox 格式。

使用说明
-----

在命令行执行：

	mboxtool -i -e path/to/eml -m path/to/mbox

执行上述命令后，系统将自动进行转换
