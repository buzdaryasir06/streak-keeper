"""
streak.py — GitHub Streak Keeper
Automatically generates a daily log entry and commits it to maintain your GitHub streak.

Usage:
    python streak.py           # Normal run (commits the daily log)
    python streak.py --dry-run # Preview only, no git operations
"""

import argparse
import datetime
import os
import subprocess
import sys
from pathlib import Path

from quotes import get_quote_seeded

# ─── Configuration ────────────────────────────────────────────────────────────
LOGS_DIR = Path(__file__).parent / "logs"
TIMEZONE_OFFSET = 5  # PKT (Pakistan Standard Time, UTC+5)
# ──────────────────────────────────────────────────────────────────────────────


def get_local_now() -> datetime.datetime:
    """Return current datetime in local timezone (PKT UTC+5)."""
    utc_now = datetime.datetime.utcnow()
    tz = datetime.timezone(datetime.timedelta(hours=TIMEZONE_OFFSET))
    return utc_now.replace(tzinfo=datetime.timezone.utc).astimezone(tz)


def get_day_of_year(dt: datetime.datetime) -> int:
    """Return the day number within the year (1–366)."""
    return dt.timetuple().tm_yday


def get_log_path(dt: datetime.datetime) -> Path:
    """Return the path to this month's log file."""
    month_str = dt.strftime("%Y-%m")
    return LOGS_DIR / f"{month_str}.md"


def log_entry_exists(log_path: Path, today_str: str) -> bool:
    """Check if a log entry for today already exists."""
    if not log_path.exists():
        return False
    content = log_path.read_text(encoding="utf-8")
    return today_str in content


def build_log_entry(dt: datetime.datetime) -> str:
    """Build a formatted markdown log entry for today."""
    today_str = dt.strftime("%Y-%m-%d")
    time_str = dt.strftime("%H:%M:%S %Z")
    day_of_year = get_day_of_year(dt)
    weekday = dt.strftime("%A")
    quote = get_quote_seeded(seed=int(dt.strftime("%Y%j")))

    entry = f"""
---

### 📅 {today_str} · {weekday}

- 🕐 **Logged at:** {time_str}
- 📆 **Day of year:** {day_of_year}
- 🔥 **Streak entry:** Day {day_of_year} of {dt.year}

> 💬 *{quote}*

"""
    return entry.lstrip()


def ensure_log_file(log_path: Path, dt: datetime.datetime) -> None:
    """Create the log file with a header if it doesn't exist."""
    LOGS_DIR.mkdir(exist_ok=True)
    if not log_path.exists():
        month_label = dt.strftime("%B %Y")
        header = f"# 📓 Streak Log — {month_label}\n\n"
        log_path.write_text(header, encoding="utf-8")


def append_entry(log_path: Path, entry: str) -> None:
    """Append a new entry to the log file."""
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run a git command and return the result."""
    result = subprocess.run(
        ["git"] + args,
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent,
    )
    if check and result.returncode != 0:
        print(f"❌ Git error: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    return result


def git_commit_and_push(log_path: Path, dt: datetime.datetime) -> None:
    """Stage, commit, and push the updated log file."""
    day_of_year = get_day_of_year(dt)
    today_str = dt.strftime("%Y-%m-%d")
    commit_msg = f"🔥 Day {day_of_year} streak — {today_str}"

    print(f"  📁 Staging: {log_path.relative_to(Path(__file__).parent)}")
    run_git(["add", str(log_path)])

    print(f"  💾 Committing: '{commit_msg}'")
    run_git([
        "commit",
        "--message", commit_msg,
        "--author", "streak-bot <streak-bot@users.noreply.github.com>",
    ])

    print("  🚀 Pushing to remote...")
    run_git(["push"])

    print(f"\n✅ Streak maintained! Commit: '{commit_msg}'")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="GitHub Streak Keeper — automatic daily commit bot"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the log entry without making any git operations",
    )
    args = parser.parse_args()

    now = get_local_now()
    today_str = now.strftime("%Y-%m-%d")
    log_path = get_log_path(now)

    print("─" * 55)
    print("🔥 GitHub Streak Keeper")
    print(f"   Date  : {today_str}")
    print(f"   Time  : {now.strftime('%H:%M:%S %Z')}")
    print(f"   Log   : {log_path.name}")
    print("─" * 55)

    # Check for existing entry
    if log_entry_exists(log_path, today_str):
        print(f"✅ Already committed for {today_str}. Streak is safe!")
        return

    # Build and preview the entry
    entry = build_log_entry(now)
    print("\n📝 New log entry:\n")
    print(entry)

    if args.dry_run:
        print("🏃 Dry-run mode — no git operations performed.")
        return

    # Write and commit
    ensure_log_file(log_path, now)
    append_entry(log_path, entry)
    print("✍️  Entry written to log.\n")

    git_commit_and_push(log_path, now)


if __name__ == "__main__":
    main()
