1、PO思想通过 --- 分四层

2、basepage --- 通用  查找元素、等待、元素操作、++++ app端的特有操作

3、pytest --- 通用

# 页面封装  相对于web网页--- 可见区域小、每个页面的逻辑不复杂、元素也不多
   ---  灵活度

# 与设备之间进行会话。
  web: driver = webdriver.Chrome()
  app:  准备一堆启动参数、driver = webdriver.Remote("appium server地址",启动参数)
        noReset = True
        chromedriverExe... = "..."
        unicodeKeyboard = True
        automationName = "UiAutomator2"
        platformName
        platfromVersion
        device
        appPackage
        appActivity
        配置化 -  conf \ yaml

yaml:
    YAML 是一种简洁的非标记语言。
YAML以数据为中心，使用空白，缩进，分行组织数据，从而使得表示更加简洁易

基本规则：
- 大小写敏感
- 使用缩进表示层级关系
- 禁止使用tab缩进，只能使用空格键
- 缩进长度没有限制，只要元素对齐就表示这些元素属于一个层级。
- 使用#表示注释
- 字符串可以不用引号标注

# 读取yaml文件的数据，并转换成python对象
- 打开yaml文件
- 使用yaml的load()函数