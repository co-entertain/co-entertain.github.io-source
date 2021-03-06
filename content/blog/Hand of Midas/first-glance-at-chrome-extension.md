title:报销助手--Chrome插件 
Date: 2015-12-27 11:11
Modified: 2015-12-27 11:11
Tags: Chrome-Extension, js
Slug: chrome-extension-reimbursement-assistant 
image: {photo}Hand of Midas/chinacache-seat.jpg
## 楔子
其实现在已经是很久以后了，太懒了

某个周末闲的发慌，突然想到公司的报销流程还是非常繁琐的，需要从一个报销系统去查自己的考勤情况，根据加班情况可以申请饭补，然后填写到报销系统里面。一来报销系统设计的巨复杂，每添加一项得点点点填填填，其次整个过程非常枯燥，机械的重复。我是一个非常怕麻烦的人，但是我还是去报销了，因为我算了一下，即便是我花了一个小时申请完报销，那么时薪就有五六百了，已经远远超过我目前的薪水了。

但是这个过程应该可以优化吧

Talk is cheap! 仔细分析一番决定写一个Chrome插件，虽然之前没有任何插件的经验，爬取考勤系统数据，自动填写到报销系统里面，这个过程用户只需要填一个简单的表单，就可以一键Fire了。本来打算爬虫部分也用JS实现的，考虑到自己的渣渣JS功底，最后还是用Python写了一个爬虫服务端。


具体的技术分析和实现在下面详细写了，还有一些邮件也一并记录了。第一次发大群邮件非常激动，当时第一版写完的时候是半夜两点，按耐不住内心的激动，索性当时就发了邮件，想着第二天大家一到公司就发现了这么一个神器会不会特别激动。。。然后发现自己权限不够发不了`all-staff`的邮件组，就只发了研发的。幸好当时没有发全部员工，第一版的怎么可能没有bug呢！之后很多热心测试人员纷纷提出了很多意见建议，最终这个工具能够实际使用。

对对对，我还录制了一段使用报销插件的报销视频，附在邮件里面

非常开心的是技术部门的两个老大也回复邮件了，给予赞赏，并且还转发了另一个加班严重的邮件组--运维，哈哈哈哈，希望这个小工具帮他们节省了时间吧

最最开心的是每次看到日志又多了几行，那种快感也只有我们这些苦逼码农才知道了

演示视频如下：


{% vimeo 173331689 [640] [400] %}

##功能分析以及实现
###自动报销：

 1. 进入报销页面，点击图标，弹出界面
 2. 输入用户名，密码，daterange，点击fire
 3. js后台提交，前端等待获取数据，并解析
 4. python实现一个简单的网页爬虫功能，模拟登陆后获取考勤详情
 5. 根据获取到的数据自动填写 

 
 
###报错优化
- 无法从报销系统获取数据时候报错提示，以及多页获取
- 不同部门的加班规则不太一样，需要区别处理
- js加载后的页面无法绑定js，需要重新绑定
- 因为报销系统js极其复杂，需要模拟各种 blur, click, change 事件
- 简单的配置页面，提供服务器地址更改功能


###美化
- popup 页面提供所有可选参数，cookie中记录成功报销之后的值以便于下一次操作（事实证明这个非常方便）
- 成功之后显示打赏按钮与作者个人信息
- 图标，论ps的重要性
- 流程上更为完善，比方说点击Fire之后 disable 掉按钮并作一些 css 处理，然后按钮的地方可以显示进度
 
 
###技术基础：  
- [一个简单的 chrome extension 的入门教程](https://robots.thoughtbot.com/how-to-make-a-chrome-extension)
- 主要是 JS 太难，遇到各种 JS 问题
- Python 实现简单爬去考勤数据，这个相对熟悉一点写起来很快

### 持续跟进
之后过了很久，公司的报销系统更新了，导致插件不能继续使用。好多人RTX问我啥时候能再更新一版，当时就觉得满满的成就感。那个周末就抽空，匹配了新的报销系统，那个感觉真是好极了，虽然没有任何物质上的回报。


##第一次邮件

报销系统极其考验人们的智商和耐心，而聪明的人是这么做的：【请看附件中的视频】

简而言之，就是一个我周末灵光一现想出来的一个chrome插件，收集考勤系统的用户名密码，从而获取你所有能够报销的数据，并自动填写到报销系统中，从而让报销变得轻松愉快。
###如何使用？
> 首先你需要一个Chrome浏览器，如果你没有甚至你不知道什么是chrome，你的朋友会耻笑你，你的家人会嫌弃你。。。  

1. 下载邮件附件`cc-helper.crx`，如果弹出警告请忽略
2. 打开Chrome浏览器，地址栏输入`chrome://extensions/`,然后回车
3. 在你的硬盘中找到刚才下载的附件，拖动到当前窗口，根据提示安装

恭喜你，到此为止你已经安装完毕。  
模仿视频中的操作试试吧，任何问题欢迎邮件/RTX交流。



##第二次邮件
多谢大家的支持，早上来收到很多使用反馈，当然也有一些bug和改进意见。现更新一版：
  
- 添加编码方式，解决部分机器乱码问题，如果还出现乱码请设置浏览器编码方式为UTF-8
- 解决最后一行统计没有结果的bug
- 添加贪婪模式，解决部分没有打卡记录但是仍然需要报销的情况

希望大家持续反馈，让这个小工具更好用

##第三次邮件

上周末写出了这个插件的第一版，虽然之后优化了很多地方，但是插件存在一个致命BUG，无法提交和保存。周内因为抽不出来时间，所以一直拖到这周末，望谅解。


下面给出该插件完整功能介绍。  
1. 在报销详情页面打开该插件（后附有如何安装此插件），填写考勤系统的用户名，密码，以及需要报销的时间段，默认餐补和加班原因  
2. 贪婪模式是考虑到部分打卡故障，勾选此项之后将统计所有可能存在加班的情况（上下班如不全按正常上下班记），此类数据需要之后手工微调  
3. 如果依然出现不能保存的情况，请刷新页面，清除缓存再次尝试  
4. 增加配置服务器（主要用来获取考勤记录）地址页面，默认已经添加，如果后续更改将会通过邮件告知


感谢之前很多热心同事帮忙测试，谢谢，希望这个小插件能够节省大家的时间

##后记
非常喜欢这种感觉，运用技术解决生活中的难题，非常有成就感。另外得到那么多人的赞赏也是很开心的嘛

技术其实不必很厉害，很多东西都是现学的，比方说 Chrome 插件，看着教程然后一步一步实现自己的想法

当初选择技术这条路线也是同样的想法，勿忘初衷
