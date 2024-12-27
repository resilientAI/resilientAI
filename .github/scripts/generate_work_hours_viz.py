name: Update Work Hours Visualization

on:
  schedule:
    - cron: '0 0 * * *'  # Runs every day at midnight
  workflow_dispatch:  # Allows manual triggering

jobs:
  update-work-hours:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests matplotlib
    - name: Generate work hours visualization
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python .github/scripts/generate_work_hours_viz.py
    - name: Commit and push if changed
      run: |
        git config --global user.email "action@github.com"
        git config --global user.name "GitHub Action"
        git add -A
        git commit -m "Update work hours visualization" || exit 0
        git push

