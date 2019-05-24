# cs_304_project_backend
## 登陆注册界面
### 注册
网址： /register  
前端给后端的表单：  
name: xxxxx  
password: xxxxx  
mail: xxxxxxx  
后端给前端的数字：  
1： 用户以及邮箱合法  
2： 注册失败，填入信息不合法或用户名已存在  
3： 注册失败邮箱已存在  
4： 邮箱不合法  
  
网址： /register_verification  
前端给后端的表单：  
name: xxxxx  
password: xxxxx  
mail: xxxxxxx  
verification_code: xxxxxxx  
后端给前端的数字：  
1： 注册成功  
2： 注册失败  
### 登陆
网址： /login  
前端给后端的表单：  
name: xxxxx  
password: xxxxx  
后端给前端的东西：  
1： 登陆成功  
2： 登陆失败  
### 修改密码
网址： /change_password  
前端给后端的表单：  
name: xxxxx  
或者mail: xxxxxxx  
后端给前端的数字：  
1： 用户以及邮箱匹配成功  
2： 失败，邮箱或者用户名不匹配或不存在  
3： 邮箱不合法  
  
网址： /change_password_verification  
前端给后端的表单：  
name: xxxxx  
new_password: xxxxx  
verification_code: xxxxxxx  
后端给前端的数字：  
1： 修改成功  
2： 修改失败，验证码错误  
## 个人信息界面
### 获取个人信息
网址： /get_mail  
前端给后端的表单：  
name: xxxxx  
后端给前端：  
798637048@qq.com  
### 修改绑定邮箱
网址： /change_mail  
前端给后端的表单：  
name: xxxxx  
new_mail: xxxxxxx  
后端给前端的数字：  
1： 成功  
2:  失败，邮箱已被占用  
3： 失败，邮箱不合法  
网址： /change_mail_verification  
前端给后端的表单：  
name: xxxxx  
new_mail: xxxxxxx  
verification_code: xxxxxxx  
后端给前端的数字：  
1： 修改成功  
2： 修改失败，验证码错误  
### 修改密码
网址： /change_inside_password  
前端给后端的表单：  
name: xxxxx  
old_password: xxxx  
new_password: xxxxxxx  
后端给前端的数字：  
1： 修改成功  
2： 失败，原密码输入错误  
## 云端界面
### 获取当前用户已有的文件名
网址： /get_filenames  
前端给后端的表单：  
name: xxxxx  
后端给前端：  
begin xxxx.txt qqqq.txt kkkk.txt end

### 上传
网址： /file_upload  
前端给后端的表单：  
name: xxxxx  
filename: xxxxxx  
content: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
后端给前端：  
1: 成功  
2: 失败  

### 下载
网址： /file_download  
前端给后端的表单：  
name: xxxxx  
filename: xxxxxx  
后端给前端：  
文件中的内容  
## 图片转换
网址： /image_translation  
前端给后端的表单：  
name: xxxxx  
image: base64编码图片文件  
后端给前端：  
识别内容  
