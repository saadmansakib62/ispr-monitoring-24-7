# Deploying ISPR News Monitoring System to Render.com, GitHub Pages & Netlify

## Option 1: One-Click Deploy to Render.com (Python Backend + Frontend)
1. Upload all 11 repository files to your GitHub repository:
   - `.gitignore`
   - `DEPLOY_TO_RENDER.md`
   - `README.md`
   - `SOURCE_CATALOGUE.md`
   - `START_HERE.txt`
   - `app.py`
   - `index.html`
   - `render.yaml`
   - `requirements.txt`
   - `run_mac_linux.sh`
   - `run_windows.bat`
2. Log in to [https://dashboard.render.com](https://dashboard.render.com).
3. Click **New +** -> **Blueprint** (or **Web Service**) and connect your GitHub repository.
4. Render automatically reads `render.yaml`, installs `requirements.txt`, and launches `gunicorn app:app`.

## Option 2: Deploy to Netlify (`https://isprbdnewsreport.netlify.app/`)
1. Connect the same GitHub repository to [https://app.netlify.com](https://app.netlify.com).
2. Leave the Build Command blank and set the Publish Directory to `.`.
3. Change your site name to `isprbdnewsreport`.

## Option 3: Deploy to GitHub Pages
1. In your GitHub repository, open **Settings -> Pages**.
2. Under **Branch**, select `main` and `/ (root)` and click **Save**.