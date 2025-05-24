# translate_ipynb.py

import json
import os
import requests
import sys
from pathlib import Path

API_KEY = os.getenv("ALIBABACLOUD_API_KEY")
API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation "

def qwen_translate(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "qwen-plus",
        "input": {
            "prompt": f"请将以下英文翻译成中文，只输出翻译结果，不要解释：\n\n{text}"
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    return result['output']['text'].strip()

def translate_ipynb_content(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            original = ''.join(cell['source'])
            translated = qwen_translate(original)
            cell['source'] = translated.split('\n')

        elif cell['cell_type'] == 'code':
            new_source = []
            for line in cell['source']:
                if line.strip().startswith('#'):
                    comment = line.split('#', 1)[1]
                    translated_comment = qwen_translate(comment)
                    new_line = '# ' + translated_comment
                    new_source.append(new_line)
                else:
                    new_source.append(line)
            cell['source'] = new_source

    return nb

def main():
    input_dir = sys.argv[1]  # 输入根目录
    output_dir = sys.argv[2]  # 输出根目录
    file_list = sys.argv[3:]  # 要翻译的文件列表

    # 缓存已翻译的文件夹名和文件名，避免重复调用 API
    folder_name_cache = {}
    file_name_cache = {}

    def translate_folder_name(name):
        if name in folder_name_cache:
            return folder_name_cache[name]
        translated = qwen_translate(name)
        folder_name_cache[name] = translated
        return translated

    def translate_file_name(name):
        if name in file_name_cache:
            return file_name_cache[name]
        translated = qwen_translate(name.rsplit('.', 1)[0]) + '.ipynb'
        file_name_cache[name] = translated
        return translated

    for rel_path in file_list:
        path = Path(input_dir) / rel_path
        if not path.exists():
            continue

        parts = Path(rel_path).parts

        # 翻译路径中所有文件夹名
        translated_parts = []
        for part in parts[:-1]:  # 只翻译文件夹部分
            translated_part = translate_folder_name(part)
            translated_parts.append(translated_part)

        # 翻译文件名
        translated_filename = translate_file_name(parts[-1])

        # 构建输出路径
        translated_path = Path(output_dir) / '/'.join(translated_parts) / translated_filename

        # 创建输出目录
        translated_path.parent.mkdir(parents=True, exist_ok=True)

        print(f"Translating: {path} → {translated_path}")

        # 翻译并保存 .ipynb 内容
        translated_nb = translate_ipynb_content(path)
        with open(translated_path, 'w', encoding='utf-8') as f:
            json.dump(translated_nb, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python translate_ipynb.py <input_dir> <output_dir> <file1.ipynb> [file2.ipynb] ...")
        sys.exit(1)

    main()