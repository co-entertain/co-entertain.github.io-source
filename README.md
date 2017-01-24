show how it works here!

###须知
- 每增加一个目录或者标签，在content/background 目录相应的增加以其名称命名的背景图片，jpg结尾


### work locally
1. environment settings

		easy_install-2.7 pip
		pip install virtualenv
		pip install virtualenvwrapper

2. add following in your .profile file, and run it
	
		export WORKON_HOME=~/.Envs
		source /usr/local/bin/virtualenvwrapper.sh
3. create new virtual environment and fire

		mkvirtualenv pelican
		workon pelican
		pip install -r requirements.txt
		make serve
		
### work instantly
all you need is git pull and write you blod, commit and push, wait a minute and then you will see online