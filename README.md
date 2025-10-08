# VIRTUAL_PAINTER
# 🎨 Virtual Painter (Computer Vision Project)

A fun and interactive **Virtual Painter** built using **OpenCV** and **MediaPipe** 
that lets you draw on the screen using your **hand gestures** — no mouse or stylus needed! 🖐️💻

---

## 🚀 Features

- 🖐️ **Hand Tracking** using MediaPipe
- ✍️ **Draw with index finger** in real-time
- 🎨 **Color selection** using finger position
- 🧽 **Eraser mode** to remove drawings
- 📷 **Camera feed overlay** for visual feedback
- 💡 **FPS counter** for performance monitoring

---

## 🧰 Technologies Used

| Tool / Library | Purpose |
|-----------------|----------|
| **Python 3.12** | Programming language |
| **OpenCV** | Image processing and drawing functions |
| **MediaPipe** | Hand detection and tracking |
| **NumPy** | Array operations |
| **cvzone (optional)** | Simplified computer vision utilities |

---

## 🖥️ How It Works

1. The camera captures your hand in real time.
2. MediaPipe detects your hand landmarks (index, middle, etc.).
3. If **only index finger is up**, it activates *drawing mode*.
4. If **both index and middle fingers are up**, it activates *selection mode* to change colors or erase.
5. The system draws lines on a blank canvas, merged with the camera feed.


