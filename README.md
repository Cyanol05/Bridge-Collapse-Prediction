# Bridge-Collapse-Prediction
This project addresses a critical real-world problem, especially relevant in developing countries where aging infrastructure poses significant safety risks.

# Bridge Crack Detection Project

#Architecture, Working and Flow
# Bridge Failure Prediction — AI/ML Module

## What this does

Analyses bridge inspection photos and predicts:

- **What damage exists** (crack, corrosion, spalling, deformation, none)
- **How severe it is** (0–100 structural health score)
- **When it will fail** (estimated days to critical state)
- **What to do** (AI-generated maintenance report)

---

## Project structure

```
bridge_ai/
├── model.py          ← CNN architecture (EfficientNet-B3 + 3 heads)
├── dataset.py        ← Data loading and image augmentation
├── train.py          ← Training loop with multi-task loss
├── predict.py        ← Inference + LLM report generation
└── requirements.txt
```

---

## Step-by-step setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare your data

Create a CSV with these exact columns:

```
image_path,damage_type,severity_score,days_to_failure
images/bridge_001.jpg,crack,45,120
images/bridge_002.jpg,none,85,730
images/bridge_003.jpg,corrosion,62,60
```

- `damage_type`: one of `none | crack | corrosion | spalling | deformation`
- `severity_score`: 0 (destroyed) to 100 (perfect)
- `days_to_failure`: expert-estimated days until urgent intervention needed

Split into `data/train.csv` and `data/val.csv` (80/20 split).

If you don't have labels yet — **use Roboflow or Label Studio** to annotate.
Public dataset to start: CODEBRIM (Bridge Defect dataset) on Kaggle.

### 3. Train the model

```bash
python train.py
```

Training runs in 2 phases:

- Epochs 1–10: Only the 3 output heads train (backbone frozen)
- Epochs 11–20: Last 3 backbone blocks unfreeze for fine-tuning

Checkpoint saved to `checkpoints/bridge_model.pt`.

### 4. Run predictions

```bash
python predict.py checkpoints/bridge_model.pt path/to/bridge_image.jpg
```

Output:

```
==================================================
DAMAGE TYPE   : crack (91.3% confidence)
SEVERITY      : 38.2/100
DAYS TO FAIL  : 87 days
RISK LEVEL    : HIGH
==================================================

WHAT IS THE ISSUE:
Surface-level flexural cracking was detected along the mid-span...

WHY IT HAPPENED:
Repeated traffic loading combined with freeze-thaw cycles...

WHEN IS IT CRITICAL:
At the current deterioration rate, structural intervention is needed
within approximately 87 days...

NEXT STEPS:
1. Schedule emergency inspection by certified structural engineer
2. Apply epoxy injection to seal active cracks
3. Install strain gauges for real-time monitoring
...
```

---

## Improving accuracy

| Strategy                     | When to use                                        |
| ---------------------------- | -------------------------------------------------- |
| Collect more labelled images | <500 images per class                              |
| Use Grad-CAM visualization   | To verify model looks at cracks, not background    |
| Add temporal sequences       | If you have images of the same bridge over time    |
| Add metadata features        | Bridge age, material, traffic load as extra inputs |
| Ensemble multiple models     | For production deployment                          |

---

## Setting your API key (for LLM reports)

```bash
export ANTHROPIC_API_KEY=your_key_here
```

Or replace `"YOUR_API_KEY_HERE"` in `predict.py`.

## Dataset
The dataset is hosted on Kaggle:

🔗 https://www.kaggle.com/datasets/arnavr10880/concrete-crack-images-for-classification?resource=download

### Download Instructions:

1. Open the link above
2. Click "Download"
3. Extract the dataset

### Folder Structure Required:

dataset/
├── deck/
├── pavement/
├── wall/

## Setup Instructions

1. Import database:
   * Run bridge_db.sql in MySQL
2. Place dataset folder:
   project/
   ├── dataset/

3. Run the project

## Important Notes

* Do NOT change folder names
* Database uses relative paths (dataset/...)
* ⚠️ Dataset is not included in this repository due to size limits.

