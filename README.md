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

## 详细用法

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
