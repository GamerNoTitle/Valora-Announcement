# Valora-Announcement

## English | [简体中文](#简体中文)

This is a [Valora](https://github.com/GamerNoTitle/Valora) announcement management system. In order to make your announcement be seen by users easily, I developed this and help you with that. 

Valora-Announcement (I will use VAMS as Valora-Announcement-Management-System insteam in the following) depends on the services of leancloud. If you are in China Mainland, I suggest that you should choose Chinese Version, or you should use International one.

I will guide you step by step in the following.

### Step 1: Add new app

![](https://registry.npmmirror.com/gamernotitle-oss/1.0.3/files/img/Github/Valora-Announcement/msedge-20230721-165638.png)

When you log into your console, click `Create app`, and enter the essential informations to create your app

### Step 2: Add `announcement` class

![](https://registry.npmmirror.com/gamernotitle-oss/1.0.3/files/img/Github/Valora-Announcement/msedge-20230721-165828.png)

Next, you need to add a new class named `announcement`

**DO NOT SHARE YOUR CREDENTIALS TO ANYONE!!!**

### Step 3: Add essential columns

![](https://registry.npmmirror.com/gamernotitle-oss/1.0.3/files/img/Github/Valora-Announcement/msedge-20230721-170324.png)

![](https://registry.npmmirror.com/gamernotitle-oss/1.0.3/files/img/Github/Valora-Announcement/msedge-20230721-170344.png)

Finally, you need to add columns by clicking `Add column` with four times. Add `en` `zh_CN` `zh_TW` `ja_JP` columns.

GREAT! You finished the initation!

### Step 4: Deploy your app and add variables

Now the only thing is that you need to deploy your app. Click `LeanEngine` and follow the steps to do it. 
Choose `Deploy from git`, and enter the link of this repo `https://github.com/GamerNoTitle/Valora-Announcement.git`
DO NOT FORGET TO ADD VARIABLES `PORT` (Fix to `443`， do not change it) & `TOKEN` (This is the basic authentication, make it complex) in the settings.
After you deployed, you can access to path `/api/get`, if you see the following data, then you make it!
```json
{
    "announcement": {
        "en": "When you see this message, it means that your Valora has successfully integrated the announcement system! The announcement system GitHub repository link: <u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>",
        "ja-JP": "このメッセージを見ると、Valora が公告システムを正常に統合したことを意味します！公告システムの GitHub リポジトリのリンク：<u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>",
        "zh-CN": "当你看到这个提示，说明你的Valora已经成功接入了公告系统！公告系统Github仓库链接：<u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>",
        "zh-TW": "當你看到這個提示，說明你的 Valora 已經成功接入了公告系統！公告系統 Github 倉庫連結：<u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>"
    },
    "code": 200,
    "id": "64ba50cb55768272182d9e11",
    "msg": "success"
}
```

### Step 5: Link VAMS to your Valora

You need to add a new variable named `ANNOUNCEMENT` to your app. The value should be the domain contains protocol that Valora should access to. For example: `https://announcement.val.bili33.top`

### Step 6: Add new announcement

You should access to your VAMS and add the announcement manually. This step needs a token verification. Make sure your token is **STRONG ENOUGH**, or this may cause XSS attack in your Valora(Valora uses safe tag when rendering template with Jinja2).

## 简体中文

本项目是专属于[Valora](https://github.com/GamerNoTitle/Valora)的公告系统，主要是为了在不需要重新部署Valora的情况下轻松更新公告，正因如此，我做了这个系统

Valora-Announcement（下面简称VAMS，为Valora-Announcement-Management-System的缩写）需要运行在Leancloud服务上面，如果你在中国大陆内使用本服务，请将区域选择为华东或者华北（**国内部署需要备案域名**），因为国际版是不支持国内进行访问的，所以你必须选择合适的位置进行部署。如果你是在中国大陆以外的地方使用，那就随便你了

### 第一步：添加APP

![]()

登录到控制台后，点击创建应用，名字按照它的要求填好后，点击创建

### 第二步：添加`announcement`类（class）

![]()

你需要按照如图的步骤，添加名为`announcement`的类（class）

请注意：不要将你的APPID或者APPKEY分享给任何人，这会导致安全问题！

### 第三步：添加必须的列

![]()

![]()

你需要点击添加列按钮，添加名为`en` `zh_CN` `zh_TW` `ja_JP`的四列，对应Valora支持的四种语言（如果你不想加对应语言的公告的话，添加的时候可以随便写，但是必须有这四列）

### 第四步：部署你的应用并添加必须的变量

你需要点击左边的引擎，然后部署你的应用，选择`Git部署`，然后填入本仓库的链接`https://github.com/GamerNoTitle/Valora-Announcement.git`
别忘了在设置中添加变量哦~你需要添加的变量为`PORT`（固定为`443`，请不要修改）和`TOKEN`（这个是用于添加公告时鉴权的，请设置得复杂一点）
当你部署完以后，你可以尝试访问路径`/api/get`，如果你看到了下面的内容，说明你已经部署成功了！
```json
{
    "announcement": {
        "en": "When you see this message, it means that your Valora has successfully integrated the announcement system! The announcement system GitHub repository link: <u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>",
        "ja-JP": "このメッセージを見ると、Valora が公告システムを正常に統合したことを意味します！公告システムの GitHub リポジトリのリンク：<u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>",
        "zh-CN": "当你看到这个提示，说明你的Valora已经成功接入了公告系统！公告系统Github仓库链接：<u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>",
        "zh-TW": "當你看到這個提示，說明你的 Valora 已經成功接入了公告系統！公告系統 Github 倉庫連結：<u><a href=\"https://github.com/GamerNoTitle/Valora-Announcement\">Valora-Announcement</a></u>"
    },
    "code": 200,
    "id": "64ba50cb55768272182d9e11",
    "msg": "success"
}
```

### 第五步：将VAMS连接到你的Valora

你需要在Valora的环境变量中添加名为`ANNOUNCEMENT`的变量，这个变量应该带有协议头和你的域名，例如`https://announcement.val.bili33.top`

### 第六步：添加新的公告

你需要访问你的应用页面，然后在页面中添加你的新公告；这个过程中需要Token来鉴权，所以请**确保你的Token很复杂**，要不然可能会造成XSS攻击（Valora在渲染公告的时候选择了Jinja2的safe标签）