# 如何使用

1. 安装 Python
2. 克隆仓库
  ```
git clone https://github.com/ECUsam/HakushinTranz.git
```
3. 打开config.py，填好游戏路径和paratranz路径
4. 命令行输入

  ```
python strat.py --mode [mode]
```

可选的 `mode` 参数：

- `trans`：需要 `gamePath` 和 `paraPath`，将 Paratranz 中的翻译导入到游戏内。
- `paraData`：需要 `gamePath`，输出用于 Paratranz 格式的数据。
- `updateParaData`：需要 `gamePath` 和 `paraPath`，更新已有数据并输出 Paratranz 格式的数据。
