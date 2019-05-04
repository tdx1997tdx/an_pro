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
2： 注册失败用户名已存在  
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
2： 注册失败，验证码错误  
### 登陆
网址： /login  
前端给后端的表单：  
name: xxxxx  
password: xxxxx  
mail: xxxxxxx  
后端给前端的东西：  
1： 验证成功  
2： 验证失败  
### 修改密码
网址： /change_password  
前端给后端的表单：  
name: xxxxx  
new_password: xxxxx  
mail: xxxxxxx  
后端给前端的数字：  
1： 用户以及邮箱匹配成功  
2： 失败，用户名不存在  
3： 失败，邮箱用户名不匹配  
4： 邮箱不合法  
  
网址： /change_password_verification  
前端给后端的表单：  
name: xxxxx  
new_password: xxxxx  
verification_code: xxxxxxx  
后端给前端的数字：  
1： 修改成功  
2： 修改失败，验证码错误  
## 个人信息界面
### 修改绑定邮箱
网址： /change_mail  
前端给后端的表单：  
name: xxxxx  
new_mail: xxxxxxx  
后端给前端的数字：  
1： 成功  
2： 失败，邮箱不合法  
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
