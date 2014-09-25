
mbox数据导入导出工具
====

简介
-------

本工具用于对mbox文件进行导入和导出，导入或导出的文件为eml格式。
前段时间准备把邮件客户端从Outlook迁入Thunderbird中，在邮件的格式转中
出现了难题。

于是在网上搜了一个发现一个可行的方案是先安装Foxmail然后把Outlook的PST
文件转换为eml格式文件，然后再安装ImportExportTools扩展进行导入。

Foxmail 转换的效果非常不错，可以正常将PST转换为eml文件，
但ImportExportTools扩展就不太好用了。

于是在使用python编写了这个小工具，可以将eml文件批量转换为mbox 格式。

最主要还是用来将eml文件转换为Thunderbird文件夹。

待办事项
-----
* 导出功能

将mbox中的邮件导出为eml文件格式。需要解决的问题是文件名问题。要符合
如下原则：
	1. 文件名在Linux 和 Windows 平台均合法有效。
	2. 重名文件的处理。

* 文件夹命名规则调整

	1. mbox的文件名以目标文件夹的名称命名。
	   - Linux文件名规范：
		 - 除"/"以外所有的字符均合法
		 - 最长256字节（以UTF8）编码
	   - windows 文件名规范：
		 - 最多 250 个字符，除了以下字符其余均可： \,/,*,”,<,>,|
		 - 最多 250 个字符
	   - 无文件名的编码规范：
	     - 以export 开头，然后从1起开始编号。
		 
	2. 如目标文件夹的名称有扩展名（如.sbd），则新建的文件夹，均带此
	扩展名（支持Thunderbird）。


使用说明
-----

* 在命令行执行：

	mboxtool -i -e path/to/eml -m path/to/mbox

	执行上述命令后，系统将自动进行转换
* 常见用途：
把path/to/eml目录下的邮件全部导入存档文件夹中。使用如下命令：
	mboxtool -i -e path/to/eml -m "path/to/thunderbird/Local Folders\存档.sbd"
