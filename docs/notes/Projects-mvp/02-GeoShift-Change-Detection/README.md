# GeoShift Change Detection
Satellite-Based Before vs After Change Detection using Geospatial ML

![Status](https://img.shields.io/badge/Status-MVP_Prototype-blue?style=flat-square)
![Tech](https://img.shields.io/badge/Built_With-Python_•_Streamlit_•_Rasterio_•_OpenCV-00C853?style=flat-square)
![License](https://img.shields.io/badge/License-Apache_2.0-green?style=flat-square)

<p align="center">

  <img src="assets/asset1.jpg" alt="GeoShift Change Detection" width="800"/>
</p>


## Overview
GeoShift is an MVP system that detects and visualizes landscape changes using multi-temporal satellite imagery.
By comparing “Before vs After” scenes, the system automatically highlights areas that have undergone transformations such as:

✔ Deforestation
✔ New constructions & roads
✔ Water body shrinkage
✔ Urban expansion
✔ Agricultural land-use shift

The project demonstrates **remote sensing + machine learning + temporal analysis**, making it suitable for environmental monitoring & geospatial AI portfolios.

> 📚 [Read the full story on Medium](https://sukriti-speaks.medium.com/geoshift-automated-landscape-intelligence-from-space-aefe3099a9bb?postPublishedType=initial)

---
## Streamlit App Demo

Below is the visual interface of the GeoShift app detecting landscape changes using uploaded satellite images:

<p align="center"> <img src="assets/ss1.png" alt="GeoShift Streamlit UI - Home" width="800"/> <br> <em>Home Screen — Upload Before/After imagery</em> </p>  

<p align="center">
  <img src="assets/ss2.png" alt="GeoShift Streamlit Change Heatmap" width="400"/>
  <img src="assets/ss3.png" alt="Before After Comparison" width="400"/>
</p> 

---

## Key Features

| Module | Capability |
|-------|------------|
| Data Acquisition | Upload "Before" and "After" GeoTIFF images |
| Pre-processing | Basic raster alignment (reprojection) |
| Change Detection Engine | Spectral Change Detection (NDVI Differencing) |
| Visualization Layer | Difference Heatmaps + Change Masks + Side-by-Side Comparison |
| Output Metrics | % Area Changed, GeoTIFF Mask Export |

---

## Methodology

### **Spectral Change Detection (MVP baseline)**
- Compute NDVI/NDWI/NBR for both timestamps
- Generate difference raster: `delta = im_after - im_before`
- Threshold differences to create change mask
- Overlay mask on original scene for visualization

<!-- ### Option B — **Siamese Change Detection Model (Advanced)**
```
Image T1 → CNN Encoder ─┐
│→ Feature Difference → Upsampling Decoder → Change Mask
Image T2 → CNN Encoder ─┘
```
Loss Used: **Binary Cross Entropy + Dice**
Output: Pixel-level change classification heatmap -->

---

## Tech Stack


| Category | Tools |
|---|---|
| Language | Python |
| Geospatial Processing | Rasterio, NumPy |
| ML / CV | OpenCV, Matplotlib |
| Data Source | User Upload / Synthetic Mock Data |
| Visualization | Streamlit |
| Deployment | Local Streamlit Server |

---

## Project Structure
```
GeoShift-Change-Detection/
│── data/               # input imagery + output masks
│── src/
│   ├── preprocessor.py       # image alignment + band extraction
│   ├── differencer.py        # NDVI change computation
│   ├── generate_mock_data.py # synthetic data generator
│   ├── debug_ndvi.py         # debug script for NDVI values
│   ├── test_differencer.py   # unit tests for differencer
│── results/            # heatmaps, overlays, reports
│── app.py              # Streamlit frontend
│── requirements.txt    # dependencies
│── README.md
```

---

## How to Run
```bash
# 1. Clone the repository
git clone https://github.com/SukritiC/GeoShift-Change-Detection.git
cd GeoShift-Change-Detection

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate mock data (Optional, for testing)
python src/generate_mock_data.py

# 4. Run the application
streamlit run app.py
```

## License

This documentation and conceptual content are distributed under the **Apache License**.
See the [LICENSE](./LICENSE) file for more information.

---
## Connect with Me

I’m always open to connecting with **developers**, **AI enthusiasts**, and **innovators** working on **Generative AI projects**.
Let’s connect, collaborate, and create impact together!

<p align="center">
  <a href="https://www.linkedin.com/in/sukritichatterjee/" target="_blank" style="margin-right: 15px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="40" height="40" alt="LinkedIn"/>
  </a>
  <a href="https://github.com/SukritiC" target="_blank" style="margin-right: 15px;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="40" height="40" alt="GitHub"/>
  </a>
   <a href="https://sukriti-speaks.medium.com/" target="_blank" style="margin-right: 15px;">
    <img src="assets/medium.png" width="40" height="40" alt="Medium"/>
  </a>
  <a href="https://x.com/SukritiSpeak" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Twitter_new_X_logo.png" width="40" height="40" alt="X (Twitter)"/>
  </a>
</p>

---

<p align="center">
  Let’s exchange ideas on <b>Generative AI</b> and build something extraordinary together. 🌍
</p>

---
