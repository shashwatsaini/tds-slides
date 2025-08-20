#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-https://github.com/YOUR-ORG/YOUR-REPO.git}"
BRANCH="feat/px-2024-analysis"
TMPDIR="$(mktemp -d)"
echo "Using temp dir: $TMPDIR"
git clone "$REPO_URL" "$TMPDIR"
cd "$TMPDIR"
git checkout -b "$BRANCH"

mkdir -p analysis/healthcare_performance_pr
cp -r "/mnt/c/Users/shash/OneDrive/Desktop/IIT Madras/Tools in DS/Week 7/healthcare_performance_pr/." analysis/healthcare_performance_pr/

git add -A
git commit -m "feat: Healthcare PX 2024 analysis, visuals, and data story \(avg=2.1\)"
git push -u origin "$BRANCH"

echo "Now open a PR on GitHub from branch $BRANCH."
