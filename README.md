<h1 align="center">🔥 GitHub Streak Keeper</h1>

<p align="center">
  <em>Never break your GitHub contribution streak again — fully automated, runs in the cloud for free.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-Automated-2088FF?logo=github-actions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Streak-Maintained%20Daily-orange?logo=github" alt="Streak" />
  <img src="https://img.shields.io/badge/Cost-Free-brightgreen" alt="Free" />
</p>

---

## 🧠 How It Works

```
GitHub Actions (cron: daily at 00:30 UTC)
        │
        ▼
  streak.py runs on GitHub's servers
        │
        ├── Already committed today? → skip ✅
        │
        └── No commit yet → appends a new daily log entry
            (date + timestamp + motivational quote)
                    │
                    └── git commit + push → 🔥 streak maintained
```

A small, meaningful log entry is added to `logs/YYYY-MM.md` each day. Every commit counts toward your GitHub contribution graph — so your streak stays alive **automatically**, even when you're busy, traveling, or taking a break.

---

## 🚀 Setup (One-Time, ~5 minutes)

### Step 1 — Push this repo to GitHub

```bash
# In the streak-keeper folder:
git init
git add .
git commit -m "🚀 Initial commit — streak keeper is live"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/streak-keeper.git
git push -u origin main
```

> Create a new **public** or **private** repository named `streak-keeper` on GitHub first.

---

### Step 2 — Enable Actions Write Permissions

1. Go to your repo on GitHub
2. Click **Settings** → **Actions** → **General**
3. Scroll to **Workflow permissions**
4. Select ✅ **Read and write permissions**
5. Click **Save**

That's it — the built-in `GITHUB_TOKEN` can now push commits automatically.

---

### Step 3 — Test It Manually

1. Go to your repo → **Actions** tab
2. Click **🔥 GitHub Streak Keeper** in the left sidebar
3. Click **Run workflow** → **Run workflow**
4. Watch it run (should take ~30 seconds)
5. Check your GitHub profile → contributions graph 🎉

---

## ⏰ Schedule

The workflow runs every day at **00:30 UTC** (05:30 PKT).

To change the time, edit `.github/workflows/streak.yml`:

```yaml
schedule:
  - cron: "30 0 * * *"   # minute hour day month weekday
```

Use [crontab.guru](https://crontab.guru) to customize the schedule.

---

## 🧪 Local Dry Run

Preview what the script would do without making any commits:

```bash
python streak.py --dry-run
```

---

## 📁 Project Structure

```
streak-keeper/
├── .github/
│   └── workflows/
│       └── streak.yml     # GitHub Actions workflow (daily cron)
├── logs/
│   ├── 2026-03.md         # Monthly log files (auto-created)
│   └── 2026-04.md
├── streak.py              # Core automation script
├── quotes.py              # 100+ curated daily quotes
├── requirements.txt
└── README.md
```

---

## 🛡️ Safety & Ethics

- ✅ Commits are made to **your own repository**
- ✅ Each entry is **timestamped and unique**
- ✅ The bot **skips** if you've already committed today (no duplicate commits)
- ✅ Uses only the built-in `GITHUB_TOKEN` — no external credentials stored
- ✅ Pure Python standard library — zero dependencies

---

## 📋 Example Log Entry

```markdown
### 📅 2026-03-07 · Saturday

- 🕐 Logged at: 05:30:12 PKT
- 📆 Day of year: 66
- 🔥 Streak entry: Day 66 of 2026

> 💬 *Consistency is more important than perfection.*
```

---

<p align="center">Made with ❤️ to keep the streak alive.</p>
