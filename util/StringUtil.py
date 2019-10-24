from array import array


class StringUtil(object):
    @staticmethod
    def cut_str_between_two_str(text, str1, str2):
        length = len(str1)
        pos1 = text.find(str1)
        pos2 = text.find(str2, pos1 + length)
        return text[pos1 + length:pos2]

    @staticmethod
    def get_all_str_beween_two_str(text, str1, str2):
        num = text.count(str1)
        pos = 0
        result = []
        for i in range(num):
            length = len(str1)
            pos1 = text.find(str1, pos)
            pos2 = text.find(str2, pos1 + length)
            text1 = text[pos1 + length:pos2]
            result.append(text1)
            length1 = len(text1)
            if length1 is 0:
                length1 = 1
            pos = pos1 + length1
        return result

    @staticmethod
    def get_str_in_label(text):
        pos1 = text.find(">")
        pos2 = text.find("<", pos1)
        if pos1 is 0 and pos2 is 0:
            return text
        else:
            return text[pos1 + 1:pos2]


if __name__ == '__main__':
    text = """
    <div class="spec-title">注册证书信息</div>
    
                        
                                <table class="data-list">
                                    <tbody><tr>
                                        
                                        <th width="20%">注册类别</th>
                                        <th width="15%">注册号</th>
                                        <th width="20%">注册单位</th>
                                        <th width="25%">发证机关</th>
                                        <th width="10%">签发日期</th>
                                        <th width="10%">有效期</th>
                                    </tr>
                            
                                <tr>
                                    
                                    <td>二级注册建造师</td>
                                    <td>粤2441416065514</td>
                                    <td>深圳市科宇达机电安装有限公司</td>
                                    <td>广东省建设执业资格注册中心</td>
                                    <td>2019-04-09</td>
                                    <td>2022-01-08</td>
                                </tr>
                            
                                </tbody></table>
                            
                        
                        
    
                        <!--列表最多显示5条，5条以上的显示更多按钮-->
    
                        <a class="gotop" href="#nav">回到顶部</a>
                    
                        <div class="spec-title">职称证书信息</div>
                        
                                <table class="data-list">
                                    <tbody><tr>
                                        
                                        <th width="30%">证书名称</th>
                                        <th width="11%">职称等级</th>
                                        
                                        <th width="35%">发证机关</th>
                                        <th width="12%">发证日期</th>
                                        <th width="12%">有效期</th>
                                    </tr>
                            
                                <tr>
                                    
                                    <td>广东省中级专业技术资格证</td>
                                    <td>中级</td>
                                    
                                    <td>佛山市人力资源和社会保障局</td>
                                    <td>2018-03-14</td>
                                    <td></td>
                                </tr>
                            
                                <tr>
                                    
                                    <td>经济师</td>
                                    <td>中级</td>
                                    
                                    <td>广州市人力资源和社会保障局</td>
                                    <td>2010-11-07</td>
                                    <td></td>
                                </tr>
                            
                                </tbody></table>
                            
                        
    
                        
    
                        <!--列表最多显示5条，5条以上的显示更多按钮-->
                        <a class="gotop" href="#nav">回到顶部</a>
                    
                        <div class="spec-title">安全生产考核合格证</div>
    
                        
                                <table class="data-list">
                                    <tbody><tr>
                                        
                                        <th width="15%">证书类型</th>
                                        <th width="15%">证书编号</th>
                                        <th width="30%">发证机关</th>
                                        <th width="12%">发证日期</th>
                                        <th width="13%">有效期</th>
                                    </tr>
                            
                                <tr>
                                    
                                    <td><span title="企业项目负责人安全生产考核合格证书">三类人员安全生产考核合格证</span></td>
                                    <td>粤建安B(2017)0005125</td>
                                    <td>广东省住房和城乡建设厅</td>
                                    <td>2017-06-28</td>
                                    <td>2020-06-27</td>
                                </tr>
                            
                                </tbody></table>
                            
                        
                        
    
                        <!--列表最多显示5条，5条以上的显示更多按钮-->
                        <a class="gotop" href="#nav">回到顶部</a>
                    
                        <div class="spec-title">岗位证书信息</div>
                        
                                <table class="data-list">
                                    <tbody><tr>
                                        
                                        <th width="20%">证书名称</th>
                                        <th width="15%">证书编号</th>
                                        <th width="30%">发证机关</th>
                                        <th width="10%">发证日期</th>
                                        <th width="20%">有效期</th>
                                    </tr>
                            
                                <tr>
                                    
                                    <td>二级建造师</td>
                                    <td>GD042547</td>
                                    <td>广东省人力资源和社会保障厅</td>
                                    <td>2015-01-19</td>
                                    <td></td>
                                </tr>
                            
                                <tr>
                                    
                                    <td>职业培训合格证</td>
                                    <td>18361201141906148</td>
                                    <td>江西省建设职业培训学校</td>
                                    <td>2018-09-21</td>
                                    <td></td>
                                </tr>
                            
                                </tbody></table>
                            
                        
    
                        
    
    
                        <!--列表最多显示5条，5条以上的显示更多按钮-->
                        <a class="gotop" href="#nav">回到顶部</a>
                    
                        <div class="spec-title">工程项目</div>
                        
                        <div id="ctl00_ContentPlaceHolder1_divempty_protect" class="empty">暂无信息</div>
                        
                        <a class="gotop" href="#nav">回到顶部</a>
                    
                        <div class="spec-title">良好行为</div>
    
                        
                        <div id="ctl00_ContentPlaceHolder1_divempty_award" class="empty">暂无信息</div>
                        
    
                        <!--列表最多显示5条，5条以上的显示更多按钮-->
                        
    
    
                        <a class="gotop" href="#nav">回到顶部</a>
    
                    
                        <div class="spec-title">不良行为</div>
    
                        
                        <div id="ctl00_ContentPlaceHolder1_divempty_punish" class="empty">暂无信息</div>
                        
    
                        <!--列表最多显示5条，5条以上的显示更多按钮-->
                        
    
                        <a class="gotop" href="#nav">回到顶部</a>"""
    str1 = '<div class="spec-title">安全生产考核合格证</div>'
    # str1 = '<div class="spec-title">注册证书信息</div>'
    # str1 = '<div class="spec-title">职称证书信息</div>'
    str2 = '<!--列表最多显示5条，5条以上的显示更多按钮-->'
    str3 = '<td>'
    str4 = '</td>'
    str_util = StringUtil()
    text = str_util.cut_str_between_two_str(text, str1, str2)
    result = str_util.get_all_str_beween_two_str(text, str3, str4)
    print(result[1])
