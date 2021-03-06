# Can be used in the test data like ${MyObject()} or ${MyObject(1)}
class MyObject:
    def __init__(self, index=''):
        self.index = index
    def __str__(self):
        return '<MyObject%s>' % self.index

账号输入框="Xpath=//input[@type='text']"
密码输入框="Xpath=//input[@type='password']"
#新建公告
新建公告按钮="Xpath=//button[@type='button']"
##新建公告类别
公告类别输入框="Xpath=//*[@id=\"AnnouncementCategoryId\"]/div/div/div"
公告类别添加按钮="Xpath=//li[text()='+ 添加']"
公告名称输入框="id=category"
公告类别保存按钮="Xpath=//div[@class='ant-modal-content']/div[@class='ant-modal-footer']/button[2]"
##新建公告管理
选择新建的公告类别="//ul[@role='listbox']/li[last()-1]"
公告管理区下拉框="//span[text()='请选择发送范围！']"
公告选择所有管理区="//ul/li[1]/span[2]"
勾选后台系统="//div[@id='PublishChannels']/label[3]/span[@class='ant-checkbox']/input[@value='2']"
公告主题输入="//input[@placeholder='请输入公告主题']"
公告内容输入="//div[@id='ddd']/div[2]/div[1]"
公告保存按钮="//div[@class='ant-modal-footer']//button[@type='button'][2]"
公告保存并发布按钮="//div/button[3][@class='ant-btn ant-btn-primary']"
#搜索公告
公告搜索输入框="Xpath=//div/span//input[@placeholder='搜索...']"
公告搜索按钮="Xpath=//div//span[@class='ant-input-suffix']"
公告发布按钮="Xpath=//tbody/tr[1]/td/span/a[1]"
公告删除按钮="Xpath=//tbody/tr[1]/td/span/a[3]"
公告确认删除按钮="//button[@class='ant-btn ant-btn-primary ant-btn-sm']"
#我收到的公告
我收到的公告标签="//div[text()='我收到的公告']"
我收到的公告标题="//tbody/tr[1]/td[2]/a"
公告查看取消按钮1="//button[@class='ant-btn']"
收到公告删除按钮="//tr[1]/td[6]/a"
公告复选框="//tr[1]/td[1]/span/label/span/input"
公告批量删除按钮="//div[@class='ant-popover ant-popover-placement-topRight']//button[@class='ant-btn ant-btn-primary ant-btn-sm']"

#待办事项
新建待办事项按钮="//button/span[text()='新 建']/.."
待办事项主题输入框="//span/input[@id='subject']"
待办事项内容编辑器="//div[@class='w-e-text']"
结束时间="//span[@id='finshedDate']//input"
此刻按钮="//span/a[@class='ant-calendar-today-btn ']"
选择日期按钮="//span/a[@class='ant-calendar-time-picker-btn']"
选择时间确定按钮="//a[@class='ant-calendar-ok-btn']"
指派人下拉框="//div[text()='请选择指派用户']"
指派人选择admin="//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[1]"
待办事项确定按钮="//div[@class='ant-modal-footer']/div/button[@class='ant-btn ant-btn-primary']"
查看待办事项="//tr[1]/td/span/a[1]"
编辑待办事项="//tr[1]/td/span/a[2]"
取消查看="//div/button[@class='ant-btn']"
确定查看="//div[@class='ant-modal-footer']/div/button[@class='ant-btn ant-btn-primary']"
完成待办事项="//tr[1]/td/span/a[4]"
删除待办事项="//tr[1]/td/span/a[3]"
待办事项删除二次确认="//div[@class='ant-popover ant-popover-placement-topRight']//button[@class='ant-btn ant-btn-primary ant-btn-sm']"

#文档类别管理
新建文档类别按钮="//button/span[text()='新 建']/.."
文档类别名称="//div//input[@id='name']"
文档类别备注="//div//input[@id='remark']"
文档类别保存按钮="//span/button[@class='ant-btn ant-btn-primary']"
文档类别取消按钮="//span/button[@type='button']"
编辑文档类别按钮="//button/span[text()='编 辑']/.."
删除文档类别按钮="//button/span[text()='删 除']/.."
文档类别复选框="//tbody/tr[1]//input[@class='ant-checkbox-input']"
文档类别搜索框="//div/span//input[@placeholder='搜索...']"

#会议类别管理
新建会议类别按钮="//button/span[text()='新 建']/.."
会议类别名称="//div//input[@id='name']"
会议类别备注="//div//input[@id='remark']"
会议类别保存按钮="//span/button[@class='ant-btn ant-btn-primary']"
会议类别取消按钮="//span/button[@type='button']"
编辑会议类别按钮="//button/span[text()='编 辑']/.."
删除会议类别按钮="//button/span[text()='删 除']/.."
会议类别复选框="//tbody/tr[1]//input[@class='ant-checkbox-input']"
会议类别搜索框="//div/span//input[@placeholder='搜索...']"

#计划类别管理
新建计划类别按钮="//button/span[text()='新 建']/.."
计划类别名称="//div//input[@id='name']"
计划类别备注="//div//input[@id='remark']"
计划类别保存按钮="//span/button[@class='ant-btn ant-btn-primary']"
计划类别取消按钮="//span/button[@type='button']"
编辑计划类别按钮="//div/button[@class='ant-btn ant-btn-primary'][1]"
删除计划类别按钮="//div/button[@class='ant-btn ant-btn-primary'][2]"
计划类别复选框="//tr[1]//span/label//input[@class='ant-checkbox-input']"
计划类别搜索框="//input[@class='ant-input ant-input-lg']"

#文档资料管理
新建文档资料按钮="//button/span[text()='新 建']/.."
文档资料管理区下拉框="//div[@id='regionId']//div[@class='ant-select-selection__placeholder']"
文档资料选择管理区="//ul[@role='listbox']/li[last()]"
文档编号="//input[@id='number']"
文档名称="//input[@id='name']"
文档类型下拉框="//div[@id='documentCategoryId']//div[@class='ant-select-selection__placeholder']"
文档类别选择类别="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
文档版本="//input[@id='version']"
文档资料保存按钮="//span/button[@class='ant-btn ant-btn-primary']"
文档资料取消按钮="//button[@class='ant-btn ant-btn-default']"
#文档资料查看版本信息="//tr[1]//span[@class='ant-table-row-expand-icon ant-table-row-collapsed']"
编辑文档资料="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[1]"
查看文档资料="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[text()='查看']"
文档资料返回="//button[@class='ant-btn ant-btn-default']"
文档资料更多="//div[@class='ant-table-fixed-right']//tbody//tr[1]//span/a[text()='更多']"
更多删除="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[1]"
更多添加附件="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[2]"
添加附件确定="//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']"
更多删除附件="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[3]"
更多审核="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[4]"
更多撤销审核="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[5]"
文档资料管理搜索框="//input[@class='ant-input ant-input-lg']"

#会议记录
新建会议记录="//button/span[text()='新 建']/.."
会议记录管理区选择下拉框="//div[@id='regionId']//div[@class='ant-select-selection__placeholder']"
会议记录选择管理区="//ul[@role='listbox']/li[last()]"
会议记录序号="//input[@id='number']"
会议名称="//input[@id='name']"
会议类别下拉框="//div[@id='officeManagementCategoryId']//div[@class='ant-select-selection__placeholder']"
选择会议类别="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
会议记录保存按钮="//button[@class='ant-btn ant-btn-primary']"
会议记录取消按钮="//button[@class='ant-btn ant-btn-default']"
编辑会议记录="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[text()='编辑']"
查看会议记录="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[text()='查看']"
删除会议记录="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[text()='删除']"
会议主题="//input[@id='meetingTheme']"
会议搜索框="//input[@class='ant-input ant-input-lg']"
查看会议记录返回="//button[@class='ant-btn ant-btn-default']"

#工作计划
新建工作计划按钮="//button/span[text()='新 建']/.."
工作计划管理区下拉框="//div[@id='regionId']//div[@class='ant-select-selection__placeholder']"
工作计划选择管理区="//ul[@role='listbox']/li[last()]"
工作计划序号="//input[@id='number']"
工作计划名称="//input[@id='name']"
工作计划下拉框="//div[@id='officeManagementCategoryId']//div[@class='ant-select-selection__placeholder']"
工作计划选择类别="//div[@style='position: absolute; top: 0px; left: 0px; width: 100%;'][2]//ul[@role='listbox']/li[1]"
工作计划开始时间="//span[@id='startDate']//input"
选择开始时间="//div[@class='ant-calendar-body']//tr[3]/td[3]/div"
工作计划结束时间="//span[@id='endDate']//input"
选择结束时间="//div[@class='ant-calendar-body']//tr[3]/td[4]/div"
工作内容="//input[@id='planContent']"
工作计划保存按钮="//span[@class='ant-form-item-children']/button[1]"
工作计划取消按钮="//span[@class='ant-form-item-children']/button[2]"
工作计划查看备注="//tr[1]//span[@class='ant-table-row-expand-icon ant-table-row-collapsed']"
编辑工作计划="//div[@class='ant-table-fixed-right']//tbody/tr[1]/td/span/a[text()='编辑']"
工作计划更多="//div[@class='ant-table-fixed-right']//tbody//tr[1]//span/a[text()='更多 ']"
更多删除工作="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[1]"
更多更改状态="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[2]"
状态选择下拉框="//div[@id='state']//div"
工作计划保存状态="//div/button[@class='ant-btn ant-btn-primary']"
暂停工作计划="//ul[@role='listbox']/li[last()]"
更多审核工作="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[3]"
更多撤销审核工作="//ul[@class='ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical']/li[4]"
二次确认审核="//div[@class='ant-popover-buttons']/button[2]"
二次确认撤销="//div[5]//button[@class='ant-btn ant-btn-primary ant-btn-sm']"
工作计划管理搜索框="//input[@class='ant-input ant-input-lg']"





