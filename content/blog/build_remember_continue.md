title:建站续，附乱七八糟
Date: 2014-11-11 11:11
Modified: 2014-11-11 11:11
Category: 琐碎
Tags: 找工作,blog
Slug: build-and-remember-continued
Authors: nullne
Summary: 
*逛了一圈论坛博客神马的发现好多人也都在写点东西纪念今天*

距离上一次写东西已经很久了，主要原因是因为Air跪了！幸灾乐祸的主儿可以去看看[原微](http://weibo.com/2356978633/B7CNpb52w?type=comment#_rnd1415671779372)，那可是目前自己微博上最火的一个

![Alt text](http://ww2.sinaimg.cn/large/8c7ca3c9jw1eh3fj6ouc4j21kw23u1kx.jpg)

应该说这是之前那篇文章的续吧，可惜那篇的_Markdown_格式的已经弄没了，附上[链接](nullne.com/archivi/abc.html)（估计也是唯一一个入口了）。当初心血来潮，也不完全心血来潮，算是小时候一个梦想吧，搞了这么一个极有技术含量的博客。现在看看当时还在初学者水平，只是简单的按照别人的教程做了下来。因为本儿跪了之后源代码也一并去了，所以一直都没有再更新，这一次重建博客，在之前的基础上新增加了很多东西，[**Travis**](https://travis-ci.org/)就是一个牛逼了的东西，待会儿我会接着把这一次的技术性细节一并简单介绍。
###技术细节
- [**Travis CI**](https://travis-ci.org/)
>Travis CI is a hosted continuous integration service.
Travis CI's build environment provides different runtimes for different languages, for instance multiple versions of Ruby, PHP, Node.js. It also comes preinstalled with a variety of data stores and common tools like message brokers.

    使用**Pelican**的常规思路是在本地写好**md**或者其他格式的文件，然后`make publish`，当然这是集成命令，分解开就是先生成静态页面然后PUSH到**Git page**。看着似乎很简单，这是建立在首先配置好你的本地环境的基础上，并且每次换一台机器之后你都需要重新配置你的环境。配环境这事儿我只能呵呵了，那么多的的平台配法儿都不太一样。
 
    但是，当你遇到**Travis CI**一切就都不一样了。你只要一次性配置完成，将你的source文件PUSH到某一个github仓库。之后的事情就容易多了，按最坏的情况来说，你的本撒手人寰了（哭瞎），你写了一篇文章纪念。以最快的速度把舍友的本儿扯过来.
```shell
git clone git://github.com/username/bri.github.io-source
mv remember.md path/to/content/
git add *
git commit -m "love you forever"
git push
```
    
Done! 你的本儿在天之灵，看到以后应该就会安息了。

废话不说了，按照[Zonca](http://zonca.github.io)的[教程](http://zonca.github.io/2013/09/automatically-build-pelican-and-publish-to-github-pages.html)一步一步下来基本没有错误，但是当时我走了很多弯路，自作聪明的改了一些脚本。如果遇到什么问题欢迎讨论。

- [**Tipue**](http://www.tipue.com/)
>Tipue Search is a site search engine jQuery plugin. It's free, open source and responsive.

    还是跟上面一样，按照[Moparx](http://moparx.com)的[教程](http://moparx.com/2014/04/adding-search-capabilities-within-your-pelican-powered-site-using-tipue-search/)走吧。

    还有很多其他插件，像_Sitemap_什么的，之所以单独把这个列在这儿是因为发现原来静态页面也是可以交互的，它提供了一个思路。简单说就是将所有的网站页面存储到一个_JSON_文件，然后在搜索页面直接加载这个文件在本地搜索,非常快速。

- **Google Comments**

    之前用的是**Disqus**,但是总感觉不是很舒服，这儿有一个简单的[教程](http://browsingthenet.blogspot.com/2013/04/google-plus-comments-on-any-website.html)
    
###都说是纪念了
高大上的*APEC*假期马上就结束了，按照大四之前的性子，至少半个月前已经在他乡了，异国不敢说，但是已经开始筹划了，护照就是第一步。六天的假期在我这儿怎么也得有半个月。最近却怂怂的呆在学校哪儿也不敢去。

反正就是没有找到工作。

*好的工作*应该是什么样子的，我想了很多遍，从最开始投的第一家说起吧。

阿里巴巴，以网上笔试结果**诚信第一**终结了我。当时第一次参加网上笔试，幸灾乐祸的跟队友共同战斗以望能够从人海中脱颖而出。至于诚信什么的以后再说吧，大学之后关于这个的定义改变了很多。百度两次笔试无果，腾讯没有投递。BAT梦石沉大海，系统关照我有选择困难症。这之前我一直以为找份BAT的工作很容易，这之后我才去想一些事情。

。。。。。。

算了先就不无病呻吟了，刚才接到**知道创宇**HR的电话，在这么一个特殊的节日去面试。

最后附图纪念 ***1111***

![Alt text](https://lh5.googleusercontent.com/-foXL3QCuRco/VGDh3Wvvy8I/AAAAAAAAADg/iwtexzazuGg/s481/yule.jpg)
