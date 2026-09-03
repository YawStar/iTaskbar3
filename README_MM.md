# iTaskbar3

**PySide6** နဲ့ ရေးထားတဲ့ Windows GUI Application တွေမှာ Windows ရဲ့ Native **ITaskbarList3 COM API** ကို အသုံးပြုပြီး Taskbar Progress နဲ့ Overlay Icon တွေကို ထိန်းချုပ်နိုင်အောင် ပြုလုပ်ထားတဲ့ Lightweight Python Project ဖြစ်ပါတယ်။

`iTaskbar3` ကို အသုံးပြုပြီး Application ရဲ့ Downloading, Paused, Error, Completed, Loading စတဲ့ State တွေကို Windows Taskbar ပေါ်မှာ ပြသနိုင်ပါတယ်။

## Features

- Native Windows `ITaskbarList3` support
- Taskbar Progress Bar
- Windows Taskbar Progress State ၅ မျိုး
  - `TBPF.NO_PROGRESS`
  - `TBPF.INDETERMINATE`
  - `TBPF.NORMAL`
  - `TBPF.ERROR`
  - `TBPF.PAUSED`
- Taskbar Overlay Icon
- Downloading State
- Paused State
- Error State
- Completed State
- Loading / Indeterminate State
- Progress Value / Maximum Value သတ်မှတ်နိုင်ခြင်း
- COM Initialization / Cleanup အလိုအလျောက်လုပ်ဆောင်ခြင်း
- PySide6 မှ Native Windows `HWND` ရယူအသုံးပြုနိုင်ခြင်း
- Taskbar API အတွက် Python Package ထပ်မံ Install လုပ်ရန်မလိုခြင်း
- `ctypes` ကိုအသုံးပြုထားသော Lightweight Implementation

## Requirements

- Windows 10 သို့မဟုတ် Windows 11
- Python 3.10+
- PySide6
- Windows Desktop Environment

## Project Structure

```text
iTaskbar3/
│
├── iTaskbar3.py
├── iTaskbar3_Example.py
│
└── resources/
    ├── downloading.ico
    ├── paused.ico
    ├── error.ico
    └── completed.ico
```

## Installation

PySide6 ကို Install လုပ်ရန်—

```powershell
pip install PySide6
```

`uv` အသုံးပြုနေပါက—

```powershell
uv add PySide6
```

`ITaskbarList3` အတွက် သီးခြား Python Package ထပ်ပြီး Install လုပ်ရန် မလိုပါ။

## Basic Usage

`taskbar.py` မှာရှိတဲ့ Class တွေကို Import လုပ်ပါ။

```python
from taskbar import ITaskbarList3, TBPF
```

PySide6 Window ရဲ့ Native Windows `HWND` ကို ရယူပါ။

```python
hwnd = int(self.winId())

self.taskbar = ITaskbarList3(hwnd)
```

## Normal Progress

ပုံမှန် Download Progress ပြရန်—

```python
self.taskbar.set_state(TBPF.NORMAL)
self.taskbar.set_progress(50, 100)
```

ဒါဆို Windows Taskbar မှာ 50% Progress ပြပါမယ်။

## Indeterminate Progress

လုပ်ဆောင်ချက်တစ်ခုလုပ်နေတယ်ဆိုတာ သိပေမယ့် ဘယ်လောက် % ပြီးပြီဆိုတာ မသိသေးတဲ့အချိန်မှာ သုံးနိုင်ပါတယ်။

```python
self.taskbar.set_state(TBPF.INDETERMINATE)
```

ဥပမာ—

- Loading
- Metadata Fetching
- Connecting
- Preparing
- Processing

စတဲ့အခြေအနေတွေမှာ အသုံးဝင်ပါတယ်။

## Paused

Download ကို Pause လုပ်ထားတဲ့အခါ—

```python
self.taskbar.set_state(TBPF.PAUSED)
self.taskbar.set_progress(50, 100)
```

## Error

Download သို့မဟုတ် အခြား Operation တစ်ခုခု Error ဖြစ်တဲ့အခါ—

```python
self.taskbar.set_state(TBPF.ERROR)
self.taskbar.set_progress(50, 100)
```

## Progress ဖျောက်ရန်

```python
self.taskbar.set_state(TBPF.NO_PROGRESS)
```

သို့မဟုတ်—

```python
self.taskbar.clear_progress()
```

ကို အသုံးပြုနိုင်ပါတယ်။

# Overlay Icon

`ITaskbarList3` မှာ Application ရဲ့ Taskbar Icon ပေါ်ကို Small Overlay Icon တစ်ခု ထပ်တင်နိုင်ပါတယ်။

## Downloading

```python
self.taskbar.set_overlay_icon(
    "resources/downloading.ico",
    "Downloading"
)
```

## Paused

```python
self.taskbar.set_overlay_icon(
    "resources/paused.ico",
    "Paused"
)
```

## Error

```python
self.taskbar.set_overlay_icon(
    "resources/error.ico",
    "Error"
)
```

## Completed

```python
self.taskbar.set_overlay_icon(
    "resources/completed.ico",
    "Completed"
)
```

## Overlay Icon ဖျောက်ရန်

```python
self.taskbar.clear_overlay_icon()
```

# Convenience Methods

အသုံးများတဲ့ State တွေအတွက် Helper Method တွေပါ ထည့်ထားပါတယ်။

## Downloading

```python
self.taskbar.downloading(
    72,
    100,
    "resources/downloading.ico"
)
```

ဒါဆို—

```text
Progress = 72%
State    = NORMAL
Icon     = Downloading
```

ဖြစ်သွားပါမယ်။

## Paused

```python
self.taskbar.paused(
    72,
    100,
    "resources/paused.ico"
)
```

## Error

```python
self.taskbar.error(
    72,
    100,
    "resources/error.ico"
)
```

## Loading

```python
self.taskbar.indeterminate(
    "resources/downloading.ico"
)
```

## Completed

```python
self.taskbar.completed(
    "resources/completed.ico"
)
```

Completed ဖြစ်သွားတဲ့အခါ Progress Bar ကို ဖျောက်ပြီး Completed Overlay Icon ကို ပြပါမယ်။

## Reset

Progress နဲ့ Overlay Icon နှစ်ခုလုံးကို ပြန်ဖျောက်ရန်—

```python
self.taskbar.reset()
```

# Example State Flow

Downloader Application တစ်ခုမှာ ဒီလို State Flow အသုံးပြုနိုင်ပါတယ်။

```text
          ┌──────────────┐
          │   Loading    │
          │ INDETERMINATE│
          └──────┬───────┘
                 │
                 ▼
          ┌──────────────┐
          │ Downloading  │
          │    NORMAL    │
          └───┬──────┬───┘
              │      │
        Pause │      │ Error
              ▼      ▼
        ┌────────┐ ┌───────┐
        │ Paused │ │ Error │
        └───┬────┘ └───────┘
            │
            │ Resume
            ▼
       ┌─────────────┐
       │ Downloading │
       └──────┬──────┘
              │
              │ Complete
              ▼
       ┌─────────────┐
       │  Completed  │
       │ ✓ Overlay   │
       └─────────────┘
```

# Taskbar Progress States

| State | Value | အဓိပ္ပါယ် |
|---|---:|---|
| `TBPF.NO_PROGRESS` | `0x00` | Progress Bar မပြ |
| `TBPF.INDETERMINATE` | `0x01` | Progress ဘယ်လောက်ပြီးပြီ မသိသေး |
| `TBPF.NORMAL` | `0x02` | ပုံမှန် Progress |
| `TBPF.ERROR` | `0x04` | Error State |
| `TBPF.PAUSED` | `0x08` | Pause State |

`TBPF.COMPLETED` ဆိုတဲ့ State သီးခြားမရှိပါဘူး။

ဒါကြောင့် Completed ဖြစ်သွားတဲ့အခါ—

```python
self.taskbar.set_state(TBPF.NO_PROGRESS)

self.taskbar.set_overlay_icon(
    "resources/completed.ico",
    "Completed"
)
```

လိုအသုံးပြုနိုင်ပါတယ်။

# Resource Icons

Overlay Icon တွေအတွက် အောက်ပါ Size တွေကို အသုံးပြုနိုင်ပါတယ်။

```text
16 × 16
20 × 20
24 × 24
32 × 32
```

`.ico` Format ကို အသုံးပြုရန် အကြံပြုပါတယ်။

```text
resources/
├── downloading.ico
├── paused.ico
├── error.ico
└── completed.ico
```

Windows က သင့်တော်တဲ့ Icon Size ကို လိုအပ်သလို Scale လုပ်ပေးနိုင်ပါတယ်။

# Cleanup

Application ပိတ်တဲ့အချိန်မှာ COM Object ကို Release လုပ်ပေးသင့်ပါတယ်။

```python
def closeEvent(self, event):
    self.taskbar.close()
    super().closeEvent(event)
```

`iTaskbar3` မှာ Destructor Cleanup လည်း ထည့်သွင်းထားပါတယ်။

# ဘာကြောင့် ctypes ကို အသုံးပြုထားသလဲ?

`iTaskbar3` က Python ရဲ့ Built-in `ctypes` Module ကို အသုံးပြုပြီး Windows COM Interface ကို တိုက်ရိုက် Access လုပ်ထားပါတယ်။

ဒီလိုလုပ်ခြင်းအားဖြင့် Windows Taskbar API အတွက် သီးခြား Python Wrapper Package တစ်ခု ထပ်ပြီး Install လုပ်ရန် မလိုတော့ဘဲ Project ကို Lightweight ဖြစ်အောင် ထိန်းထားနိုင်ပါတယ်။

# Platform

`iTaskbar3` သည် Windows အတွက် ရည်ရွယ်ထားသော Project ဖြစ်ပါတယ်။

```text
Windows 10
Windows 11
```

Linux နှင့် macOS ရဲ့ Taskbar / Dock API တွေအတွက် ဒီ Project ကို ရည်ရွယ်ထားခြင်း မရှိပါ။

# License

Project အတွက် သင့်တော်တဲ့ License ကို ရွေးချယ်အသုံးပြုနိုင်ပါတယ်။

ဥပမာ—

```text
MIT License
```

# Project Name

**iTaskbar3**

Project Name မှာ `iTaskbar3` လို့ ပေးထားခြင်းက Windows ရဲ့ အသုံးပြုထားတဲ့ Native Interface ဖြစ်တဲ့ **`ITaskbarList3`** ကို ရည်ညွှန်းထားတာ ဖြစ်ပါတယ်။