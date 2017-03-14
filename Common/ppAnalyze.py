#  -*- coding: UTF-8 -*-

# {
# Title = 对象Inspector说明
# Owner = Irisa
# Partner = 邱晨龙 张煌辉 张宏星
# Create = 2017/3/7
# Update = 2017/3/7
# }


import re
import json



def read_file():
    f = open('./ppMachine.py')
    line = f.readline()


    flag = False

    ## 每个类所包含的json数据
    data = {}
    ## 最终返回的json数据
    res_data = []


    ## 代码层面
    class_list = []
    def_list = []
    p_var_list = []

    ## 产品层面
    p_list = []
    p_i_list = []
    m_list = []
    m_i_list = []
    m_f_list = []


    ## 前一行
    bef_obj = ''
    bef_m = ''
    bef_p = ''


    while line:

        '''
        正则表达式
        '''
        ## 匹配obj
        obj_pattern = '.*#obj\s[A-Za-z0-9\u4e00-\u9fa5]+'
        if re.match(obj_pattern, line) != None:

            value = print_format(re.match(obj_pattern, line).group())

            if flag == True:

                bef_obj = ''
                bef_m = ''

                res_data.append(data)


                data = {}

                data['obj'] = value

                p_list = []
                p_i_list = []
                m_list = []
                m_i_list = []
                m_f_list = []

            else:
                data['obj'] = value
                flag = True

            bef_obj = value


        ## 匹配class
        class_pattern = '.*class\s[A-Za-z0-9\u4e00-\u9fa5_]+'
        if re.match(class_pattern, line) != None:
            value = print_format(re.match(class_pattern, line).group())
            class_list.append(bef_obj + ' : ' + value)
            data['class'] = class_list

        ## 匹配def
        def_pattern = '.*def\s[A-Za-z0-9\u4e00-\u9fa5_]+'
        if re.match(def_pattern, line) != None:
            value = print_format(re.match(def_pattern, line).group())
            def_list.append(bef_m + ' : ' + value)
            data['def'] = def_list

        ## 匹配p
        if '=' in line:
            p_pattern = '.*#p\s.+'
            if re.match(p_pattern, line) != None:
                value = re.match(p_pattern, line).group()

                p_list.append(value.strip().split(' ')[1])
                p_i_list.append(value.strip().split(' ')[1] + " : " + value.strip().split('=')[1])
                data['p'] = p_list
                data['p_i'] = p_i_list

                bef_p = value.strip().split(' ')[1]
        else:
            p_pattern = '.*#p\s[A-Za-z0-9\u4e00-\u9fa5]+'
            if re.match(p_pattern, line) != None:
                value = print_format(re.match(p_pattern, line).group())
                p_list.append(value)
                data['p'] = p_list

                bef_p = value

        ## 匹配m
        if '=' in line:
            m_pattern = '.*#m\s.+'
            if re.match(m_pattern, line) != None:
                value = re.match(m_pattern, line).group()

                m_list.append(value.strip().split(' ')[1])
                m_i_list.append(value.strip().split(' ')[1] + " : " + value.strip().split('=')[1])
                data['m'] = m_list
                data['m_i'] = m_i_list

                bef_m = value.strip().split(' ')[1]
        else:
            m_pattern = '.*#m\s[A-Za-z0-9\u4e00-\u9fa5]+'
            if re.match(m_pattern, line) != None:
                value = print_format(re.match(m_pattern, line).group())
                m_list.append(value)
                data['m'] = m_list

                bef_m = value

        ## 匹配f
        f_pattern = '.*#f\s.+'  # [A-Za-z0-9\u4e00-\u9fa5、\s]
        if re.match(f_pattern, line) != None:
            value = print_format(re.match(f_pattern, line).group())
            m_f_list.append(bef_m + ' : ' + value)
            data['m_f'] = m_f_list


        ## 匹配创建人、创建时间、更新人、更新时间
        func1('creator', line, data)
        func1('createtime', line, data)
        func1('updater', line, data)
        func1('updatetime', line, data)





        # i_pattern = '.*#i\s[A-Za-z0-9\u4e00-\u9fa5]+'
        # match_process(i_pattern, 'i', line)

        # _pattern = '.*##\s[A-Za-z0-9\u4e00-\u9fa5]+'
        # match_process(_pattern, '##', line)




        line = f.readline()

        if bef_p.strip() != '' and '#' not in line and line != '\n' and line.strip() != '':
            # print(bef_p.strip() + '---' + line)
            p_var_list.append(bef_p + ' : ' + line.strip())
            data['p_var'] = p_var_list

        if '#' in line:
            bef_p = ''



    res_data.append(data)

    print(res_data)

    f.close()




def func1(type, line, data):
    creator_pattern = '.*#' + type +'\s=\s[A-Za-z0-9\u4e00-\u9fa5/.-]+'
    if re.match(creator_pattern, line) != None:
        value = re.match(creator_pattern, line).group()
        data[type] = value.split('=', 1)[1].strip()




def print_format(value):

    res = ''

    if '=' in value:
        # print(value.strip().split(' ')[1] + ' :: ' + value.strip().split('=')[1])
        res = value.strip().split(' ')[1]
    elif ' ' in value:
        # print(value.strip().split(' ', 1)[1])
        res = value.strip().split(' ', 1)[1]
    else:
        # print(value.strip())
        res = value.strip()

    return res


if __name__ == '__main__':
    read_file()