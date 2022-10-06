from flask import Flask, render_template, send_file, send_from_directory, json, jsonify, make_response, request, redirect, url_for
import os
app = Flask(__name__)

path = ""  # 文件夹目录


@app.route("/")
def root():
    if path[len(path)-1] != "/":
        files = os.listdir(path+"/")  # 得到文件夹下的所有文件名称
    else:
        files = os.listdir(path)
    str = ""
    for file in files:  # 遍历文件夹
        if os.path.isdir(path+"/"+file):
            str = str+"""
            <li class="mdui-list-item mdui-ripple">
            <i class="mdui-list-item-avatar mdui-icon material-icons">folder</i>
            <div class="mdui-list-item-content" onclick="window.open('/folder/?dir=%s','_self')">%s</div>
            </li>""" % (file, file)
        else:
            str = str+"""
            <li class="mdui-list-item mdui-ripple">
            <i class="mdui-list-item-avatar mdui-icon material-icons">insert_drive_file</i>
            <div class="mdui-list-item-content" onclick="window.open('/folder/?dir=%s','_self')">%s</div>
            </li>""" % (file, file)
    return """
    <html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no"/>
    <meta name="renderer" content="webkit"/>
    <meta name="force-rendering" content="webkit"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <title>文件目录</title>
    <link href="https://lf9-cdn-tos.bytecdntp.com/cdn/expire-1-M/mdui/1.0.2/css/mdui.min.css" type="text/css" rel="stylesheet" />
    <script src="https://lf9-cdn-tos.bytecdntp.com/cdn/expire-1-M/mdui/1.0.2/js/mdui.min.js" type="application/javascript"></script>
    </head>
    <body class="mdui-theme-primary-indigo mdui-theme-accent-pink">
    <div class="mdui-appbar">
    <div class="mdui-toolbar mdui-color-theme">
    <a href="javascript:;" class="mdui-btn mdui-btn-icon">
    </a>
    <a href="javascript:;" class="mdui-typo-headline">列表</a>
    <a href="https://www.hunyl.com" class="mdui-typo-title">Powered by M1saka</a>
    </div>
    </div>
    <div class="mdui-container">
    <ul class="mdui-list">
    %s
    </ul>
    </div>
    </body>
    </html>
    """ % (str)


@app.route('/folder/', methods=['GET'])
def file():
    filename = request.args.get('dir')
    if filename == "":
        return redirect(url_for('root'))
    if os.path.isdir(path+"/"+filename):
        return view_path(filename)
    else:
        try:
            path_cache = filename.split("/")
            path_added = path
            if len(path_cache) > 1:
                for i in range(0, len(path_cache)-1):
                    path_added = path_added+"/"+path_cache[i]
                filename = path_cache[len(path_cache)-1]
            #print("path_added: "+path_added+" filename: "+filename)
            response = make_response(
                send_from_directory(path_added, filename, as_attachment=True))
            return response
        except Exception as e:
            return jsonify({"code": "异常", "message": "{}".format(e)})


def view_path(add_path):
    files = os.listdir(path+"/"+add_path)  # 得到文件夹下的所有文件名称
    str = ""
    add_path_1 = ""
    p_1 = add_path.split("/")
    for i in range(0, len(p_1)-1):
        add_path_1 = add_path_1+p_1[i]
        if i != len(p_1)-2:
            add_path_1 = add_path_1+"/"
    if add_path != "" and add_path[len(add_path)-1] != "/":
        add_path = add_path+"/"
    for file in files:  # 遍历文件夹    for file in files:  # 遍历文件夹
        if os.path.isdir(path+"/"+add_path+file):
            str = str+"""
            <li class="mdui-list-item mdui-ripple">
            <i class="mdui-list-item-avatar mdui-icon material-icons">folder</i>
            <div class="mdui-list-item-content" onclick="window.open('/folder/?dir=%s','_self')">%s</div>
            </li>""" % (add_path+file, file)
        else:
            str = str+"""
            <li class="mdui-list-item mdui-ripple">
            <i class="mdui-list-item-avatar mdui-icon material-icons">insert_drive_file</i>
            <div class="mdui-list-item-content" onclick="window.open('/folder/?dir=%s','_self')">%s</div>
            </li>""" % (add_path+file, file)
    return """
    <html>
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, shrink-to-fit=no"/>
    <meta name="renderer" content="webkit"/>
    <meta name="force-rendering" content="webkit"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <title>文件目录</title>
    <link href="https://lf9-cdn-tos.bytecdntp.com/cdn/expire-1-M/mdui/1.0.2/css/mdui.min.css" type="text/css" rel="stylesheet" />
    <script src="https://lf9-cdn-tos.bytecdntp.com/cdn/expire-1-M/mdui/1.0.2/js/mdui.min.js" type="application/javascript"></script>
    </head>
    <body class="mdui-theme-primary-indigo mdui-theme-accent-pink">
    <div class="mdui-appbar">
    <div class="mdui-toolbar mdui-color-theme">
    <a href="javascript:;" class="mdui-btn mdui-btn-icon">
    </a>
    <a href="javascript:;" class="mdui-typo-headline">列表</a>
    <a href="https://www.hunyl.com" class="mdui-typo-title">Powered by M1saka</a>
    </div>
    </div>
    <div class="mdui-container">
    <ul class="mdui-list">
    <li class="mdui-list-item mdui-ripple">
    <i class="mdui-list-item-avatar mdui-icon material-icons">arrow_back</i>
    <div class="mdui-list-item-content" onclick="window.open('/folder/?dir=%s','_self')">返回上级目录</div>
    </li>
	%s
    </ul>
    </div>
    </body>
    </html>
    """ % (add_path_1, str)


if __name__ == '__main__':
    from waitress import serve
    import sys
    import getopt
    path = os.getcwd()
    set_port = "8080"
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "h", ["help", "path=", "port="])
    except getopt.GetoptError as err:
        print("%s\npython3 app.py --path <path> --port <port>" % (err))
        sys.exit(2)
    if(len(opts) == 0):
        print("请输入运行目录(为空则使用当前目录):")
        path = input()
        print("请输入端口(默认为8080):")
        set_port = input()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('python3 app.py --path <path> --port <port>')
            sys.exit()
        elif opt == "--path":
            path = arg
        elif opt == "--port":
            set_port = arg
    if path == "":
        path = os.getcwd()
    if set_port == "":
        set_port = "8080"
    print("运行目录:%s\n服务器正在启动中.....请打开浏览器输入: http://localhost:%s" %
          (path, set_port))
    serve(
        app,
        host='*',
        port=set_port
    )
