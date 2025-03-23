# x_jinja2

自带各类好用过滤器的 jinja2 渲染器。

## 安装

你可以通过 pip 安装 `x_jinja2`包：

```bash
pip install x_jinja2
```

## 简单用法

```python
from x_jinja2 import XEnvironment

env = XEnvironment()
output = env.from_string("{{ data.foo | normalize_csv }}").render(
    data={
        "foo": "bar",
    },
)
print(output)
```

## 支持的过滤器

根据你提供的过滤器信息，我已经整理成表格形式如下：

### 支持的过滤器

| 过滤器名称                   | 描述                                   | 来源                        |
| ---------------------------- | -------------------------------------- | --------------------------- |
| **Base 64**                  |                                        | `ansible_core_filters`      |
| b64decode                    | Base64 解码                            |                             |
| b64encode                    | Base64 编码                            |                             |
| **UUID**                     |                                        | `ansible_core_filters`      |
| to_uuid                      | 生成 UUID                              |                             |
| **JSON**                     |                                        | `ansible_core_filters`      |
| to_json                      | 将对象转换为 JSON 字符串               |                             |
| to_nice_json                 | 将对象转换为格式化的 JSON 字符串       |                             |
| from_json                    | 将 JSON 字符串转换为对象               |                             |
| **YAML**                     |                                        | `ansible_core_filters`      |
| to_yaml                      | 将对象转换为 YAML 字符串               |                             |
| to_nice_yaml                 | 将对象转换为格式化的 YAML 字符串       |                             |
| from_yaml                    | 将 YAML 字符串转换为对象               |                             |
| from_yaml_all                | 将多个 YAML 文档的字符串转换为对象列表 |                             |
| **Path**                     |                                        | `ansible_core_filters`      |
| basename                     | 获取文件名                             |                             |
| dirname                      | 获取目录名                             |                             |
| expanduser                   | 扩展用户路径                           |                             |
| expandvars                   | 扩展环境变量                           |                             |
| path_join                    | 连接路径                               |                             |
| realpath                     | 获取绝对路径                           |                             |
| relpath                      | 获取相对路径                           |                             |
| splitext                     | 分离文件扩展名                         |                             |
| win_basename                 | 获取 Windows 文件名                    |                             |
| win_dirname                  | 获取 Windows 目录名                    |                             |
| win_splitdrive               | 分离 Windows 驱动器和路径              |                             |
| commonpath                   | 获取公共路径                           |                             |
| normpath                     | 规范化路径                             |                             |
| **File Glob**                |                                        | `ansible_core_filters`      |
| fileglob                     | 文件通配符匹配                         |                             |
| **Types**                    |                                        | `ansible_core_filters`      |
| bool                         | 转换为布尔值                           |                             |
| to_datetime                  | 转换为日期时间对象                     |                             |
| **Date Formatting**          |                                        | `ansible_core_filters`      |
| strftime                     | 格式化日期时间                         |                             |
| **Quote String**             |                                        | `ansible_core_filters`      |
| quote                        | 为 shell 使用引用字符串                |                             |
| **Hash Filters**             |                                        | `ansible_core_filters`      |
| md5                          | MD5 哈希值                             |                             |
| sha1                         | SHA1 哈希值                            |                             |
| checksum                     | 校验和                                 |                             |
| password_hash                | 密码哈希                               |                             |
| hash                         | 通用哈希                               |                             |
| **Regex**                    |                                        | `ansible_core_filters`      |
| regex_replace                | 正则表达式替换                         |                             |
| regex_escape                 | 正则表达式转义                         |                             |
| regex_search                 | 正则表达式搜索                         |                             |
| regex_findall                | 正则表达式查找所有匹配项               |                             |
| **Ternary**                  |                                        | `ansible_core_filters`      |
| ternary                      | 三元运算符                             |                             |
| **Random Stuff**             |                                        | `ansible_core_filters`      |
| random                       | 生成随机数                             |                             |
| shuffle                      | 打乱列表                               |                             |
| **Undefined**                |                                        | `ansible_core_filters`      |
| mandatory                    | 强制参数                               |                             |
| **Comment-Style Decoration** |                                        | `ansible_core_filters`      |
| comment                      | 添加注释                               |                             |
| **Debug**                    |                                        | `ansible_core_filters`      |
| type_debug                   | 获取对象类型                           |                             |
| **Data Structures**          |                                        | `ansible_core_filters`      |
| combine                      | 合并字典                               |                             |
| extract                      | 提取字典中的键值对                     |                             |
| flatten                      | 展平列表                               |                             |
| dict2items                   | 将字典转换为键值对列表                 |                             |
| items2dict                   | 将键值对列表转换为字典                 |                             |
| subelements                  | 获取子元素                             |                             |
| split                        | 分割字符串                             |                             |
| **URL**                      |                                        | `ansible_urls_filters`      |
| urldecode                    | URL 解码                               |                             |
| **URL Split**                |                                        | `ansible_urlsplit_filters`  |
| urlsplit                     | URL 分割                               |                             |
| **Math Stuff**               |                                        | `ansible_mathstuff_filters` |
| log                          | 对数                                   |                             |
| pow                          | 幂                                     |                             |
| root                         | 开方                                   |                             |
| **Set Theory**               |                                        | `ansible_mathstuff_filters` |
| unique                       | 去重                                   |                             |
| intersect                    | 交集                                   |                             |
| difference                   | 差集                                   |                             |
| symmetric_difference         | 对称差集                               |                             |
| union                        | 并集                                   |                             |
| **Combinatorial**            |                                        | `ansible_mathstuff_filters` |
| product                      | 笛卡尔积                               |                             |
| permutations                 | 排列                                   |                             |
| combinations                 | 组合                                   |                             |
| **Computer Theory**          |                                        | `ansible_mathstuff_filters` |
| human_readable               | 人类可读格式                           |                             |
| human_to_bytes               | 人类可读格式转字节                     |                             |
| rekey_on_member              | 根据成员重新键化                       |                             |
| **Zip**                      |                                        | `ansible_mathstuff_filters` |
| zip                          | 压缩                                   |                             |
| zip_longest                  | 长度不等时压缩                         |                             |
| **Custom**                   |                                        | `x_jinja2/core.py`          |
| normalize_csv                | 将输入值格式化为 CSV 格式的字符串      |                             |
| jsonpath                     | 使用 JSONPath 表达式提取 JSON 数据     |                             |

## 高阶用法

### 导入并使用 `XEnvironment`

`x_jinja2` 提供了一个扩展的 `XEnvironment` 类，该类继承自 `jinja2.Environment` 并添加了一些有用的过滤器。以下是如何使用 `XEnvironment` 的示例：

```python
from x_jinja2 import XEnvironment

# 创建一个 XEnvironment 实例
env = XEnvironment(
    loader=FileSystemLoader('templates'),  # 模板文件加载器
    autoescape=select_autoescape(['html', 'xml'])  # 自动转义
)

# 加载模板
template = env.get_template('example.html')

# 渲染模板
rendered = template.render(name="World")

print(rendered)
```

### 使用过滤器

`XEnvironment` 包含了一些内置的过滤器，例如 `normalize_csv`。以下是如何在模板中使用这些过滤器的示例：

```html
<!-- example.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <p>{{ name | normalize_csv }}</p>
  </body>
</html>
```
