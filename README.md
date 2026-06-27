# 🏗️ AutoCAD V2 Hybrid MCP Project: Curtain Wall Bracket Shop Drawings

[![AutoCAD](https://img.shields.io/badge/AutoCAD-2022%2B-red.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](#)
[![C# .NET](https://img.shields.io/badge/C%23-.NET%208.0-purple.svg)](#)
[![MCP](https://img.shields.io/badge/MCP-Protocol-green.svg)](#)
[![Standard](https://img.shields.io/badge/Standard-JIS-orange.svg)](#)

## 📌 Project Overview / Tổng quan dự án

**[EN]** This project demonstrates the integration of **AI Automation** with **AutoCAD** to automatically generate a complete Shop Drawing package and 3D Models for a Stainless Steel Curtain Wall Bracket system. 
**Version 2.0 Upgrade:** The project has evolved from a pure Python 2D script to a **Hybrid Architecture**:
1. **Python MCP Server**: Handles AI orchestration and engineering calculations.
2. **C# .NET AutoCAD Plugin (ObjectARX)**: Handles high-performance 3D solid modeling and geometric extraction.

**[VN]** Dự án này thể hiện sự tích hợp giữa **Trí tuệ nhân tạo (AI)** và **AutoCAD** để tự động hóa việc xuất hồ sơ bản vẽ gia công (Shop Drawing) và Mô hình 3D cho hệ thống Bracket Inox mặt dựng kính.
**Bản nâng cấp V2.0:** Dự án đã tiến hóa từ script 2D Python thuần túy sang **Kiến trúc Hybrid**:
1. **Python MCP Server**: Xử lý điều phối AI và tính toán kỹ thuật.
2. **C# .NET AutoCAD Plugin (ObjectARX)**: Xử lý mô hình hóa Solid 3D hiệu năng cao và trích xuất hình học.

---

## 🎯 V2 Key Features / Tính năng nổi bật V2

1. **JIS Compliance (Chuẩn JIS):**
   * **JIS B 0001**: Technical drafting conventions (Layers, Linetypes, Dimension Styles).
   * **JIS Z 3021**: Welding symbols (Ký hiệu hàn).
   * **JIS B 3402**: Bilingual (JP/EN) A3 Title Block fields.
2. **Engineering Calculation Engine (Động cơ tính toán):**
   * Python-based module calculating Bracket Weight, Material Density (SUS304), and Bending Stress safety factors.
3. **C# 3D Solid Generation (Mô hình 3D C#):**
   * A compiled `.dll` loaded into AutoCAD executing operations orders of magnitude faster than COM.
   * Parametric generation of 3D solids, boolean subtractions for bolt holes, and mass property extraction.
4. **AI-Driven Automation (Tự động hóa qua AI):**
   * An MCP Server translates AI Agent prompts into executable Python calculations and AutoCAD commands.

---

## 🛠️ Technology Stack / Công nghệ sử dụng

* **CAD Software:** AutoCAD 2022 / 2023 / 2024
* **Languages:** Python 3.9+ & C# (.NET 8.0)
* **APIs:** AutoCAD COM API (`pywin32`) & AutoCAD Managed .NET API (ObjectARX)
* **Protocol:** `mcp` (Model Context Protocol server)

---

## 📂 Project Structure / Cấu trúc thư mục

```text
AutoCad-2D-MCP-Project/
│
├── README.md                         # Project documentation
├── STATE.md                          # Triage and progression state
├── autocad_mcp_server.py             # Main Python MCP server connecting to AutoCAD
│
├── AutoCad3DPlugin/                  # [V2] C# .NET Project for AutoCAD
│   ├── AutoCad3DPlugin.csproj
│   └── BracketBuilder.cs             # 3D Solid generation logic
│
├── plans/                            # AI Agent planning files (.md)
│   ├── 00-master-plan.md
│   ├── ...
│   └── 11-calc-engine.md             # V2 logic plans
│
├── scripts/                          # Execution scripts & Calculation engine
│   ├── calc_engine.py                # [V2] Structural calculation logic
│   ├── draw_3d_bracket.py            # [V2] Demo script connecting Calc + 3D
│   ├── draw_dwg001.py                # V1 2D generation scripts
│   └── ...
│
├── drawings/                         # Output generated .dwg files
├── pdf-output/                       # Exported PDF deliverables
└── reference/                        # Reference materials & standards
```

---

## 🚀 Getting Started / Hướng dẫn cài đặt

### 1. Prerequisites (Yêu cầu hệ thống)
* Windows OS with AutoCAD installed.
* Python 3.9+ installed.
* .NET 8.0 SDK (to build the C# plugin).

### 2. Installation & Build (Cài đặt & Build)
Clone the repository and build the C# plugin:
```bash
git clone https://github.com/TPH-Per/AutoCad-2D-MCP-Project.git
cd AutoCad-2D-MCP-Project
pip install -r requirements.txt

# Build the C# Plugin
cd AutoCad3DPlugin
dotnet build -c Release
```

### 3. Running the V2 Demo (Chạy thử nghiệm)
1. Open **AutoCAD** and start a new blank drawing (`acad.dwt`).
2. Run the V2 demo script:
   ```bash
   python scripts/draw_3d_bracket.py
   ```
   *This will run the Python structural calculations, connect to AutoCAD, load the compiled C# `.dll`, and generate the 3D solid bracket automatically.*

---

## 🤝 Contact / Liên hệ
* **Author:** [TPH-Per]
* **Repository:** [https://github.com/TPH-Per/AutoCad-2D-MCP-Project](https://github.com/TPH-Per/AutoCad-2D-MCP-Project)
