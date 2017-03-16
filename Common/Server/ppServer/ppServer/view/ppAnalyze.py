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

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_file(path):
    # f = open('./ppMachine.py')

    # path = os.path.join(BASE_DIR, 'view\\ppMachine.py').replace('\\', '/')

    # path = os.path.join(BASE_DIR, 'view\\ppMachine.py').replace('\\', '/')
    # path = path.replace('Server/ppServer/ppServer/view', '')

    f = open(path)

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
    obj_list = []
    p_list = []
    p_i_list = []
    m_list = []
    m_i_list = []
    m_f_list = []


    ## 前一行
    bef_obj = ''
    bef_m = ''
    bef_p = ''

    obj_info_array_info = {}
    p_info_array_info = {}
    m_info_array_info = {}


    while line:

        '''
        正则表达式
        '''
        ## 匹配obj
        '''
        obj 必须为顶格对齐
        '''
        obj_pattern = '#obj\s*.+'  ## [A-Za-z0-9\u4e00-\u9fa5]
        if re.match(obj_pattern, line) != None:

            # print(re.match(obj_pattern, line).group().strip())
            value = print_format(re.match(obj_pattern, line).group())


            if flag == True:

                if len(obj_info_array_info) > 0:
                    obj_list.append(obj_info_array_info)
                    data['obj'] = obj_list
                else:
                    class_info = {}
                    class_info['class'] = ""

                    class_info_array = []
                    class_info_array.append(class_info)

                    obj_info_array_info[bef_obj] = class_info_array

                    obj_list.append(obj_info_array_info)
                    data['obj'] = obj_list



                p_list.append(p_info_array_info)
                data['p'] = p_list

                m_list.append(m_info_array_info)
                data['m'] = m_list


                bef_obj = ''
                bef_m = ''

                res_data.append(data)


                data = {}


                obj_list = []
                p_list = []
                p_i_list = []
                m_list = []
                m_i_list = []
                m_f_list = []

                obj_info_array_info = {}
                p_info_array_info = {}
                m_info_array_info = {}

            else:

                flag = True

            bef_obj = value


        ## 匹配class
        class_pattern = '.*class\s[A-Za-z0-9\u4e00-\u9fa5_]+'
        if re.match(class_pattern, line) != None and '#' not in line:
            value = print_format(re.match(class_pattern, line).group())


            class_info = {}
            class_info['class'] = value


            class_info_array = []
            class_info_array.append(class_info)


            obj_info_array_info[bef_obj] = class_info_array




        ## 匹配def
        def_pattern = '.*def\s[A-Za-z0-9\u4e00-\u9fa5_]+'
        if re.match(def_pattern, line) != None:
            value = print_format(re.match(def_pattern, line).group())

            def_info = {}
            def_info['def'] = value

            def_info_array = []
            def_info_array.append(def_info)

            if bef_m != '':
                m_info_array_info[bef_m] += def_info_array



        ## 匹配p
        if '=' in line:
            p_pattern = '.*#p\s.+'
            if re.match(p_pattern, line) != None:
                value = re.match(p_pattern, line).group()

                p_info = {}
                p_info['i'] = value.strip().split('=')[1]

                p_info_array = []
                p_info_array.append(p_info)

                p_info_array_info[value.strip().split(' ')[1]] = p_info_array

                bef_p = value.strip().split(' ')[1]
        else:
            p_pattern = '.*#p\s[A-Za-z0-9\u4e00-\u9fa5]+'
            if re.match(p_pattern, line) != None:
                value = print_format(re.match(p_pattern, line).group())

                p_info = {}
                p_info['i'] = ''

                p_info_array = []
                p_info_array.append(p_info)


                p_info_array_info[value] = p_info_array


                bef_p = value

        ## 匹配m
        if '=' in line:
            m_pattern = '.*#m\s.+'
            if re.match(m_pattern, line) != None:
                value = re.match(m_pattern, line).group()

                m_info = {}
                m_info['i'] = value.strip().split('=')[1]

                m_info_array = []
                m_info_array.append(m_info)

                m_info_array_info[value.strip().split(' ')[1]] = m_info_array


                bef_m = value.strip().split(' ')[1]
        else:
            m_pattern = '.*#m\s[A-Za-z0-9\u4e00-\u9fa5]+'
            if re.match(m_pattern, line) != None:
                value = print_format(re.match(m_pattern, line).group())

                m_info = {}
                m_info['i'] = ''

                m_info_array = []
                m_info_array.append(m_info)

                m_info_array_info[value] = m_info_array


                bef_m = value

        ## 匹配f
        f_pattern = '.*#f\s.+'  # [A-Za-z0-9\u4e00-\u9fa5、\s]
        if re.match(f_pattern, line) != None:
            value = print_format(re.match(f_pattern, line).group())
            m_f_list.append(bef_m + ' : ' + value)

            f_info = {}
            f_info['f'] = value

            f_info_array = []
            f_info_array.append(f_info)

            if bef_m != '':
                m_info_array_info[bef_m] += f_info_array




        ## 匹配创建人、创建时间、更新人、更新时间
        func1('creator', line, data)
        func1('createtime', line, data)
        func1('updater', line, data)
        func1('updatetime', line, data)







        line = f.readline()

        if bef_p.strip() != '' and '#' not in line and line != '\n' and line.strip() != '':

            p_var_pattern = '[A-Za-z0-9\u4e00-\u9fa5_]+'
            if re.match(p_var_pattern, line.strip()) != None:
                value = print_format(re.match(p_var_pattern, line.strip()).group())

                p_info = {}
                p_info['p_var'] = value

                p_info_array = []
                p_info_array.append(p_info)

                p_info_array_info[bef_p] += p_info_array




        if '#' in line:
            bef_p = ''


    # obj_list.append(obj_info_array_info)
    # data['obj'] = obj_list
    if len(obj_info_array_info) > 0:
        obj_list.append(obj_info_array_info)
        data['obj'] = obj_list
    else:
        class_info = {}
        class_info['class'] = ""

        class_info_array = []
        class_info_array.append(class_info)

        obj_info_array_info[bef_obj] = class_info_array

        obj_list.append(obj_info_array_info)
        data['obj'] = obj_list

    p_list.append(p_info_array_info)
    data['p'] = p_list
    m_list.append(m_info_array_info)
    data['m'] = m_list


    res_data.append(data)
    print(res_data)


    # print('key = ' + os.path.basename(path))


    ## post请求，塞入内存数据
    from ppServer.view import ppSendData
    ppSendData.send_data_to_project('Comb_Analyze', '文档代码一体化', '~~~')
    ppSendData.send_data_to_proitem('Comb_Analyze', path, json.dumps(res_data, ensure_ascii=False))



    f.close()


    return json.dumps(res_data, ensure_ascii=False)  # encoding='utf-8',




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

def dir_list(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dir_list(filepath, allfile)
        else:
            allfile.append(filepath)
            if '.py' in filepath and '.pyc' not in filepath:
                # print(filepath)

                read_file(filepath)

    return allfile



# if __name__ == '__main__':
    # read_file()
    dir_list(BASE_DIR.replace('/Common/Server/ppServer/ppServer', ''), [])