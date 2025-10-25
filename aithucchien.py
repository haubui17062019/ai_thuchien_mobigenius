from openai import OpenAI


###Sinh văn bản (Text Generation)###
# --- Cấu hình ---
# Thay <your_api_key> bằng API key của bạn
def text_generation(user_request):
    client = OpenAI(
    api_key="sk-7ErXm0hBZEez4MSgnB1_Bw",
    base_url="https://api.thucchien.ai"
    )

    # --- Thực thi ---
    response = client.chat.completions.create(
    model="gemini-2.5-flash", # Chọn model bạn muốn #gemini-2.5-flash
    messages=[
        {
            "role": "user",
            "content": user_request
        }
    ],
    temperature=0
    )

    return response.choices[0].message.content

user_question = "Give me an image with the theme of Tet, a family riding a golden carp flying up together with a rapid growth chart."
# rs = text_generation(user_request=user_question)
# print(rs)
###Sinh hình ảnh (Image Generation)###
import requests
import json
import base64

# --- Cấu hình ---
AI_API_BASE = "https://api.thucchien.ai"
AI_API_KEY = "sk-7ErXm0hBZEez4MSgnB1_Bw"


def image_generation(model, user_request, num_gen_image):
    print(AI_API_KEY)
    print(model)
    print(AI_API_BASE)
    # --- Gọi API để tạo hình ảnh ---
    url = f"{AI_API_BASE}/images/generations"
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AI_API_KEY}"
    }
    data = {
    "model": model,
    "prompt": user_request,
    "n": num_gen_image, # Yêu cầu 1 ảnh
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        result = response.json()
    
        # --- Xử lý và lưu từng ảnh ---
        for i, image_obj in enumerate(result['data']):
            b64_data = image_obj['b64_json']
            image_data = base64.b64decode(b64_data)
            
            save_path = f"generated_image_{i+1}.png"
            with open(save_path, 'wb') as f:
                f.write(image_data)
            print(f"Image saved to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        print(f"Response body: {response.text if 'response' in locals() else 'No response'}")

image_prompt = """Give me an image with the theme of lunar new year, a family riding a golden carp flying up together with a rapid growth chart."""
image_generation("imagen-4", image_prompt, 1)


def get_dataset():
    import pandas as pd
    import glob

    # Bước 1: Liệt kê tất cả file TXT trong thư mục
    file_list = glob.glob("E:/Dataset_Final/*.txt")

    # Bước 2: Load và concat tất cả file
    df_list = []
    for file in file_list:
        # Đọc file TXT (tab-separated)
        df = pd.read_csv(file, sep="\t", on_bad_lines="skip", header=None, engine="python")

        # Gán tên cột (nếu file không có header)
        df.columns = ["id", "Câu 1", "Câu 2", "score"]

        df_list.append(df)

    # Bước 3: Gộp tất cả file lại
    df_all = pd.concat(df_list, ignore_index=True)

    # Bước 4: Chuẩn hóa điểm về thang 0–1
    df_all["Similarity Score"] = df_all["score"] / 5.0

    # Bước 5: Kiểm tra nhanh
    print(df_all.head())
    print(f"Tổng số dòng: {len(df_all)}")

    # Bước 6: Lưu ra Excel
    output_path = "E:/Dataset_Final/dataset_full_normalized.xlsx"
    df_all.to_excel(output_path, index=False)

    print(f"✅ Dataset đã lưu thành công tại: {output_path}")

# get_dataset()
def tts():
    import requests

    # --- Cấu hình ---
    AI_API_BASE = "https://api.thucchien.ai"
    AI_API_KEY = "sk-QkdYynDUd9WAfFN5M8GjeQ" # Thay bằng API key của bạn

    # --- Thực thi ---
    url = f"{AI_API_BASE}/audio/speech"
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {AI_API_KEY}"
    }
    data = {
    "model": "gemini-2.5-pro-preview-tts",
    "input": "Tất cả mọi người sinh ra đều có quyền bình đẳng. Tạo hoá cho họ những quyền không ai có thể xâm phạm được; trong những quyền ấy, có quyền được sống, quyền tự do và quyền mưu cầu hạnh phúc.",
    "voice": "Ho Chi Minh, Vietnam's President"
    }

    response = requests.post(url, headers=headers, json=data, stream=True)

    if response.status_code == 200:
        with open("speech_from_requests.mp3", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("File âm thanh đã được tạo thành công!")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# tts()

#!/usr/bin/env python3
"""
Complete example for Veo video generation through LiteLLM proxy.

This script demonstrates how to:
1. Generate videos using Google's Veo model
2. Poll for completion status
3. Download the generated video file

Requirements:
- LiteLLM proxy running with Google AI Studio pass-through configured
- Google AI Studio API key with Veo access

# This file is forked and adapted from: https://github.com/BerriAI/litellm/blob/main/docs/my-website/docs/proxy/veo_video_generation.md .Please refer to the original for license details.
"""

import json
import os
import time
import requests
from typing import Optional


class VeoVideoGenerator:
  """Complete Veo video generation client using LiteLLM proxy."""
  
  def __init__(self, base_url: str = "https://api.thucchien.ai/gemini/v1beta", 
               api_key: str = "sk-1234"):
      """
      Initialize the Veo video generator.
      
      Args:
          base_url: Base URL for the LiteLLM proxy with Gemini pass-through
          api_key: API key for LiteLLM proxy authentication
      """
      self.base_url = base_url
      self.api_key = api_key
      self.headers = {
          "x-goog-api-key": api_key,
          "Content-Type": "application/json"
      }
  
  def generate_video(self, prompt: str) -> Optional[str]:
      """
      Initiate video generation with Veo.
      
      Args:
          prompt: Text description of the video to generate
          
      Returns:
          Operation name if successful, None otherwise
      """
      print(f"🎬 Generating video with prompt: '{prompt}'")
      
      url = f"{self.base_url}/models/veo-3.0-generate-preview:predictLongRunning"
      payload = {
          "instances": [{
              "prompt": prompt
          }]
      }
      
      try:
          response = requests.post(url, headers=self.headers, json=payload)
          response.raise_for_status()
          
          data = response.json()
          operation_name = data.get("name")
          
          if operation_name:
              print(f"✅ Video generation started: {operation_name}")
              return operation_name
          else:
              print("❌ No operation name returned")
              print(f"Response: {json.dumps(data, indent=2)}")
              return None
              
      except requests.RequestException as e:
          print(f"❌ Failed to start video generation: {e}")
          if hasattr(e, 'response') and e.response is not None:
              try:
                  error_data = e.response.json()
                  print(f"Error details: {json.dumps(error_data, indent=2)}")
              except:
                  print(f"Error response: {e.response.text}")
          return None
  
  def wait_for_completion(self, operation_name: str, max_wait_time: int = 600) -> Optional[str]:
      """
      Poll operation status until video generation is complete.
      
      Args:
          operation_name: Name of the operation to monitor
          max_wait_time: Maximum time to wait in seconds (default: 10 minutes)
          
      Returns:
          Video URI if successful, None otherwise
      """
      print("⏳ Waiting for video generation to complete...")
      
      operation_url = f"{self.base_url}/{operation_name}"
      start_time = time.time()
      poll_interval = 10  # Start with 10 seconds
      
      while time.time() - start_time < max_wait_time:
          try:
              print(f"🔍 Polling status... ({int(time.time() - start_time)}s elapsed)")
              
              response = requests.get(operation_url, headers=self.headers)
              response.raise_for_status()
              
              data = response.json()
              
              # Check for errors
              if "error" in data:
                  print("❌ Error in video generation:")
                  print(json.dumps(data["error"], indent=2))
                  return None
              
              # Check if operation is complete
              is_done = data.get("done", False)
              
              if is_done:
                  print("🎉 Video generation complete!")
                  
                  try:
                      # Extract video URI from nested response
                      video_uri = data["response"]["generateVideoResponse"]["generatedSamples"][0]["video"]["uri"]
                      print(f"📹 Video URI: {video_uri}")
                      return video_uri
                  except KeyError as e:
                      print(f"❌ Could not extract video URI: {e}")
                      print("Full response:")
                      print(json.dumps(data, indent=2))
                      return None
              
              # Wait before next poll, with exponential backoff
              time.sleep(poll_interval)
              poll_interval = min(poll_interval * 1.2, 30)  # Cap at 30 seconds
              
          except requests.RequestException as e:
              print(f"❌ Error polling operation status: {e}")
              time.sleep(poll_interval)
      
      print(f"⏰ Timeout after {max_wait_time} seconds")
      return None
  
  def download_video(self, video_uri: str, output_filename: str = "generated_video.mp4") -> bool:
      """
      Download the generated video file.
      
      Args:
          video_uri: URI of the video to download (from Google's response)
          output_filename: Local filename to save the video
          
      Returns:
          True if download successful, False otherwise
      """
      print(f"⬇️  Downloading video...")
      print(f"Original URI: {video_uri}")
      
      # Convert Google URI to LiteLLM proxy URI
      # Example: https://generativelanguage.googleapis.com/v1beta/files/abc123 -> /gemini/download/v1beta/files/abc123:download?alt=media
      if video_uri.startswith("https://generativelanguage.googleapis.com/"):
          relative_path = video_uri.replace(
              "https://generativelanguage.googleapis.com/",
              ""
          )
      else:
          relative_path = video_uri

      # base_url: https://api.thucchien.ai/gemini/v1beta
      if self.base_url.endswith("/v1beta"):
          base_path = self.base_url.replace("/v1beta", "/download")
      else:
          base_path = self.base_url

      litellm_download_url = f"{base_path}/{relative_path}"
      print(f"Download URL: {litellm_download_url}")
      
      try:
          # Download with streaming and redirect handling
          response = requests.get(
              litellm_download_url, 
              headers=self.headers, 
              stream=True,
              allow_redirects=True  # Handle redirects automatically
          )
          response.raise_for_status()
          
          # Save video file
          with open(output_filename, 'wb') as f:
              downloaded_size = 0
              for chunk in response.iter_content(chunk_size=8192):
                  if chunk:
                      f.write(chunk)
                      downloaded_size += len(chunk)
                      
                      # Progress indicator for large files
                      if downloaded_size % (1024 * 1024) == 0:  # Every MB
                          print(f"📦 Downloaded {downloaded_size / (1024*1024):.1f} MB...")
          
          # Verify file was created and has content
          if os.path.exists(output_filename):
              file_size = os.path.getsize(output_filename)
              if file_size > 0:
                  print(f"✅ Video downloaded successfully!")
                  print(f"📁 Saved as: {output_filename}")
                  print(f"📏 File size: {file_size / (1024*1024):.2f} MB")
                  return True
              else:
                  print("❌ Downloaded file is empty")
                  os.remove(output_filename)
                  return False
          else:
              print("❌ File was not created")
              return False
              
      except requests.RequestException as e:
          print(f"❌ Download failed: {e}")
          if hasattr(e, 'response') and e.response is not None:
              print(f"Status code: {e.response.status_code}")
              print(f"Response headers: {dict(e.response.headers)}")
          return False
  
  def generate_and_download(self, prompt: str, output_filename: str = None) -> bool:
      """
      Complete workflow: generate video and download it.
      
      Args:
          prompt: Text description for video generation
          output_filename: Output filename (auto-generated if None)
          
      Returns:
          True if successful, False otherwise
      """
      # Auto-generate filename if not provided
      if output_filename is None:
          timestamp = int(time.time())
          safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in (' ', '-', '_')).rstrip()
          output_filename = f"veo_video_{safe_prompt.replace(' ', '_')}_{timestamp}.mp4"
      
      print("=" * 60)
      print("🎬 VEO VIDEO GENERATION WORKFLOW")
      print("=" * 60)
      
      # Step 1: Generate video
      operation_name = self.generate_video(prompt)
      if not operation_name:
          return False
      
      # Step 2: Wait for completion
      video_uri = self.wait_for_completion(operation_name)
      if not video_uri:
          return False
      
      # Step 3: Download video
      success = self.download_video(video_uri, output_filename)
      
      if success:
          print("=" * 60)
          print("🎉 SUCCESS! Video generation complete!")
          print(f"📁 Video saved as: {output_filename}")
          print("=" * 60)
      else:
          print("=" * 60)
          print("❌ FAILED! Video generation or download failed")
          print("=" * 60)
      
      return success


# def main():
#   """
#   Example usage of the VeoVideoGenerator.
  
#   Configure these environment variables:
#   - LITELLM_BASE_URL: Your LiteLLM proxy URL (default: https://api.thucchien.ai/gemini/v1beta)
#   - LITELLM_API_KEY: Your LiteLLM API key (default: sk-1234)
#   """
  
#   # Configuration from environment or defaults
#   base_url = os.getenv("LITELLM_BASE_URL", "https://api.thucchien.ai/gemini/v1beta")
#   api_key = os.getenv("LITELLM_API_KEY", "sk-QkdYynDUd9WAfFN5M8GjeQ")
  
#   print("🚀 Starting Veo Video Generation Example")
#   print(f"📡 Using LiteLLM proxy at: {base_url}")
  
#   # Initialize generator
#   generator = VeoVideoGenerator(base_url=base_url, api_key=api_key)
  
#   # Example prompts - try different ones!
#   example_prompts = [
#       "A majestic cinematic scene of President Ho Chi Minh standing on the podium at Ba Dinh Square in Hanoi, 1945, reading the Declaration of Independence of Vietnam. A large red flag with a yellow star waves proudly under the golden sunlight. Thousands of people gather below, holding flags and cheering. The atmosphere is solemn, historical, and filled with patriotic emotion. Realistic lighting, 4K resolution, golden warm tone, cinematic camera movement, historical film style. Duration: 8 seconds. Include authentic Vietnamese male voice reading the opening lines of the Declaration of Independence."
#   ]
  
#   # Use first example or get from user
#   prompt = example_prompts[0]
#   print(f"🎬 Using prompt: '{prompt}'")
  
#   # Generate and download video
#   success = generator.generate_and_download(prompt)
  
#   if success:
#       print("✅ Example completed successfully!")
#       print("💡 Try modifying the prompt in the script for different videos!")
#   else:
#       print("❌ Example failed!")
#       print("🔧 Check your API Configuration")

# if __name__ == "__main__":
#   main()