# 🤖 Mobile Robot for Gauge Inspection

An autonomous mobile robot that navigates industrial environments and reads analogue pressure gauges using a **Neuro-Fuzzy system** combining Fuzzy Logic for motion control and a Convolutional Neural Network (CNN) for gauge reading.

---

## Overview

In hazardous industrial environments, sending workers to manually read gauges poses serious safety risks. This project addresses that by deploying an autonomous robot that:

<img width="470" height="468" alt="image" src="https://github.com/user-attachments/assets/709a409a-732b-4d34-89d3-5171ef228e7c" />


1. **Follows a track** using IR sensors
2. **Avoids obstacles** intelligently using Fuzzy Logic + ultrasonic sensors
3. **Stops at a gauge**, detects it via computer vision, and reads its value using a trained CNN

---

## Features

- 🧠 **Neuro-Fuzzy hybrid system** combining the interpretability of fuzzy logic with the pattern recognition power of neural networks
- 🚧 **Obstacle avoidance** with a 27-rule fuzzy inference system (3 sensors × 3 MFs each)
- 📷 **Gauge detection** using Hough Circle & Line Transforms + Canny Edge Detection
- 📊 **Gauge reading** via a CNN trained on pressure gauge images (0–100 psi)
- 🖨️ **3D-printed chassis** designed in SolidWorks with adjustable ultrasonic sensor mounts

---

## prototype

<img width="461" height="375" alt="image" src="https://github.com/user-attachments/assets/b9c56359-3dc0-40a9-98f6-7ace9876f656" />


## Hardware Components

| Component | Purpose |
|---|---|
| Raspberry Pi Pico | Main microcontroller |
| Ultrasonic Sensors (HC-SR04) | Obstacle distance measurement (left, front, right) |
| DC Motors + Motor Driver | Differential drive locomotion |
| IR Sensors | Line following on track |
| Camera | Visual gauge detection and reading |

---

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Mobile Robot                      │
│                                                     │
│  IR Sensors ──► Line Following                      │
│                                                     │
│  Ultrasonic   ──► Fuzzy Logic ──► Motor Control     │
│  Sensors (×3)     (27 Rules)      (Differential     │
│                                    Drive)           │
│                                                     │
│  Camera ──► Computer Vision ──► CNN ──► Gauge Value │
│             (Hough Transform,                       │
│              Canny Edge)                            │
└─────────────────────────────────────────────────────┘
```

## Fuzzy Logic — Motion Control

### Why Fuzzy Logic?
Fuzzy logic is preferred over neural networks for obstacle avoidance because it is more hardware-efficient, interpretable, and cost-effective in real-time embedded scenarios.

### Inputs & Outputs

- **Inputs:** Left ultrasonic sensor, Front ultrasonic sensor, Right ultrasonic sensor
- **Outputs:** Left motor speed, Right motor speed

### Membership Functions

**Inputs (Distance — HC-SR04 range: 3cm to 400cm)**

| Fuzzy Set | Type | Range |
|---|---|---|
| Near | `trimf` | [2, 2, 25] |
| Medium | `trimf` | [~25, mid, ~200] |
| Far | `trapmf` | [~150, 400, 400, 400] |

**Outputs (Motor Speed — range: -200 to 200)**

| Fuzzy Set | Description |
|---|---|
| Negative Fast | Move backward quickly |
| Negative Slow | Move backward slowly |
| Zero | Stop |
| Positive Slow | Move forward slowly |
| Positive Fast | Move forward quickly |

### Rule Base

The system uses **27 fuzzy rules** (3³ combinations). 

<img width="567" height="692" alt="fuzzy rules" src="https://github.com/user-attachments/assets/d70d1e86-70bd-4c59-8d98-76e79028c82a" />

---

## Neural Network — Gauge Inspection

### Pipeline

Camera Frame
    │
    ▼

    

<img width="185" height="186" alt="image" src="https://github.com/user-attachments/assets/9700ec93-129b-4a3a-b1fb-c3092b317a4d" />


Canny Edge Detection  (noise reduction) 
    │
    ▼


    

<img width="196" height="196" alt="image" src="https://github.com/user-attachments/assets/899c7818-4537-464c-a89f-9b26e2be1dad" />


Hough Circle Transform  (detect gauge dial)
    │
    ▼


    
<img width="193" height="188" alt="image" src="https://github.com/user-attachments/assets/3a53e25f-2dea-49bb-bf8e-7de171fb6eb6" />


Hough Line Transform  (detect needle)
    │
    ▼


    
<img width="167" height="181" alt="image" src="https://github.com/user-attachments/assets/5beb50b3-f73e-4e65-bfa5-d65edb278524" />


CNN Inference  (classify gauge reading)
    │
    ▼
    
Output: Pressure Value (psi)


---

## Software & Libraries

| Library | Purpose |
|---|---|
| `scikit-fuzzy` (skfuzzy) | Fuzzy logic system — membership functions & rules |
| `MicroPython` | Raspberry Pi Pico motor & sensor control |
| `OpenCV` | Image processing, Hough transforms, Canny edge detection |
| `TensorFlow` | CNN model training and inference |
