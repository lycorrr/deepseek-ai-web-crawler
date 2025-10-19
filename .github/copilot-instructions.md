# Deep Seek Crawler Copilot 指南

本文档旨在帮助 AI 编码代理高效参与 `deepseek-ai-web-crawler` 代码库开发。请遵循以下约定和工作流程进行有效贡献。

## 架构概览

- **目标：** 基于 [Crawl4AI](https://pypi.org/project/Crawl4AI/) 和 LLM 提取的异步 Python 婚礼场地数据爬虫。
- **主流程：**
  - `main.py` 为主入口，负责调度爬取、抽取和结果保存。
  - `config.py` 存放常量（URL、选择器、必填字段）。
  - `models/venue.py` 定义场地数据结构（Pydantic）。
  - `utils/data_utils.py` 负责数据校验和 CSV 导出。
  - `utils/scraper_utils.py` 配置爬虫、LLM 策略和页面处理逻辑。
- **数据流：**
  - 爬虫抓取页面 → LLM 抽取场地数据 → 数据校验与去重 → 结果保存到 `complete_venues.csv`。

## 开发者工作流

- **环境搭建：**
  - 使用 Conda：`conda create -n deep-seek-crawler python=3.12 -y && conda activate deep-seek-crawler`
  - 安装依赖：`pip install -r requirements.txt`
  - 添加 `.env` 文件，包含 LLM 抽取所需的 `DEEPSEEK_API_KEY`。
- **运行：**
  - 启动爬虫：`python main.py`
  - 输出文件：项目根目录下的 `complete_venues.csv`。
- **配置修改：**
  - 更改爬取目标或必填字段请修改 `config.py`。
  - LLM 提供方和抽取 schema 在 `utils/scraper_utils.py:get_llm_strategy()` 中设置。

## 项目特有模式

- **模块化：**
  - 爬取、抽取、校验、保存分别在独立模块中实现，职责分明。
  - 所有场地数据需符合 `models/venue.py` 的 schema，并通过 `is_complete_venue` 校验。
- **去重：**
  - 通过 `seen_names` 集合按名称去重场地。
- **错误处理：**
  - 采用 print 打印状态和错误信息，暂未引入高级日志。
- **可扩展性：**
  - 新增字段需同步修改 `models/venue.py`、`config.py` 及 `scraper_utils.py` 中的抽取指令。

## 集成点

- **外部：**
  - 使用 [Crawl4AI](https://docs.crawl4ai.com/) 进行爬取和 LLM 抽取。
  - `.env` 文件用于存放 API 密钥（请勿提交该文件）。
- **内部：**
  - 所有跨模块导入均使用相对路径（如 `from utils.data_utils import ...`）。

## 示例

- 更换目标网站：修改 `config.py` 中的 `BASE_URL`。
- 调整抽取逻辑：修改 `get_llm_strategy()` 里的 `instruction` 字符串。
- 新增场地字段：需同步更新 Pydantic 模型和 CSV 逻辑。

## 约定

- 所有数据模型均使用 Pydantic。
- 所有工具函数集中在 `utils/` 目录。
- 仅保存通过完整性和去重校验的场地数据。
- 爬取和抽取时建议开启 verbose 模式，便于调试。

---

如有任何不清楚或遗漏的部分，请反馈以便进一步完善。
