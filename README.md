# 🏗️ AutoCAD 2D MCP Project: Curtain Wall Bracket Shop Drawings

[![AutoCAD](https://img.shields.io/badge/AutoCAD-2022%2B-red.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](#)
[![MCP](https://img.shields.io/badge/MCP-Protocol-green.svg)](#)
[![Standard](https://img.shields.io/badge/Standard-JIS-orange.svg)](#)

## 📌 Project Overview / Tổng quan dự án

**[EN]** This project demonstrates the integration of **AI Automation** with **AutoCAD 2D** to automatically generate a complete Shop Drawing package for a Stainless Steel Curtain Wall Bracket system. It leverages the **Model Context Protocol (MCP)** and Python's `win32com` library to control AutoCAD via the COM API. The drawings strictly follow the **Japanese Industrial Standards (JIS)**, making it highly applicable for Japanese architectural and metalwork projects.

**[VN]** Dự án này thể hiện sự tích hợp giữa **Trí tuệ nhân tạo (AI)** và **AutoCAD 2D** để tự động hóa việc xuất một bộ hồ sơ bản vẽ gia công (Shop Drawing) hoàn chỉnh cho hệ thống Bracket Inox mặt dựng kính. Dự án sử dụng **Model Context Protocol (MCP)** và thư viện `win32com` của Python để giao tiếp với AutoCAD COM API. Các bản vẽ tuân thủ nghiêm ngặt **Tiêu chuẩn Công nghiệp Nhật Bản (JIS)**, phù hợp cho môi trường làm việc kỹ thuật cơ khí & kiến trúc Nhật Bản.

---

## 🎯 Key Features / Tính năng nổi bật

1. **JIS Compliance (Chuẩn JIS):**
   * **JIS B 0001**: Technical drafting conventions (Layers, Linetypes, Dimension Styles).
   * **JIS Z 3021**: Welding symbols (Ký hiệu hàn).
   * **JIS B 3402**: Bilingual (JP/EN) A3 Title Block fields.
2. **Shop Drawing Package (Bộ hồ sơ hoàn chỉnh):**
   * DWG-001: General Arrangement (Mặt đứng tổng thể)
   * DWG-002: Bracket Type-A Detail (Chi tiết Bracket A)
   * DWG-003: Bracket Type-B Detail (Chi tiết Bracket B)
   * DWG-004: Connection & Anchor Detail (Chi tiết neo & hàn)
   * DWG-005: 3D Exploded View in 2D (Bản vẽ phân rã Isometric)
   * DWG-006: Bill of Materials (Bảng thống kê vật tư)
3. **AI-Driven Automation (Tự động hóa qua AI):**
   * An MCP Server translates AI Agent prompts into executable AutoCAD commands.
   * Automates the creation of Layers, Lines, Polylines, Hatches, Dimensions, and Texts directly in the Model Space.

---

## 🛠️ Technology Stack / Công nghệ sử dụng

* **CAD Software:** AutoCAD 2022 / 2023 / 2024
* **Language:** Python 3.9+
* **Libraries:** `pywin32` (COM automation), `mcp` (Model Context Protocol server)
* **AI Integration:** Claude Desktop / Any MCP-compatible AI client

---

## 📂 Project Structure / Cấu trúc thư mục

```text
AutoCad-2D-MCP-Project/
│
├── README.md                         # Project documentation
├── autocad_mcp_server.py             # Main Python MCP server connecting to AutoCAD
├── requirements.txt                  # Python dependencies (pywin32, mcp)
│
├── plans/                            # AI Agent planning files (.md)
│   ├── 00-master-plan.md
│   ├── 01-mcp-server-spec.md
│   ├── 02-drawing-setup.md
│   ├── 03-dwg001-assembly.md
│   ├── ...
│
├── drawings/                         # Output generated .dwg files
│   ├── DWG-001_General-Arrangement.dwg
│   ├── DWG-002_Bracket-Type-A.dwg
│   └── ...
│
└── reference/                        # Reference materials & standards
    └── JIS_Guidelines.pdf
```

---

## 🚀 Getting Started / Hướng dẫn cài đặt

### 1. Prerequisites (Yêu cầu hệ thống)
* Windows OS with AutoCAD installed.
* Python 3.9+ installed.

### 2. Installation (Cài đặt)
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/TPH-Per/AutoCad-2D-MCP-Project.git
cd AutoCad-2D-MCP-Project
pip install -r requirements.txt
```

### 3. Running the MCP Server (Khởi chạy Server)
1. Open **AutoCAD** and start a new blank drawing (`acad.dwt`).
2. Run the MCP server in your terminal:
   ```bash
   python autocad_mcp_server.py
   ```
3. Configure your AI Client (e.g., Claude Desktop) to connect to this local MCP server by adding it to your `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "autocad": {
         "command": "python",
         "args": ["C:/path/to/your/AutoCad-2D-MCP-Project/autocad_mcp_server.py"]
       }
     }
   }
   ```

### 4. Executing Prompts (Thực thi bản vẽ)
Once connected, you can ask the AI to draw objects based on the plans provided in the `plans/` directory. For example:
> *"Load the DWG-002 plan and use the AutoCAD MCP tools to generate the Bracket Type-A details."*

---

## 🤝 Contact / Liên hệ
* **Author:** [TPH-Per]
* **Repository:** [https://github.com/TPH-Per/AutoCad-2D-MCP-Project](https://github.com/TPH-Per/AutoCad-2D-MCP-Project)
