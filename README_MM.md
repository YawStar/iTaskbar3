# iTaskbar3

[**<img src="Flags/us-36816f7e.png" height="14" style="vertical-align:middle"> English**](README.md) | [**<img src="Flags/mm-8f96fa94.png" height="14" style="vertical-align:middle"> Burmese**](README_MM.md)

Native Windows **ITaskbarList3 COM API** ကို အသုံးပြုထားသော **PySide6** application များအတွက် ပေါ့ပါးသော Windows Taskbar integration library တစ်ခု ဖြစ်သည်။

`iTaskbar3` သည် PySide6 application များမှ Windows Taskbar ၏ progress indicator ကို ထိန်းချုပ်နိုင်စေပြီး downloading, paused, error နှင့် completed ကဲ့သို့ application state အမျိုးမျိုးအတွက် overlay icon များကို ပြသနိုင်စေသည်။

---

## 📸 Screenshots

![Main](Screenshots/iTaskbar3_Demo.png)

<video src="Screenshots/iTaskbar3_Demo.mp4" controls width="100%"></video>

---

## လုပ်ဆောင်ချက်များ

- Native Windows `ITaskbarList3` support
- Taskbar progress bar
- Windows Taskbar progress state ၅ မျိုး:
  - `TBPF.NO_PROGRESS`
  - `TBPF.INDETERMINATE`
  - `TBPF.NORMAL`
  - `TBPF.ERROR`
  - `TBPF.PAUSED`
- Taskbar overlay icon များ
- Downloading state
- Paused state
- Error state
- Completed state
- Loading / indeterminate state
- Progress value နှင့် maximum value ကို ထောက်ပံ့ပေးခြင်း
- COM initialization နှင့် cleanup ကို အလိုအလျောက် ပြုလုပ်ပေးခြင်း
- PySide6 မှတစ်ဆင့် native Windows `HWND` ကို ထောက်ပံ့ပေးခြင်း
- Taskbar API အတွက် အခြား Python package ထပ်မံလိုအပ်ခြင်း မရှိခြင်း
- ပေါ့ပါးသော `ctypes` implementation

## လိုအပ်ချက်များ

- Windows 10 သို့မဟုတ် Windows 11
- Python 3.10+
- PySide6
- Windows desktop environment

## Project ဖွဲ့စည်းပုံ

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

PySide6 ကို install လုပ်ပါ:

```powershell
pip install PySide6
```

`uv` ကို အသုံးပြုနေပါက:

```powershell
uv add PySide6
```

`ITaskbarList3` အတွက် အခြား Python package ထပ်မံလိုအပ်ခြင်း မရှိပါ။

## အခြေခံအသုံးပြုပုံ

Taskbar class ကို import လုပ်ပါ:

```python
from taskbar import ITaskbarList3, TBPF
```

PySide6 မှ native Windows window handle ကို ရယူပါ:

```python
hwnd = int(self.winId())

self.taskbar = ITaskbarList3(hwnd)
```

### ပုံမှန် Progress

```python
self.taskbar.set_state(TBPF.NORMAL)
self.taskbar.set_progress(50, 100)
```

Windows Taskbar တွင် progress 50% ခန့်ကို ပြသပေးမည်။

### Indeterminate Progress

Application က အလုပ်လုပ်နေသော်လည်း တိကျသော progress ကို မသိသေးသည့်အခါ အသုံးပြုပါ:

```python
self.taskbar.set_state(TBPF.INDETERMINATE)
```

အောက်ပါလုပ်ဆောင်မှုများအတွက် အသုံးဝင်သည်:

- Loading
- Fetching metadata
- Connecting
- Preparing
- Processing

### Paused

```python
self.taskbar.set_state(TBPF.PAUSED)
self.taskbar.set_progress(50, 100)
```

### Error

```python
self.taskbar.set_state(TBPF.ERROR)
self.taskbar.set_progress(50, 100)
```

### Clear Progress

```python
self.taskbar.set_state(TBPF.NO_PROGRESS)
```

or:

```python
self.taskbar.clear_progress()
```

## Overlay Icons

`ITaskbarList3` သည် application ၏ Taskbar icon ပေါ်တွင် သေးငယ်သော overlay icon တစ်ခုကို ပြသနိုင်သည်။

### Downloading

```python
self.taskbar.set_overlay_icon(
    "resources/downloading.ico",
    "Downloading"
)
```

### Paused

```python
self.taskbar.set_overlay_icon(
    "resources/paused.ico",
    "Paused"
)
```

### Error

```python
self.taskbar.set_overlay_icon(
    "resources/error.ico",
    "Error"
)
```

### Completed

```python
self.taskbar.set_overlay_icon(
    "resources/completed.ico",
    "Completed"
)
```

### Overlay Icon ဖယ်ရှားခြင်း

```python
self.taskbar.clear_overlay_icon()
```

## Convenience Methods

`iTaskbar3` တွင် ပုံမှန်အသုံးပြုသည့် application state များအတွက် higher-level helper method များ ပါဝင်သည်။

### Downloading

```python
self.taskbar.downloading(
    72,
    100,
    "resources/downloading.ico"
)
```

### Paused

```python
self.taskbar.paused(
    72,
    100,
    "resources/paused.ico"
)
```

### Error

```python
self.taskbar.error(
    72,
    100,
    "resources/error.ico"
)
```

### Loading

```python
self.taskbar.indeterminate(
    "resources/downloading.ico"
)
```

### Completed

```python
self.taskbar.completed(
    "resources/completed.ico"
)
```

### Reset

```python
self.taskbar.reset()
```

## State Flow နမူနာ

Downloader application တစ်ခုသည် အောက်ပါ state flow ကို အသုံးပြုနိုင်သည်:

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

## Taskbar Progress State များ

| State                |  Value | Description                 |
| -------------------- | -----: | --------------------------- |
| `TBPF.NO_PROGRESS`   | `0x00` | Hide the progress indicator |
| `TBPF.INDETERMINATE` | `0x01` | Progress is unknown         |
| `TBPF.NORMAL`        | `0x02` | Normal progress             |
| `TBPF.ERROR`         | `0x04` | Error state                 |
| `TBPF.PAUSED`        | `0x08` | Paused state                |

သီးခြား `TBPF.COMPLETED` state မရှိပါ။ Operation တစ်ခု ပြီးဆုံးသွားပါက အောက်ပါနည်းလမ်းကို အသုံးပြုနိုင်သည်:

```python
self.taskbar.set_state(TBPF.NO_PROGRESS)
self.taskbar.set_overlay_icon(
    "resources/completed.ico",
    "Completed"
)
```

## Resource Icons

အကြံပြုထားသော overlay icon အရွယ်အစားများ:

```text
16 × 16
20 × 20
24 × 24
32 × 32
```

Windows က Taskbar အတွက် သင့်လျော်သော icon အရွယ်အစားကို ရွေးချယ်နိုင်သောကြောင့် ICO file များကို အသုံးပြုရန် အကြံပြုသည်။

နမူနာ:

```text
resources/
├── downloading.ico
├── paused.ico
├── error.ico
└── completed.ico
```

## Cleanup

Application ပိတ်သည့်အခါ Taskbar COM object ကို release လုပ်ပါ:

```python
def closeEvent(self, event):
    self.taskbar.close()
    super().closeEvent(event)
```

ဤ implementation တွင် destructor မှတစ်ဆင့် automatic cleanup ကိုလည်း ထည့်သွင်းပေးထားသည်။

## ဘာကြောင့် ctypes ကို အသုံးပြုသလဲ?

`iTaskbar3` သည် Windows COM interface ကို တိုက်ရိုက် access လုပ်ရန် Python ၏ built-in `ctypes` module ကို အသုံးပြုထားသည်။

ထို့ကြောင့် project ကို ပေါ့ပါးစွာ ထိန်းသိမ်းနိုင်ပြီး သီးခြား Windows Taskbar wrapper package တစ်ခု ထပ်မံလိုအပ်ခြင်းကို ရှောင်ရှားနိုင်သည်။

## Project အမည်

**iTaskbar3**

ဤအမည်သည် project တွင် အသုံးပြုထားသော Windows `ITaskbarList3` interface ကို ရည်ညွှန်းထားခြင်း ဖြစ်သည်။

## Platform

`iTaskbar3` ကို အထူးသဖြင့် အောက်ပါ platform များအတွက် ရည်ရွယ်ဖန်တီးထားသည်:

```text
Windows 10
Windows 11
```

Linux သို့မဟုတ် macOS ၏ Taskbar/Dock API များကို ထောက်ပံ့ပေးရန် ရည်ရွယ်ထားခြင်း မရှိပါ။

## 📜 License

ဤ project ကို MIT License အောက်တွင် ဖြန့်ချိထားသည် - အသေးစိတ်အတွက် [LICENSE](LICENSE) file ကို ကြည့်ပါ။

## 👤 Developer အကြောင်း

**YawHackka** မှ ❤️ ဖြင့် ဖန်တီးထားသည်

- 🐙 GitHub: [@yawstar](https://github.com/yawstar)
- 📦 Repository: [iTaskbar3](https://github.com/YawStar/iTaskbar3)

## 🙏 ကျေးဇူးတင်လွှာ

- **QT6** - အခြေခံ Framework
- **Pyside6** - Qt အတွက် Python Bindings
- **IconArchive** - Icon များအတွက် Resource

---

<div align="center">

**[⬆ အပေါ်သို့ ပြန်သွားရန်](#-access-configurations)**

Made with 💚 by YawHackka

</div>
</div>
