from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


TEMPLATE_FILES = {
    "problem_analysis.md": "# 问题分析\n\n## 题目本质\n\n## 逐问拆解\n\n## 数据需求\n\n## 建模难点\n\n## 可行路线\n",
    "model_plan.md": "# 建模方案\n\n## 候选模型比较\n\n## 主模型\n\n## 变量与假设\n\n## 求解方法\n\n## 检验方案\n",
    "experiment_log.md": "# 实验记录\n\n| 时间 | 代码/脚本 | 输入 | 输出 | 结论 | 问题 |\n|---|---|---|---|---|---|\n",
    "paper_notes.md": "# 论文素材\n\n## 摘要素材\n\n## 图表解释\n\n## 关键结论\n",
    "ai_record.md": "# AI 使用记录\n\n| 时间 | 工具 | 用途 | 提示词摘要 | 输出摘要 | 采纳与核验 |\n|---|---|---|---|---|---|\n",
}


def init_problem(name: str) -> Path:
    slug = name.strip().replace(" ", "_")
    problem_dir = ROOT / "01_problems" / f"{date.today().isoformat()}_{slug}"
    problem_dir.mkdir(parents=True, exist_ok=True)

    for filename, content in TEMPLATE_FILES.items():
        path = problem_dir / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    for subdir in ["data", "code", "outputs", "figures", "paper"]:
        (problem_dir / subdir).mkdir(exist_ok=True)

    return problem_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new modeling problem workspace.")
    parser.add_argument("name", help="Problem name, for example CUMCM_2026_A")
    args = parser.parse_args()

    problem_dir = init_problem(args.name)
    print(f"Created: {problem_dir}")


if __name__ == "__main__":
    main()

