from flask import Flask, request, jsonify, send_from_directory
from spark_api import get_spark_response
from flask_cors import CORS
# from werkzeug.utils import secure_filename
import os
from secure_file import secure_filename_wood
from rag_chain import create_rag_chain

app = Flask(__name__)
CORS(app)  # 允许所有域名的请求

# 配置上传文件的保存路径和允许的文件扩展名
# 获取当前文件的目录路径
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'json', 'jsonl', 'csv', 'xlsx', 'xls', 'pptx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 创建 RAG 链实例
rag_chain = create_rag_chain()

# 定义 Flask 路由
@app.route('/api/rag', methods=['POST'])
def rag():
    data = request.get_json()
    query = data.get('prompt', '')
    print(f'query: {query}')
    inputs = {'query': query}
    # if not query:
    #     return jsonify({'error': 'No query provided'}), 400
    
    response = rag_chain(inputs)
    print(f'response: {response}')
    return jsonify({'response': response})

@app.route('/api/message', methods=['POST'])
def message():
    data = request.get_json()
    prompt = data.get('prompt', '')
    print(f'Prompt: {prompt}')
    
    if prompt:
        response = get_spark_response(prompt)
        print(f'response: {response}')
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'No prompt provided'}), 400
    
@app.route('/upload', methods=['POST'])
def upload_file():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    # 如果用户没有选择文件，浏览器也会提交一个空的part
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename_wood(file.filename)
        # print(f'Filename: {filename}')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True, 'filename': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400
    
@app.route('/files', methods=['GET'])
def list_files():
    files = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
