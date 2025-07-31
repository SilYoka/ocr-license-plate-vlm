import os
import base64
import requests
import pandas as pd
from PIL import Image
from Levenshtein import distance as levenshtein_distance

# Path
DATASET_PATH = "images/Indonesian License Plate Dataset/images/test"
GROUND_TRUTH_FILE = "ground_truth.csv"
OUTPUT_CSV = "result.csv"

# LMStudio API endpoint
LMSTUDIO_ENDPOINT = "http://localhost:1234/v1/chat/completions"

# Prompt
PROMPT = "What is the license plate number shown in this image? Respond only with the plate number."

# Load ground truth
df_gt = pd.read_csv(GROUND_TRUTH_FILE)

results = []

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

for _, row in df_gt.iterrows():
    filename = row['image']
    gt = row['ground_truth']
    img_path = os.path.join(DATASET_PATH, filename)

    if not os.path.exists(img_path):
        print(f"Missing: {img_path}")
        continue

    base64_img = encode_image(img_path)

    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llava",  # atau model multimodal lain seperti "bakllava", "phi-3-vision"
        "messages": [
            {"role": "user", "content": [
                {"type": "text", "text": PROMPT},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"}}
            ]}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(LMSTUDIO_ENDPOINT, headers=headers, json=data)
        response_json = response.json()
        prediction = response_json['choices'][0]['message']['content'].strip().replace(" ", "").upper()

        S = levenshtein_distance(gt, prediction)
        N = len(gt)
        CER = S / N if N > 0 else 1.0

        results.append({
            "image": filename,
            "ground_truth": gt,
            "prediction": prediction,
            "CER_score": round(CER, 3)
        })

    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Save to CSV
pd.DataFrame(results).to_csv(OUTPUT_CSV, index=False)
print("Selesai! Hasil disimpan di:", OUTPUT_CSV)
